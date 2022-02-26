class Package:
    """
    Package class
    """
    def __init__(self, id, address, deadline, city, zipcode, weight, notes):
        self.id = id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = 'Not Delivered'
        self.timestamp = 0.0