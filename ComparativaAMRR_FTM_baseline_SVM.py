#Fichero encargado de la lectura de los resultados de las predicciones y de representar los boxplots

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy import stats

path = "C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/"
#files_name = ["resultadosNoTimestampSMOreg", "resultadosErrorLAGMOAAMRulesRegressor","resultadosErrorLAGMOAFadingTargetMean","resultados6diasAnterior"]
#files_name = ["resultados1diaNoTimestampSMOreg", "resultadosError1diaLAGMOAAMRulesRegressor","resultadosError1diaLAGMOAFadingTargetMean","resultados1diaAnterior"]
#files_name = ["resultados1horaNoTimestampSMOreg", "resultadosError1horaLAGMOAAMRulesRegressor","resultadosError1horaLAGMOAFadingTargetMean","resultados1horaAnterior"]
#files_name = ["resultadosReentrenadosSMOreg","resultadosReentrenadoMOAAMRulesRegressor1dia","resultados1diareentrenado"]
files_name = ["SMOreg","LAGMOAAMRulesRegressor","LAGMOAFadingTargetMean","Anterior"]
figure_num=1;

# data_to_plot1= []
# means = []
# for i in range(len(files_name)):
#     values = []
#     f = open(path +  files_name[i]+".txt")
#     for line in f:
#         if len(line)!=0:
#             values.append(float(line))
#     means.append(np.asarray(values).mean())
#     data_to_plot1.append(values)
# print(means)
# # Create a figure instance
# fig = plt.figure(figure_num, figsize=(9, 6))
# figure_num+=1
# x = range(len(means))
# plt.bar(x, means, 1/5, color=["#566ADA","#14F026","#E11515","#E15F15"], align='center')
# plt.grid(True)
#
#
# plt.xticks(range(len(means)),['SVM', 'RT','kNN','baseline'])
# plt.title("MAE promedio")
# plt.yticks(np.arange(0.00,0.05,0.01))
#
# # Create a figure instance
# fig = plt.figure(figure_num, figsize=(9, 6))
# figure_num+=1
# # Create an axes instance
# ax = fig.add_subplot(111)
#
# meanpointprops = dict(marker='D', markeredgecolor='black',
#                       markerfacecolor='yellow')
#
# # Create the boxplot
# bp = ax.boxplot(data_to_plot1, patch_artist=True,showmeans=True,meanprops=meanpointprops)
# ax.grid(True)
#
# ax.set_title("Boxplots de los valores de MAE, algoritmos vs baseline")
#
# i=0
# for box in bp['boxes']:
#     if i==0:
#         # change outline color
#         box.set( color='#7570b3', linewidth=2)
#         # change fill color
#         box.set( facecolor = '#566ADA' )
#     elif i==1:
#         # change outline color
#         box.set( color='#7570b3', linewidth=2)
#         # change fill color
#         box.set( facecolor = '#8A4B08' )
#     elif i==2:
#         # change outline color
#         box.set( color='#7570b3', linewidth=2)
#         # change fill color
#         #box.set( facecolor = '#6E6E6E' )
#         box.set( facecolor = '#610B21' )
#     elif i==3:
#         # change outline color
#         box.set( color='#7570b3', linewidth=2)
#         # change fill color
#         box.set( facecolor = '#610B21' )
#     i+=1
#
# # change color and linewidth of the whiskers
# for whisker in bp['whiskers']:
#     whisker.set(color='#7570b3', linewidth=2)
#
# ## change color and linewidth of the caps
# for cap in bp['caps']:
#     cap.set(color='#7570b3', linewidth=2)
#
# ## change color and linewidth of the medians
# for median in bp['medians']:
#     median.set(color='#b2df8a', linewidth=2)
#
# ## change the style of fliers and their fill
# for flier in bp['fliers']:
#     flier.set(marker='o', color='#e7298a', alpha=0.5)
#
# ax.set_xticklabels(['SVM', 'AMRulesRegressor','baseline','baseline'])
#
# plt.yticks(np.arange(0.00,0.3,0.05))
#
# datos1 = np.asarray(data_to_plot1[0])
# datos2 = np.asarray(data_to_plot1[1])
# datos3 = np.asarray(data_to_plot1[2])
# # datos4 = np.asarray(data_to_plot1[3])
#
# def twoSampZ(X1, X2, mudiff, sd1, sd2, n1, n2):
#     from numpy import sqrt, abs, round
#     from scipy.stats import norm
#     pooledSE = sqrt(sd1**2/n1 + sd2**2/n2)
#     z = ((X1 - X2) - mudiff)/pooledSE
#     pval = 2*(1 - norm.cdf(abs(z)))
#     return round(z, 3), round(pval, 4)
# # Función obtenida en http://stats.stackexchange.com/questions/124096/two-samples-z-test-in-python
# # El procedimiento es el mismo que el del libro
#
# #n=979
# #n=610
# #n=325
# n=407
# z, p = twoSampZ(datos1.mean(), datos2.mean(), 0, datos1.std(), datos2.std(), n, n)
# print(z, p)
#
# z, p = twoSampZ(datos1.mean(), datos3.mean(), 0, datos1.std(), datos3.std(), n, n)
# print(z, p)
#
# # z, p = twoSampZ(datos1.mean(), datos4.mean(), 0, datos1.std(), datos4.std(), n, n)
# # print(z, p)
# #
# z, p = twoSampZ(datos2.mean(), datos3.mean(), 0, datos2.std(), datos3.std(), n, n)
# print(z, p)
# #
# # z, p = twoSampZ(datos2.mean(), datos4.mean(), 0, datos2.std(), datos4.std(), n, n)
# # print(z, p)
# #
# # z, p = twoSampZ(datos3.mean(), datos4.mean(), 0, datos3.std(), datos4.std(), n, n)
# # print(z, p)
#
#
#
#
#
#
#
#
#
#
#


