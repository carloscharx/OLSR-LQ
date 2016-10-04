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

# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
x = range(len(means))
plt.bar(x, means, 1/5, color="blue", align='center')
plt.xticks(range(len(means)),['SMOReg', 'REPTree','IBk','GaussianProcesses'])
plt.title("Average MAE original")

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

ax.set_xticklabels(['SMOReg', 'REPTree','IBk','GaussianProcesses'])

plt.yticks(np.arange(0.00,1.05,0.05))

data_to_plot2= []
means2 = []
for i in range(len(files_name)):
    values = []
    f = open(path + "resultadosBis" + files_name[i]+".txt")
    for line in f:
        if len(line)!=0:
            values.append(float(line))
    means2.append(np.asarray(values).mean())
    data_to_plot2.append(values)

# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
x = range(len(means2))
plt.bar(x, means2, 1/5, color="green", align='center')
plt.xticks(range(len(means2)),['SMOReg', 'REPTree','IBk','GaussianProcesses'])
plt.title("Average MAE después de la mejora de SMOreg y GaussianProcesses")

# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot2, patch_artist=True)

ax.set_title("Comparación de los 4 algoritmos, después de la mejora en SMOreg y GaussianProcesses")

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

plt.yticks(np.arange(0.00,1.05,0.05))

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
plt.hist(data_to_plot1[1],num_bins)
plt.title("Histograma de los datos de REPTree")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.xticks(np.arange(0.00,1.1,0.1))

figIBk=plt.figure(figure_num,figsize=(9,6))
figure_num+=1
plt.hist(data_to_plot1[2],num_bins)
plt.title("Histograma de los datos de IBK")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.xticks(np.arange(0.00,1.1,0.1))

figGP=plt.figure(figure_num,figsize=(9,6))
figure_num+=1
plt.hist([data_to_plot1[3], data_to_plot2[3]],num_bins)
plt.title("Histograma de los datos originales y nuevos de GaussianProcesses")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.legend(handles=[blue_patch,green_patch])
plt.xticks(np.arange(0.00,1.1,0.1))

# Descomentar para ver las gráficas
plt.show()

# Test de Gaussianidad(kstest perform the Kolmogorov-Smirnov test for goodness of fit)
datos = np.asarray(data_to_plot1[3])
normed_data=((datos-datos.mean())/datos.std())
print(stats.kstest(normed_data,'norm'))
print("Como el pvalue es 0, rechazamos la hipótesis nula de que las dos distribuciones sean iguales "
      "es decir, los datos NO son gaussianos")

# Entonces t-test no se hace