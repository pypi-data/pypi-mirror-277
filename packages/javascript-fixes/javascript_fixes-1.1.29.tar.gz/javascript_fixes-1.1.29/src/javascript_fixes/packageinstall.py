import os
PACKAGEJSON = '{\n\t"name": "js-modules",\n\t"description": "This folder holds the installed JS deps",\n\t"dependencies": {}\n}'

def packageinstall(package):
    os.chdir(os.path.dirname(__file__) + "/js")
    if not os.path.exists("package.json"):
        with open("package.json", "w") as f:
            f.write(PACKAGEJSON)
    os.system(f"npm install {package}")
