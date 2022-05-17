from tkinter import E
from numpy import append
import numpy as np
import method2 as m2

print("Cálculo de Momentos y Reacciones\n")
nombreV=input("Introduzca el nombre de la viga: ")
f=open(f"{nombreV}.txt","x")
f.write(f"{nombreV}\n")
ei=1.0#float(input("Introduzca el valor de EI: "))
print("Se asume que la Viga ",nombreV," tiene 3 apoyos y está empotrada a ambos extremos\n")
f.write(f"Se asume que la Viga {nombreV} tiene 3 apoyos y está empotrada a ambos extremos\n")

def datosCargaP(numCargasP): #función que recoge los datos de las cargas puntuales en una luz
    cargas=[] #matriz para almacenar los datos
    if numCargasP==1: #para una sola carga
        cargas.append(float(input(f"(Carga) Introduzca la distancia desde la izquierda: ")))
        f.write(f"(Carga) Introduzca la distancia desde la izquierda: {cargas[0]}\n")
        cargas.append(float(input(f"(Carga) Introduzca la magnitud de la carga: ")))
        f.write(f"(Carga) Introduzca la magnitud de la carga: {cargas[1]}\n")
        return cargas
    elif numCargasP>=2: #más de una carga
        for x in range(numCargasP):
            cargaslinea=[]
            cargaslinea.append(float(input(f"(Carga {x+1}) Introduzca la distancia desde la izquierda: ")))
            f.write(f"(Carga {x+1}) Introduzca la distancia desde la izquierda: {cargaslinea[0]}\n")
            cargaslinea.append(float(input(f"(Carga {x+1}) Introduzca la magnitud de la carga: ")))
            f.write(f"(Carga {x+1}) Introduzca la magnitud de la carga: {cargaslinea[1]}\n")
            cargas.append(cargaslinea)
        return cargas
    else:
        cargas=[0.0,0.0]
        return cargas
    
def datosCargaM(numCargasD): #recolección de datos para carga distribuida en una luz
    cargasD=[]
    if numCargasD==1:
        magCD=float(input("Introduzca la magnitud de la carga: "))
        f.write(f"Introduzca la magnitud de la carga: {magCD}\n")
        distanciaCd=float(input(f"Introduzca la distancia de la carga desde la izquierda: "))
        f.write(f"Introduzca la distancia de la carga desde la izquierda: {distanciaCd}\n")
        longitudCd=float(input(f"Introduzca la longitud de la distribución: "))
        f.write(f"Introduzca la longitud de la distribución: {longitudCd}\n")
        cargasD.append(magCD)
        cargasD.append(distanciaCd)
        cargasD.append(longitudCd)
        #print(cargasD)
        return cargasD
    else:
        cargasD=[0.0,0.0,0.0]
        return cargasD
    
