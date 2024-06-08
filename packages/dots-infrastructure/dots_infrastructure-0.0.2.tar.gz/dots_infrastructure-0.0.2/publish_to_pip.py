import subprocess

def main():
    subprocess.run("py -m build")
    subprocess.run("py -m twine upload --repository testpypi dist/*")

if __name__ == "__main__":
    exit(main())