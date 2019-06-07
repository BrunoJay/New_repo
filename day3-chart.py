import matplotlib.pyplot as plt

labels = 'AFRICA', 'ASIA', 'EUROPE'

fracs = [54, 48, 44]

# Make square figures and axes

plt.pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True)

plt.savefig('Pie Chart')# -*- coding: utf-8 -*-

