import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        if change > 0:
            self.current_speed = min(self.current_speed + change, self.max_speed)
        elif change < 0:
            self.current_speed = max(self.current_speed + change, 0)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

car = Car(registration_number="ABC-123", max_speed=142)

print("Initial Properties of the Car:")
print(f"Registration Number: {car.registration_number}")
print(f"Maximum Speed: {car.max_speed} km/h")
print(f"Current Speed: {car.current_speed} km/h")
print(f"Travelled Distance: {car.travelled_distance} km\n")

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print(f"Current Speed after acceleration: {car.current_speed} km/h\n")

car.accelerate(-200)

print(f"Final Speed after emergency brake: {car.current_speed} km/h\n")

car.drive(1.5)

print(f"Travelled Distance after driving for 1.5 hours: {car.travelled_distance} km\n")

car_list = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    car_list.append(Car(registration_number, max_speed))

race_distance = 0
hour = 1

while True:
    for car in car_list:
        change_in_speed = random.randint(-10, 15)
        car.accelerate(change_in_speed)
        car.drive(1)

    if any(car.travelled_distance >= 10000 for car in car_list):
        break

    print(f"\nHour {hour} of the Race:")
    print("{:<15} {:<15} {:<15} {:<15}".format("Registration", "Max Speed (km/h)", "Current Speed", "Travelled Distance"))
    for car in car_list:
        print("{:<15} {:<15} {:<15} {:<15}".format(car.registration_number, car.max_speed, car.current_speed, car.travelled_distance))

    hour += 1

print("\nRace Finished!")
