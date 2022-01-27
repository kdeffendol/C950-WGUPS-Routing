from PackageRepository import PackageRepository
from Package import Package
from Graph import Graph
from Vertex import Vertex
import csv

package_repo = PackageRepository(40)

def load_package_data(file_name):
    with open(file_name, encoding='utf-8-sig') as package_file:
        package_data = csv.reader(package_file, delimiter = ',')
        for p in package_data:
            new_package = Package(int(p[0]), p[1], p[2], p[3], p[4], p[5], p[6])
            package_repo.insert(new_package)


load_package_data('packages.csv')        

def load_address_data(file_name):
    addresses = ['HUB','1060 Dalton Ave S','1330 2100 S','1488 4800 S','177 W Price Ave','195 W Oakland Ave','2010 W 500 S','2300 Parkway Blvd','233 Canyon Rd','2530 S 500 E','2600 Taylorsville Blvd','2835 Main St','300 State St','3060 Lester St','3148 S 1100 W','3365 S 900 W','3575 W Valley Central Station bus Loop','3595 Main St','380 W 2880 S','410 S State St','4300 S 1300 E','4580 S 2300 E','5025 State St','5100 S 2700 W','5383 S 900 E #104','600 E 900 S','6351 S 900 E']
    return addresses

def load_distance_data(file_name):
    with open(file_name) as distance_file:
        reader = csv.reader(distance_file)
        distances = list(reader)
    
    return distances


def create_map():
    distance_map = Graph()
    addresses = load_address_data('addresses.csv')
    distances = load_distance_data('distances.csv')
    vertices = []
    for a in addresses:
        vertex = Vertex(a)
        distance_map.add_vertex(vertex)
        vertices.append(vertex)

    #set up edges-----
    for r in range(len(distances)):
        for c in range(len(distances[r])):
            if (float(distances[r][c]) == 0):
                break
            distance_map.add_directed_edge(vertices[r], vertices[c], float(distances[r][c]))

    print(distance_map.edge_weights)

create_map()