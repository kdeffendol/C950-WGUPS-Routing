"""
Kelsey Deffendol
C950 - Data Structures & Algorithms 2
Student Id: 001243817
"""
from PackageRepository import PackageRepository
from Package import Package
import csv
import math

def load_package_data(file_name):
    """Takes a csv file and returns a list of package objects from the given data. -> O(n)"""
    with open(file_name, encoding='utf-8-sig') as package_file:
        package_data = csv.reader(package_file, delimiter = ',')
        for p in package_data:
            new_package = Package(int(p[0]), p[1], p[2], p[3], p[4], p[5], p[6])
            packages.append(new_package)     

def load_address_data(file_name):
    """Returns a list of the address data given. -> O(1)"""
    addresses = ['HUB','1060 Dalton Ave S','1330 2100 S','1488 4800 S','177 W Price Ave','195 W Oakland Ave','2010 W 500 S','2300 Parkway Blvd','233 Canyon Rd','2530 S 500 E','2600 Taylorsville Blvd','2835 Main St','300 State St','3060 Lester St','3148 S 1100 W','3365 S 900 W','3575 W Valley Central Station bus Loop','3595 Main St','380 W 2880 S','410 S State St','4300 S 1300 E','4580 S 2300 E','5025 State St','5100 S 2700 W','5383 S 900 E #104','600 E 900 S','6351 S 900 E']
    return addresses

def load_distance_data(file_name):
    """Takes a csv file and returns a 2d array of the distance data. -> O(1)"""
    with open(file_name) as distance_file:
        reader = csv.reader(distance_file)
        distances = list(reader)
    
    return distances

def find_distance(current_address, destination):
    """Finds the distance between the two given addresses from the distance 2d array and returns it. -> O(n)"""
    
    #Find indexes of the addresses given
    current_address_index = addresses.index(current_address)
    destination_index = addresses.index(destination)

    #find the highest index
    if (current_address_index > destination_index):
        distance = distances[current_address_index][destination_index]
    else:
        distance = distances[destination_index][current_address_index]
    
    return float(distance)

def find_closest_package_id(current_address, package_list):
    """Finds and returns the closest package id to the current address. -> O(n)"""
    lowest_distance = 100.0 #dumb max float
    lowest_package_id = 0
    
    for p in package_list: 
        package = package_table.search(p)
        distance = float(find_distance(current_address, package.address))
        if (distance < lowest_distance):
            lowest_distance = distance
            lowest_package_id = package.id
    
    return lowest_package_id

def order_package_list(starting_point, package_list):
    """Orders a list of packages using a nearest neighbor algorithm, then returns the ordered list of packages. -> O(n^2)"""
    current_address = starting_point
    ordered_package_list = []
    while len(package_list) != 0:
        package_id = find_closest_package_id(current_address, package_list)
        ordered_package_list.append(package_id)
        current_address = package_table.search(package_id).address
        package_list.remove(package_id)
    
    return ordered_package_list


def deliver_packages(delivery_start_time, truck_packages):
    """Delivers packages in the sorted package list and timestamps the package data. Also calculates the distance driven. -> O(n^2)"""
    distance_traveled = 0.0
    current_time = delivery_start_time
    starting_address = 'HUB'
    for package_id in truck_packages:
        package = package_table.search(package_id)
        distance = find_distance(starting_address, package.address)
        distance_traveled += distance #Add distance to distance tracker
        time_taken = distance / 18
        current_time += time_taken
        package.timestamp = current_time #timestamp package

        #set new starting_address for next iteration
        starting_address = package_table.search(package_id).address

    #Travel back to HUB
    distance = find_distance(starting_address, 'HUB')
    current_time += distance / 18

    distance_traveled += distance
    time = current_time

    #print('Distance Traveled: ', distance_traveled)
    #print('Current time: ', time)

    return distance_traveled


def convert_timestamp_to_hours_minutes(timestamp):
    """Converts a fractional hours number and returns a Hours:Minutes format -> O(1)"""
    hours = int(timestamp)
    minutes = math.floor((timestamp - hours) * 60)

    return str(hours) + ':' + '{:0>2}'.format(str(minutes))

def convert_hours_minutes_to_fractional_hours(hours_minutes):
    """Converts an HH:MM format to a fractional hours format -> O(1)"""
    hours_minutes_list = hours_minutes.split(':')
    hours = hours_minutes_list[0]
    minutes = hours_minutes_list[1]

    fractional_minutes = int(minutes) / 60

    return int(hours) + fractional_minutes

def print_package_statuses(timestamp):
    """For each package in the packages list, it pulls the data from the hash table and prints it to the CLI. -> O(n^2)"""
    for package in packages:
        package = package_table.search(package.id)
        fractional_timestamp = convert_hours_minutes_to_fractional_hours(timestamp)
        set_delivery_status(package, fractional_timestamp)
        print(package.id, '|', package.address, '|', package.city, '|', package.zipcode, '|', package.deadline, '|', package.weight, '|', package.notes, '|', package.status, '|', convert_timestamp_to_hours_minutes(package.timestamp))

def set_delivery_status(package, timestamp):
    """Sets a package's status to 'Delivered' if the delivery time is less than the given time -> O(1)"""
    if (float(timestamp) >= package.timestamp):
        package.status = 'Delivered'




#Get data from the csv files.
packages = []
load_package_data('packages.csv')   
addresses = load_address_data('addresses.csv')
distances = load_distance_data('distances.csv')

#Load trucks
truck1 = [13, 1, 14, 15, 16, 19, 20, 26, 21, 29, 30, 31, 34, 40]
truck2 = [2, 3, 7, 18, 36, 37, 38, 4, 17, 23, 27, 35, 33, 6]
truck3 = [8, 9, 25, 28, 32, 5, 12, 22, 24, 39, 35, 10, 11]

#Create an empty hash table and load the package list into the hash table.
package_table = PackageRepository(40)
package_table.load_packages_list(packages)

#Order the trucks' packages using the nearest neighbor algorithm.
hub_address = 'HUB'
truck1 = order_package_list(hub_address, truck1)
truck2 = order_package_list(hub_address, truck2)
truck3 = order_package_list(hub_address, truck3)

#starting times of each truck leaving the hub and keeps track of the total distance traveled.
total_distance = deliver_packages(8.0, truck1) + deliver_packages(9.08, truck2) + deliver_packages(10.03, truck3) 

#--------Command Line Interface----------
print('Enter in a time in HH:MM format (please use military time): ')
hours_minutes_time = input()
print('-------------------------------------------------------')
print('Total Distance Traveled:', total_distance, 'miles')
print('-------------------------------------------------------')
print('Packages: ')
print('ID | Address | State | Zipcode | City | Deadline | Weight | Delivery Status | Delivery Time ')
print_package_statuses(hours_minutes_time)