# Fichero encargado de la lectura de los resultados de las predicciones y de representar los boxplots

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy import stats

path = "C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/"
files_name = ["SMOreg", "RT", "IBk","GaussianProcesses"]

figure_num=1;

data_to_plot1= []
means1 = []
for i in range(len(files_name)):
    values = []
    #f = open(path + "resultadosSiTimestampConPotencias" + files_name[i]+".txt")
    #f = open(path + "resultados1diaSiTimestampConPotencias" + files_name[i]+".txt")
    f = open(path + "resultados1horaSiTimestampConPotencias" + files_name[i]+".txt")
    for line in f:
        if len(line)!=0:
            values.append(float(line))
    means1.append(np.asarray(values).mean())
    data_to_plot1.append(values)
print(means1)
# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
x = range(len(means1))
plt.bar(x, means1, 1/5, color=["#566ADA","#14F026","#E11515","#E15F15"], align='center')
plt.grid(True)


plt.xticks(range(len(means1)),['SVM', 'RT','kNN','GPR'])
plt.title("MAE promedio")
plt.yticks(np.arange(0.00,0.07,0.01))

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

plt.yticks(np.arange(0.00,0.8,0.05))




data_to_plot2= []
means2 = []
for i in range(len(files_name)):
    values = []
    #f = open(path + "resultados1SiTimestamp" + files_name[i]+".txt")
    #f = open(path + "resultados1diaSiTimestamp" + files_name[i]+".txt")
    f = open(path + "resultados1horaSiTimestamp" + files_name[i]+".txt")
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
plt.bar(x, means2, 1/5, color=["#566ADA","#14F026","#E11515","#E15F15"], align='center')
plt.grid(True)


plt.xticks(range(len(means2)),['SVM', 'RT','kNN','GPR'])
plt.title("MAE promedio")
plt.yticks(np.arange(0.00,0.07,0.01))

# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot2, patch_artist=True)
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

plt.yticks(np.arange(0.00,0.8,0.05))



data_to_plot3= []
means3 = []
for i in range(len(files_name)):
    values = []
    #f = open(path + "resultadosNoTimestamp" + files_name[i]+".txt")
    #f = open(path + "resultados1diaNoTimestamp" + files_name[i]+".txt")
    f = open(path + "resultados1horaNoTimestamp" + files_name[i]+".txt")
    for line in f:
        if len(line)!=0:
            values.append(float(line))
    means3.append(np.asarray(values).mean())
    data_to_plot3.append(values)
print(means3)
# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
x = range(len(means3))
plt.bar(x, means3, 1/5, color=["#566ADA","#14F026","#E11515","#E15F15"], align='center')
plt.grid(True)


plt.xticks(range(len(means3)),['SVM', 'RT','kNN','GPR'])
plt.title("MAE promedio")
plt.yticks(np.arange(0.00,0.07,0.01))

# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot3, patch_artist=True)
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

plt.yticks(np.arange(0.00,0.8,0.05))


# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1

x = np.arange(len(means3))

plt.bar(x-0.2, means1, 1/5, color=["#566ADA","#14F026","#E11515","#E15F15"], align='center')
plt.bar(x, means2, 1/5, color=["#566ADA","#14F026","#E11515","#E15F15"], align='center')
plt.bar(x+0.2, means3, 1/5, color=["#566ADA","#14F026","#E11515","#E15F15"], align='center')
plt.xticks(range(len(means3)),['SVM', 'RT','kNN','GPR'])
plt.grid(True)
plt.title("MAE promedio con timestamp, potencias y productos; con timestamp; y sin timestamp")
plt.yticks(np.arange(0.00,0.06,0.01))




