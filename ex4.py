# "Variables and Names."
cars = 50
driver = 5
passengers = 40
owner = "Samuelio"
space_in_the_car = 4.0
cars_driven = driver
cars_not_driven = cars - driver
carpool_capacity = cars_driven * space_in_the_car
average_passenger_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", driver, "drivers available.")
print("I", owner, "have more than", cars, "cars but, only have", driver, "drivers.")
print(owner, "don't allow any passenger in his car.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passenger_per_car, "in each day.")
