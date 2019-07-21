# Fichero encargado de la lectura de los resultados de REPTree para varios valores de lag window

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy import stats

path = "C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/"
files_name = "RTlag"

figure_num=1;

data_to_plot1= []
means = []
for i in range(24):
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
plt.xticks(range(len(means)),['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'])
plt.title("MAE promedio de RT para lag window desde 1 hasta 24")
plt.yticks(np.arange(0.00,0.03,0.003))
plt.grid()

# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
# Create an axes instance
ax = fig.add_subplot(111)
ax.grid(True)
# Create the boxplot
bp = ax.boxplot(data_to_plot1, patch_artist=True)

ax.set_title("Boxplots de RT para valores de lag window desde 1 hasta 24")

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

ax.set_xticklabels(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'])

plt.yticks(np.arange(0.00,0.7,0.05))


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

def twoSampZ(X1, X2, mudiff, sd1, sd2, n1, n2):
    from numpy import sqrt, abs, round
    from scipy.stats import norm
    pooledSE = sqrt(sd1**2/n1 + sd2**2/n2)
    z = ((X1 - X2) - mudiff)/pooledSE
    pval = 2*(1 - norm.cdf(abs(z)))
    return round(z, 3), round(pval, 4)
# Función obtenida en http://stats.stackexchange.com/questions/124096/two-samples-z-test-in-python
# El procedimiento es el mismo que el del libro

datosref=np.asarray(data_to_plot1[11])
for i in range(24):
    if i==11:
        continue
    datos=np.asarray(data_to_plot1[i])
    z, p = twoSampZ(datosref.mean(), datos.mean(), 0, datosref.std(), datos.std(), 979, 979)
    print(z, p)

# No se puede rechazar la hipótesis nula de que las medias sean iguales