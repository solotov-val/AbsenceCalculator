from datetime import datetime, timedelta

def berechne_tage_bis_heute(startdatum, enddatum):
    # Heutiges Datum
    heute = datetime.now().date()

    # Tage zählen
    tage_bis_heute = 0
    aktuelles_datum = startdatum
    while aktuelles_datum <= heute and aktuelles_datum <= enddatum:
        if aktuelles_datum.weekday() < 5:  # Montag bis Freitag
            tage_bis_heute += 1
        aktuelles_datum += timedelta(days=1)

    return tage_bis_heute

def berechne_abwesenheit_bis_heute(fehlstunden, tage_bis_heute, stunden_pro_tag):
    # Gesamtstunden bis heute
    gesamtstunden_bis_heute = tage_bis_heute * stunden_pro_tag

    # Abwesenheitsrate berechnen
    abwesenheitsrate = (fehlstunden / gesamtstunden_bis_heute) * 100 if gesamtstunden_bis_heute > 0 else 0

    return abwesenheitsrate

def hauptprogramm():
    # Schuljahr Informationen
    startdatum = datetime(2023, 9, 5).date()
    enddatum = datetime(2024, 6, 14).date()

    # Durchschnittliche Stunden pro Tag (Annahme: gleiche Verteilung über die Woche)
    stunden_pro_wochentag = {"Montag": 8, "Dienstag": 6, "Mittwoch": 9, "Donnerstag": 6, "Freitag": 6}
    durchschnitt_stunden_pro_tag = sum(stunden_pro_wochentag.values()) / len(stunden_pro_wochentag)

    # Tage bis heute berechnen
    tage_bis_heute = berechne_tage_bis_heute(startdatum, enddatum)

    # Eingabe der Fehlstunden
    try:
        fehlstunden = int(input("Bitte geben Sie die Anzahl Ihrer Fehlstunden ein: "))
        if fehlstunden < 0:
            raise ValueError("Die Anzahl der Fehlstunden kann nicht negativ sein.")
    except ValueError as e:
        print("Ungültige Eingabe. Bitte geben Sie eine gültige Zahl ein.")
        return

    # Abwesenheitsrate berechnen
    abwesenheitsrate = berechne_abwesenheit_bis_heute(fehlstunden, tage_bis_heute, durchschnitt_stunden_pro_tag)

    # Ergebnisse ausgeben
    print(f"Anzahl der Unterrichtstage bis heute: {tage_bis_heute}")
    print(f"Abwesenheitsrate: {abwesenheitsrate:.2f}%")

# Hauptprogramm ausführen
hauptprogramm()
