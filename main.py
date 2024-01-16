from datetime import datetime, timedelta, date

def daterange(start_date, end_date):
    """Erzeugt ein Datum für jeden Tag zwischen start_date und end_date."""
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

def berechne_schultage_bis_heute(startdatum, enddatum, ferientage):
    # Schulwochentage zählen (Montag bis Freitag), Ferien ausschließen
    schultage = 0
    aktuelles_datum = startdatum
    while aktuelles_datum <= enddatum and aktuelles_datum <= datetime.now().date():
        if aktuelles_datum.weekday() < 5 and aktuelles_datum not in ferientage:  # Montag bis Freitag ausschließlich Ferien
            schultage += 1
        aktuelles_datum += timedelta(days=1)
    return schultage

def berechne_abwesenheit_bis_heute(fehlstunden, schultage_bis_heute, stunden_pro_tag):
    # Gesamtstunden bis heute
    gesamtstunden_bis_heute = schultage_bis_heute * stunden_pro_tag

    # Abwesenheitsrate berechnen
    abwesenheitsrate = (fehlstunden / gesamtstunden_bis_heute) * 100 if gesamtstunden_bis_heute > 0 else 0

    return abwesenheitsrate

# Ferienzeiträume und einzelne Ferientage
ferienzeitraeume = [
    (date(2023, 10, 28), date(2023, 11, 5)),
    (date(2023, 12, 23), date(2024, 1, 7)),
    (date(2024, 2, 10), date(2024, 2, 18)),
    (date(2024, 3, 28), date(2024, 4, 2)),
    (date(2024, 4, 25), date(2024, 4, 28)),
]
einzelne_ferientage = [date(2023, 12, 8), date(2024, 5, 1), date(2024, 5, 20)]

# Ferien in einzelne Tage umwandeln
ferientage = set(einzelne_ferientage)
for start, ende in ferienzeitraeume:
    for single_date in daterange(start, ende):
        ferientage.add(single_date)

# Schuljahr Informationen
startdatum = date(2023, 9, 5)
enddatum = date(2024, 6, 14)

# Durchschnittliche Stunden pro Schultag (Annahme: gleiche Verteilung über die Woche)
stunden_pro_wochentag = {"Montag": 8, "Dienstag": 6, "Mittwoch": 9, "Donnerstag": 6, "Freitag": 6}
durchschnitt_stunden_pro_tag = sum(stunden_pro_wochentag.values()) / len(stunden_pro_wochentag)

# Interaktive Eingabe von Fehlstunden
while True:
    fehlstunden_input = input("Geben Sie die Anzahl der Fehlstunden ein (oder 'exit' zum Beenden): ")
    if fehlstunden_input.lower() == 'exit':
        break
    try:
        fehlstunden = float(fehlstunden_input)
        # Anzahl der Schultage bis heute berechnen, unter Berücksichtigung der Ferien
        schultage_bis_heute = berechne_schultage_bis_heute(startdatum, enddatum, ferientage)
        # Abwesenheitsrate berechnen
        abwesenheitsrate = berechne_abwesenheit_bis_heute(fehlstunden, schultage_bis_heute, durchschnitt_stunden_pro_tag)
        # Ergebnisse ausgeben
        print(f"Anzahl der Schultage bis heute: {schultage_bis_heute}")
        print(f"Abwesenheitsrate: {abwesenheitsrate:.2f}%")
        print("Hinweis: Eine Fehlerquote von etwa 0.5% ist möglich.")
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine Zahl oder 'exit' ein.")

