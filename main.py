from load_data import load_data
import sort
import matplotlib.pyplot as plt
import numpy as np
import csv

data = load_data('activity.csv')
power_W = data['PowerOriginal']
print(power_W)


# Daten sortieren

#sorted_data = sort.bubble_sort()
sorted_data = sort.bubble_sort(power_W)
# Grafik erstellen und speichern


#plt.plot(sorted_data)
img_new = np.rot90(sorted_data, 2)
plt.plot(img_new)

plt.savefig("figures/power_curve.png")


