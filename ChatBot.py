import random
from datetime import datetime
import pytz

# Zeitzone Berlin
zeitzone_berlin = pytz.timezone('Europe/Berlin')
# Uhrzeit initialisieren
now = datetime.now(zeitzone_berlin)
# Derzeitige Uhrzeit initialisieren
current_time = now.strftime("%H:%M:%S")

# Benutzerklasse um Daten zu erfassen
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

# Benutzer initialisieren
benutzer = None

# Nutzerinformationen in der Klasse "benutzer" speichern
def save_user_name():
    global benutzer
    if benutzer is None:
        name = input("Wie ist dein Name?: ")
        height = input("Wie groß bist du in cm?: ")
        benutzer = Benutzer(name, height)
        print(f"Benutzer '{name}' mit der Größe '{height} cm' wurde erstellt.")
    else:
        print("Ein Benutzer existiert bereits.")

# Ja/Nein Schleife für Funktionen
def input_yes_no(text):
    y = input(text)
    return y.strip().lower() == "y"

# Funktion Taschenrechner
def ma_rechner():
    try:
        while input_yes_no("Willst du den Taschenrechner benutzen (Y/N): "):
            operandie = input("Wie willst du rechnen? (+ - / *): ")
            if operandie not in ['+', '-', '/', '*']:
                print("Ungültige Operation!")
                continue

            zahl1 = int(input("Welche Zahl?: "))
            zahl2 = int(input("Soll mit welcher Zahl berechnet werden?: "))
            summe = None

            if operandie == '+':
                summe = zahl1 + zahl2
            elif operandie == '-':
                summe = zahl1 - zahl2
            elif operandie == '*':
                summe = zahl1 * zahl2
            elif operandie == '/':
                if zahl2 != 0:
                    summe = zahl1 / zahl2
                else:
                    print("Du kannst nicht durch 0 dividieren.")
                    continue

            print(f"{zahl1} {operandie} {zahl2} = {summe}")

    except ValueError:
        print("Nur Zahlen sind erlaubt!")
    except Exception as e:
        print("Es ist ein Fehler aufgetreten:", e)

# Dreisatz
def dreisatz():
    while input_yes_no("Willst du ein Dreisatz ausrechnen? (Y/N): "):
        try:
            drei_satz_pvariable0 = float(input("Was ist die erste proportionale Zahl?: "))
            drei_satz_pvariable1 = float(input("Was ist die zweite proportionale Zahl?: "))
            drei_satz_avariable0 = float(input("Was ist die erste anti-proportionale Zahl (ist meist die Suchzahl)?: "))

            dsumme = drei_satz_pvariable1 * drei_satz_avariable0 / drei_satz_pvariable0
            print("Die Antwort ist:", dsumme)
        except ValueError:
            print("Bitte gib gültige Zahlen ein.")

# cm in Inch
def incm():
    while input_yes_no("Willst du den CM/INCH Umrechner benutzen? (Y/N): "):
        einheit = input("Welche Einheit hat das Maß? (cm/inch): ").strip().lower()

        try:
            if einheit == "cm":
                cm = float(input("Größe in cm?: "))
                inch = cm / 2.54
                print(f"{cm} cm sind: {inch:.2f} inch")
            elif einheit == "inch":
                inch = float(input("Größe in inch?: "))
                cm = inch * 2.54
                print(f"{inch} inch sind: {cm:.2f} cm")
            else:
                print("Ungültige Eingabe. Bitte 'cm' oder 'inch' wählen.")
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")

# FC Umrechner
def fc():
    while input_yes_no("Willst du den Fahrenheit/Celsius Umrechner benutzen? (Y/N): "):
        einheit = input("Welche Einheit hat das Maß? (Fahrenheit/Celsius): ").strip().lower()

        try:
            if einheit == "fahrenheit":
                fa = float(input("Wie viel Grad Fahrenheit?: "))
                gradcelsius = (fa - 32) / 1.8
                print(f"{fa} Grad Fahrenheit sind: {gradcelsius:.2f} Grad Celsius")
            elif einheit == "celsius":
                gradcelsius = float(input("Wie viel Grad Celsius?: "))
                fa = (gradcelsius * 1.8) + 32
                print(f"{gradcelsius}°C sind: {fa:.2f}°F")
            else:
                print("Ungültige Eingabe. Bitte 'Fahrenheit' oder 'Celsius' wählen.")
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")

# Prozentrechnen
def prozentrechnen():
    while input_yes_no("Willst du Prozentrechnen? (Y/N): "):
        try:
            prozentwert = float(input("Was ist der Prozentwert (kleine Zahl)?: "))
            grundwert = float(input("Was ist der Grundwert (hohe Zahl)?: "))

            prozentsatz = (prozentwert * 100) / grundwert
            print(f"{prozentwert} von {grundwert} sind: {prozentsatz:.2f}%")
        except ValueError:
            print("Bitte gib gültige Zahlen ein.")

