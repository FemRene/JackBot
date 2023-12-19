import random

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
        "aussehen": ["Du bist wunderschön", "Dein Aussehen ist großartig","Du hast schöne Augen","Du slayst","Dein Style ist sehr cool","Du riechst nach Old Spice, mega nice *sniff*","Du wirkst sehr talentiert","Du hast nen coolen Vibe","Big Dick energy","Du bist ein richtiger Schnuggiputz uwu"],
        "lieblingsfarbe": "Meine Lieblingsfarbe ist Blau und deine?",
        "uhrzeit": "Bitte hier Uhrzeit Value eingeben",
        "mathe": ma_rechner, #Ma_rechner wird hier gesetzt
        "findest": ["Gefällt mir !","Das ist echt cool !","slayed mega !","Sehr gut !","finde ich gut","naja könnte besser sein"]
    }

    print("Hallo, ich bin JACK'O'BOT, ich hoffe du hast ein Schönen Tag")
    print("Wenn du mich beenden willst schreib einfach 'bye'")

    # Benutzereingabe initialisieren
    userinput = input(str("Über was möchtest du mit mir reden?: "))

    while userinput.lower() != "bye":
        userinput = input("Deine Frage/Antwort?: ")

        user_woerter = userinput.lower().split()

        antwort_gefunden = False
        for einzel_woerter in user_woerter:
            if einzel_woerter in reactions:
                #Liste für "aussehen" in Dictionary "Reactions" wird aufgerufen
                if einzel_woerter == "aussehen":
                    print(random.choice(reactions[einzel_woerter]))
                #Liste für "findest" in Dictionary "Reactions" wird aufgerufen
                elif einzel_woerter == "findest":
                    print(random.choice(reactions[einzel_woerter]))
                #Ma_rechner wird hier initialisiert
                elif einzel_woerter == "mathe":
                    reactions[einzel_woerter]()

                else:
                    print(reactions[einzel_woerter])
                antwort_gefunden = True

        if not antwort_gefunden:
            print(random.choice(random_antwort))

    print("Ein schönen Tag Wünsch ich dir!")

if __name__ == "__main__":
    main()