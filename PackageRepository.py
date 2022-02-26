class PackageRepository:
    """
    Can insert and get packages from the hash table
    """
    def __init__(self, capacity):
        """Initiatlizes new PackageRepository -> O(n)"""
        self.table = []
        for i in range(capacity):
            self.table.append([])

    def insert(self, package):
        """Inserts a new package into the repository -> O(1)"""
        bucket_num = hash(package.id) % len(self.table)
        bucket_list = self.table[bucket_num]

        bucket_list.append(package)

    def search(self, package_id):
        """Searches for package by the key and returns it. -> O(n)"""
        bucket_num = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket_num]

        for package in bucket_list:
            if package.id == package_id:
                return package
            else:
                return None 

    def remove(self, package_id):
        """Removes a package from repository by the key. -> O(n)"""
        bucket_num = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket_num]

        for package in bucket_list:
            if package.id == package_id:
                bucket_list.remove(package)

    def load_packages_list(self, package_list):
        """Takes in a list of packages and inserts each of them into the hash table. -> O(n)"""
        for p in package_list:
            self.insert(p)
