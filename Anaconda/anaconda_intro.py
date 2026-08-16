from importlib.util import find_spec
import os
import sys


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def package_status(name):
    return "installed" if find_spec(name) else "not installed"


def main():
    section("Which Python is running?")
    print("Executable:", sys.executable)
    print("Version:", sys.version.split()[0])

    section("Conda-related environment variables")
    print("CONDA_DEFAULT_ENV:", os.environ.get("CONDA_DEFAULT_ENV", "not set"))
    print("CONDA_PREFIX:", os.environ.get("CONDA_PREFIX", "not set"))

    section("Packages to check after conda install")
    for package_name in ["numpy", "pandas", "matplotlib", "jupyterlab"]:
        print(f"{package_name:12} {package_status(package_name)}")

    section("The command line workflow")
    commands = [
        "conda create -n py-basics python=3.11",
        "conda activate py-basics",
        "conda install numpy pandas matplotlib jupyterlab",
        "python python_lessons/01_anaconda_intro.py",
        "conda deactivate",
    ]
    for command in commands:
        print("$", command)


if __name__ == "__main__":
    main()

