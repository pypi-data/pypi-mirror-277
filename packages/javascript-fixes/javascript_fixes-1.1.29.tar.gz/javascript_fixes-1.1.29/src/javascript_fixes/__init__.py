import os
import sys

def check_node():
    import subprocess
    import re

    def extract_number(s):
        if isinstance(s, str):
            # Use regular expression to find all numbers in the text
            numbers = re.findall(r"\b\d+(?:\.\d+)?\b", s)
            # Convert the extracted strings to floats or integers
            ls = [float(num) if "." in num else int(num) for num in numbers]

            return ls[0] if ls else None

        if isinstance(s, int) or isinstance(s, float):
            return s

    try:
        NODE_BIN = os.environ.get("NODE_BIN") or (
            getattr(os.environ, "NODE_BIN")
            if hasattr(os.environ, "NODE_BIN")
            else "node"
        )
        node_version = subprocess.check_output(
            [NODE_BIN, "-v"], universal_newlines=True
        ).replace("v", "")
        major_version = int(extract_number(node_version))

        MIN_VER = 14
        if major_version < MIN_VER:
            print(
                f"Your Node.js version is {major_version}, which is less than {MIN_VER}. To use proxy with Botasaurus, you need Node.js {MIN_VER}+, Kindly install it by visiting https://nodejs.org/."
            )
            sys.exit(1)
    except Exception as e:
        print(
            "To use proxy with Botasaurus, you need to have Node.js installed on your system. You do not have Node.js installed on your system, Kindly install it by visiting https://nodejs.org/. After installation, please restart your PC."
        )
        sys.exit(1)

def packageinstall():
    base_path = os.path.join(os.path.dirname(__file__), "js", "node_modules")
    has_paths = os.path.exists(os.path.join(base_path, "proxy-chain"))  and os.path.exists(os.path.join(base_path, "botasaurus-controls"))
    
    if not has_paths: 
        check_node()
        PACKAGEJSON = '{\n\t"name": "js-modules",\n\t"description": "This folder holds the installed JS deps",\n\t"dependencies": {}\n}'
        original_directory = os.getcwd()

        os.chdir(os.path.dirname(__file__) + "/js")
        if not os.path.exists("package.json"):
            with open("package.json", "w") as f:
                f.write(PACKAGEJSON)
        
        
        os.system(f"npm install proxy-chain botasaurus-controls")

        os.chdir(original_directory)

packageinstall()

from . import config, proxy, events
import threading, inspect, time, atexit

def init():
    global console, globalThis, RegExp, start, stop, abort
    if config.event_loop:
        return  # Do not start event loop again
    config.event_loop = events.EventLoop()
    start = config.event_loop.startThread
    stop = config.event_loop.stopThread
    abort = config.event_loop.abortThread
    config.event_thread = threading.Thread(target=config.event_loop.loop, args=(), daemon=True)
    config.event_thread.start()
    config.executor = proxy.Executor(config.event_loop)
    config.global_jsi = proxy.Proxy(config.executor, 0)
    console = config.global_jsi.console  # TODO: Remove this in 1.0
    globalThis = config.global_jsi.globalThis
    RegExp = config.global_jsi.RegExp
    atexit.register(config.event_loop.on_exit)

    if config.global_jsi.needsNodePatches():
        config.node_emitter_patches = True


init()


def terminate():
    if config.event_loop:
        config.event_loop.stop()


def require(name, version=None):
    calling_dir = None
    if name.startswith("."):
        # Some code to extract the caller's file path, needed for relative imports
        try:
            namespace = sys._getframe(1).f_globals
            cwd = os.getcwd()
            rel_path = namespace["__file__"]
            abs_path = os.path.join(cwd, rel_path)
            calling_dir = os.path.dirname(abs_path)
        except Exception:
            # On Notebooks, the frame info above does not exist, so assume the CWD as caller
            calling_dir = os.getcwd()

    return config.global_jsi.require(name, version, calling_dir, timeout=900)


def eval_js(js):
    frame = inspect.currentframe()
    rv = None
    try:
        local_vars = {}
        for local in frame.f_back.f_locals:
            if not local.startswith("__"):
                local_vars[local] = frame.f_back.f_locals[local]
        rv = config.global_jsi.evaluateWithContext(js, local_vars, forceRefs=True)
    finally:
        del frame
    return rv


def AsyncTask(start=False):
    def decor(fn):
        fn.is_async_task = True
        t = config.event_loop.newTaskThread(fn)
        if start:
            t.start()

    return decor


# You must use this Once decorator for an EventEmitter in Node.js, otherwise
# you will not be able to off an emitter.
def On(emitter, event):
    # print("On", emitter, event,onEvent)
    def decor(_fn):
        # Once Colab updates to Node 16, we can remove this.
        # Here we need to manually add in the `this` argument for consistency in Node versions.
        # In JS we could normally just bind `this` but there is no bind in Python.
        if config.node_emitter_patches:

            def handler(*args, **kwargs):
                _fn(emitter, *args, **kwargs)

            fn = handler
        else:
            fn = _fn

        emitter.on(event, fn)
        # We need to do some special things here. Because each Python object
        # on the JS side is unique, EventEmitter is unable to equality check
        # when using .off. So instead we need to avoid the creation of a new
        # PyObject on the JS side. To do that, we need to persist the FFID for
        # this object. Since JS is the autoritative side, this FFID going out
        # of refrence on the JS side will cause it to be destoryed on the Python
        # side. Normally this would be an issue, however it's fine here.
        ffid = getattr(fn, "iffid")
        setattr(fn, "ffid", ffid)
        config.event_loop.callbacks[ffid] = fn
        return fn

    return decor


# The extra logic for this once function is basically just to prevent the program
# from exiting until the event is triggered at least once.
def Once(emitter, event):
    def decor(fn):
        i = hash(fn)

        def handler(*args, **kwargs):
            if config.node_emitter_patches:
                fn(emitter, *args, **kwargs)
            else:
                fn(*args, **kwargs)
            del config.event_loop.callbacks[i]

        emitter.once(event, handler)
        config.event_loop.callbacks[i] = handler

    return decor


def off(emitter, event, handler):
    emitter.off(event, handler)
    del config.event_loop.callbacks[getattr(handler, "ffid")]


def once(emitter, event):
    val = config.global_jsi.once(emitter, event, timeout=1000)
    return val
