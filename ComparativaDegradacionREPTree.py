# Fichero encargado de la lectura de los resultados de REPTree para distinto tamaño de conjunto de entrenamiento

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy import stats

path = "C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/"
files_name = "RTdegradado"

figure_num=1;

data_to_plot1= []
means = []
for i in range(12):
    values = []
    f = open(path + "resultados" + files_name+ str(i+1)+".txt")
    for line in f:
        if len(line)!=0:
            values.append(float(line))
    means.append(np.asarray(values).mean())
    data_to_plot1.append(values)
print(means)
# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
x = range(len(means))
plt.bar(x, means, 1/5, color="#14F026", align='center')
plt.xticks(range(len(means)),['144','288','432','576','720','864','1008','1152','1296','1440','1584','1728'])
plt.title("MAE promedio de RT, varios tamaños test y entrenamiento 288 unidades")
plt.yticks(np.arange(0.00,0.115,0.005))
plt.grid()


# 0.0038631309 * test + 0.0458432175 test va de 1 a 12
plt.plot([-1, 12], [0.0458, 0.09598], 'k-', lw=2) # esto está hecho un jaleo porque el gráfico que quiero pintar yo va de 0 a 13 e internamente creo que lo tiene de 0 a 12

# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot1, patch_artist=True)

ax.set_title("Boxplots de RT, varios tamaños de test y entrenamiento 288 unidades")

for box in bp['boxes']:
    # change outline color
    box.set( color='#7570b3', linewidth=2)
    # change fill color
    box.set( facecolor = '#14F026' )

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='#7570b3', linewidth=2)

## change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color='#7570b3', linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='#b2df8a', linewidth=2)

## change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5)

ax.set_xticklabels(['144','288','432','576','720','864','1008','1152','1296','1440','1584','1728'])

plt.yticks(np.arange(0.00,1.05,0.05))

file_name = "RTEvolution"

f= open(path + "resultados" + file_name+ ".txt");
h=288;
w=979;
Matrix = [[0 for x in range(w)] for y in range(h)]
for i in range(w):
    for j in range(h):
        Matrix[j][i]=f.readline();
plt.figure(3)
plt.plot(Matrix, 'bo', markersize=1)

file_name = "RTEvolution2"

f= open(path + "resultados" + file_name+ ".txt");
h=288;
w=979;
Matrix = [[0 for x in range(w)] for y in range(h)]
for i in range(w):
    for j in range(h):
        Matrix[j][i]=f.readline();
plt.figure(4)
plt.plot(Matrix, 'bo', markersize=1)










# Descomentar para ver las gráficas
plt.show()
