# Fichero encargado de la lectura de los resultados de las predicciones y de representar los boxplots

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy import stats

path = "C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/"
files_name = ["SMOreg", "RT", "IBk","GaussianProcesses"]

figure_num=1;

data_to_plot1= []
means = []
for i in range(len(files_name)):
    values = []
    f = open(path + "resultadosSiTimestampConPotencias" + files_name[i]+".txt")
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
plt.bar(x, means, 1/5, color=["#566ADA","#14F026","#E11515","#E15F15"], align='center')
plt.grid(True)


plt.xticks(range(len(means)),['SVM', 'RT','kNN','GPR'])
plt.title("MAE promedio")
plt.yticks(np.arange(0.00,0.05,0.01))

# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot1, patch_artist=True)
ax.grid(True)

ax.set_title("Boxplots de los valores de MAE")

i=0
for box in bp['boxes']:
    if i==0:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#566ADA' )
    elif i==1:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#14F026' )
    elif i==2:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#E11515' )
    elif i==3:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#E15F15' )
    i+=1

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

ax.set_xticklabels(['SVM', 'RT','kNN','GPR'])

plt.yticks(np.arange(0.00,0.6,0.05))

num_bins=20
blue_patch = mpatches.Patch(color='#566ADA', label='SVM')
green_patch = mpatches.Patch(color='#14F026', label='RT')
red_patch = mpatches.Patch(color='#E11515', label='kNN')
cyan_patch = mpatches.Patch(color='#E15F15', label='GPR')
figComp=plt.figure(figure_num,figsize=(9,6))
figure_num+=1
plt.hist([data_to_plot1[0], data_to_plot1[1],data_to_plot1[2],data_to_plot1[3]],num_bins,label='Original',color=('#566ADA','#14F026','#E11515','#E15F15'))
plt.title("Histograma de los valores de MAE obtenidos")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.legend(handles=[blue_patch,green_patch,red_patch,cyan_patch])
plt.xticks(np.arange(0.00,1.1,0.1))

datos1 = np.asarray(data_to_plot1[0])
datos2 = np.asarray(data_to_plot1[1])
datos3 = np.asarray(data_to_plot1[2])
datos4 = np.asarray(data_to_plot1[3])

def twoSampZ(X1, X2, mudiff, sd1, sd2, n1, n2):
    from numpy import sqrt, abs, round
    from scipy.stats import norm
    pooledSE = sqrt(sd1**2/n1 + sd2**2/n2)
    z = ((X1 - X2) - mudiff)/pooledSE
    pval = 2*(1 - norm.cdf(abs(z)))
    return round(z, 3), round(pval, 4)
# Función obtenida en http://stats.stackexchange.com/questions/124096/two-samples-z-test-in-python
# El procedimiento es el mismo que el del libro

z, p = twoSampZ(datos1.mean(), datos2.mean(), 0, datos1.std(), datos2.std(), 979, 979)
print(z, p)

z, p = twoSampZ(datos1.mean(), datos3.mean(), 0, datos1.std(), datos3.std(), 979, 979)
print(z, p)

z, p = twoSampZ(datos1.mean(), datos4.mean(), 0, datos1.std(), datos4.std(), 979, 979)
print(z, p)

z, p = twoSampZ(datos2.mean(), datos3.mean(), 0, datos2.std(), datos3.std(), 979, 979)
print(z, p)

z, p = twoSampZ(datos2.mean(), datos4.mean(), 0, datos2.std(), datos4.std(), 979, 979)
print(z, p)

z, p = twoSampZ(datos3.mean(), datos4.mean(), 0, datos3.std(), datos4.std(), 979, 979)
print(z, p)

plt.show()

