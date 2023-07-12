# delete DS_Store from dir
import os
import sys
def main():
    root = sys.argv[1]
    for dir, _, files in os.walk(root):
        for file in files:
            if file.endswith(".DS_Store"):
                os.remove(os.path.join(dir,file))
            elif '._' in file:
                os.remove(os.path.join(dir,file))
if __name__=="__main__":
    main()