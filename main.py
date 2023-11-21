import math
import time
import random

#_______________________________________________________________________________________________________________________
#https://www.youtube.com/watch?v=XKHEtdqhLK8  Video
#_______________________________________________________________________________________________________________________
#functions = I WILL NOT REPEAT MY CODE!

def hello(name):
    print("Hallo "+name)
    print("https://pointerpointer.com/")
#_______________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________
#float while schleife (Der code wird erst fortgesetzt wenn eine Eingabe erfolgt ist)

def float_input(text):
    v = None
    while not v:
        v = float(input(text))
    return v
#_______________________________________________________________________________________________________________________
#string while schleife (Der code wird erst fortgesetzt wenn eine Eingabe erfolgt ist)

def string_input(name):
    x = ""
    while len(x) ==0:
        x = input(name)
    return x
#_______________________________________________________________________________________________________________________
#int while schleife (Der code wird erst fortgesetzt wenn eine Eingabe erfolgt ist)

def int_input(text):
    y = None
    while not y:
        y = int(input(text))
    return y
#_______________________________________________________________________________________________________________________
#Input schleife mit boolean wenn der Input(Y) ist dann gibt er TRUE zurück andernfalls False

def input_yes_no(text):
    y = input(text)
    if y.upper=="Y":
        return True
    else:
        return False
#_______________________________________________________________________________________________________________________
#dreisatz

def dreisatz():

    while True:
        y = input_yes_no("Willst du ein dreisatz ausrechen?(Y/N): ")
        if not y:
            break
        
        drei_satz_pvariable0 = float_input("Was ist die erste proportionale Zahl?: ")
        drei_satz_pvariable1 = float_input("Was ist die zweite proportionale Zahl?: ")
        drei_satz_avariable0 = float_input("Was ist die erste anti-proportionale Zahl?(ist meist die such zahl): ")

        dsumme = drei_satz_pvariable1 * drei_satz_avariable0 / drei_satz_pvariable0
        print("Die Antwort ist: "+str(dsumme))

#_______________________________________________________________________________________________________________________
#dreisatz_antiproportional

def anti_dreisatz():

    while True:
        y= input_yes_no("Willst du denn antiporportionalen Dreisatz ausrechnen?(Y/N): ")
        if not y:
            break

        dreisatz_pvariable0 = float_input("Wie lautet die erste Zahl in deinem Satz?: ")
        dreisatz_pvariable1 = float_input("Wie lautet die zweite Zahl in deinem Satz?: ")
        dreisatz_avariable0 = float_input("Wie lautet die Partner Zahl der Zahl die gesucht wird?: ")

        dpsummer = dreisatz_pvariable1 / dreisatz_pvariable0
        gsumme = dreisatz_avariable0 / dpsummer
        print("Die Antwort ist: "+str(gsumme))
    
#_______________________________________________________________________________________________________________________
#taschenrechner
def taschenrechner():

    while True:
        y = input_yes_no("Willst du den Taschenrechner benutzen(Y/N): ")
        if not y:
            break

        operandie = input("Wie willst du rechnen?(+ - / *): ")
        zahl1 = int(input("Welche zahl?: "))
        zahl2 = int(input("Soll mit welcher Zahl berechnet werden?: "))
        summe = None

        if operandie == '+':
            summe = zahl1 + zahl2
            print(Zahl1+"+"+Zahl2+"="+summe)
        elif operandie == '-':
            summe = zahl1 - zahl2
            print(Zahl1+"-"+Zahl2+"="+summe)
        elif operandie == '*':
            summe = zahl1 * zahl2
            print(Zahl1+"*"+Zahl2+"="+summe)
        elif operandie == '/':
            summe = zahl1 / zahl2
            print(Zahl1+"/"+Zahl2+"="+summe)
        else:
            continue
#_______________________________________________________________________________________________________________________
#2d listen
#l1 = {}
#l2 = {}


#x_liste_updaten = input("Liste updaten oder abrufen?")
#x_liste_updaten = x_liste_updaten.lower

                        
#if x_liste_updaten =="updaten":
#    ls.update = string_input("")


#elif x_liste_updaten=="abrufen":
#for x in ls:
#        print(x)

                        

#_______________________________________________________________________________________________________________________
#cm in Inch

