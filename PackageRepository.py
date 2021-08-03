class PackageRepository:
    """
    Can insert and get packages from the hash table
    """
    def __init__(self, capacity):
        """Initiatlizes new PackageRepository"""
        self.table = []
        for i in range(capacity):
            self.table.append([])

    def insert(self, package_id):
        """Inserts a new package into the repository"""
        bucket_num = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket_num]

        bucket_list.append(package_id)

    def search(self, package_id):
        """Searches for package by the id and returns it."""
        bucket_num = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket_num]

        if package_id in bucket_list:
            package_id = bucket_list.index(package_id)
            return bucket_list[package_id]
        else:
            return None 

    def remove(self, key):
        """Removes a package from repository by the key."""
        bucket_num = hash(key) % len(self.table)
        bucket_list = self.table[bucket_num]

        if key in bucket_list:
            bucket_list.remove(key)
