import random

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
    "mathe": "Leider kann ich im moment noch nicht Rechnen, frag doch meinen Ersteller",
    "findest": ["Gefällt mir !","Das ist echt cool !","Der slayed mega !","Seh gut !"]
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
            if einzel_woerter == "aussehen":
                print(random.choice(reactions[einzel_woerter]))
            elif einzel_woerter == "findest":
                print(random.choice(reactions[einzel_woerter]))
            else:
                print(reactions[einzel_woerter])
            antwort_gefunden = True

    if not antwort_gefunden:
        print(random.choice(random_antwort))

print("Ein schönen Tag Wünsch ich dir!")