def incm():

    while True:
        x = input_yes_no("Willst du den CM/INCH umrechner benutzen?(Y/N): ")
        if not x:
            break
    einheit = string_input("Welche Einheit hat das Maß?(cm/inch): ")

    while einheit is True:
        if einheit =="cm":
            cm = int_input("Größe?: ")
            inch = cm*2,54
            print(str(cm)+"cm sind: "+str(inch)+"inch")
            return True
        elif einheit =="inch":
            inch1 = int_input("Größe?: ")
            cm1 = inch1/2,54
            print(str(inch1)+"inch sind: "+str(cm1)+"inch")
            return True
        else:
            return False
    
#_______________________________________________________________________________________________________________________
#celsius in Fahrenheit

def fc():

    while True:
        x = input_yes_no("Willst du den Fahrenheit/Celsius umrechner benutzen(Y/N): ")
        if not x:
            break
    
    einheit = string_input("Welche Einheit hat das Maß?(Fahrenheit/Celsius)")
    einheit = einheit.upper

    while einheit is True:
        if einheit =="FAHRENHEIT":
            fa = float_input("Wie viel Grad Fahrenheit?: ")
            gradcelsius = fa/1,8-32
            print(str(fa)+"Grad Fahrenheit sind: "+str(gradcelsius)+"inch")
            return True
        elif einheit =="CELSIUS":
            gradcelsius1 = float_input("Wie viel Grad Celsius?: ")
            fa1 = gradcelsius1*1,8+32
            print(str(gradcelsius1)+"°C sind: "+str(fa1)+"°F")
            return True
        else:
            return False


#_______________________________________________________________________________________________________________________
#Prozent rechnen

def prozentrechnen():

    while True:
        x = input_yes_no("Willst du Prozentrechnen?(Y/N): ")
        if not x:
            break

    prozentwert = None
    grundwert = None

    while not prozentwert:
        prozentwert = float(input("Was ist der Prozentwert(Kleine Zahl)?: "))




    while not grundwert:
        grundwert = float(input("Was ist der Grundwert(Hohe Zahl)?: "))

    prozentsatz = prozentwert * 100 / grundwert
    print(str(prozentwert)+" von "+str(grundwert)+" Sind: "+str(prozentsatz)+"%")

#_______________________________________________________________________________________________________________________
#hochrechnen

def hochrechnen():

    while True:
        x = input_yes_no("Willst du Hochrechnen?(Y/N): ")
        if not x:
            break
    
    pwrrechnen = None
    pwrhoch = None

    while not pwrrechnen:
        pwrrechnen = int(input("Welche Zahl soll hoch gerechnet werden?: "))

    while not pwrhoch:
        pwrhoch = int(input("Hoch wie viel?: "))

    hochsumme = pow(pwrrechnen, pwrhoch)
    print(str(pwrrechnen)+" Hoch "+str(pwrhoch)+" = "+str(hochsumme))

#_______________________________________________________________________________________________________________________
#Wurzel ziehen

def sqrt():
    while True:
        y = input_yes_no("Willst du die Wurzel einer Zahl?(Y/N): ")
        if not y:
            break

    sqrt = None

    float_input(sqrt)
    print("Die Wurzel deiner Zahl ist: "+str(math.sqrt(sqrt)))

#_______________________________________________________________________________________________________________________
#Satz des Pythagoras

def pythago():
    while True:
        y = input_yes_no("Willst du den Satz des Pythagoras ausrechnen?(Y/N): ")
        if not y:
            break

    seite_a = float_input("Wie lang ist seite A?: ")
    seite_b = float_input("Wie lang ist seite B?: ")

    seite_c = seite_a + seite_b
    print("Die größe der Seite C ist "+str(seite_c)+"²")
    
#_______________________________________________________________________________________________________________________
#Kelvin in Celsius

def kelvin_celsius():
    while True:
        y = input_yes_no("Kelvin/Celsius Umrechner benutzen?(Y/N): ")
        if not y:
            break
    x[0:0] = input("Welche einheit soll umgerechnet werden?(Grad/Kelvin): ")
    
    if x.upper=="K":

        kelvinh = float_input("Wie viel Kelvin?: ")
        grads = kelvin - 273.15
        print(str(kelvin)+"Kelvin sind: "+str(grad)+"°C")

    else:

        gradh = float_input("Wie viel Grad?: ")
        kelvinh = gradh + 273.25
        print(str(gradh)+"°C sind: "+str(kelvinh)+"Kelvin")

