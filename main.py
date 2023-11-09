import math
import time
#https://www.youtube.com/watch?v=XKHEtdqhLK8  Video
#_______________________________________________________________________________________________________________________
#while loop und While not loops mehr info auf ZEILE 105
name = ""
while len(name) ==0:
    name = input("Wie ist dein Name?: ")

partner_name = ""
while len(partner_name) ==0:
    partner_name = input("Wie ist der name deines Partners?: ")

age = None
while not age:
    age = int(input("Wie alt bist du?: "))

height = None
while not height:
    height = float(input("Wie groß bist du?: "))

my_name = "Jack Saering"

                                                                                                                        #int
#age += 1
pi = 3.14
x = 4
y = 3
z = 2

print(round(pi))
print(math.ceil(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(pi))
print(max(x,y,z))

human = False                                                                                                           #booleans

name1, age1, human1 = "Jessy", 26, True                                                                                 #multiple assigmnent
Jack = Jonas = Cora = Johanna = Tobias = "IT Klasse"

print("Hallo "+name.upper()+" wie geht es dir?")                                                                        #string Methods .method() nach nem string
print("ich bin: "+str(age)+" Jahre alt.")                                                                               #+str() um int oder andere werte zu schreiben

print("Ich bin: "+str(height)+" cm groß!")

print("Bin ich menschlich? "+str(human))

print(Jack)
print(Jonas)
print(Cora)
print(Johanna)

#_______________________________________________________________________________________________________________________

print(name*4)                                                                                                           #wie oft soll etwas displayd wer



print(float(age))
print(int(height))
print(int(len(name*4)))
#_______________________________________________________________________________________________________________________

#Slicing indexing[] slice() [start:stop:step]

first_name = my_name[0:4]
last_name = my_name[5:]
encode_name = my_name[0:12:3]
reversed_name = my_name[::-1]

print(last_name)
print(first_name)
print(encode_name)
print(reversed_name)


website = "http://google.com"
website1 = "http://Youtube.com"

slice = slice(7,-4)

print(website[slice])
print(website1[slice])

#_______________________________________________________________________________________________________________________
#if statements
#logical operator (and,or,not)

if age == 100:
    print("GZ du alter sack!")
elif age >= 18:
    print("https://pornhub.com")
elif age < 0:
    print("was bist du? Benjamin Button?")
else:
    print("Sorry nicht alt genug!:c")

temp = int(input("Wie warm ist es heute?: "))

if not(temp >= 0 and temp <= 30):
    print("übel das schlimme Wetter!")
elif not(temp < 0 or temp > 30):
    print("Temperatur geht voll klar!")
else:
    print("Scheiß wetter!")
#_______________________________________________________________________________________________________________________
#while loops: werden solange ausgeführt bis sich die Parameter ändern
#while not: siehe Zeile 4-14!!!!!!

#while 1==1:
    #print("Hilfe ich stecke Fest")
#_______________________________________________________________________________________________________________________
#for loop ein loop der eine bestimmte anzahl wiederholt wird
#for i in range(10):
    #print(i+1)

#for i in range (50,100+1,2): #(start,ende,schritte)
    #print(i)

for seconds in range(3,-3,-1):
    print(seconds)
    time.sleep(1)
print("Du hast echt geduld.")
#_______________________________________________________________________________________________________________________
#nested loops (ein loop in einem loop)

rows = int(input("Wie viele reihen soll das Quadrat haben?: "))
collums = int(input("Wie viele Zeilen soll es haben?: "))
zeichen = (input("Welches Zeichen soll verwendet werden?: "))

for i in range(rows):
    for j in range (collums):
        print(zeichen, end="")
    print()

#_______________________________________________________________________________________________________________________

#while 1==1:
    #print("Orthografitrainer ist kacke!")
    #print("Die Deutsche Sprache macht micht Aggresiv!")
    #print("Ich finde Sortieren langweilig!")
#_______________________________________________________________________________________________________________________
#tuple ähnlich wie listen aber nicht änderbar

student = ("Jack",25,"male")
print(student.count("Jack"))
print(student.index("male"))

for x in student:
    print (x)

if "Jack" in student:
    print("Jack ist da!")
else:
    print("Jack ist abwesend!")

#_______________________________________________________________________________________________________________________
#dictionary = veränderbare variablen paare mit einem einzigartigen key, sehr schnell, benutzen hashing
#KÖNNEN GEÄNDERT BZW GEUPDATED WERDEN WÄREND DAS PROGRAMM LÄUFT!

mitschueler = {'Jonas':'IT-Klasse',
               'Jack':'IT-Klasse',
               'Paul':'Kaufmann',
               'eyecandy':'Kaufmann',
               'Wiland':'IT-Klasse'}

mitschueler.update({'Cora':'IT-Klasse'})
mitschueler.update({'Wiland':'Kaufmann'})

#print(mitschueler.get('Jack'))

for key,value in mitschueler.items():
    print(key,value)


#_______________________________________________________________________________________________________________________
#set = ansammlung von unegordneten variablen, keine dublikate
geschirr = {"messer","gabel","löffel"}
geschirr1 = {"flache Teller", "tiefe Teller","Schüssel","löffel"}

#geschirr.update(geschirr1)
essens_tisch = geschirr.union(geschirr1)

#print(geschirr.difference(geschirr1))
for x in geschirr:
    print(x)


#_______________________________________________________________________________________________________________________
#listen = werden benutzt um mehr als eine Variable in einer Variable zu verstauen
#2d lists= Listen von listen

valoranks = ["Iron","Bronze","Silber","Gold","Platin","Diamond","Ascendent","Immortal","Radiant"]
students = ["Jonas","Cora","Johanna","Maxim"]

noobs = [valoranks, students]

print(valoranks[0][1])

#List commands

#valoranks.append("Unranked")
#valoranks.remove("Iron")
#valoranks.pop() #removes last index
#valoranks.insert(7,"Ascendent")
#valoranks.sort() #alpabetisch
#valoranks.clear()

#_______________________________________________________________________________________________________________________
#loop control statements
#break=beendet den loop komplett
#continue=Skippt den nächsten loop zyklus
#pass=macht garnichts ist einfach ein Platzhalter

while True:
    loopname = input("Wer geht dir am meisten auf den Sack?: ")
    if loopname != "":
        break

telefonnummer = "+49-1523-4567890"

for i in telefonnummer:
    if i == "-":
        continue
    print(i, end="")

for i in range (1,21):
    if i == "13":
        pass
    print(i)
#_______________________________________________________________________________________________________________________
#
klassenliste = {}

yn = input("Willst du jemanden zu Klassenliste hinzufügen oder sie abrufen?")
if yn =""



#_______________________________________________________________________________________________________________________
#Taschenrechner


operandie = input("Wie willst du rechnen?(+ - / *): ")
zahl1 = int(input("Welche zahl?: "))
zahl2 = int(input("Soll mit welcher Zahl berechnet werden?: "))
summe = None

if operandie == '+':
    summe = zahl1 + zahl2
    print(summe)
elif operandie == '-':
    summe = zahl1 - zahl2
    print(summe)
elif operandie == '*':
    summe = zahl1 * zahl2
    print(summe)
elif operandie == '/':
    summe = zahl1 / zahl2
    print(summe)
else:
    print("dann halt nicht")

#_______________________________________________________________________________________________________________________
#Wurzel ziehen

sqrt = None

while not sqrt:
    sqrt = float(input("Von welcher zahl willst du die Quadratwurzel?: "))

print("Die Wurzel deiner Zahl ist: "+str(math.sqrt(sqrt)))

#_______________________________________________________________________________________________________________________
#Hochrechnen

pwrrechnen = None
pwrhoch = None

while not pwrrechnen:
    pwrrechnen = int(input("Welche Zahl soll hoch gerechnet werden?: "))

while not pwrhoch:
    pwrhoch = int(input("Hoch wie viel?: "))

hochsumme = pow(pwrrechnen, pwrhoch)
print(str(pwrrechnen)+" Hoch "+str(pwrhoch)+" = "+str(hochsumme))

#_______________________________________________________________________________________________________________________
#Prozent rechnen

prozentwert = None
grundwert = None

while not prozentwert:
    prozentwert = float(input("Was ist der Prozentwert(Kleine Zahl)?: "))




while not grundwert:
    grundwert = float(input("Was ist der Grundwert(Hohe Zahl)?: "))

prozentsatz = prozentwert * 100 / grundwert

print(str(prozentwert)+" von "+str(grundwert)+" Sind: "+str(prozentsatz)+"%")

#_______________________________________________________________________________________________________________________
#dreisatz
drei_satz_pvariable0 = None
drei_satz_pvariable1 = None
drei_satz_avariable0 = None

while not drei_satz_pvariable0:
    drei_satz_pvariable0 = float(input("Was ist die erste proportionale Zahl?: "))

while not drei_satz_pvariable1:
    drei_satz_pvariable1 = float(input("Was ist die zweite proportionale Zahl?: "))

while not drei_satz_pvariable0:
    drei_satz_avariable0 = float(input("Was ist die erste anti-proportionale Zahl?(ist meist die such zahl): "))

drei_satz_avariable1 = drei_satz_pvariable1 * drei_satz_avariable0 / drei_satz_pvariable0

if drei_satz_avariable1 <0:
    print("Die Antwort ist: "+str(drei_satz_avariable1))


#_______________________________________________________________________________________________________________________
#valo zeugs

vrank = None

while not vrank:
    vrank = input("Welchen Rank hast du in Valorant?: ")

if vrank =="Iron":
    print("Hör auf, auf die Füße zu schauen!")
elif vrank =="Bronze":
    print("Aimlabs = Free")
elif vrank =="Silver":
    print("Coachings + YT is free = KOMM IN DIE GRUPPE!")
elif vrank =="Gold":
    print("Hör auf zu fillen!")
elif vrank =="Platin":
    print("Dein Ego ist größer als meine Zukunft!")
elif vrank =="Diamond":
    print("Vllt mal Strats üben = Freelo")
elif vrank =="Ascendent":
    print("Hardstuck 4 Life UwU")
elif vrank =="Immortal":
    print("No Brain but aim/Dont cheat on your E-Kittens")
elif vrank =="Radiant":
    print("Touch Grass")
else:
    print("Uranked? ganz schön lame")

#_______________________________________________________________________________________________________________________

