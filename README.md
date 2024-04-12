## Installationsanleitung
- lade den Ordner herunter und öffne den Ordner in Visual Studio Code
- Öffne ein Terminal
- Erstelle eine neue Python-Umgebung
  - python -m venv .venv
- Aktiviere die Umgebung 
  - Windows: .venv\Scripts\Activate
- Installiere die Pakete
  - Entweder mit pip install <paketname>
  - Oder mit pip install -r requirement.txt
- Dann wird das Programm mit python main.py gestartet


## Wie wird der Code genutzt?
Zuerst werden die Dateien importiert und mithilfe des Moduls load_data die Daten von power_W geladen.
Anschließend werden die Daten mithilfe der Bubble Sort vom Modul sort sortiert.
Es wird ein Graph erstellt, der um 90° gedreht wird.
Die Werte der x-Achse sind in Sekunden angegeben, diese werden mithilfe einer Array Liste in Minuten konvertiert.
Die Grafik wird im Ordner figures als power_curve.png abgespeichert.