def datos(luz1,luz2): #función que reúne los datos de cada tramo
    #print(f"Información del tramo {tramo}")
    ei1=float(input(f"Introduzca el coeficiente EI de luz {luz1}: "))
    f.write(f"Introduzca el coeficiente EI de luz {luz1}: {ei1}\n")
    ei2=float(input(f"Introduzca el coeficiente EI de luz {luz2}: "))
    f.write(f"Introduzca el coeficiente EI de luz {luz2}: {ei2}\n")
    longTramIzq=float(input(f"Longitud de luz {luz1}: "))
    f.write(f"Longitud de luz {luz1}: {longTramIzq}\n")
    longTramDer=float(input(f"Longitud de luz {luz2}: "))
    f.write(f"Longitud de luz {luz2}: {longTramDer}\n")
    numCargasP1=int(input(f"número de cargas puntuales en luz {luz1}: "))
    f.write(f"número de cargas puntuales en luz {luz1}: {numCargasP1}\n")
    cargasPIzq=datosCargaP(numCargasP1)
    numCargasD1=int(input(f"número de cargas distribuidas en luz {luz1}: "))
    f.write(f"número de cargas distribuidas en luz {luz1}: {numCargasD1}\n")
    cargasDIzq=datosCargaM(numCargasD1)
    numCargasP2=int(input(f"número de cargas puntuales en luz {luz2}: "))
    f.write(f"número de cargas puntuales en luz {luz2}: {numCargasP2}\n")
    cargasPDer=datosCargaP(numCargasP2)
    numCargasD2=int(input(f"número de cargas distribuidas en luz {luz2}: "))
    f.write(f"número de cargas distribuidas en luz {luz2}: {numCargasD2}\n")
    cargasDDer=datosCargaM(numCargasD2)
    
    diccionario={
        "LongitudLuz1":longTramIzq,
        "LongitudLuz2":longTramDer,
        "LongitudT":longTramDer+longTramIzq,#verificar
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

def datos2(ei,longTI,ncp1,cpi,ncd1,cdi,luz): #función que reúne los datos de cada tramo
    #print(f"Información del tramo {tramo}")
    ei1=ei
    ei2=float(input(f"Introduzca el coeficiente EI de luz {luz}: "))
    f.write(f"Introduzca el coeficiente EI de luz {luz}: {ei2}\n")
    longTramIzq=longTI
    longTramDer=float(input(f"Longitud luz {luz}: "))
    f.write(f"Longitud luz {luz}: {longTramDer}\n")
    numCargasP1=ncp1
    cargasPIzq=cpi
    numCargasD1=ncd1
    cargasDIzq=cdi
    numCargasP2=int(input(f"número de cargas puntuales en luz {luz}: "))
    f.write(f"número de cargas puntuales en luz {luz}: {numCargasP2}\n")
    cargasPDer=datosCargaP(numCargasP2)
    numCargasD2=int(input(f"número de cargas distribuidas en luz {luz}: "))
    f.write(f"número de cargas distribuidas en luz {luz}: {numCargasD2}\n")
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
            ei2,
            ecu):
    sumI=0
    sumD=0
    #print(cargasPDer)
    if numCargasP2>1:#derecha
        for linea in cargasPDer:
            sumD+=float(((linea[1]*longTramDer**2)/(ei2*ei))*((longTramDer-linea[0])/longTramDer-((longTramDer-linea[0])/longTramDer)**3))
    elif numCargasP2==1:
        sumD+=float(((cargasPDer[1]*longTramDer**2)/(ei2*ei))*((longTramDer-cargasPDer[0])/longTramDer-((longTramDer-cargasPDer[0])/longTramDer)**3))
    if numCargasP1>1:#izq
        for linea in cargasPIzq:
            sumI+=float(((linea[1]*longTramIzq**2)/(ei1*ei))*(linea[0]/longTramIzq-(linea[0]/longTramIzq)**3))
    elif numCargasP1==1:
        sumI+=float(((cargasPIzq[1]*longTramIzq**2)/(ei1*ei))*(cargasPIzq[0]/longTramIzq-(cargasPIzq[0]/longTramIzq)**3))

        
    valorDI=float((float(cargasDIzq[0])*float(longTramIzq)**3)/(4*ei1*ei))
    valorDD=float((float(cargasDDer[0])*float(longTramDer)**3)/(4*ei2*ei))
    total=-sumI-sumD-valorDI-valorDD
    m1=longTramIzq/(ei1*ei)
    m2=2*(longTramIzq/(ei1*ei)+longTramDer/(ei2*ei))
    m3=longTramDer/(ei2*ei)
    #print(f"ecuación: {m1}M1+{m2}M2+{m3}M3={total}")
    if ecu==1:
        matrizmini=[m2,m3,0,0,0,total]
    elif ecu==2:
        matrizmini=[m1,m2,m3,0,0,total]
    elif ecu==3:
        matrizmini=[0,m1,m2,m3,0,total]
    elif ecu==4:
        matrizmini=[0,0,m1,m2,m3,total]
    elif ecu==5:
        matrizmini=[0,0,0,m1,m2,total]
    
    
    return matrizmini

 #logica del programa     
