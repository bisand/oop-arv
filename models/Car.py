class Car:

    instanceCount: int = 0
    cars = []

    def __init__(
        self,
        brand: str = "Toyota",
        model: str = "Corolla",
        year: int = 2000,
        speed: int = 100,
    ) -> None:
        self.brand: str = brand
        self.model: str = model
        self.year: int = year
        self.speed: int = speed
        Car.instanceCount += 1
        Car.cars.append(self)

    def __str__(self) -> str:
        return f"This is a {self.brand} {self.model}, made in {self.year}, and can run in {self.speed} km/h"

    def __repr__(self) -> str:
        return f"Car('{self.brand}','{self.model}','{self.year}','{self.speed}')"

    def __del__(self):
        print(f"Destroying the {self.brand}")
        Car.instanceCount += 1
        Car.cars.remove(self)

    @classmethod
    def print_available_cars(cls):
        for car in cls.cars:
            print(car)

    @classmethod
    def get_available_cars(cls):
        result = []
        for car in cls.cars:
            result.append(car.__dict__)
        return result

    def increase_speed(self, speed: int):
        self.speed += speed

    def print_speed(self):
        print(f"Max speed is: {self.speed} km/h")

    def print_instace_count(self):
        print(f"Instances: {Car.instanceCount}")
