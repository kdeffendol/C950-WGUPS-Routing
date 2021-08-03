class Package:
    """
    Package class
    """
    def __init__(self, id, address, deadline, city, zipcode, weight, status):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.status = status