matriz=[]#matriz para obtener los resultados de cada ecuación
datosTramo1=datos("AB","BC")#llamamos a la función para obtener los datos del primer tramo
cargasP=[0,0]
cargasD=[0,0,0]
datosTramo1.keys()
matriz=ecuacion1(0,
        datosTramo1["LongitudLuz1"],
        datosTramo1["LongitudLuz1"],
        cargasP,
        0,
        datosTramo1["CargasPLuz1"],
        datosTramo1["#CargasPLuz1"],
        cargasD,
        datosTramo1["CargasDLuz1"],
        ei,
        datosTramo1["EI1"],
        1
        )
matriz1=[matriz[0],matriz[1],matriz[2],matriz[3],matriz[4]]
matriz2=[]
matriz2.append(matriz1)
matriz3=[]
matriz3.append(matriz[5])
#print(datosTramo1["CargasDLuz2"])
matriz=ecuacion1(datosTramo1["LongitudLuz1"],
        datosTramo1["LongitudLuz2"],
        datosTramo1["LongitudT"],
        datosTramo1["CargasPLuz1"],
        datosTramo1["#CargasPLuz1"],
        datosTramo1["CargasPLuz2"],
        datosTramo1["#CargasPLuz2"],
        datosTramo1["CargasDLuz1"],
        datosTramo1["CargasDLuz2"],
        datosTramo1["EI1"],
        datosTramo1["EI2"],
        2)
matriz1=[matriz[0],matriz[1],matriz[2],matriz[3],matriz[4]]
matriz2.append(matriz1)
matriz3.append(matriz[5])

datosTramo2=datos2(datosTramo1["EI2"],datosTramo1["LongitudLuz2"],datosTramo1["#CargasPLuz2"],datosTramo1["CargasPLuz2"],1,datosTramo1["CargasDLuz2"],"CD")
matriz=ecuacion1(datosTramo2["LongitudLuz1"],
        datosTramo2["LongitudLuz2"],
        datosTramo2["LongitudT"],
        datosTramo2["CargasPLuz1"],
        datosTramo2["#CargasPLuz1"],
        datosTramo2["CargasPLuz2"],
        datosTramo2["#CargasPLuz2"],
        datosTramo2["CargasDLuz1"],
        datosTramo2["CargasDLuz2"],
        datosTramo2["EI1"],
        datosTramo2["EI2"],
        3)
matriz1=[matriz[0],matriz[1],matriz[2],matriz[3],matriz[4]]
matriz2.append(matriz1)
matriz3.append(matriz[5])
datosTramo3=datos2(datosTramo2["EI2"],datosTramo2["LongitudLuz2"],datosTramo2["#CargasPLuz2"],datosTramo2["CargasPLuz2"],1,datosTramo2["CargasDLuz2"],"DE")
matriz=ecuacion1(datosTramo3["LongitudLuz1"],
        datosTramo3["LongitudLuz2"],
        datosTramo3["LongitudT"],
        datosTramo3["CargasPLuz1"],
        datosTramo3["#CargasPLuz1"],
        datosTramo3["CargasPLuz2"],
        datosTramo3["#CargasPLuz2"],
        datosTramo3["CargasDLuz1"],
        datosTramo3["CargasDLuz2"],
        datosTramo3["EI1"],
        datosTramo3["EI2"],
        4)
matriz1=[matriz[0],matriz[1],matriz[2],matriz[3],matriz[4]]
matriz2.append(matriz1)
matriz3.append(matriz[5])
matriz=ecuacion1(datosTramo3["LongitudLuz2"],
        0,
        datosTramo3["LongitudLuz2"],
        datosTramo3["CargasPLuz2"],
        datosTramo3["#CargasPLuz2"],
        cargasP,
        0,
        datosTramo3["CargasDLuz2"],
        cargasD,
        datosTramo3["EI2"],
        ei,
        5)
