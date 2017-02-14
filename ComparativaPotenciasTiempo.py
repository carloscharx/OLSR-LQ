
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy import stats

path = "C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/"
files_name = ["SMOreg", "REPTree", "IBk","GaussianProcesses"]

figure_num=1;

data_to_plot1= []
means = []
for i in range(len(files_name)):
    values = []
    f = open(path + "resultados3" + files_name[i]+".txt")
    for line in f:
        if len(line)!=0:
            values.append(float(line))
    means.append(np.asarray(values).mean())
    data_to_plot1.append(values)
print(means)