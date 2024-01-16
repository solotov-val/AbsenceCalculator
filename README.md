# Schulabwesenheitsrechner

## Beschreibung
Dieses Projekt ist ein einfacher Python-basierter Rechner, der dazu dient, die Abwesenheitsrate von Schülern zu überwachen und zu verwalten. Es berechnet die Anzahl der bis zum aktuellen Datum vergangenen Schultage, die aktuelle Abwesenheitsrate, sowie die verbleibende erlaubte Abwesenheit in Stunden und Tagen für das gesamte Schuljahr, basierend auf einem Limit von 25%.

## Features
- Berechnung der Anzahl der Schultage bis zum aktuellen Datum.
- Ermittlung der aktuellen Abwesenheitsrate in Prozent.
- Berechnung der verbleibenden erlaubten Abwesenheitsstunden und -tage für das gesamte Schuljahr.

## Voraussetzungen
- Python 3.x

## Installation
1. Stellen Sie sicher, dass Python auf Ihrem System installiert ist.
2. Klonen Sie das Repository oder laden Sie die Skriptdateien herunter.
3. Optional: Installieren Sie `prettytable` für eine formatierte Tabellenausgabe: pip install prettytable


## Benutzung
Führen Sie das Skript in einem Python-fähigen Terminal oder einer IDE aus. Geben Sie bei Aufforderung die Anzahl der Fehlstunden ein. Das Programm berechnet und zeigt die relevanten Abwesenheitsdaten an.

## Beispiel
Geben Sie die Anzahl der Fehlstunden ein (oder 'exit' zum Beenden): 10
Ausgabe:
+---------------------------------------------------------+
| Kategorie                                 | Wert        |
+---------------------------------------------------------+
| Anzahl der Schultage bis heute            | 100         |
| Abwesenheitsrate                          | 10.00%      |
| Verbleibende Fehlstunden bis 25% (gesamt) | 150 Stunden |
| Verbleibende Fehltage bis 25% (gesamt)    | 18.75 Tage  |
+---------------------------------------------------------+


## Lizenz
[MIT License](LICENSE)

## Kontakt
Für Fragen und Anregungen können Sie [hier](https://github.com/solotov-val/AbsenceCalculator/issues)ein Issue eröffnen.