data_to_plot5= []

values = []
f = open(path + "resultadosNoTimestamp" + files_name[0]+".txt")
for line in f:
    if len(line)!=0:
        values.append(float(line))
data_to_plot5.append(values)
values = []

f = open(path + "resultados1diaNoTimestamp" + files_name[0]+".txt")
for line in f:
    if len(line)!=0:
        values.append(float(line))
data_to_plot5.append(values)
values = []

f = open(path + "resultados1horaNoTimestamp" + files_name[0]+".txt")
for line in f:
    if len(line)!=0:
        values.append(float(line))
data_to_plot5.append(values)


values = []
f = open(path + "resultadosError" + files_name[1]+".txt")
for line in f:
    if len(line)!=0:
        values.append(float(line))
data_to_plot5.append(values)
values = []

f = open(path + "resultadosError1dia" + files_name[1]+".txt")
for line in f:
    if len(line)!=0:
        values.append(float(line))
data_to_plot5.append(values)
values = []

f = open(path + "resultadosError1hora" + files_name[1]+".txt")
for line in f:
    if len(line)!=0:
        values.append(float(line))
data_to_plot5.append(values)



values = []
f = open(path + "resultadosError" + files_name[2]+".txt")
for line in f:
    if len(line)!=0:
        values.append(float(line))
data_to_plot5.append(values)
values = []

f = open(path + "resultadosError1dia" + files_name[2]+".txt")
for line in f:
    if len(line)!=0:
        values.append(float(line))
data_to_plot5.append(values)
values = []

f = open(path + "resultadosError1hora" + files_name[2]+".txt")
for line in f:
    if len(line)!=0:
        values.append(float(line))
data_to_plot5.append(values)


values = []
f = open(path + "resultados6dias" + files_name[3]+".txt")
for line in f:
    if len(line)!=0:
        values.append(float(line))
data_to_plot5.append(values)
values = []

f = open(path + "resultados1dia" + files_name[3]+".txt")
for line in f:
    if len(line)!=0:
        values.append(float(line))
data_to_plot5.append(values)
values = []

f = open(path + "resultados1hora" + files_name[3]+".txt")
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
plt.xticks(range(4),['SVM', 'RT','kNN','GPR'])
plt.grid(True)
plt.title("Boxplots con 6 días entrenamiento, 1 día test; 1 día entrenamiento,\n 6 días test; 1 hora entrenamiento 6 días y 23 horas test\n")
plt.ylabel("MAE de predicción de LQ")
ax.set_xticklabels(['SVM', 'AMRulesRegressor','FadingTargetMean','baseline'])

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
        box.set( facecolor = '#8A4B08' )
    elif i<9:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#6E6E6E' )
    elif i<12:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#610B21' )
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

# Create a figure instance
fig = plt.figure(figure_num, figsize=(9, 6))
figure_num+=1

tiempos1=[127,20,2]

plt.bar(np.arange(3), tiempos1,1/5, color=["#566ADA","#8A4B08","#610B21","#E15F15"], align='center')
plt.xticks(range(3),['SVM', 'AMRulesRegressor','baseline'])
plt.grid(True)
plt.title("Coste computacional de SVM, AMRulesRegressor y baseline")
plt.ylabel("Segundos")

plt.show()


