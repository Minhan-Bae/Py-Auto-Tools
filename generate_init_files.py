"""
This script creates __init__.py files for all directories and subdirectories
in the specified repository path. For each __init__.py file, it also adds
import statements for all the Python modules in the same directory.
Please note that this approach can lead to complications when managing
complex package structures. Modify the script as needed before using it
in a real project.
"""

import os
import sys

def create_init_py(path):
    """
    Create __init__.py files in all directories and subdirectories
    within the given path, and add import statements for all Python modules
    in the same directory.

    Args:
        path (str): The root directory to start creating __init__.py files from.
    """
    # Iterate through all directories and files in the given path.
    for root, _, files in os.walk(path):
        init_path = os.path.join(root, "__init__.py")

        # Create a new __init__.py file.
        with open(init_path, "w") as init_file:
            # Write the default comment.
            init_file.write("# This is an automatically generated __init__.py file\n")

            # Import all modules in the current directory.
            for file in sorted(files):
                if file.endswith(".py") and file != "__init__.py":
                    module_name = file[:-3]  # Remove '.py' extension
                    init_file.write(f"from . import {module_name}\n")

            print(f"Created: {init_path}")

def delete_empty_init_py(path):
    """
    Deletes __init__.py files if they have no content (except comments)

    Args:
        path (str): The root directory to start deleting empty __init__.py files from.
    """
    for root, _, files in os.walk(path):
        init_path = os.path.join(root, "__init__.py")

        # If the file exists and is empty (ignoring comments), delete it
        if os.path.isfile(init_path):
            with open(init_path, "r") as init_file:
                lines = init_file.readlines()

                # Check if all lines are comments or blank
                is_empty = all((line.strip() == '' or line.strip().startswith('#')) for line in lines)

                if is_empty:
                    os.remove(init_path)
                    print(f"Deleted: {init_path}")


if __name__=="__main__":
    repository_path = sys.argv[1]
    create_init_py(repository_path)
    delete_empty_init_py(repository_path)