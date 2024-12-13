class Car: 
    def __init__(self,model,name,color,owner,accelerate=0):
        self.model = model
        self.name = name
        self.color = color
        self.owner = owner
        self.accelerate = accelerate
    def drive(self):
         self.accelerate += 5
         return self.accelerate
    def brake(self):
        self.accelerate -=2
        return self.accelerate
    