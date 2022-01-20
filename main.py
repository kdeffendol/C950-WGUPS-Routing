from PackageRepository import PackageRepository
from Package import Package
from Graph import Graph
from Vertex import Vertex
import csv

def load_package_data(file_name):
    with open(file_name) as package_file:
        package_data = csv.reader(package_file, delimiter = ',')
        next(package_data)
        for p in package_data:
            new_package = Package(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7])
            PackageRepository.insert(p[1], new_package)            

load_package_data('packages.csv')



