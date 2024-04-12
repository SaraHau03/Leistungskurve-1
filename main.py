from load_data import load_data
import sort
import matplotlib.pyplot as plt
import numpy as np

data = load_data('activity.csv')
power_W = data['PowerOriginal']
print(power_W)

sorted_data = sort.bubble_sort(power_W)

img_new = sorted_data[::-1]

time_s = np.array(list(range(0,len(img_new))))/60

plt.plot(time_s, img_new)
plt.xlabel("Time/min")
plt.ylabel("W/kg")


plt.savefig("figures/power_curve.png")
plt.show()

