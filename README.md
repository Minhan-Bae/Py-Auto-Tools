# Py-Auto-Tools*Python Repository Automation Tools)

This repository provides a collection of automation scripts useful for Python project development. These tools enhance development efficiency by automating common tasks such as generating directory structures, managing `__init__.py` files, creating dependency lists, and cleaning up unnecessary files.

## Key Features

**1. Automatic Directory Structure Generation**
- Automatically creates the necessary directory structure for projects
- Quickly set up the basic structure when starting a new project

**2. `__init__.py` File Generation**
- Automatically generates `__init__.py` files for Python package structures
- Makes directories recognizable as Python modules for easier imports

**3. Requirements.txt File Generation**
- Saves dependency packages in a `requirements.txt` file
- Simplifies environment replication and dependency management

**4. Cleaning Unnecessary Files**
- Removes `.DS_Store` files and hidden files with `._` prefixes
- Especially useful for cleaning metadata files generated on macOS

## Script Descriptions

**`generate_dir_structure.py`**
- Function: Automatically creates the necessary directory structure for a project
- Helps maintain consistent project organization across different projects
- Saves time when setting up new project environments

**`generate_init_files.py`**
- Function: Automatically generates `__init__.py` files in specified directories and their subdirectories
- Ensures proper Python package structure to enable module imports
- Supports code organization through directory modularization

**`generate_requirements_txt.py`**
- Function: Saves the list of installed packages in the current environment to a `requirements.txt` file
- Stores the file in the path specified by the command line argument (`sys.argv[1]`)
- Provides the ability to include additional requirements as needed

**`delete_DS.py`**
- Function: Recursively finds and deletes `.DS_Store` files and files with `._` prefixes
- Allows specifying the directory to clean via command line arguments (`argv`)
- Useful for cleaning unnecessary metadata files, particularly in macOS environments

**`__init__.py`**
- Function: Used for package initialization settings
- Current version provides streamlined initialization with empty functions removed

## Usage

### Generate Directory Structure

```bash
python generate_dir_structure.py [path]
```

Creates the basic project directory structure at the specified path.

### Generate `__init__.py` Files

```bash
python generate_init_files.py [path]
```

Creates `__init__.py` files in all subdirectories of the specified path.

### Generate Requirements.txt

```bash
python generate_requirements_txt.py [save_path] [additional_requirements]
```

Saves the list of packages from the current environment to a `requirements.txt` file at the specified path. Optionally, specify additional requirements.

### Clean Unnecessary Files

```bash
python delete_DS.py [path]
```

Recursively finds and deletes `.DS_Store` files and files with `._` prefixes in the specified path.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/username/repository-name.git
```

2. Install the necessary dependencies:
```bash
pip install -r requirements.txt
```

## Example Workflow

When starting a new project, you can use the scripts as follows:

1. First, generate the directory structure:
```bash
python generate_dir_structure.py new_project
```

2. Add `__init__.py` files to the generated directories:
```bash
python generate_init_files.py new_project
```

3. Generate the list of project dependencies:
```bash
python generate_requirements_txt.py new_project
```

4. Clean up unnecessary files:
```bash
python delete_DS.py new_project
```

## Contributing

If you wish to contribute to this project, please follow these steps:

1. Fork this repository
2. Develop new features or fix bugs
3. Commit and push your changes
4. Submit a pull request

All types of contributions are welcome!

## License

This project is distributed under the [License Name]. See the LICENSE file for details.
