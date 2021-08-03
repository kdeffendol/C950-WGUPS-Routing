from Package import Package
from PackageRepository import PackageRepository
import unittest

class PackageRepositoryTests(unittest.TestCase):
    
    def test_InsertNewPackageIntoRepository(self):
        repo = PackageRepository(10)
        package = Package(123, "", "", "City", "55555", 3.1, "")
        repo.insert(package)

        self.assertEqual(123, package.id)

    def test_RemoveNewPackageFromRepository(self):
        repo = PackageRepository(10)
        package = Package(123, "", "", "City", "55555", 3.1, "")
        repo.insert(package)
        repo.remove(package.id)

        self.assertEqual(None, repo.search(123))

if __name__ == '__main__':
    unittest.main()