matriz1=[matriz[0],matriz[1],matriz[2],matriz[3],matriz[4]]
matriz2.append(matriz1)
matriz3.append(matriz[5])
a = np.array(matriz2)
b = np.array(matriz3)
c=0
print("Momentos\n")
f.write("Momentos\n")
for x in a:
    print(f"{x}={b[c]}")
    f.write(f"{x}={b[c]}\n")
    c+=1
m = np.linalg.solve(a,b)
c=0
momentos=['A','B','C','D','E']
for x in m:
    print(f"M{momentos[c]}={x}")
    f.write(f"M{momentos[c]}={x}\n")
    c+=1
fC=[]
#fuerzas cortantes
def fCort(longLuz,m1,m2,cargaP,numCP,cargaD,luz,l1,l2):#función que calcula las fuerzas cortantes en una luz
    print(f"Cortantes Luz {luz}")
    f.write(f"Cortantes Luz {luz}\n")
    cortantes=[]
    if numCP<2:#una o cero cargas puntuales
        v1=(-m1+m2+cargaP[1]*(longLuz-cargaP[0])+cargaD[0]*cargaD[2]*(cargaD[2]/2))/longLuz
        v2=-v1+cargaP[1]+cargaD[0]*longLuz
        cortantes.append(v1)
        cortantes.append(v2)
        print(f"V{l1} = {cortantes[0]}")
        f.write(f"V{l1} = {cortantes[0]}\n")
        print(f"V{l2} = {cortantes[1]}")
        f.write(f"V{l2} = {cortantes[1]}\n")
        return cortantes
    elif numCP>=2:#más de una carga puntual
        sum=0
        sum2=0
        for x in cargaP:
            sum+=(longLuz-x[0])*x[1]
            sum2+=x[1]
        v1=(-m1+m2+sum+cargaD[0]*longLuz*(longLuz/2))/longLuz
        v2=-v1+sum2+cargaD[0]*longLuz
        cortantes.append(v1)
        cortantes.append(v2)
        print(f"V{l1} = {cortantes[0]}")
        f.write(f"V{l1} = {cortantes[0]}\n")
        print(f"V{l2} = {cortantes[1]}")
        f.write(f"V{l2} = {cortantes[1]}\n")
        return cortantes
    
print("Fuerzas Cortantes: ")
f.write("Fuerzas Cortantes: \n")
fpC=fCort(datosTramo1["LongitudLuz1"],m[0],m[1],datosTramo1["CargasPLuz1"],datosTramo1["#CargasPLuz1"],datosTramo1["CargasDLuz1"],"AB","AB","BA")
fC.append(fpC[0])
fC.append(fpC[1])
fpC=fCort(datosTramo2["LongitudLuz1"],m[1],m[2],datosTramo2["CargasPLuz1"],datosTramo2["#CargasPLuz1"],datosTramo2["CargasDLuz1"],"BC","BC","CB")
fC.append(fpC[1])
fC[1]+=fpC[0]
fpC=fCort(datosTramo3["LongitudLuz1"],m[2],m[3],datosTramo3["CargasPLuz1"],datosTramo3["#CargasPLuz1"],datosTramo3["CargasDLuz1"],"CD","CD","DC")
fC.append(fpC[1])
fC[2]+=fpC[0]
fpC=fCort(datosTramo3["LongitudLuz2"],m[3],m[4],datosTramo3["CargasPLuz2"],datosTramo3["#CargasPLuz2"],datosTramo3["CargasDLuz2"],"DE","DE","ED")
fC.append(fpC[1])
fC[3]+=fpC[0]
c=0
print("Reacciones: ")
f.write("Reacciones: \n")
momentos=['RA','RB','RC','RD','RE']
for x in fC:
    print(f"{momentos[c]}={x}")
    f.write(f"{momentos[c]}={x}\n")
    c+=1
f.close()
m2.e(datosTramo1,datosTramo2,datosTramo3)