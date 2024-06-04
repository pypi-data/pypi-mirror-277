import unittest
from pkg_vers.package_manager import _get_installed_packages, _get_package_versions
from pkg_vers.package_manager import _get_imported_top_level_packages

class TestPackageManager(unittest.TestCase):

    def test_get_installed_packages(self):
        packages = _get_installed_packages()
        self.assertIsInstance(packages, dict)

    def test_get_specific_package_versions(self):
        versions = _get_package_versions(['os', 'sys'], {'os': '1.0', 'sys': '2.0'})
        self.assertIsInstance(versions, dict)

    def test_get_imported_top_level_packages(self):
        imported_packages = _get_imported_top_level_packages([__file__])
        self.assertIsInstance(imported_packages, list)

if __name__ == '__main__':
    unittest.main()
