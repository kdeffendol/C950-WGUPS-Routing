import PackageRepository

class Truck:
    def __init__(self, capacity, speed):
        self.packages = PackageRepository(16)
        self.capacity = capacity
        self.speed = speed

    def load_package(self, package):
        self.packages.insert(package)

    def remove_package(self, package_id):
        self.package.remove()
        