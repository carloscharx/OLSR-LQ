# comparacion de algoritmos

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


files_name = ["1horatrain","1diatrain","6diatrain"]

path = "C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/resultadosORTO"

figure_num=1;
data_to_plot= []
means = []
for i in range(len(files_name)):
    values = []
    f = open(path + files_name[i]+".txt")
    for line in f:
        if len(line)!=0:
            values.append(float(line))
    means.append(np.asarray(values).mean())
    data_to_plot.append(values)
print(means)
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
plt.plot(data_to_plot[0])
plt.plot(data_to_plot[1])
plt.plot(data_to_plot[2])
plt.show()


path = "C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/resultadosRT"

figure_num=1;
data_to_plot= []
means = []
for i in range(len(files_name)):
    values = []
    f = open(path + files_name[i]+".txt")
    for line in f:
        if len(line)!=0:
            values.append(float(line))
    means.append(np.asarray(values).mean())
    data_to_plot.append(values)
print(means)
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
plt.plot(data_to_plot[0])
plt.plot(data_to_plot[1])
plt.plot(data_to_plot[2])
plt.show()