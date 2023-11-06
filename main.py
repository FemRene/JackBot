import math

name = input("Wie ist dein Name?: ")

age = int(input("Wie alt bist du?: "))

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
#logical operator (and,or)

if age == 100:
    print("GZ du alter sack!")
elif age >= 18:
    print("https://pornhub.com")
elif age < 0:
    print("was bist du? Benjamin Button?")
else:
    print("Sorry nicht alt genug!:c")

temp = int(input("Wie warm ist es heute?: "))

if temp >= 0 and temp <= 30:
    print("Temperatur geht voll klar!")
elif temp < 0 or temp > 30:
    print("übel das schlimme Wetter!")
else:
    print("Scheiß wetter!")
