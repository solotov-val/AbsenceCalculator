from datetime import datetime, timedelta, date

def daterange(start_date, end_date):
    """Erzeugt ein Datum für jeden Tag zwischen start_date und end_date."""
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

def berechne_gesamte_schultage(startdatum, enddatum, ferientage):
    gesamte_schultage = 0
    for single_date in daterange(startdatum, enddatum):
        if single_date.weekday() < 5 and single_date not in ferientage:  # Montag bis Freitag ausschließlich Ferien
            gesamte_schultage += 1
    return gesamte_schultage

def berechne_schultage_bis_heute(startdatum, enddatum, ferientage):
    schultage = 0
    aktuelles_datum = startdatum
    while aktuelles_datum <= enddatum and aktuelles_datum <= datetime.now().date():
        if aktuelles_datum.weekday() < 5 and aktuelles_datum not in ferientage:
            schultage += 1
        aktuelles_datum += timedelta(days=1)
    return schultage

def berechne_abwesenheit_bis_heute(fehlstunden, schultage_bis_heute, stunden_pro_tag):
    gesamtstunden_bis_heute = schultage_bis_heute * stunden_pro_tag
    abwesenheitsrate = (fehlstunden / gesamtstunden_bis_heute) * 100 if gesamtstunden_bis_heute > 0 else 0
    return abwesenheitsrate

def berechne_verbleibende_abwesenheit_gesamt(abwesenheitsrate, stunden_pro_tag, gesamte_schultage):
    maximal_zulaessige_abwesenheit = 25
    verbleibende_abwesenheit = maximal_zulaessige_abwesenheit - abwesenheitsrate

    verbleibende_fehlstunden_gesamt = verbleibende_abwesenheit * (gesamte_schultage * stunden_pro_tag) / 100
    verbleibende_fehltage_gesamt = verbleibende_fehlstunden_gesamt / stunden_pro_tag

    return verbleibende_abwesenheit, verbleibende_fehlstunden_gesamt, verbleibende_fehltage_gesamt

# Ferienzeiträume und einzelne Ferientage definieren
ferienzeitraeume = [
    (date(2023, 10, 28), date(2023, 11, 5)),
    (date(2023, 12, 23), date(2024, 1, 7)),
    (date(2024, 2, 10), date(2024, 2, 18)),
    (date(2024, 3, 28), date(2024, 4, 2)),
    (date(2024, 4, 25), date(2024, 4, 28)),
]
einzelne_ferientage = [date(2023, 12, 8), date(2024, 5, 1), date(2024, 5, 20)]

# Ferientage in einzelne Tage umwandeln
ferientage = set(einzelne_ferientage)
for start, ende in ferienzeitraeume:
    for single_date in daterange(start, ende):
        ferientage.add(single_date)

# Schuljahr Informationen
startdatum = date(2023, 9, 5)
enddatum = date(2024, 6, 14)

# Durchschnittliche Stunden pro Schultag
stunden_pro_wochentag = {"Montag": 8, "Dienstag": 6, "Mittwoch": 9, "Donnerstag": 6, "Freitag": 6}
durchschnitt_stunden_pro_tag = sum(stunden_pro_wochentag.values()) / len(stunden_pro_wochentag)

# Hilfsfunktionen für farbige Ausgabe
def print_in_color(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "endc": "\033[0m"
    }
    print(colors.get(color, colors["white"]) + text + colors["endc"])


# Interaktive Eingabe von Fehlstunden
while True:
    fehlstunden_input = input("Geben Sie die Anzahl der Fehlstunden ein (oder 'exit' zum Beenden): ")
    if fehlstunden_input.lower() == 'exit':
        break
    try:
        fehlstunden = float(fehlstunden_input)
        schultage_bis_heute = berechne_schultage_bis_heute(startdatum, enddatum, ferientage)
        gesamte_schultage = berechne_gesamte_schultage(startdatum, enddatum, ferientage)
        abwesenheitsrate = berechne_abwesenheit_bis_heute(fehlstunden, schultage_bis_heute, durchschnitt_stunden_pro_tag)
        verbleibende_abwesenheit, verbleibende_fehlstunden_gesamt, verbleibende_fehltage_gesamt = berechne_verbleibende_abwesenheit_gesamt(
            abwesenheitsrate, durchschnitt_stunden_pro_tag, gesamte_schultage)

        print_in_color(f"Anzahl der Schultage bis heute: {schultage_bis_heute}", "blue")
        print_in_color(f"Abwesenheitsrate: {abwesenheitsrate:.2f}%", "cyan")
        print_in_color(f"Verbleibende Abwesenheit bis zum Limit von 25% für das gesamte Schuljahr: {verbleibende_abwesenheit:.2f}%", "green")
        print_in_color(f"Verbleibende Fehlstunden bis zum Limit von 25% für das gesamte Schuljahr: {verbleibende_fehlstunden_gesamt:.2f} Stunden", "yellow")
        print_in_color(f"Verbleibende Fehltage bis zum Limit von 25% für das gesamte Schuljahr: {verbleibende_fehltage_gesamt:.2f} Tage", "magenta")
    except ValueError:
        print_in_color("Ungültige Eingabe. Bitte geben Sie eine Zahl oder 'exit' ein.", "red")