# Main Funktion
def main():
    # Zufällige Antworten generieren
    random_antwort = [
        "Oh, wirklich",
        "Ich finde du siehst heute toll aus, nur mal so am Rande",
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
        "aussehen": [
            "Du bist wunderschön", 
            "Dein Aussehen ist großartig",
            "Du hast schöne Augen",
            "Du slayst",
            "Dein Style ist sehr cool",
            "Du riechst nach Old Spice, mega nice *sniff*",
            "Du wirkst sehr talentiert",
            "Du hast nen coolen Vibe",
            "Big Dick Energy",
            "Du bist ein richtiger Schnuggiputz uwu"
        ],
        "wie findest du mein Aussehen?": [
            "Gefällt mir!",
            "Das ist echt cool!",
            "Slayed mega!",
            "Sehr gut!",
            "Finde ich gut",
            "Ich glaube längere Haare würden dir besser stehen."
        ],
        "lieblingsfarbe": "Meine Lieblingsfarbe ist Blau und deine?",
        "uhrzeit": current_time,
        "Was kannst du?": "Meine Features sind: Taschenrechner, Dreisatz (Einfach), Inch/CM Rechner, Fahrenheit/Celsius Rechner, Prozentrechnen, Speicher meine Daten, Benutzer info, Benutzer löschen",
        "taschenrechner": ma_rechner,
        "dreisatz": dreisatz,
        "cm rechner": incm,
        "celsius umrech": fc,
        "prozent": prozentrechnen,
        "speicher meine daten": save_user_name,
        "benutzer info": lambda: benutzer.info() if benutzer else print("Kein Benutzer gespeichert."),
        "benutzer löschen": lambda: benutzer.delete() if benutzer else print("Kein Benutzer gespeichert."),
        "wie geht es dir?": "Mir geht es gut, danke! Und dir?",
        "gut, danke": "Das freut mich zu hören!",
        "schlecht": "Oh, das tut mir leid zu hören.",
        "was machst du gerne?": "Ich unterhalte mich gerne und lerne ständig dazu!",
        "hast du Geschwister?": "Ich bin ein Einzelkind, aber ich habe viele Geschwister-Bots!",
        "bist du ein Mensch?": "Ich bin ein Chatbot, programmiert, um zu helfen und zu unterhalten!",
        "magst du Musik?": "Musik ist toll! Was ist dein Lieblingslied?",
        "ich bin müde": "Vielleicht solltest du eine Pause machen und dich ausruhen.",
        "erzähl mir einen Witz": "Warum hat das Mathematikbuch geweint? Weil es viele Probleme hatte!",
        "was ist dein Ziel?": "Mein Ziel ist es, dir zu helfen und dich zu unterhalten!",
        "was ist das Wetter?": "Leider habe ich keinen Zugriff auf Wetterdaten.",
        "wie alt bist du?": "Ich bin ein virtueller Assistent, Alter ist für mich irrelevant!",
        "benutzer": "Mit 'Benutzer info' kannst du dir deine Daten anzeigen lassen. \nMit 'Benutzer löschen' kannst du deine Daten löschen. \nMit 'Speicher meine Daten' kannst du einen Benutzer anlegen."
        "help": """ Lieblingsfarbe = Ich sag dir welche meine LIelingsfarbe ist-
        
                    uhrzeit             = Ich sag dir, in deiner Zeitzone, deine Uhrzeit an. 
                    
                    Was kannst du?      = Gibt dir eine kurze Übersicht über meine Features.
                    
                    taschenrechner      = Ich habe einen eingebauten Taschenrechner, damit kannst ihn aufrufen.
                    
                    dreisatz            = Damit kannst du den Dreisatz ausrechnen.
                    
                    cm rechner          = Damit kannst du CM in INCH umrechnen.
                    
                    celsius umrechner   = Damit kannst du Celsius in Fahrenheit und andersrum umrechnen."""
    }

    print("""                    *****************
               ******               ******
           ****                           ****
        ****                                 ***
      ***                                       ***
     **           ***               ***           **
   **           *******           *******          ***
  **            *******           *******            **
 **             *******           *******             **
 **               ***               ***               **
**                                                     **
**       *                                     *       **
**      **                                     **      **
 **   ****                                     ****   **
 **      **                                   **      **
  **       ***                             ***       **
   ***       ****                       ****       ***
     **         ******             ******         **
      ***            ***************            ***
        ****                                 ****
           ****                           ****
               ******               ******
                    *****************""")
 
    print("Hallo, ich bin JACK'O'BOT, ich hoffe du hast einen schönen Tag")
    print("Bitte vergiss nicht, ich bin ein Roboter. Ich kann nichts dafür, wie mich mein Erschaffer programmiert hat.")
    print("Wenn du mich beenden willst, schreibe einfach 'bye'.")
    print("___________________________________________________________________________________________________________")
    print("Wenn du mal nicht weiter kommst, schreibe einfach 'Was kannst du?' dann zeige ich dir meine Features.")

    # Benutzereingabe initialisieren
    userinput = input("Über was möchtest du mit mir reden?: ").strip().lower()
    
    while userinput != "bye":
        userinput = input("Deine Frage/Antwort?: ").strip().lower()

        antwort_gefunden = False
        for key in reactions:
            if key in userinput:
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

    print("Einen schönen Tag wünsche ich dir!")

if __name__ == "__main__":
    main()
