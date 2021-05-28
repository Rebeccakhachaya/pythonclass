class Car:
    name="vehicle"
    def __init__(self,make,colour,milleage,model):
        self.make=make
        self.colour=colour
        self.milleage=colour
        self.model=model
    def speed(self):
             return f" I love {self.colour} {self.make}{self.model}"
    def acceleretor(self):
             return f"{self.model} moves at high {self.milleage}"
             
    
       