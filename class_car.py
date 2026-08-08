class car:
    wheels : 4

    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def details(self):
        print(f"{self.brand},{self.model},{self.year}")

car1 = car("Hero","Vida",2023)
car1.details()


