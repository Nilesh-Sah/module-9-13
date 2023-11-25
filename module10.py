import random

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, destination_floor):
        while self.current_floor != destination_floor:
            if self.current_floor < destination_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.elevators[0].bottom_floor)

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change_in_speed = random.randint(-10, 15)
            car.accelerate(change_in_speed)
            car.drive(1)

    def print_status(self):
        print("\nRace Status:")
        print("{:<15} {:<15} {:<15}".format("Car", "Current Speed", "Travelled Distance"))
        for car in self.cars:
            print("{:<15} {:<15} {:<15}".format(car.registration_number, car.current_speed, car.travelled_distance))

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)


elevator = Elevator(bottom_floor=1, top_floor=10)
elevator.go_to_floor(5)
elevator.go_to_floor(1)

building = Building(bottom_floor=1, top_floor=10, num_elevators=3)
building.run_elevator(elevator_number=2, destination_floor=8)
building.fire_alarm()

cars_for_race = [cars_for_race(f"Car-{i}", random.randint(100, 200)) for i in range(1, 11)]
grand_demolition_derby = Race(name="Grand Demolition Derby", distance=8000, cars=cars_for_race)

hours = 0
while not grand_demolition_derby.race_finished():
    if hours % 10 == 0:
        grand_demolition_derby.print_status()
    grand_demolition_derby.hour_passes()
    hours += 1

print("\nRace Finished!")
grand_demolition_derby.print_status()
