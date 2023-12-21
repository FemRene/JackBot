import random
from datetime import datetime
import pytz

class Benutzer:

    def __init__(self,name,height,eyecolor,haircolor):
        self.name = name
        self.height = height
    def info(self):
        pass
    
    def delete(self):
        pass


#Timezone Berlin
zeitzone_berlin = pytz.timezone('Europe/Berlin')
#Uhrzeit initialisieren
now = datetime.now(zeitzone_berlin)
#Derzeitige Uhrzeit initialisieren
current_time = now.strftime("%H:%M:%S")

#Yes/No schleife für funktionen
def input_yes_no(text):
    y = input(text)
    if y.upper()=="Y":
        return True
    else:
        return False
#funktion Taschenrechner
def ma_rechner():
    try:
        while True:
            y = input_yes_no("Willst du den Taschenrechner benutzen (Y/N): ")
            if not y:
                break

            operandie = input("Wie willst du rechnen? (+ - / *): ")
            if operandie not in ['+', '-', '/', '*']:
                print("Ungültige Operation!")
                continue

            zahl1 = int(input("Welche Zahl?: "))
            zahl2 = int(input("Soll mit welcher Zahl berechnet werden?: "))
            summe = None

            if operandie == '+':
                summe = zahl1 + zahl2
                print(str(zahl1) + " + " + str(zahl2) + " = " + str(summe))
            elif operandie == '-':
                summe = zahl1 - zahl2
                print(str(zahl1) + " - " + str(zahl2) + " = " + str(summe))
            elif operandie == '*':
                summe = zahl1 * zahl2
                print(str(zahl1) + " * " + str(zahl2) + " = " + str(summe))
            elif operandie == '/':
                if zahl2 != 0:
                    summe = zahl1 / zahl2
                    print(str(zahl1) + " / " + str(zahl2) + " = " + str(summe))
                else:
                    print("Du kannst nicht durch 0 dividieren.")

    except ValueError as e:
        print("Nur Zahlen sind erlaubt!")

    except Exception as e:
        print("Es ist ein Fehler aufgetreten:", e)

    except ZeroDivisionError as e:
        print(e)
        print("Du kannst nicht durch 0 Dividieren.")

    except ValueError as e:
        print(e)
        print("Nur Zahlen!")

    except Exception as e:
        print(e)
        print("Es scheint so als hättest etwas versucht, was in der Mathematik nicht funktioniert!")
#dreisatz
def dreisatz():

    while True:
        y = input_yes_no("Willst du ein dreisatz ausrechen?(Y/N): ")
        if y:
            break
        
        drei_satz_pvariable0 = float_input("Was ist die erste proportionale Zahl?: ")
        drei_satz_pvariable1 = float_input("Was ist die zweite proportionale Zahl?: ")
        drei_satz_avariable0 = float_input("Was ist die erste anti-proportionale Zahl?(ist meist die such zahl): ")

        dsumme = drei_satz_pvariable1 * drei_satz_avariable0 / drei_satz_pvariable0
        print("Die Antwort ist: "+str(dsumme))
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
#FC umrechner
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
#Main funktion
def main():
    # zufällige Antworten generieren
    random_antwort = [
        "Oh, wirklich",
        "Ich finde du siehst heute toll aus, nur mal so am rande",
        "Interessant.....",
        "Ich verstehe.....",
        "Bist du dir sicher?",
        "Wenn du das sagst",
        "Ich glaub das wird mir gerade zu viel",
        "Das ist sehr kompliziert"
    ]
    # Reaktionen auf bestimmte Schlüsselwörter
    reactions = {
        "hallo": "Hallo?",
        "essen": "Ich bin eine Maschine, ich habe keine Geschmacksknospen :C",
        "aussehen": ["Du bist wunderschön", 
                    "Dein Aussehen ist großartig",
                    "Du hast schöne Augen",
                    "Du slayst",
                    "Dein Style ist sehr cool",
                    "Du riechst nach Old Spice, mega nice *sniff*",
                    "Du wirkst sehr talentiert",
                    "Du hast nen coolen Vibe",
                    "Big Dick energy",
                    "Du bist ein richtiger Schnuggiputz uwu"],
        "wie findest du meine Aussehen?": ["Gefällt mir !",
                                    "Das ist echt cool !",
                                    "slayed mega !",
                                    "Sehr gut !",
                                    "finde ich gut",
                                    "Ich glaube längre Haare würden dir besser stehen."],
        "lieblingsfarbe": "Meine Lieblingsfarbe ist Blau und deine?",
        "uhrzeit":current_time,
        "was kannst du":"Meine features sind: Taschenrechner, Dreisatz(Einfach), inch/cm Rechner, Fahrenheit/Celsius Rechner, Prozentrechnen",
        "taschenrechner":dreisatz,
        "cm rechner":incm,
        "celsius umrechnen":fc
        "prozent":prozentrechnen
        
    }
    print("Hallo, ich bin JACK'O'BOT, ich hoffe du hast ein Schönen Tag")
    print("Bitte vergiss nicht, ich bin ein Roboter ich kann nicht's dafür wie mich mein Erschaffer Programiert hat.")
    print("Wenn du mich beenden willst schreib einfach 'bye'")

    # Benutzereingabe initialisieren
    userinput = input(str("Über was möchtest du mit mir reden?: "))
    
    while userinput.lower() != "bye":
        userinput = input("Deine Frage/Antwort?: ")

        user_woerter = userinput.lower().split()

        antwort_gefunden = False
        for key in reactions:
            if key.lower() in userinput.lower():
                if isinstance(reactions[key], list):
                    print(random.choice(reactions[key]))
                else:
                    print(reactions[key])
                antwort_gefunden = True
                break

        if not antwort_gefunden:
            print(random.choice(random_antwort))

    print("Ein schönen Tag Wünsch ich dir!")

if __name__ == "__main__":
    main()