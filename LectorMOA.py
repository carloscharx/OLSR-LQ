# Fichero encargado de la lectura de los ficheros de topología de la red OLSR, para después crear el fichero .arff

import os # Biblioteca encargada de obtener el nombre de los ficheros del directorio
import matplotlib.pyplot as plt # Biblioteca encargada de realizar gráficas

path = "C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/tsv"
files_list = os.listdir(path)
files_num = len(files_list)
days = int(files_num / 288) # Cada día son 288 ficheros tomados cada 5 minutos
print("Tenemos " + str(files_num) + " ficheros de topología, es decir, " + str(days) + " días")

# 6 días de conjunto de entrenamiento + 1 día de conjunto de test(1728 + 288 muestras)
days_training = 1/24

days_test = 7-days_training

length_data_set = int(days_training + days_test)* 288
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
plt.plot(links_num)
plt.ylabel("Número de enlaces, evolución temporal")
plt.xlabel("Muestras tomadas cada 5 minutos")


LQ_per_link = []
for key in links:
    LQ_per_link.append(len(links[key]))

print("Tenemos un total de " + str(len(LQ_per_link)) +" enlaces, antes de eliminar los enlaces que no varían")


variable_links = {} # Enlaces que varían
for key in links:
    if len(links[key])!=length_data_set or (len(links[key])==length_data_set and max(links[key])!=min(links[key])):
        variable_links[key] = [] # Simplemente asigno un vector vacío para después ya meter los datos finales de LQ

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

print("Tenemos un total de " + str(len(final_links)) + " después de eliminar enlaces de los que no hay suficientes datos para entrenar, y aquellos con conjunto de entrenamiento constante")


