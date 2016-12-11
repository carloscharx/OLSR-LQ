import matplotlib.pyplot as plt
path = "C:/Users/carloscharx/Documentos/Teleco/4º Teleco/Prácticas y TFG/datos-Funkfeuer-CONFINE/"
file_name = "IBkEvolution"

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
file_name = "IBkEvolution2"

f= open(path + "resultados" + file_name+ ".txt");
h=288;
w=979;
Matrix = [[0 for x in range(w)] for y in range(h)]
for i in range(w):
    for j in range(h):
        Matrix[j][i]=f.readline();
plt.figure(2)
plt.plot(Matrix, 'bo', markersize=1)

plt.show()