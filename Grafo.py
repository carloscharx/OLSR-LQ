import networkx as nx
import matplotlib.pyplot as plt






# Fichero encargado de la lectura de los ficheros de topología de la red OLSR, para después crear el grafo

import os # Biblioteca encargada de obtener el nombre de los ficheros del directorio
import matplotlib.pyplot as plt # Biblioteca encargada de realizar gráficas

path = "C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/tsv"
files_list = os.listdir(path)
files_num = len(files_list)
days = int(files_num / 288) # Cada día son 288 ficheros tomados cada 5 minutos
print("Tenemos " + str(files_num) + " ficheros de topología, es decir, " + str(days) + " días")

# 6 días de conjunto de entrenamiento + 1 día de conjunto de test(1728 + 288 muestras)
days_training = 6
#days_training = 1/24
days_test = 1
#days_test = 7-days_training
length_data_set = int(days_training + days_test) *  288
print("Tomamos " + str(length_data_set) + " ficheros de topología, para tener " + str(days_training) \
      + " días de conjunto de entrenamiento y " + str(days_test) + " de test")


data_set = files_list[0:length_data_set]
links_num = []
links = {}
dates = []
for i in range(len(data_set)):
    # Abrimos un fichero
    f = open(path + "/" + data_set[i])
    strings = data_set[i].split("-")
    hours = strings[4].split("_")
    minutes = hours[1].split(".")
    dates.append(strings[1] + "-" + strings[2] + "-" + strings[3] + "-" + hours[0] + ":" + minutes[0] + ":" + "00")

    # Leemos las dos primeras líneas que no nos interesan
    f.readline()
    f.readline()

    # Leemos las líneas que tienen datos que nos interesan
    # NOTA: NO TODOS LOS FICHEROS TIENEN LAS MISMAS LINEAS; ES DECIR NO EXISTEN LOS MISMOS ENLACES
    for line in f:
        words = line.split()
        if (len(words)) != 0:
            a = (words[0] + "-" + words[1]) in links
            if not a:
                links[words[0] + "-" + words[1]] = []

    f.close()

total_links = len(links) #Este es el número de enlaces distintos históricos que ha habido, ahora añadimos a cada uno de ellos las calidades


for i in range(len(data_set)):
    # Abrimos un fichero
    f = open(path + "/" + data_set[i])

    # Leemos las dos primeras líneas que no nos interesan
    f.readline()
    f.readline()

    # Uncomment if necessary
    # Dest_IP = []
    # Last_hop_IP = []
    # LQ = []
    # NLQ = []
    # Cost = []

    # Leemos las líneas que tienen datos que nos interesan
    # NOTA: NO TODOS LOS FICHEROS TIENEN LAS MISMAS LINEAS; ES DECIR NO EXISTEN LOS MISMOS ENLACES
    lines_num = 0
    for line in f:
        words = line.split()
        if (len(words)) != 0:
            lines_num += 1
            # Uncomment if necessary
            # Dest_IP.append(words[0])
            # Last_hop_IP.append(words[1])
            # LQ.append(words[2])
            # NLQ.append(words[3])
            # Cost.append(words[4])
            links[words[0] + "-" + words[1]].append(words[2])

    f.close()
    links_num.append(lines_num)

plt.figure(1)
Gglobal = nx.Graph()
for key in links:
    direcciones=key.split("-")
    Gglobal.add_edge(direcciones[0],direcciones[1])

nx.draw_random(Gglobal)

# plt.plot(links_num)
# plt.ylabel("Número de enlaces, evolución temporal a lo largo de 7 días")
# plt.xlabel("Medidas tomadas cada 5 minutos")


LQ_per_link = []
for key in links:
    LQ_per_link.append(len(links[key]))

print("Tenemos un total de " + str(len(LQ_per_link)) +" enlaces, antes de eliminar los enlaces que no varían")

plt.figure(2)
G = nx.Graph()
variable_links = {} # Enlaces que varían
i=0
for key in links:

    if len(links[key])!=length_data_set or (len(links[key])==length_data_set and max(links[key])!=min(links[key])):
        variable_links[key] = [] # Simplemente asigno un vector vacío para después ya meter los datos finales de LQ
        i+=1
    # else:
    #     direcciones=key.split("-")
    #     G.add_edge(direcciones[0],direcciones[1],color='b',weigth=1)# añadimos al grafo los enlaces de calidad constante

print(i)

print("Tenemos un total de " + str(len(variable_links)) + " enlaces, después de eliminar los enlaces \
que no varían, y antes de eliminar los enlaces de los que no hay suficientes datos para entrenar")

for i in range(len(data_set)):
    # Abrimos un fichero
    f = open(path + "/" + data_set[i])

    # Leemos las dos primeras líneas que no nos interesan
    f.readline()
    f.readline()

    # Leemos las líneas que tienen datos que nos interesan
    for line in f:
        words = line.split()
        if (len(words)) != 0:
            if (words[0] + "-" + words[1]) in variable_links:
                variable_links[words[0] + "-" + words[1]].append(words[2])

    f.close()
    for key in variable_links:
        if len(variable_links[key])!= i+1:
            variable_links[key].append(0.000)

# Ahora hay que eliminar los enlaces de los que no hay "suficientes datos". Pese a la ambigüedad, seguimos la idea de
# que no hya suficientes datos si el conjunto de entrenamiento es nulo. También eliminamos los enlaces que dan error
# en Weka, que son aquellos en los cuales el conjunto de entrenamiento es constante.
final_links = {}
for key in variable_links:
    suma = 0.000
    max = 0.000
    min = 1.000
    for i in range(int(days_training*288)):
        valor = float(variable_links[key][i])
        suma=suma + float(variable_links[key][i])
        if valor > max:
            max = valor
        if valor < min:
            min = valor
    if suma!=0.000 and min!=max:
        final_links[key]=variable_links[key]
    # else:
    #     direcciones=key.split("-")
    #     G.add_edge(direcciones[0],direcciones[1],color='r',weigth=1)# añadimos al grafo los enlaces con calidad constante(en el entrenamiento) y aquellos sin conjunto de entrenamiento


print("Tenemos un total de " + str(len(final_links)) + " después de eliminar enlaces de los que no hay suficientes datos para entrenar, y aquellos con conjunto de entrenamiento constante")

for key in final_links:
    direcciones=key.split("-")
    G.add_edge(direcciones[0],direcciones[1],color='g',weigth=1)

# nx.draw_circular(G)

print(G.number_of_nodes())
print(G.number_of_edges())
print(Gglobal.number_of_nodes())
print(Gglobal.number_of_edges())
# nx.draw_random(G)
# plt.show()

pos = nx.random_layout(G)

edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]
weigths = [G[u][v]['weigth'] for u,v in edges]

nx.draw(G, pos, edges=edges, edge_color=colors, width=weigths)
plt.show()