#_______________________________________________________________________________________________________________________
#identifer
def identifer(first,middle,last):
    print("Hallo "+first+" "+middle+" "+last)

#_______________________________________________________________________________________________________________________
#args ums mehr als nur einer value ohne eine reinfolge zu senden
#tupels können nur geändert werdenn sie zu einer list formatiert werden

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(5,6,1,66,12,52))
#_______________________________________________________________________________________________________________________
#kwargs macht alle agrumente in eine dictionary so das eine funktion mehr Keyword arguments akzeptiert
#WICHTIG FÜR ABSCHLUSSARBEIT

def inputnachweis(**nachweis):

    print("Könnte wie folgt aussehen: ",end="\t \t \t")
    for key,value in nachweis.items():
        print(value,end="\t \t \t")

#_______________________________________________________________________________________________________________________
#binär rechner


def binrel():
    while True:
        x = input_yes_no("Willst du den Binärrechner benutzen?(Y/N): ")

        if not x:
            break
    print("Deine Nummer in Binär: {bina:b}".format(bina=int_input("Eine Zahl die du in Binär haben möchtest: ")))
#_______________________________________________________________________________________________________________________
#octal rechner
def octare():
    while True:
        x = input_yes_no("Willst du den Binärrechner benutzen?(Y/N): ")

        if not x:
            break
    print("Deine Nummer in Binär: {bina:o}".format(bina=int_input("Eine Zahl die du in Binär haben möchtest: ")))
#_______________________________________________________________________________________________________________________
#hexadezimalrechner
def hexare():
    while True:
        x = input_yes_no("Willst du den Binärrechner benutzen?(Y/N): ")

        if not x:
            break
    print("Deine Nummer in Binär: {bina:X}".format(bina=int_input("Eine Zahl die du in Binär haben möchtest: ")))
#_______________________________________________________________________________________________________________________
#Rock,Paper,Sciccors

def rpcgame():
    while True:
        x = input_yes_no("Willst du eine Runde Schere, Stein, Papier spielen?(Y/N): ")
        if not x:
            break

    rpcgame_List = ['Schere', 'Stein', 'Papier']
    computeri = random.choice(rpcgame_List)
    use_input = string_input("Wähle: Schere, Stein oder Papier!: ")

    if use_input =="Schere" and computeri =="Stein":
        print("Du Gewinnst, der Computer hatte {:^5}".format(computeri))
    elif use_input =="Schere" and computeri =="Papier":
        print("Du Verlierst, der Computer hatte {:^5}".format(computeri))
    elif use_input =="Schere" and computeri =="Schere":
        print("Unentschieden, der Computer hatte {:^5}".format(computeri))

    elif use_input =="Stein" and computeri =="Stein":
        print("Unentschieden, der Computer hatte {:^5}".format(computeri))
    elif use_input =="Stein" and computeri =="Papier":
        print("Du Verlierst, der Computer hatte {:^5}".format(computeri))
    elif use_input =="Stein" and computeri =="Schere":
        print("Du Gewinnst, der Computer hatte {:^5}".format(computeri))

    elif use_input =="Papier" and computeri =="Stein":
        print("Du Gewinnst, der Computer hatte {:^5}".format(computeri))
    elif use_input =="Papier" and computeri =="Papier":
        print("Unentschieden, der Computer hatte {:^5}".format(computeri))
    elif use_input =="Papier" and computeri =="Schere":
        print("Du Verlierst, der Computer hatte {:^5}".format(computeri))

#_______________________________________________________________________________________________________________________


#valo zeug
def valo():

    while True:
        x = input_yes_no()
        if not x:
            break

        vrank = None

        while not vrank:
            vrank = input("Welchen Rank hast du in Valorant?: ")
            vrank.upper[0]

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

#_______________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________
#while loop und While not loops mehr info auf ZEILE 105

#_______________________________________________________________________________________________________________________
#dreisatz()
#anti_dreisatz()
#taschenrechner()
#sqrt()
#hochrechnen()
#prozentrechnen()
#pythago()
#valo()
#binre()
rpcgame()
#_______________________________________________________________________________________________________________________


name = string_input("Wie ist dein name?: ")

partner_name = string_input("Wie ist der name deines Partners?: ")

