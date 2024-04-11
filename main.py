# load_data.py
def load_data(filename):
    # Hier den Code zum Laden der Daten aus der CSV-Datei einfügen
    pass
# sort.py
def bubble_sort(data):
    # Hier den Code für den Bubble-Sort-Algorithmus einfügen
    pass
# main.py
import load_data
import sort
import matplotlib.pyplot as plt

# Daten laden
data = load_data.load_data("activity.csv")

# Daten sortieren
sorted_data = sort.bubble_sort(data)

# Grafik erstellen und speichern
plt.plot(sorted_data)
plt.savefig("figures/power_curve.png")

hallo
