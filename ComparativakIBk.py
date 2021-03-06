# Fichero encargado de la lectura de los resultados de IBk para varios valores de k

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy import stats

path = "C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/"
files_name = "IBk"

figure_num=1;

data_to_plot1= []
means = []
for i in range(10):
    values = []
    f = open(path + "resultadosk" + str(i+1) + files_name+".txt")
    for line in f:
        if len(line)!=0:
            values.append(float(line))
    means.append(np.asarray(values).mean())
    data_to_plot1.append(values)
values = []
f = open(path + "resultadoskX"  + files_name+".txt")
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
plt.bar(x, means, 1/5, color="#E11515", align='center')
plt.grid(True)
plt.xticks(range(len(means)),['k=1','k=2','k=3','k=4','k=5','k=6','k=7','k=8','k=9','k=10','k=X'])
plt.title("MAE promedio de kNN para k=1 hasta k=10 y XV")
plt.yticks(np.arange(0.00,0.06,0.005))

# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot1, patch_artist=True)

ax.set_title("Boxplots de kNN para los valores de k=1 hasta k=10 y XV")
ax.grid(True)

for box in bp['boxes']:
    # change outline color
    box.set( color='#7570b3', linewidth=2)
    # change fill color
    box.set( facecolor = '#E11515' )

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

ax.set_xticklabels(['k=1','k=2','k=3','k=4','k=5','k=6','k=7','k=8','k=9','k=10','k=X'])

plt.yticks(np.arange(0.00,1.05,0.05))


num_bins=20

# blue_patch = mpatches.Patch(color='blue', label='k=1')
# green_patch = mpatches.Patch(color='green', label='k=2')
# red_patch = mpatches.Patch(color='red', label='k=3')
# black_patch = mpatches.Patch(color='black', label='k=4')
# yellow_patch = mpatches.Patch(color='yellow', label='k=5')
# brown_patch = mpatches.Patch(color='brown', label='k=6')
# pink_patch = mpatches.Patch(color='pink', label='k=7')
# orange_patch = mpatches.Patch(color='orange', label='k=8')
# grey_patch = mpatches.Patch(color='grey', label='k=9')
# purple_patch = mpatches.Patch(color='purple', label='k=10')


# figIBk=plt.figure(figure_num,figsize=(9,6))
# figure_num+=1
# plt.hist([data_to_plot1[0],data_to_plot1[1],data_to_plot1[2],data_to_plot1[3],data_to_plot1[4],data_to_plot1[5],data_to_plot1[6],data_to_plot1[7],data_to_plot1[8],data_to_plot1[9],data_to_plot1[10]])
# plt.title("Histograma de IBk para k=1 hasta k=10 y XV")
# plt.xlabel("Valor")
# plt.ylabel("Frecuencia")
#plt.legend(handles=[blue_patch,green_patch,red_patch,black_patch,yellow_patch,brown_patch,pink_patch,orange_patch,grey_patch,purple_patch])

# Descomentar para ver las gráficas
plt.show()
