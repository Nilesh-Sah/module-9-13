class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")

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

    def print_distance(self):
        print(f"Distance Travelled: {self.travelled_distance} km")

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

# Main program
donald_duck = Magazine(name="Donald Duck", chief_editor="Aki Hyyppä")
compartment_no_6 = Book(name="Compartment No. 6", author="Rosa Liksom", page_count=192)

donald_duck.print_information()
print("\n")
compartment_no_6.print_information()
print("\n")

electric_car = ElectricCar(registration_number="ABC-15", max_speed=180, battery_capacity=52.5)
gasoline_car = GasolineCar(registration_number="ACD-123", max_speed=165, tank_volume=32.3)

electric_car.accelerate(120)
gasoline_car.accelerate(90)

electric_car.drive(3)
gasoline_car.drive(3)

electric_car.print_distance()
gasoline_car.print_distance()