data_to_plot4= []
for i in range(len(files_name)):
    values = []
    #f = open(path + "resultadosSiTimestampConPotencias" + files_name[i]+".txt")
    #f = open(path + "resultados1diaSiTimestampConPotencias" + files_name[i]+".txt")
    f = open(path + "resultados1horaSiTimestampConPotencias" + files_name[i]+".txt")
    for line in f:
        if len(line)!=0:
            values.append(float(line))
    data_to_plot4.append(values)
    values = []
    #f = open(path + "resultadosSiTimestamp" + files_name[i]+".txt")
    #f = open(path + "resultados1diaSiTimestamp" + files_name[i]+".txt")
    f = open(path + "resultados1horaSiTimestamp" + files_name[i]+".txt")
    for line in f:
        if len(line)!=0:
            values.append(float(line))
    data_to_plot4.append(values)
    values = []
    #f = open(path + "resultadosNoTimestamp" + files_name[i]+".txt")
    #f = open(path + "resultados1diaNoTimestamp" + files_name[i]+".txt")
    f = open(path + "resultados1horaNoTimestamp" + files_name[i]+".txt")
    for line in f:
        if len(line)!=0:
            values.append(float(line))
    data_to_plot4.append(values)

# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1
# Create an axes instance
ax = fig.add_subplot(111)

meanpointprops = dict(marker='D', markeredgecolor='black',
                      markerfacecolor='pink')

# Create the boxplot
bp = ax.boxplot(data_to_plot4, positions=[-0.2,0,0.2,0.8,1,1.2,1.8,2,2.2,2.8,3,3.2],patch_artist=True,showmeans=True,meanprops=meanpointprops,widths=0.15)
ax.grid(True)

ax.set_title("Boxplots de los valores de MAE")
plt.xticks(range(len(means3)),['SVM', 'RT','kNN','GPR'])
plt.grid(True)
plt.title("Boxplots con timestamp, potencias y productos; con timestamp; y sin timestamp\n")
ax.set_xticklabels(['SVM', 'RT','kNN','GPR'])

plt.yticks(np.arange(0.00,1.05,0.1))

i=0
for box in bp['boxes']:
    if i<3:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#566ADA' )
    elif i<6:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#14F026' )
    elif i<9:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#E11515' )
    elif i<12:
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




datos11 = np.asarray(data_to_plot1[0])
datos21 = np.asarray(data_to_plot1[1])
datos31 = np.asarray(data_to_plot1[2])
datos41 = np.asarray(data_to_plot1[3])

datos12 = np.asarray(data_to_plot2[0])
datos22 = np.asarray(data_to_plot2[1])
datos32 = np.asarray(data_to_plot2[2])
datos42 = np.asarray(data_to_plot2[3])

datos13 = np.asarray(data_to_plot3[0])
datos23 = np.asarray(data_to_plot3[1])
datos33 = np.asarray(data_to_plot3[2])
datos43 = np.asarray(data_to_plot3[3])

def twoSampZ(X1, X2, mudiff, sd1, sd2, n1, n2):
    from numpy import sqrt, abs, round
    from scipy.stats import norm
    pooledSE = sqrt(sd1**2/n1 + sd2**2/n2)
    z = ((X1 - X2) - mudiff)/pooledSE
    pval = 2*(1 - norm.cdf(abs(z)))
    return round(z, 3), round(pval, 4)
# Función obtenida en http://stats.stackexchange.com/questions/124096/two-samples-z-test-in-python
# El procedimiento es el mismo que el del libro

print('______________________________')

z, p = twoSampZ(datos11.mean(), datos12.mean(), 0, datos11.std(), datos12.std(), 979, 979)
print(z, p)

z, p = twoSampZ(datos11.mean(), datos13.mean(), 0, datos11.std(), datos13.std(), 979, 979)
print(z, p)

z, p = twoSampZ(datos12.mean(), datos13.mean(), 0, datos12.std(), datos13.std(), 979, 979)
print(z, p)

print('______________________________')

z, p = twoSampZ(datos21.mean(), datos22.mean(), 0, datos21.std(), datos22.std(), 979, 979)
print(z, p)

z, p = twoSampZ(datos21.mean(), datos23.mean(), 0, datos21.std(), datos23.std(), 979, 979)
print(z, p)

z, p = twoSampZ(datos22.mean(), datos23.mean(), 0, datos22.std(), datos23.std(), 979, 979)
print(z, p)

print('______________________________')

print(datos31.mean(),datos32.mean(),datos33.mean())
z, p = twoSampZ(datos31.mean(), datos32.mean(), 0, datos31.std(), datos32.std(), 979, 979)
print(z, p)

