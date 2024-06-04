import os
import tempfile
import unittest
import nbformat
from nbformat.v4 import new_notebook, new_code_cell
from pkg_vers.package_manager import _get_imported_top_level_packages_from_ipynb

class TestGetImportedPackages(unittest.TestCase):
    def test_get_imported_packages_from_ipynb(self):
        # Create a temporary notebook file with sample import statements
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.ipynb') as temp_file:
            # Create a new notebook
            notebook = new_notebook()

            # Add code cells with import statements
            code_cell1 = new_code_cell(source='import numpy as np\nimport pandas as pd')
            code_cell2 = new_code_cell(source='from sklearn.model_selection import train_test_split')
            code_cell3 = new_code_cell(source='import matplotlib.pyplot as plt')

            # Add the code cells to the notebook
            notebook.cells.extend([code_cell1, code_cell2, code_cell3])

            # Write the notebook to the temporary file
            nbformat.write(notebook, temp_file)
            temp_file_path = temp_file.name

        # Call the function with the temporary notebook file path
        imported_packages = _get_imported_top_level_packages_from_ipynb(temp_file_path)

        # Define the expected set of imported packages
        expected_packages = {'numpy', 'pandas', 'sklearn', 'matplotlib'}

        # Assert that the imported packages match the expected set
        self.assertEqual(imported_packages, expected_packages)

        # Clean up the temporary file
        os.unlink(temp_file_path)

if __name__ == '__main__':
    unittest.main()