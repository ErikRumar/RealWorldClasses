
class Car:

    def __init__(self, speed, model, license_plate):
        # self.driver = driver
        self.speed = speed
        self.model = model
        self.license_plate = license_plate

    def __str__(self) -> str:
        return f"En {self.model} i {self.speed} km/h. Registreringsnummer: {self.license_plate}"
        # return f"{self.driver} kör en {self.model} i {self.speed} km/h. Registreringsnummer: {self.license_plate}"

    def give_fine(self):
        reason = input("varför: ")
        cost = int(input("hur mycket pengar(kr): "))
        print(f"skyldig {cost} kr därför {reason}")
        # print(f"{self.driver} är skyldig {cost} kr därför {reason}")


class Driver(Car):

    def __init__(self, name, age, favorite_color):
        self.name = name
        self.age = age
        self.favorite_color = favorite_color

    def __str__(self) -> str:
        return f"{self.name} är {self.age} år, och gillar {self.favorite_color}"
        
        #super().__str__()

def main():

    linus = Driver("Linus", 18, "rosa")
    car1 = Car(34, "volvov75+", "reg123")
    print(car1)
    print(linus)
    Car.give_fine(car1)


if __name__ == "__main__":
    main()