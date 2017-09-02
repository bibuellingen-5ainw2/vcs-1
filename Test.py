
class MeineKlasse:
    def __init__(self):
        self.attribut = None
        
    def __str__(self):
        return ""
        
    def berechne(self):
        self.attribut = 5
        return self.attribut**2
        
        
objekt = MeineKlasse()

objekt.berechne()

print(str(objekt))
