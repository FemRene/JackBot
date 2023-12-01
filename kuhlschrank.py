class Kuhlschrank:


#__init__ steht für initialize und ist dafür da die parameter zu initizialisieren
#hier muss immer self vor der variable stehen damit das programm weiß das es auf diese Funktion angewendet werden muss

    def __init__(self,owner,farbe,hohe,e_klasse,volumen):
        self.owner = owner
        self.farbe = farbe
        self.hohe = hohe
        self.e_klasse = e_klasse
        self.volumen = volumen
    def an(self):
        print(self.owner+" ist an")

    def aus(self):
        print(self.owner+" ist aus")

