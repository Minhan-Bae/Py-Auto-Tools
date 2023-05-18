# delete DS_Store from dir
import os

def main():
    root = os.getcwd()
    for dir, _, files in os.walk(root):
        for file in files:
            if file.endswith(".DS_Store"):
                os.remove(os.path.join(dir,file))

if __name__=="__main__":
    main()