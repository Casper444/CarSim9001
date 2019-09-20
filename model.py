from random import randint

class Car(object):
    def __init__(self): # Definere objekt til klassen Car.
        self.theEngine = Engine() #Erklærer  instansvariabel for engine. ved at bruge "self", kan man få adgang til attributter og metoder til klassen.

    def updateModel(self, dt):
        self.theEngine.updateModel(dt) #Kører funktionen UpdateModel() på theEngine


class Wheel(object):
    def __init__(self):
        self.orientation = randint(0, 360) #Genere et tilfældigt tal mellem 0 til 360

    def rotate(self, revolutions):
        self.orientation = (self.orientation + (revolutions * 360)) % 360 #udregner hjulets position ud fra antal omdrejninger.

class Engine(object):
    def __init__(self):
        self.throttlePosition = 0 #Erklærer instansvariabel throttlePosition lig 0
        self.theGearbox = Gearbox() #Erklærer instansvariabel for theGearbox for funktionen Gearbox
        self.currentRpm = 0 #Erklærer instansvariabel for currentRpm lig 0
        self.consumptionConstant = 0.0025 #Erklærer instansvariabel for consumptionConstant lig 0.0025
        self.maxRpm = 100 #Erklærer instansvariabel for maxRpm lig 100
        self.theTank = Tank() #Erklærer instansvariabel for theTank for funktionen Tank

    def updateModel(self, dt):
        if self.theTank.contents > 0: #Tjekker om tanken er tom
            self.currentRpm = self.throttlePosition * self.maxRpm #Udregner currentRpm ved at gange throttlePosition med maxRpm
            self.theTank.remove(self.currentRpm * self.consumptionConstant) #Remove() bliver kaldt fra theTank. Udregner fjernet mængde brændstof ved at gange currentRpm med consumptionConstant
            self.theGearbox.rotate(self.currentRpm * (dt / 60)) #Rotate() bliver kaldt fra theGearbox og udregner rotationer på theGearbox ved at gange currentRpm med (dt/60) - dt står for deltatime og enheden er i sekunder. Derfor divideres med 60 for at det i minutter.
        else:
            self.currentRpm = 0 #Hvis tanken er tom, skal currentRpm være lig 0.


class Gearbox(object):
    def __init__(self):
        self.wheels = {'frontLeft': Wheel(), 'frontRight': Wheel(), 'rearLeft': Wheel(), 'rearRight': Wheel()} #Erklærer Wheel instansvariabel, som et dictionary med hjul.
        self.currentGear = 0 #Erklærer instansvariabel currentGear lig 0
        self.clutchEngaged = False #Erklærer instansvariabel clutchEngaged til at være en boolean lig Falsk
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8] #Erklærer instansvariabel gears til at være en liste

    def shiftUp(self):
        if self.currentGear < len(self.gears) - 1 and self.clutchEngaged == False: #Tjekker om currentGears er mindre end længden af gears og om clutchEngaged er falsk
            self.currentGear = self.currentGear + 1 #skifter et gear op

    def shiftDown(self):
        if self.currentGear > 0 and self.clutchEngaged == False: #Tjekker om currentGear er højere end 0 og om clutchEngaged er Falsk
            self.currentGear = self.currentGear - 1 #Skifter et gear ned

    def rotate(self, revolutions):
        if self.clutchEngaged: #Tjekker om clutchEngaged er sand
            for i in self.wheels:
                self.wheels[i].rotate(revolutions * self.gears[self.currentGear]) #Funktionen kalder på rotate på hver instant af Wheel i Wheels. Udregner antal omdrejninger på wheels ved at sige revolutions * værdien af currentGears i Gears.

class Tank(object):
    def __init__(self):
        self.capacity = 100 #Erklærer instansvariabel capacity lig 100
        self.contents = 100 #Erklærer instansvariabel contents lig 100

    def refuel(self):
        self.contents = self.capacity #opdatere contents lig capacity

    def remove(self, amount):
        self.contents = self.contents - amount #opdatere contents fratrukket amount
        if self.contents < 0: #Tjekker om contents er lig 0
            self.contents = 0 #sætter contents lig 0
