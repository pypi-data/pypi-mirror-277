import unittest
import pkg_vers
from pkg_vers.package_manager import _get_imported_top_level_packages

class TestUtils(unittest.TestCase):

    def test_find_all_py_files(self):
        files = pkg_vers.find_all_py_files('tests')
        self.assertIsInstance(files, list)

    def test_get_imported_top_level_packages(self):
        files = pkg_vers.find_all_py_files('tests')
        packages = _get_imported_top_level_packages(files)
        self.assertIsInstance(packages, list)

if __name__ == '__main__':
    unittest.main()
