class Car:
    def __init__ (self,name,model,cost):
        self.name = name
        self.cost = cost
        self.model = model
        
    def carInfo(self):
        print(f"car name is {self.name} is {self.model} and {self.cost}")
maruti = Car ("maruti","petrol","1 lakh")
mercedes = Car ("mercedes","disel","20 lakh")

maruti.carInfo()
mercedes.carInfo()
          