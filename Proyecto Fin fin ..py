import random
global Diccionario,km,ciudades,numero,minimo,kim
Diccionario={}
km=[]
ciudades=[]
numero=[]
kim=[]
minimo=[]


def REGISTRO():
    Diccionario={}
    print("\n********REGISTRO DE DATOS********")
    cant_ciudades=int(input("\nCunatas ciudades desea ingresar: "))
    n=0
    while n<cant_ciudades:
        while True:
            x=-1
            ciu=input("\nIngrese la Ciudad : ")
            for i in range(n):
                if (ciudades[i]==ciu):
                    x=0
            if(x==0):
                print("\nCiudad Registrada")
            else:
                ciudades.append(ciu)
                n=n+1
                break
    x=0
    y=0
    while x < cant_ciudades:
        kim=[]
        y=0
        while y < cant_ciudades:
            kim.append(0)
            y=y+1
        km.append(kim)
        x=x+1
    x=0
    while x < cant_ciudades:
        y=0
        while y < cant_ciudades:
            if x==y:
                km[x][y]=0
            else:
                if y<x:
                    km[x][y]=km[y][x]
                else:
                    km[x][y]=random.randint(0,100)
            y=y+1
        Diccionario[x]=(ciudades[x],km[x])
        x=x+1
    minimo.append(random.randint(0,100))
    return Diccionario
    

def CONSULTADA(Diccionario):
    print("\n********CONSULTA DE DATOS********\n")
    ac=0
    for x in Diccionario:
         print("\t|",Diccionario[x][0],end="")
         ac=ac+1
    print()
    x=0
    while x < ac:
        y=0
        print(ciudades[x],end="\t|")
        while y < ac:
            print("  ",km[x][y],end="\t|")
            y=y+1
        print()
        x=x+1
    print("\tMinimo: ",minimo[0])
    return Diccionario


def CONSULTADI(Diccionario,numero):
    print("\n********CONSULTAR DISTANCIAS********")
    while True:
        ori_num=-1
        ori=(input("\nIngrese Ciudad de origen: "))
        for numero in Diccionario:
            if (ciudades[numero]==ori):
                ori_num=numero
        if(ori_num==-1):
            print("Error ",ori," no esta definida e la lista de ciudades.")
        else:
            break   
    while True:
        des_num=-1
        des=input("\nIngrese Ciudad Destino: ")
        for numero in Diccionario:
            if (ciudades[numero]==des):
                des_num=numero
        if(des_num==-1):
            print("Error ",des," no esta definida e la lista de ciudades.")
        else:
            break
    p_num=0
    if (km[ori_num][des_num] >= minimo[0]):
        print("La distancia entre ",ori," y ",des,"es ",km[ori_num][des_num]," km")
    else:
        for numero in Diccionario:
            if(km[ori_num][numero] >= minimo[0] and km[numero][des_num] >= minimo[0]):
                    p_num=numero
                    print("Ciudad p: ",ciudades[p_num])
                    print("La distancia entre ",ori," y ",ciudades[p_num]," es ",km[ori_num][numero],"km")
                    print("La distancia entre ",ciudades[p_num]," y ",des," es ",km[numero][des_num],"km")
                    suma=km[numero][des_num]+km[ori_num][numero]
                    print("Recorrido total ",suma,"km")
                    break
            else:
                p_num=-1
        if p_num==-1:
            print("No se puede viajar de ",ori," a ",des)
    return Diccionario
            



def GUARDAR(Diccionario,numero,kim):
    with open("distancias.txt","w") as w:
        q=[]
        for nume in Diccionario:
            q=ciudades[nume]
            w.write(str(q)+"\t")
        w.write("\n")
        for num in Diccionario:
            for n in Diccionario:             
                klm=km[num][n]
                w.write(str(klm)+"\t")
            w.write("\n")
        w.write(str(minimo[0])+"\n")
    return Diccionario

def RECUPERAR(Diccionario,minimo,ciudades,km):
    with open("distancias.txt","r")as l:
        n=l.readlines()
        l.close()
        Diccionario={}
        a=[]
        x=0
        m=0
        for i in range(len(n)):
            a.append(n[i].rstrip().split("\t"))
            x=x+1
        j=1
        ciudades=a[0]
        m=a[(x-1)]
        while j < (x-1):
            km.append(a[j])
            j=j+1
        y=0
        while y < (x-2):
            Diccionario[y]=(ciudades[y],km[y])
            y=y+1
    return m,Diccionario
while True:
    print("\n********MENU********")
    print("1. REGISTRO DE DATOS")
    print("2. CONSULTA DE DATOS")
    print("3. CONSULTAR DISTANCIAS")
    print("4. GUARDAR DATOS")
    print("5. CARGAR DATOS")
    print("6. SALIR")
    opcion=int(input("\n\t ELIJA UNA OPCION: "))
    if opcion==1:
        Diccionario=REGISTRO()
    elif opcion==2:
        CONSULTADA(Diccionario)
    elif opcion==3:
        CONSULTADI(Diccionario,numero)
    elif opcion==4:
        GUARDAR(Diccionario,numero,kim)
    elif opcion==5:
        minimo,Diccionario=RECUPERAR(Diccionario,minimo,ciudades,km)
        for n in Diccionario:
            ciudades.append(Diccionario[n][0])
            km.append(Diccionario[n][1])
    elif opcion==6:
        exit()
