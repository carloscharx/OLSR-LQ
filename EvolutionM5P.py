import matplotlib.pyplot as plt
path = "C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/"
file_name = "M5PEvolution"

f= open(path + "resultados" + file_name+ ".txt");
h=288;
w=979;
Matrix = [[0 for x in range(w)] for y in range(h)]
for i in range(w):
    for j in range(h):
        Matrix[j][i]=f.readline();
plt.figure(1)
plt.plot(Matrix, 'bo', markersize=1)



import matplotlib.pyplot as plt
path = "C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/"
file_name = "M5PEvolution2"

f= open(path + "resultados" + file_name+ ".txt");
h=288;
w=979;
Matrix = [[0 for x in range(w)] for y in range(h)]
for i in range(w):
    for j in range(h):
        Matrix[j][i]=f.readline();
plt.figure(2)
plt.plot(Matrix, 'bo', markersize=1)

file_name = "M5PdefEvolution"

f= open(path + "resultados" + file_name+ ".txt");
h=288;
w=979;
Matrix = [[0 for x in range(w)] for y in range(h)]
for i in range(w):
    for j in range(h):
        Matrix[j][i]=f.readline();
plt.figure(3)
plt.plot(Matrix, 'bo', markersize=1)



import matplotlib.pyplot as plt
path = "C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/"
file_name = "M5PdefEvolution2"

f= open(path + "resultados" + file_name+ ".txt");
h=288;
w=979;
Matrix = [[0 for x in range(w)] for y in range(h)]
for i in range(w):
    for j in range(h):
        Matrix[j][i]=f.readline();
plt.figure(4)
plt.plot(Matrix, 'bo', markersize=1)

plt.show()