z, p = twoSampZ(datos31.mean(), datos33.mean(), 0, datos31.std(), datos33.std(), 979, 979)
print(z, p)

z, p = twoSampZ(datos32.mean(), datos33.mean(), 0, datos32.std(), datos33.std(), 979, 979)
print(z, p)

print('______________________________')

print(datos41.mean(),datos42.mean(),datos43.mean())
print(datos41.std(),datos42.std(),datos43.std())
z, p = twoSampZ(datos41.mean(), datos42.mean(), 0, datos41.std(), datos42.std(), 979, 979)
print(z, p)

z, p = twoSampZ(datos41.mean(), datos43.mean(), 0, datos41.std(), datos43.std(), 979, 979)
print(z, p)

z, p = twoSampZ(datos42.mean(), datos43.mean(), 0, datos42.std(), datos43.std(), 979, 979)
print(z, p)

print('______________________________')

# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 8))
figure_num+=1

# tiempos1=[3673.33,54.42,175.78,8007.67]
# tiempos2=[1300.86,31.66,102.81,8047.20]
# tiempos3=[1150.28,30.88,85.34,8124.97]

# tiempos1=[153.81,121.94,187.83,126.97]
# tiempos2=[160.22,106.73,194.11,137.03]
# tiempos3=[67.15,52.92,90.42,80.61]

tiempos1=[63.56,65.43,64.70,62.76]
tiempos2=[35.86,37.78,37.88,37.03]
tiempos3=[31.39,33.16,32.38,32.00]

plt.bar(x-0.2, tiempos1, 1/5, color=["#566ADA","#14F026","#E11515","#E15F15"], align='center')
plt.bar(x, tiempos2,1/5, color=["#566ADA","#14F026","#E11515","#E15F15"], align='center')
plt.bar(x+0.2, tiempos3, 1/5, color=["#566ADA","#14F026","#E11515","#E15F15"], align='center')
plt.xticks(range(len(tiempos3)),['SVM', 'RT','kNN','GPR'])
plt.grid(True)
plt.title("Coste computacional con timestamp, potencias y productos;\n con timestamp; y sin timestamp\n")


data_to_plot5= []
for i in range(len(files_name)):
    values = []
    f = open(path + "resultadosNoTimestamp" + files_name[i]+".txt")
    for line in f:
        if len(line)!=0:
            values.append(float(line))
    data_to_plot5.append(values)
    values = []

    f = open(path + "resultados1diaNoTimestamp" + files_name[i]+".txt")
    for line in f:
        if len(line)!=0:
            values.append(float(line))
    data_to_plot5.append(values)
    values = []

    f = open(path + "resultados1horaNoTimestamp" + files_name[i]+".txt")
    for line in f:
        if len(line)!=0:
            values.append(float(line))
    data_to_plot5.append(values)

# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 8))
figure_num+=1
# Create an axes instance
ax = fig.add_subplot(111)

meanpointprops = dict(marker='D', markeredgecolor='black',
                      markerfacecolor='pink')

# Create the boxplot
bp = ax.boxplot(data_to_plot5, positions=[-0.2,0,0.2,0.8,1,1.2,1.8,2,2.2,2.8,3,3.2],patch_artist=True,showmeans=True,meanprops=meanpointprops,widths=0.15)
ax.grid(True)

ax.set_title("Boxplots de los valores de MAE")
plt.xticks(range(len(means3)),['SVM', 'RT','kNN','GPR'])
plt.grid(True)
plt.title("Boxplots con 6 días entrenamiento, 1 día test; 1 día entrenamiento,\n 6 días test; 1 hora entrenamiento 6 días y 23 horas test\n")
plt.ylabel("MAE de predicción de LQ")
ax.set_xticklabels(['SVM', 'RT','kNN','GPR'])

plt.yticks(np.arange(0.00,1.05,0.1))

i=0
for box in bp['boxes']:
    if i<3:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#566ADA' )
    elif i<6:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#14F026' )
    elif i<9:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#E11515' )
    elif i<12:
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


plt.show()
