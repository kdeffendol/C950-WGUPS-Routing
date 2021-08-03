class PackageRepository:
    """
    Can insert and get packages from the hash table
    """
    def __init__(self, capacity):
        """Initiatlizes new PackageRepository"""
        self.table = []
        for i in range(capacity):
            self.table.append([])

    def insert(self, package):
        """Inserts a new package into the repository"""
        bucket_num = hash(package) % len(self.table)
        bucket_list = self.table[bucket_num]

        bucket_list.append(package)

    def search(self, key):
        """Searches for package by the key and returns it."""
        bucket_num = hash(key) % len(self.table)
        bucket_list = self.table[bucket_num]

        if key in bucket_list:
            package_id = bucket_list.index(key)
            return bucket_list[package_id]
        else:
            return None 

    def remove(self, key):
        """Removes a package from repository by the key."""
        bucket_num = hash(key) % len(self.table)
        bucket_list = self.table[bucket_num]

        if key in bucket_list:
            bucket_list.remove(key)
