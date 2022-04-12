"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
from collections import Counter
from copy import copy
import csv
dic = dict()
dic_b = dic.copy()
dic_b = {}
dic_b["A"]= 0
dic_b["B"]= 0
dic_b["C"]= 0
dic_b["D"]= 0
dic_b["E"]= 0

with open("data.csv", "r",) as file:
   Lab_1 = csv.reader(file,delimiter = "\t")
   lista = list(Lab_1)
   listaa = list(Lab_1)
   #lista.sort()

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0  
    for linea in lista:
      suma += int(linea[1])
    return suma



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    for linea in lista:
       
        if linea[0] in dic:
       
            dic[linea[0]] += 1              
        else:
            dic[linea[0]] = 1
        letras_c = list(dic.items())


    return sorted(letras_c)
    


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    for linea in lista:
        sum_letra = linea[1]
        if linea[0] == "A":
            dic_b["A"] += int(sum_letra)
        if linea[0] == "B":
            dic_b["B"] += int(sum_letra)
        if linea[0] == "C":
            dic_b["C"] += int(sum_letra)
        if linea[0] == "D":
            dic_b["D"] += int(sum_letra)
        if linea[0] == "E":
            dic_b["E"] += int(sum_letra)
        letras_num = list(dic_b.items() )
    return letras_num
   


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    from collections import Counter
    mes = [linea[2].split("-")[1] for linea in lista]
    mes_num = Counter(mes).most_common(12)
    mes_num.sort()

    return mes_num

  


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    letras_A_max = max([(linea[0:2]) for linea in lista if linea[0] == "A"])
    letras_A_min = min([(linea[0:2]) for linea in lista if linea[0] == "A"])
    letras_B_max = max([(linea[0:2]) for linea in lista if linea[0] == "B"])
    letras_B_min = min([(linea[0:2]) for linea in lista if linea[0] == "B"])
    letras_C_max = max([(linea[0:2]) for linea in lista if linea[0] == "C"])
    letras_C_min = min([(linea[0:2]) for linea in lista if linea[0] == "C"])
    letras_D_max = max([(linea[0:2]) for linea in lista if linea[0] == "D"])
    letras_D_min = min([(linea[0:2]) for linea in lista if linea[0] == "D"])
    letras_E_max = max([(linea[0:2]) for linea in lista if linea[0] == "E"])
    letras_E_min = min([(linea[0:2]) for linea in lista if linea[0] == "E"])
    letrA = letras_A_max[0] , int(letras_A_max[1]) , int(letras_A_min[1])
    letrB = letras_B_max[0] , int(letras_B_max[1]) , int(letras_B_min[1])
    letrC = letras_C_max[0] , int(letras_C_max[1]) , int(letras_C_min[1])
    letrD = letras_D_max[0] , int(letras_D_max[1]) , int(letras_D_min[1])
    letrE = letras_E_max[0] , int(letras_E_max[1]) , int(letras_E_min[1])
    Conjunto = [letrA , letrB , letrC , letrD , letrE]
    
    return Conjunto


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    "separo y extraigo linea por linea su item de clave y valor"
    pr_1 = [linea[4].split(",") for linea in lista]
    union_0 = (pr_1[0]) 
    union_1 = (pr_1[1]) 
    union_2 = (pr_1[2]) 
    union_3 = (pr_1[3])
    union_4 = (pr_1[4]) 
    union_5 = (pr_1[5]) 
    union_6 = (pr_1[6]) 
    union_7 = (pr_1[7]) 
    union_8 = (pr_1[8]) 
    union_9 = (pr_1[9]) 
    union_10 = (pr_1[10]) 
    union_11 = (pr_1[11])
    union_12 = (pr_1[12]) 
    union_13 = (pr_1[13])
    union_14 = (pr_1[14]) 
    union_15 = (pr_1[15])
    union_16 = (pr_1[16]) 
    union_17 = (pr_1[17])
    union_18 = (pr_1[18]) 
    union_19 = (pr_1[19])
    union_20 = (pr_1[20]) 
    union_21 = (pr_1[21]) 
    union_22 = (pr_1[22]) 
    union_23 = (pr_1[23])
    union_24 = (pr_1[24]) 
    union_25 = (pr_1[25])
    union_26 = (pr_1[26]) 
    union_27 = (pr_1[27]) 
    union_28 = (pr_1[28]) 
    union_29 = (pr_1[29])
    union_30 = (pr_1[30]) 
    union_31 = (pr_1[31]) 
    union_32 = (pr_1[32]) 
    union_33 = (pr_1[33]) 
    union_34 = (pr_1[34]) 
    union_35 = (pr_1[35])
    union_36 = (pr_1[36]) 
    union_37 = (pr_1[37])
    union_38 = (pr_1[38]) 
    union_39 = (pr_1[39])
    "uno valores de cada linea para poder separar por clave y valor"
    u = (union_0 + union_1 + union_2 + union_3 + union_4 + union_5 + union_6 + union_7 + union_8 + union_9
        + union_10 + union_11 + union_12 + union_13 + union_14 + union_15 + union_16 + union_17 + union_18 + union_19
        + union_20 + union_21 + union_22 + union_23 + union_24 + union_25 + union_26 + union_27 + union_28 + union_29
        + union_30 + union_31 + union_32 + union_33 + union_34 + union_35 + union_36 + union_37 + union_38 + union_39)
    "separo la clave del valor"
    uz = [u[0:].split(":") for u in u]
    "corro for para sacar minimos y maximos"
    
    result = {}
    for k , v in uz:
        v = int(v)
        if k in result.keys():
            result[k].append(v)
        else:
            result[k] = [v]

    result = sorted([(k, min(v) , max(v)) for k, v in result.items()])

       
    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data = [linea[:2] for linea in lista]
    resul = {}
    for letra , valor in data:
        valor = int(valor)
        if valor in resul.keys():
             resul[valor].append(letra)
        else:
            resul[valor] = [letra]
    
    return sorted(resul.items())


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open("data.csv", "r",) as file:
        Lab_1 = csv.reader(file,delimiter = "\t")
        listaa = list(Lab_1)
    

    pr_7_0 = sorted([linea[0] for linea in listaa if linea[1] == "0"])
    pr_7_1 = sorted([linea[0] for linea in listaa if linea[1] == "1"])
    pr_7_2 = sorted([linea[0] for linea in listaa if linea[1] == "2"])
    pr_7_3 = sorted([linea[0] for linea in listaa if linea[1] == "3"])
    pr_7_4 = sorted([linea[0] for linea in listaa if linea[1] == "4"])
    pr_7_5 = sorted([linea[0] for linea in listaa if linea[1] == "5"])
    pr_7_6 = sorted([linea[0] for linea in listaa if linea[1] == "6"])
    pr_7_7 = sorted([linea[0] for linea in listaa if linea[1] == "7"])
    pr_7_8 = sorted([linea[0] for linea in listaa if linea[1] == "8"])
    pr_7_9 = sorted([linea[0] for linea in listaa if linea[1] == "9"])

    lin_0 = 0 , sorted(list(set(pr_7_0)))
    lin_1 = 1 , sorted(list(set(pr_7_1)))
    lin_2 = 2 , sorted(list(set(pr_7_2)))
    lin_3 = 3 , sorted(list(set(pr_7_3)))
    lin_4 = 4 , sorted(list(set(pr_7_4)))
    lin_5 = 5 , sorted(list(set(pr_7_5)))
    lin_6 = 6 , sorted(list(set(pr_7_6)))
    lin_7 = 7 , sorted(list(set(pr_7_7)))
    lin_8 = 8 , sorted(list(set(pr_7_8)))
    lin_9 = 9 , sorted(list(set(pr_7_9)))

   
    pr_7 = sorted([lin_0 , lin_1 , lin_2 ,lin_3 , lin_4 , lin_5 , lin_6 , lin_7 , lin_8 , lin_9])
         

        
    return pr_7


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    
    data=open('data.csv', 'r').readlines()
    data = [row[0:-1] for row in data]
    data = csv.reader(data,delimiter = "\t")
    data = [row[4].split(",") for row in data]

    result_9 = []

    for letra in data:
        data = [row.split(':') for row in letra]
        result_9 += data
        claves = []
        for a in result_9:
                claves.append(a[0])
        clavesval = Counter(claves).most_common(10)
        resultado = sorted(clavesval, reverse= False)
    return dict(resultado)


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    result_10 = []
    for letra in lista:
        letra_10 = letra[0]
        valor4 = [letra[4].split(",")]
        valor_4 = len(valor4[0])
        valor3 = [letra[3].split(",")]
        valor_3 = len(valor3[0])
        result_10.append((letra_10 , valor_3 , valor_4))
    return result_10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data=open('data.csv', 'r').readlines()
    data = [row[0:-1] for row in data]
    data = csv.reader(data,delimiter = "\t")
    data = [row[3].split(",") for row in data]
    result_9 = []

    for letra in data:
        result_9 += data
        clave = []
        for e in result_9:
            clave.append(e[0])
            resultado = sorted(list(set(clave)))

    columna1y3=[(z[3].split(','),z[1]) for z in lista]

    diccio = {}
    for clave in resultado:
        suma = 0
        for e in columna1y3:
            for letra in e[0]:
                if letra == clave:
                    suma = suma + int(e[1])
            dicc = {clave : suma}
            diccio.update(dicc)

    return diccio


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import csv
    data=open('data.csv', 'r').readlines()
    ult = data.copy()
    data = [row[0:-1] for row in data]
    data = csv.reader(data,delimiter = "\t")
    data = [(row[4].split(",") ) for row in data]


    listasumas = []
    col1 = [row[0] for row in ult]

    for letra in data:
        data = [row.split(":") for row in letra]
        total = []
        for a in data:
            val = a[1:]
            total += val
        valores = [int(row) for row in total]
        val = sum(valores)
        listasumas.append(val)
    grupos = sorted(list(zip(col1,listasumas)))
    lisletras = []
    lisfinal = []
    for a in ult:
        lisletras.append(a[0])
    for letra in set(lisletras):
        counter = 0
        for lista in grupos:
            if lista[0] == letra:
                counter= counter + lista[1]
        lisfinal.append((letra,counter))


    return dict(lisfinal)
