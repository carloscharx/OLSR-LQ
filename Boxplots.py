# Fichero encargado de la lectura de los resultados de las predicciones y de representar los boxplots

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy import stats

path = "C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/"
files_name = ["SMOreg", "REPTRee", "IBk","GaussianProcesses"]

figure_num=1;

data_to_plot1= []
means = []
for i in range(len(files_name)):
    values = []
    f = open(path + "resultados" + files_name[i]+".txt")
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
plt.bar(x, means, 1/5, color="blue", align='center')
plt.xticks(range(len(means)),['SMOreg', 'REPTree','IBk','GaussianProcesses'])
plt.title("Average MAE original")
plt.yticks(np.arange(0.00,0.25,0.05))

# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot1, patch_artist=True)

ax.set_title("Comparación de los 4 algoritmos")

for box in bp['boxes']:
    # change outline color
    box.set( color='#7570b3', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

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

ax.set_xticklabels(['SMOreg', 'REPTree','IBk','GaussianProcesses'])

plt.yticks(np.arange(0.00,1.05,0.05))

data_to_plot2= []
means2 = []
for i in range(len(files_name)):
    values = []
    f = open(path + "resultados3" + files_name[i]+".txt")
    for line in f:
        if len(line)!=0:
            values.append(float(line))
    means2.append(np.asarray(values).mean())
    data_to_plot2.append(values)
print(means2)
# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
x = range(len(means2))
plt.bar(x, means2, 1/5, color="green", align='center')
plt.xticks(range(len(means2)),['SMOreg', 'REPTree','IBk','GaussianProcesses'])
plt.title("Average MAE obtenido con los cuatro algoritmos")
plt.yticks(np.arange(0.00,0.05,0.005))

# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot2, patch_artist=True)

ax.set_title("Comparativa en forma de boxplots de los cuatro algoritmos")

for box in bp['boxes']:
    # change outline color
    box.set( color='#7570b3', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

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

ax.set_xticklabels(['SMOReg', 'REPTree','IBk','GaussianProcesses'])

plt.yticks(np.arange(0.00,0.65,0.05))

num_bins=20

blue_patch = mpatches.Patch(color='blue', label='Original')
green_patch = mpatches.Patch(color='green', label='Nuevo')

figSMOreg=plt.figure(figure_num,figsize=(9,6))
figure_num+=1
plt.hist([data_to_plot1[0],data_to_plot2[0]],num_bins,label='Original')
plt.title("Histograma de los datos originales y nuevos de SMOreg")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.legend(handles=[blue_patch,green_patch])
plt.xticks(np.arange(0.00,1.1,0.1))

figREPTRee=plt.figure(figure_num,figsize=(9,6))
figure_num+=1
plt.hist([data_to_plot1[1],data_to_plot2[1]],num_bins,label='Original')
plt.title("Histograma de los datos originales y nuevos de REPTree")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.legend(handles=[blue_patch,green_patch])
plt.xticks(np.arange(0.00,1.1,0.1))

figIBk=plt.figure(figure_num,figsize=(9,6))
figure_num+=1
plt.hist([data_to_plot1[2],data_to_plot2[2]],num_bins,label='Original')
plt.title("Histograma de los datos originales y nuevos de IBK")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.legend(handles=[blue_patch,green_patch])
plt.xticks(np.arange(0.00,1.1,0.1))

figGP=plt.figure(figure_num,figsize=(9,6))
figure_num+=1
plt.hist([data_to_plot1[3], data_to_plot2[3]],num_bins,label='Original')
plt.title("Histograma de los datos originales y nuevos de GaussianProcesses")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.legend(handles=[blue_patch,green_patch])
plt.xticks(np.arange(0.00,1.1,0.1))

blue_patch = mpatches.Patch(color='blue', label='SMOReg')
green_patch = mpatches.Patch(color='green', label='REPTree')
red_patch = mpatches.Patch(color='red', label='IBk')
cyan_patch = mpatches.Patch(color='cyan', label='GaussianProcesses')
figComp=plt.figure(figure_num,figsize=(9,6))
figure_num+=1
plt.hist([data_to_plot2[0], data_to_plot2[1],data_to_plot2[2],data_to_plot2[3]],num_bins,label='Original',)
plt.title("Histograma de los valores de MAE obtenidos")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.legend(handles=[blue_patch,green_patch,red_patch,cyan_patch])
plt.xticks(np.arange(0.00,1.1,0.1))

# Descomentar para ver las gráficas
plt.show()

datos1 = np.asarray(data_to_plot2[0])
datos2 = np.asarray(data_to_plot2[1])
datos3 = np.asarray(data_to_plot2[2])
datos4 = np.asarray(data_to_plot2[3])

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

# Se comprueba que las medias no son iguales

