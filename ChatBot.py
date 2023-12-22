import random
from datetime import datetime
import pytz

#Timezone Berlin
zeitzone_berlin = pytz.timezone('Europe/Berlin')
#Uhrzeit initialisieren
now = datetime.now(zeitzone_berlin)
#Derzeitige Uhrzeit initialisieren
current_time = now.strftime("%H:%M:%S")

#Benutzerklasse um Daten zu erfassen
class Benutzer:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def info(self):
        print("Folgender Benutzer ist gespeichert:")
        print(f"Name: {self.name}, Größe: {self.height} cm")

    def delete(self):
        self.name = None
        self.height = None
        print("Die Benutzer Information wurde erfolgreich gelöscht")

benutzer = None

#Nutzer informationen in der Klasse "benutzer" speichern
def save_user_name(benutzer):
    if benutzer is None:
        name = input("Wie ist dein Name?: ")
        height = input("Wie groß bist du in cm?: ")
        benutzer = Benutzer(name, height)
        print(f"Benutzer '{name}' mit der Größe '{height} cm' wurde erstellt.")
    else:
        print("Ein Benutzer existiert bereits.")

    return benutzer

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
        x = input_yes_no("Willst du den CM/INCH Umrechner benutzen? (Y/N): ")
        if not x:
            break
        
        einheit = input("Welche Einheit hat das Maß? (cm/inch): ")

        if einheit == "cm":
            cm = int(input("Größe in cm?: "))
            inch = cm * 2.54
            print(f"{cm}cm sind: {inch}inch")
        elif einheit == "inch":
            inch = int(input("Größe in inch?: "))
            cm = inch / 2.54
            print(f"{inch}inch sind: {cm}cm")
        else:
            print("Ungültige Eingabe. Bitte 'cm' oder 'inch' wählen.")
#FC umrechner
def fc():
    while True:
        x = input_yes_no("Willst du den Fahrenheit/Celsius Umrechner benutzen? (Y/N): ")
        if not x:
            break
    
        einheit = input("Welche Einheit hat das Maß? (Fahrenheit/Celsius): ").upper()

        if einheit == "FAHRENHEIT":
            fa = float(input("Wie viel Grad Fahrenheit?: "))
            gradcelsius = (fa - 32) / 1.8
            print(f"{fa} Grad Fahrenheit sind: {gradcelsius} Grad Celsius")
        elif einheit == "CELSIUS":
            gradcelsius = float(input("Wie viel Grad Celsius?: "))
            fa = (gradcelsius * 1.8) + 32
            print(f"{gradcelsius}°C sind: {fa}°F")
        else:
            print("Ungültige Eingabe. Bitte 'Fahrenheit' oder 'Celsius' wählen.")
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
benutzer = None
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
        "was kannst du":"Meine features sind: Taschenrechner, Dreisatz(Einfach), inch/cm Rechner, Fahrenheit/Celsius Rechner, Prozentrechnen, Speicher meine Daten, Benutzer info, Benutzer löschen",
        "taschenrechner":dreisatz,
        "cm rechner":incm,
        "celsius umrechnen":fc,
        "prozent":prozentrechnen,
        "Speicher meine Daten": lambda benutzer=benutzer: save_user_name(benutzer),
        "Benutzer info": lambda: benutzer.info() if benutzer else print("Kein Benutzer gespeichert."),
        "Benutzer löschen": lambda: benutzer.delete() if benutzer else print("Kein Benutzer gespeichert."),
        "wie geht es dir?": "Mir geht es gut, danke! Und dir?",
        "gut, danke": "Das freut mich zu hören!",
        "schlecht": "Oh, das tut mir leid zu hören.",
        "was machst du gerne?": "Ich unterhalte mich gerne und lerne ständig dazu!",
        "hast du Geschwister?": "Ich bin ein Einzelkind, aber ich habe viele Geschwister-Bots!",
        "bist du ein Mensch?": "Ich bin ein Chatbot, programmiert, um zu helfen und zu unterhalten!",
        "magst du Musik?": "Musik ist toll! Was ist dein Lieblingslied?",
        "ich bin müde": "Vielleicht solltest du eine Pause machen und dich ausruhen.",
        "erzähl mir einen Witz": "Warum hat der Mathematikbuch geweint? Weil es viele Probleme hatte!",
        "was ist dein Ziel?": "Mein Ziel ist es, dir zu helfen und dich zu unterhalten!",
        "was ist das Wetter?": "Leider habe ich keinen Zugriff auf Wetterdaten.",
        "wie alt bist du?": "Ich bin ein virtueller Assistent, Alter ist für mich irrelevant!",
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
                if callable(reactions[key]):
                    reactions[key]()
                elif isinstance(reactions[key], list):
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