age = int_input("Wie alt bist du?: ")

height = float_input("Wie groß bist du?: ")

my_name = "Jack Saering"

hello(name)
                                                                                                                        #int
#age += 1
pi = 3.14159
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
#randomizer
xrand = random.randint(1,6)
yrand = random.random()

card_list = [1,2,3,4,5,6,7,8,9,"B","D","K","A"]
rock_paper_list = ['Stein','Papier','Schere']

zrand = random.choice(rock_paper_list)
crand = random.shuffle(card_list)

print(zrand)
print(crand)


#_______________________________________________________________________________________________________________________
#str.format()= optional gibt aber mit kontrolle über den user output "{}"Placeholder "Formatfield"

#tier = "Hund"
#item = "Mond"

#print("Der {} spring über den {}".format(tier, item))
#print("Der {0} spring über den {1}".format(tier, item)) #positional argument
print("Der {animals:^5} spring über das {item:^5}".format(animals=string_input("Tier?: "),item=string_input("Gegenstand?: ")))#keywaord argument

#print("Ich hab mir deinen namen geklaut, guck hier: {:5} Bekommst du auch nie wieder".format(name))
#print("Ich hab mir deinen namen geklaut, guck hier: {:>5} Bekommst du auch nie wieder".format(name))
#print("Ich hab mir deinen namen geklaut, guck hier: {:^5} Bekommst du auch nie wieder".format(name))

print("Die nummer Pi ist: {:.2f}".format(pi))

nrlo = 1000000

print("Die nummer ist {,}".format(nrlo))
print("Die nummer ist {.E}".format(nrlo))


#textformat = "Der {} spring über den {}"
#print(text.format(tier,item))

#_______________________________________________________________________________________________________________________
#nachweis test

#inputnachweis(eins=input(),
#              zwei=input(),
#drei=input(),
#              vier=input(),
#              sechs=input(),
#              sieben=input(),
#              acht=input()
#)



#_______________________________________________________________________________________________________________________
#index operator [] = nnützlich um aus sequenzen einzelne part raus zu picken
if(name[0].islower()):
    name = name.capitalize()
    print("Hier dein name mit großem anfangsbuchstaben: " + str(name))

#_______________________________________________________________________________________________________________________
#keyword argument damit können identifer für den caller bereit gestellt werden wenn mehr information zu einer Funktion geschickt werden müssen

identifer(first=string_input("\nWie ist dein erster vorname?: "),
          middle=string_input("Wie ist dein zweit Name?: "),
          last=string_input("Wie ist dein nachname?: "))
#_______________________________________________________________________________________________________________________

first_name = name[:4].upper()
last_name = name[5:].upper()
last_character_name = name[-1]

print("dein vor name ist: "+str(first_name))
print("Dein Nachname ist"+str(last_name))
print(last_character_name)


#_______________________________________________________________________________________________________________________
#args

print(add(5,6,1,66,12,52))

#_______________________________________________________________________________________________________________________

print(name*4)#wie oft soll etwas displayd wer



print(float(age))
print(int(height))
print(int(len(name*4)))
#_______________________________________________________________________________________________________________________

#nested funktions
print(round(abs(input("Gib eine negativ nummer ein: "))))

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
#dictionary = veränderbare variablen paare mit einem einzigartigen key, sehr schnell, benutzt hashing
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

for x,y in noobs:
    print(x+"="+y)

#List commands

#valoranks.append("Unranked")
#valoranks.remove("Iron")
#valoranks.pop() #removes last index
#valoranks.insert(7,"Ascendent")
#valoranks.sort() #alpabetisch
#valoranks.clear()
#_______________________________________________________________________________________________________________________

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
#klassenliste dictionary
klassenliste = {}
klvalue = ""


while True:
    x = input_yes_no("Willst du die Klassenliste bearbeiten?(Y/N): ")
    if not x:
        break

    yn = input("Willst du jemanden zu Klassenliste hinzufügen oder sie abrufen?")
    if yn =="hinzufügen":
        klvalue = input("Bitte:Name, Klasse: ")
        klassenliste.update(klvalue)

    elif yn =="abrufen":
        for x in klassenliste:
            print(x)
    else:
        print("Keine eingabe erkannt")
        pass
#_______________________________________________________________________________________________________________________



#_______________________________________________________________________________________________________________________




