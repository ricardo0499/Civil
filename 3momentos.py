from tkinter import E
from numpy import append

print("Cálculo de Momentos y Reacciones\n")
nombreV=input("Introduzca el nombre de la viga: ")
e=float(input("Introduzca el valor de E: "))
i=float(input("Introduzca el valor de I: "))

print("Se asume que la Viga ",nombreV," tiene 3 apoyos y está empotrada a ambos extremos\n")

def datosCargaP(numCargasP): #función que recoge los datos de las cargas puntuales en una luz
    cargas=[] #matriz para almacenar los datos
    if numCargasP==1: #para una sola carga
        cargas.append(float(input(f"(Carga) Introduzca la distancia desde la izquierda: ")))
        cargas.append(float(input(f"(Carga) Introduzca la magnitud de la carga: ")))
        print(cargas)
    elif numCargasP>=2: #más de una carga
        for x in range(numCargasP):
            cargaslinea=[]
            cargaslinea.append(float(input(f"(Carga {x}) Introduzca la distancia desde la izquierda: ")))
            cargaslinea.append(float(input(f"(Carga {x}) Introduzca la magnitud de la carga: ")))
            cargas.append(cargaslinea)
    return cargas
def datosCargaM(numCargasD): #recolección de datos para carga distribuida en una luz
    cargasD=[]
    if numCargasD!=0:
        magCD=float(input(f"Introduzca la magnitud de la carga: "))
        distanciaCd=float(input(f"Introduzca la distancia de la carga desde la izquierda: "))
        longitudCd=float(input(f"Introduzca la longitud de la distribución: "))
        cargasD.append([magCD,distanciaCd,longitudCd])
    else:
         cargasD=[0,0,0]
    return cargasD
def datos(tramo): #función que reúne los datos de cada tramo
    print(f"Información del tramo {tramo}")
    ei1=int(input("Introduzca el coeficiente EI de luz izquierda: "))
    ei2=int(input("Introduzca el coeficiente EI de luz derecha: "))
    longTramIzq=float(input("Longitud Izquierda del tramo: "))
    longTramDer=float(input("Longitud Derecha del tramo: "))
    numCargasP1=int(input("número de cargas puntuales en luz Izquierda: "))
    cargasPIzq=datosCargaP(numCargasP1)
    numCargasD1=int(input("número de cargas distribuidas en luz izquierda: "))
    cargasDIzq=datosCargaM(numCargasD1)
    numCargasP2=int(input("número de cargas puntuales en luz derecha: "))
    cargasPDer=datosCargaP(numCargasP2)
    numCargasD2=int(input("número de cargas distribuidas en luz derecha: "))
    cargasDDer=datosCargaM(numCargasD2)
    
    diccionario={
        "LongitudLuz1":longTramIzq,
        "LongitudLuz2":longTramDer,
        "LongitudT":longTramDer+longTramIzq,
        "CargasPLuz1":cargasPIzq,
        "#CargasPLuz1":numCargasP1,
        "CargasPLuz2":cargasPDer,
        "#CargasPLuz2":numCargasP2,
        "CargasDLuz1":cargasDIzq,
        "CargasDLuz2":cargasDDer,
        "EI1":ei1,
        "EI2":ei2
    }
    return diccionario

def ecuacion1(longTramIzq,
            longTramDer,
            longitudT,
            cargasPIzq,
            numCargasP1,
            cargasPDer,
            numCargasP2,
            cargasDIzq,
            cargasDDer,
            ei1,
            ei2):
    sumI=0
    sumD=0
    if numCargasP2>1:
        for linea in cargasPDer:
            #print(linea)
            sumD+=float(((linea[1]*longTramDer**2)/(ei2*i*e))*(linea[0]/longitudT-(linea[0]/longitudT)**3))
    else:
        sumD+=float(((cargasPDer[1]*longTramDer**2)/(ei2*i*e))*(cargasPDer[0]/longitudT-(cargasPDer[0]/longitudT)**3))
    if numCargasP2>1:
        for linea in cargasPIzq:
            sumI+=float(((linea[1]*longTramIzq**2)/(ei1*i*e))*(linea[0]/longitudT-(linea[0]/longitudT)**3))
    else:
        sumI+=float(((cargasPIzq[1]*longTramIzq**2)/(ei1*i*e))*(cargasPIzq[0]/longitudT-(cargasPIzq[0]/longitudT)**3))

    valorDI=float((cargasDIzq[0]*longTramIzq**3)/(4*ei1*i*e))
    valorDD=float((cargasDDer[0]*longTramDer**3)/(4*ei2*i*e))
    total=-sumI-sumD-valorDI-valorDD
    m1=longTramIzq/(ei1*i*e)
    m2=2*(longTramIzq/(ei1*i*e)+longTramDer/(ei2*i*e))
    m3=longTramDer/(ei1*i*e)
    print(f"ecuación: {m1}M1+{m2}M2+{m3}={total}")

    
        
        

datosTramo1=datos("ABC")
ecuacion1(datosTramo1["LongitudLuz1"],
        datosTramo1["LongitudLuz2"],
        datosTramo1["LongitudT"],
        datosTramo1["CargasPLuz1"],
        datosTramo1["#CargasPLuz1"],
        datosTramo1["CargasPLuz2"],
        datosTramo1["#CargasPLuz2"],
        datosTramo1["CargasDLuz1"],
        datosTramo1["CargasDLuz2"],
        datosTramo1["EI1"],
         datosTramo1["EI2"])
datosTramo2=datos("CBD")
datosTramo3=datos("CDE")




#def cargasDistribuidas(magnitud,)

   







#distancias
a0a=0
ab=3
bc=3
cd=2
de=1
e=0
#momentos de inercia 
eia0a=0
eiab=1
eibc=3
eicd=2
eide=2
eie=0
#valores de las cargas
#tramo a'ab
ex=input("existen cargas puntuales? y/n: ")
cantidad=0
if ex=="y":
    cantidad=int(input("cuantas cargas puntuales? "))
    cp=[[],[]]
    for x in range(cantidad):
        c=float(input("carga puntual "))
        longd=float(input("distancia "))
        cp[0].append(c)
        cp[1].append(longd)
else:
    cp=0

for i in range (cantidad):
    print("Cargas   ",cp[[0][i]])
    print("distancia    ",cp[[1][i]])




w1=3 #ton/m
p=3 #ton


#tramo abc

#tramo bcd

#tramo cde

#tramo dee'