# Ahora debemos crear el fichero .arff para MOA
i=0
for key in final_links:

    f = open("C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/datosMOA1horaLag12/link" + str(i)+ ".arff", 'w')
    f.write("% Documento para utilizarse en Weka\n")
    f.write("@relation OLSR\n\n")
    f.write("@attribute " + "Link-12" + " numeric""\n")
    f.write("@attribute " + "Link-11" + " numeric""\n")
    f.write("@attribute " + "Link-10" + " numeric""\n")
    f.write("@attribute " + "Link-9" + " numeric""\n")
    f.write("@attribute " + "Link-8" + " numeric""\n")
    f.write("@attribute " + "Link-7" + " numeric""\n")
    f.write("@attribute " + "Link-6" + " numeric""\n")
    f.write("@attribute " + "Link-5" + " numeric""\n")
    f.write("@attribute " + "Link-4" + " numeric""\n")
    f.write("@attribute " + "Link-3" + " numeric""\n")
    f.write("@attribute " + "Link-2" + " numeric""\n")
    f.write("@attribute " + "Link-1" + " numeric""\n")
    f.write("@attribute " + "Link" + str(i)+ " numeric""\n")
    f.write("\n@data\n\n")
    for k in range(len(data_set)):
        if k >=12:
            f.write(str(final_links[key][k-12]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=11:
            f.write(str(final_links[key][k-11]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=10:
            f.write(str(final_links[key][k-10]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=9:
            f.write(str(final_links[key][k-9]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=8:
            f.write(str(final_links[key][k-8]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=7:
            f.write(str(final_links[key][k-7]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=6:
            f.write(str(final_links[key][k-6]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=5:
            f.write(str(final_links[key][k-5]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=4:
            f.write(str(final_links[key][k-4]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=3:
            f.write(str(final_links[key][k-3]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=2:
            f.write(str(final_links[key][k-2]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=1:
            f.write(str(final_links[key][k-1]))
        else:
            f.write(str(0))
        f.write(",")
        f.write(str(final_links[key][k]))
        f.write("\n")
    f.close()
    i+=1

# Ahora debemos crear el fichero .arff para MOA
i=0
for key in final_links:

    f = open("C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/datosMOA1horaLag11/link" + str(i)+ ".arff", 'w')
    f.write("% Documento para utilizarse en Weka\n")
    f.write("@relation OLSR\n\n")
    f.write("@attribute " + "Link-11" + " numeric""\n")
    f.write("@attribute " + "Link-10" + " numeric""\n")
    f.write("@attribute " + "Link-9" + " numeric""\n")
    f.write("@attribute " + "Link-8" + " numeric""\n")
    f.write("@attribute " + "Link-7" + " numeric""\n")
    f.write("@attribute " + "Link-6" + " numeric""\n")
    f.write("@attribute " + "Link-5" + " numeric""\n")
    f.write("@attribute " + "Link-4" + " numeric""\n")
    f.write("@attribute " + "Link-3" + " numeric""\n")
    f.write("@attribute " + "Link-2" + " numeric""\n")
    f.write("@attribute " + "Link-1" + " numeric""\n")
    f.write("@attribute " + "Link" + str(i)+ " numeric""\n")
    f.write("\n@data\n\n")
    for k in range(len(data_set)):
        if k >=11:
            f.write(str(final_links[key][k-11]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=10:
            f.write(str(final_links[key][k-10]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=9:
            f.write(str(final_links[key][k-9]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=8:
            f.write(str(final_links[key][k-8]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=7:
            f.write(str(final_links[key][k-7]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=6:
            f.write(str(final_links[key][k-6]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=5:
            f.write(str(final_links[key][k-5]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=4:
            f.write(str(final_links[key][k-4]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=3:
            f.write(str(final_links[key][k-3]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=2:
            f.write(str(final_links[key][k-2]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=1:
            f.write(str(final_links[key][k-1]))
        else:
            f.write(str(0))
        f.write(",")
        f.write(str(final_links[key][k]))
        f.write("\n")
    f.close()
    i+=1


# Ahora debemos crear el fichero .arff para MOA
i=0
for key in final_links:

    f = open("C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/datosMOA1horaLag10/link" + str(i)+ ".arff", 'w')
    f.write("% Documento para utilizarse en Weka\n")
    f.write("@relation OLSR\n\n")
    f.write("@attribute " + "Link-10" + " numeric""\n")
    f.write("@attribute " + "Link-9" + " numeric""\n")
    f.write("@attribute " + "Link-8" + " numeric""\n")
    f.write("@attribute " + "Link-7" + " numeric""\n")
    f.write("@attribute " + "Link-6" + " numeric""\n")
    f.write("@attribute " + "Link-5" + " numeric""\n")
    f.write("@attribute " + "Link-4" + " numeric""\n")
    f.write("@attribute " + "Link-3" + " numeric""\n")
    f.write("@attribute " + "Link-2" + " numeric""\n")
    f.write("@attribute " + "Link-1" + " numeric""\n")
    f.write("@attribute " + "Link" + str(i)+ " numeric""\n")
    f.write("\n@data\n\n")
    for k in range(len(data_set)):
        if k >=10:
            f.write(str(final_links[key][k-10]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=9:
            f.write(str(final_links[key][k-9]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=8:
            f.write(str(final_links[key][k-8]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=7:
            f.write(str(final_links[key][k-7]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=6:
            f.write(str(final_links[key][k-6]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=5:
            f.write(str(final_links[key][k-5]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=4:
            f.write(str(final_links[key][k-4]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=3:
            f.write(str(final_links[key][k-3]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=2:
            f.write(str(final_links[key][k-2]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=1:
            f.write(str(final_links[key][k-1]))
        else:
            f.write(str(0))
        f.write(",")
        f.write(str(final_links[key][k]))
        f.write("\n")
    f.close()
    i+=1


# Ahora debemos crear el fichero .arff para MOA
i=0
for key in final_links:

    f = open("C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/datosMOA1horaLag9/link" + str(i)+ ".arff", 'w')
    f.write("% Documento para utilizarse en Weka\n")
    f.write("@relation OLSR\n\n")
    f.write("@attribute " + "Link-9" + " numeric""\n")
    f.write("@attribute " + "Link-8" + " numeric""\n")
    f.write("@attribute " + "Link-7" + " numeric""\n")
    f.write("@attribute " + "Link-6" + " numeric""\n")
    f.write("@attribute " + "Link-5" + " numeric""\n")
    f.write("@attribute " + "Link-4" + " numeric""\n")
    f.write("@attribute " + "Link-3" + " numeric""\n")
    f.write("@attribute " + "Link-2" + " numeric""\n")
    f.write("@attribute " + "Link-1" + " numeric""\n")
    f.write("@attribute " + "Link" + str(i)+ " numeric""\n")
    f.write("\n@data\n\n")
    for k in range(len(data_set)):
        if k >=9:
            f.write(str(final_links[key][k-9]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=8:
            f.write(str(final_links[key][k-8]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=7:
            f.write(str(final_links[key][k-7]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=6:
            f.write(str(final_links[key][k-6]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=5:
            f.write(str(final_links[key][k-5]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=4:
            f.write(str(final_links[key][k-4]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=3:
            f.write(str(final_links[key][k-3]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=2:
            f.write(str(final_links[key][k-2]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=1:
            f.write(str(final_links[key][k-1]))
        else:
            f.write(str(0))
        f.write(",")
        f.write(str(final_links[key][k]))
        f.write("\n")
    f.close()
    i+=1

# Ahora debemos crear el fichero .arff para MOA
i=0
for key in final_links:

    f = open("C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/datosMOA1horaLag8/link" + str(i)+ ".arff", 'w')
    f.write("% Documento para utilizarse en Weka\n")
    f.write("@relation OLSR\n\n")
    f.write("@attribute " + "Link-8" + " numeric""\n")
    f.write("@attribute " + "Link-7" + " numeric""\n")
    f.write("@attribute " + "Link-6" + " numeric""\n")
    f.write("@attribute " + "Link-5" + " numeric""\n")
    f.write("@attribute " + "Link-4" + " numeric""\n")
    f.write("@attribute " + "Link-3" + " numeric""\n")
    f.write("@attribute " + "Link-2" + " numeric""\n")
    f.write("@attribute " + "Link-1" + " numeric""\n")
    f.write("@attribute " + "Link" + str(i)+ " numeric""\n")
    f.write("\n@data\n\n")
    for k in range(len(data_set)):
        if k >=8:
            f.write(str(final_links[key][k-8]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=7:
            f.write(str(final_links[key][k-7]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=6:
            f.write(str(final_links[key][k-6]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=5:
            f.write(str(final_links[key][k-5]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=4:
            f.write(str(final_links[key][k-4]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=3:
            f.write(str(final_links[key][k-3]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=2:
            f.write(str(final_links[key][k-2]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=1:
            f.write(str(final_links[key][k-1]))
        else:
            f.write(str(0))
        f.write(",")
        f.write(str(final_links[key][k]))
        f.write("\n")
    f.close()
    i+=1


# Ahora debemos crear el fichero .arff para MOA
i=0
for key in final_links:

    f = open("C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/datosMOA1horaLag7/link" + str(i)+ ".arff", 'w')
    f.write("% Documento para utilizarse en Weka\n")
    f.write("@relation OLSR\n\n")
    f.write("@attribute " + "Link-7" + " numeric""\n")
    f.write("@attribute " + "Link-6" + " numeric""\n")
    f.write("@attribute " + "Link-5" + " numeric""\n")
    f.write("@attribute " + "Link-4" + " numeric""\n")
    f.write("@attribute " + "Link-3" + " numeric""\n")
    f.write("@attribute " + "Link-2" + " numeric""\n")
    f.write("@attribute " + "Link-1" + " numeric""\n")
    f.write("@attribute " + "Link" + str(i)+ " numeric""\n")
    f.write("\n@data\n\n")
    for k in range(len(data_set)):
        if k >=7:
            f.write(str(final_links[key][k-7]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=6:
            f.write(str(final_links[key][k-6]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=5:
            f.write(str(final_links[key][k-5]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=4:
            f.write(str(final_links[key][k-4]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=3:
            f.write(str(final_links[key][k-3]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=2:
            f.write(str(final_links[key][k-2]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=1:
            f.write(str(final_links[key][k-1]))
        else:
            f.write(str(0))
        f.write(",")
        f.write(str(final_links[key][k]))
        f.write("\n")
    f.close()
    i+=1

# Ahora debemos crear el fichero .arff para MOA
i=0
for key in final_links:

    f = open("C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/datosMOA1horaLag6/link" + str(i)+ ".arff", 'w')
    f.write("% Documento para utilizarse en Weka\n")
    f.write("@relation OLSR\n\n")
    f.write("@attribute " + "Link-6" + " numeric""\n")
    f.write("@attribute " + "Link-5" + " numeric""\n")
    f.write("@attribute " + "Link-4" + " numeric""\n")
    f.write("@attribute " + "Link-3" + " numeric""\n")
    f.write("@attribute " + "Link-2" + " numeric""\n")
    f.write("@attribute " + "Link-1" + " numeric""\n")
    f.write("@attribute " + "Link" + str(i)+ " numeric""\n")
    f.write("\n@data\n\n")
    for k in range(len(data_set)):
        if k >=6:
            f.write(str(final_links[key][k-6]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=5:
            f.write(str(final_links[key][k-5]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=4:
            f.write(str(final_links[key][k-4]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=3:
            f.write(str(final_links[key][k-3]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=2:
            f.write(str(final_links[key][k-2]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=1:
            f.write(str(final_links[key][k-1]))
        else:
            f.write(str(0))
        f.write(",")
        f.write(str(final_links[key][k]))
        f.write("\n")
    f.close()
    i+=1


# Ahora debemos crear el fichero .arff para MOA
i=0
for key in final_links:

    f = open("C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/datosMOA1horaLag5/link" + str(i)+ ".arff", 'w')
    f.write("% Documento para utilizarse en Weka\n")
    f.write("@relation OLSR\n\n")
    f.write("@attribute " + "Link-5" + " numeric""\n")
    f.write("@attribute " + "Link-4" + " numeric""\n")
    f.write("@attribute " + "Link-3" + " numeric""\n")
    f.write("@attribute " + "Link-2" + " numeric""\n")
    f.write("@attribute " + "Link-1" + " numeric""\n")
    f.write("@attribute " + "Link" + str(i)+ " numeric""\n")
    f.write("\n@data\n\n")
    for k in range(len(data_set)):
        if k >=5:
            f.write(str(final_links[key][k-5]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=4:
            f.write(str(final_links[key][k-4]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=3:
            f.write(str(final_links[key][k-3]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=2:
            f.write(str(final_links[key][k-2]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=1:
            f.write(str(final_links[key][k-1]))
        else:
            f.write(str(0))
        f.write(",")
        f.write(str(final_links[key][k]))
        f.write("\n")
    f.close()
    i+=1


# Ahora debemos crear el fichero .arff para MOA
i=0
for key in final_links:

    f = open("C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/datosMOA1horaLag4/link" + str(i)+ ".arff", 'w')
    f.write("% Documento para utilizarse en Weka\n")
    f.write("@relation OLSR\n\n")
    f.write("@attribute " + "Link-4" + " numeric""\n")
    f.write("@attribute " + "Link-3" + " numeric""\n")
    f.write("@attribute " + "Link-2" + " numeric""\n")
    f.write("@attribute " + "Link-1" + " numeric""\n")
    f.write("@attribute " + "Link" + str(i)+ " numeric""\n")
    f.write("\n@data\n\n")
    for k in range(len(data_set)):
        if k >=4:
            f.write(str(final_links[key][k-4]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=3:
            f.write(str(final_links[key][k-3]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=2:
            f.write(str(final_links[key][k-2]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=1:
            f.write(str(final_links[key][k-1]))
        else:
            f.write(str(0))
        f.write(",")
        f.write(str(final_links[key][k]))
        f.write("\n")
    f.close()
    i+=1

# Ahora debemos crear el fichero .arff para MOA
i=0
for key in final_links:

    f = open("C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/datosMOA1horaLag3/link" + str(i)+ ".arff", 'w')
    f.write("% Documento para utilizarse en Weka\n")
    f.write("@relation OLSR\n\n")
    f.write("@attribute " + "Link-3" + " numeric""\n")
    f.write("@attribute " + "Link-2" + " numeric""\n")
    f.write("@attribute " + "Link-1" + " numeric""\n")
    f.write("@attribute " + "Link" + str(i)+ " numeric""\n")
    f.write("\n@data\n\n")
    for k in range(len(data_set)):
        if k >=3:
            f.write(str(final_links[key][k-3]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=2:
            f.write(str(final_links[key][k-2]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=1:
            f.write(str(final_links[key][k-1]))
        else:
            f.write(str(0))
        f.write(",")
        f.write(str(final_links[key][k]))
        f.write("\n")
    f.close()
    i+=1


# Ahora debemos crear el fichero .arff para MOA
i=0
for key in final_links:

    f = open("C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/datosMOA1horaLag2/link" + str(i)+ ".arff", 'w')
    f.write("% Documento para utilizarse en Weka\n")
    f.write("@relation OLSR\n\n")
    f.write("@attribute " + "Link-2" + " numeric""\n")
    f.write("@attribute " + "Link-1" + " numeric""\n")
    f.write("@attribute " + "Link" + str(i)+ " numeric""\n")
    f.write("\n@data\n\n")
    for k in range(len(data_set)):
        if k >=2:
            f.write(str(final_links[key][k-2]))
        else:
            f.write(str(0))
        f.write(",")
        if k >=1:
            f.write(str(final_links[key][k-1]))
        else:
            f.write(str(0))
        f.write(",")
        f.write(str(final_links[key][k]))
        f.write("\n")
    f.close()
    i+=1

# Ahora debemos crear el fichero .arff para MOA
i=0
for key in final_links:

    f = open("C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/datosMOA1horaLag1/link" + str(i)+ ".arff", 'w')
    f.write("% Documento para utilizarse en Weka\n")
    f.write("@relation OLSR\n\n")
    f.write("@attribute " + "Link-1" + " numeric""\n")
    f.write("@attribute " + "Link" + str(i)+ " numeric""\n")
    f.write("\n@data\n\n")
    for k in range(len(data_set)):
        if k >=1:
            f.write(str(final_links[key][k-1]))
        else:
            f.write(str(0))
        f.write(",")
        f.write(str(final_links[key][k]))
        f.write("\n")
    f.close()
    i+=1
