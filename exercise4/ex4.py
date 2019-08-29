'''
100 - 20 = 80. If I want to process the answer (for example,
adding 20 to the answer), I will take 80 + 20 = 100.
So, we need something to record the answer (80). That is what
we called variables.
'''

#The name of Variables is also a kind of comment
#Never use names like a, b, c or abbreviation of somebody's name
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers availabel")
print("There will be", cars_not_driven, "empty car today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put about",average_passengers_per_car, "persons in each car")
