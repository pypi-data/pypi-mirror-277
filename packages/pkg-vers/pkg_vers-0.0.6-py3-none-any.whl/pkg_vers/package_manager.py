import importlib
import shutil
import re
import sys
import ast
import nbformat
from .utils import _run_subprocess

IGNORED_LIB_MODULES = {'os', 'enum', 'random'}

def get_package_versions_from(files):
    if isinstance(files, str):
        files = [files]

    installed_packages = _get_installed_packages()
    imported_packages = _get_imported_top_level_packages(files)
    packages_with_versions = _get_package_versions(imported_packages, installed_packages)
    return packages_with_versions

def get_package_versions_from_ipynb(path):
    installed_packages = _get_installed_packages()
    imported_packages = _get_imported_top_level_packages_from_ipynb(path)
    packages_with_versions = _get_package_versions(imported_packages, installed_packages)
    return packages_with_versions

def _get_imported_top_level_packages_from_ipynb(path):
    try:
        # Read the notebook file
        with open(path, 'r') as file:
            notebook = nbformat.read(file, as_version=4)

        # Regular expression patterns to match import statements
        import_pattern = re.compile(r'^\s*import\s+(\S+)')
        from_import_pattern = re.compile(r'^\s*from\s+(\S+)\s+import')

        # Initialize a set to hold unique imports
        imports = set()

        # Iterate over each cell in the notebook
        for cell in notebook.cells:
            # Check if the cell is a code cell
            if cell.cell_type == 'code':
                # Get the cell's source code
                source = cell.source

                # Split the source code into lines
                lines = source.split('\n')

                # Iterate over each line and look for import statements
                for line in lines:
                    import_match = import_pattern.match(line)
                    from_import_match = from_import_pattern.match(line)

                    if import_match:
                        imports.add(import_match.group(1).split('.')[0])
                    elif from_import_match:
                        imports.add(from_import_match.group(1).split('.')[0])

        return imports
    except Exception as e:
        print(f"An error occurred: {e}")
        return set()

def _get_imported_top_level_packages(script_paths):
    imported_packages = set()
    for script_path in script_paths:
        with open(script_path, 'r') as file:
            code = file.read()
        
            tree = ast.parse(code, filename=script_path)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imported_packages.add(alias.name.split('.')[0])
                elif isinstance(node, ast.ImportFrom):
                    imported_packages.add(node.module.split('.')[0])
    return list(imported_packages)

def _get_installed_packages():
    packages = {}
    if shutil.which('mamba'):
        mamba_lines = _run_subprocess(['mamba', 'list'])
        for line in mamba_lines:
            if line.startswith('#'):
                continue
            parts = re.split(r'\s+', line)
            if len(parts) >= 2:
                package, version = parts[0], parts[1]
                packages[package] = version

    pip_lines = _run_subprocess([sys.executable, '-m', 'pip', 'freeze'])
    for line in pip_lines:
        if '==' in line:
            pkg, version = line.split('==')
            if pkg not in packages:
                packages[pkg] = version

    return packages

def _get_package_version(package):
    try:
        module = importlib.import_module(package)
        return getattr(module, '__version__', '')
    except ImportError:
        return ''

def _get_package_versions(imported_packages, installed_packages):
    specific_versions = {}
    for package in imported_packages:
        if package in IGNORED_LIB_MODULES:
            continue
        version = installed_packages.get(package) or installed_packages.get(package.replace("_", "-"), "")

        if not version:  # if version is empty, try to get it from module.__version__
            version = _get_package_version(package)
        specific_versions[package] = version
    return specific_versions