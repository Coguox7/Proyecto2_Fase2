"""
Universidad del Valle de Guatemala
Algoritmos y estructura de datos
Proyecto final: Algoritmo de recomendación

Camilo Mayen - 17184
Juan Carlos Menchu - 16150
Pablo Coguox - 19960
"""


"""
******************************Inicio de las funciones**************************************
"""
#Funcion para imprimir el menu
def imprimir_menu():
    print ("*********************Menu*********************")
    print ("1. Transferir datos de Excel a la base de datos")
    print ("2. Ingresar restaurante nuevo a la base de datos")
    print ("3. Pedir recomendacion de restaurante")
    print ("6. Salir\n")
    

#funcion para agregar datos de Excel a la base de datos
def agregar_datos_Excel():
    
    #se recorren las filas que no esten vacias
    for i in range(hoja.nrows):
        
        nombre_restaurante = hoja.cell_value(i,0)
        ubicacion = hoja.cell_value(i,1)
        precio = hoja.cell_value(i,2)
        tipo = hoja.cell_value(i,3)
        
        #Todos los datos del restaurantese vuelve minusculas para que sea más facil verificar si ya existen o no
        nombre_restaurante=nombre_restaurante.lower()
        ubicacion=ubicacion.lower()
        precio=precio.lower()
        tipo=tipo.lower()

        database[nombre_restaurante]=[ubicacion,precio,tipo]

        #Creacion de nodo 
        nuevo = base_datos.nodes.create(ubicacion=ubicacion, precio=precio,tipo=tipo,name=nombre_restaurante)
        dataB.add(nuevo)
        
        #Se crea una relacion entre el restaurante y sus datos 
        try:
            nuevo.relationships.create("sus_datos_son", datos.get(datos=ubicacion)[0])
        
        except Exception:
            #creacion del nodo de datos
            genNode = base_datos.nodes.create(datos=ubicacion)
            datos.add(genNode)
            #Creacion relacion con el nodo datos
            nuevo.relationships.create("sus_datos_son", datos.get(datos=ubicacion)[0])

            

        try:
            nuevo.relationships.create("sus_datos_son", datos.get(datos=precio)[0])
            #datos.get(datos=precio)[0].relationships.create("sus_datos_son", nuevo)
        except Exception:
            #creacion del nodo datos
            genNode = base_datos.nodes.create(datos=precio)
            datos.add(genNode)
            #Creacion relacion con el nodo datos
            nuevo.relationships.create("sus_datos_son", datos.get(datos=precio)[0])
            

        try:
            nuevo.relationships.create("sus_datos_son", datos.get(datos=tipo)[0])
            #datos.get(datos=tipo)[0].relationships.create("sus_datos_son", nuevo)
        except Exception:
            #creacion del nodo datos
            genNode = base_datos.nodes.create(datos=tipo)
            datos.add(genNode)
            #Creacion relacion con el nodo datos
            nuevo.relationships.create("sus_datos_son", datos.get(datos=tipo)[0])

                            
#funcion agregar restaurante
def agregar_restaurante(nombre_restaurante,ubicacion,precio,tipo):

    nuevo = base_datos.nodes.create(name=nombre_restaurante, ubicacion=ubicacion, precio=precio,tipo=tipo)
    dataB.add(nuevo)


    try:
        #Creacion relacion del nodo datos
        nuevo.relationships.create("sus_datos_son", datos.get(datos=ubicacion)[0])
    except Exception:
        #creacion del nodo datos
        genNode = base_datos.nodes.create(datos=ubicacion)
        datos.add(genNode)
        #Creacion relacion con el nodo datos
        nuevo.relationships.create("sus_datos_son", datos.get(datos=ubicacion)[0])

            

    try:
        nuevo.relationships.create("sus_datos_son", datos.get(datos=precio)[0])
        #datos.get(datos=precio)[0].relationships.create("sus_datos_son", nuevo)
    except Exception:
        #creacion del nodo datos
        genNode = base_datos.nodes.create(datos=precio)
        datos.add(genNode)
        #Creacion relacion con el nodo datos
        nuevo.relationships.create("sus_datos_son", datos.get(datos=precio)[0])
            

    try:
        nuevo.relationships.create("sus_datos_son", datos.get(datos=tipo)[0])
        #datos.get(datos=tipo)[0].relationships.create("sus_datos_son", nuevo)
    except Exception:
        #creacion nodo datos
        genNode = base_datos.nodes.create(datos=tipo)
        datos.add(genNode)
        #Creacion relacion con de nodo datos
        nuevo.relationships.create("sus_datos_son", datos.get(datos=tipo)[0])
        
    database[nombre_restaurante] = [ubicacion,precio,tipo]

#funcion que realiza las recomendaciones
def recomendacion(nombre_restaurante):
    datosderestaurante_sugerido=[]
    #Se encuentran los tres datoss
    try:
        query = "MATCH (n:Restaurante) WHERE n.name='"+nombre_restaurante+"' RETURN n.ubicacion"
        results = base_datos.query(query, data_contents=True)
        a = results.rows
        for x in a:
            datosderestaurante_sugerido.append(x[0])
        ubicacion_=datosderestaurante_sugerido[0]
    except Exception:
        print("No se encuentra en la base de datos")
        
    try:
        query = "MATCH (n:Restaurante) WHERE n.name='"+nombre_restaurante+"' RETURN n.precio"
        results = base_datos.query(query, data_contents=True)
        a = results.rows
        
        for x in a:
            datosderestaurante_sugerido.append(x[0])
        precio_=datosderestaurante_sugerido[1]
    except Exception:
        print("No se encuentra en la base de datos")
        
    try:
        query = "MATCH (n:Retaurante) WHERE n.name='"+nombre_restaurante+"' RETURN n.tipo"
        results = base_datos.query(query, data_contents=True)
        a = results.rows
        
        for x in a:
            datosderestaurante_sugerido.append(x[0])
        tipo_=datosderestaurante_sugerido[2]
    except Exception:
        print("No se encuentra en la base de datos")
    
    #Ya encontramos los tres datoss

    print ("lista de primer datos:")
    #Hacemos lista con el restaurante que tienen su primer datos
    try:
        query = "match(n:Restaurante{ubicacion:'"+ubicacion_+"'}) return n.name"
        results = base_datos.query(query, data_contents=True)
        a = results.rows
        restaurantes1 = []
        for x in a:
            if x not in restaurantes1:
                restaurantes1.append(x[0])
        for i in restaurantes1:
            print(i)    
    except Exception:
        print ("")

    print ("\nlista de segundo datos:")
    #Hacemos lista con restaurantess que tienen su segundo datos
    try:
        query = "match(n:Restaurante{ubicacion:'"+precio_+"'}) return n.name"
        results = base_datos.query(query, data_contents=True)
        a = results.rows
        restaurantes2 = []
        for x in a:
            if x not in restaurantes2:
                restaurantes2.append(x[0])
        for i in restaurantes2:
            print(i)
    except Exception:
        print("")
        
    print ("\nlista de tercer datos:")
    #Hacemos lista con restaurantess que tienen su tercer datos
    try:
        query = "match(n:Restaurante{tipo:'"+tipo_+"'}) return n.name"
        results = base_datos.query(query, data_contents=True)
        a = results.rows
        restaurantess3 = []
        for x in a:
            if x not in restaurantes3:
                restaurantes3.append(x[0])
        for i in restaurantes3:
            print(i)
    except Exception:
        print("")
        
    lista_recomendacion=[]
    for i in restaurantes1:
        if i in restaurantes2:
            lista_recomendacion.append(i)
    for i in restaurantes1:
        if i in restaurantes3:
            if i not in lista_recomendacion:
                lista_recomendacion.append (i)
    print ("\nlista de restaurantes recomendas")
    for i in lista_recomendacion:
        print(i)
    
"""
******************************Fin de las funciones**************************************
"""


#Biblioteca para poder trabajar con excel
import xlrd
#Parte donde empezamos a trabajar con excel
documento = xlrd.open_workbook("data_base.xlsx")
hoja = documento.sheet_by_index(0)


from neo4jrestclient.client import GraphDatabase
base_datos = GraphDatabase("http://localhost:8097",username="neo4j", password="12345")
dataB = base_datos.labels.create("Restaurante")
datos = base_datos.labels.create("datos")

database = {}
datoss_existentes=[]

#ciclo para el programa
ciclo = True
while ciclo:
    
    #imprimir menu
    imprimir_menu()
    opcion=input("Ingrese la accion que desea realizar (solamente el número): ")
    
    #si opcion = 1, se ingresan los datos del excel a la base de datos
    if (opcion==1):
        agregar_datos_Excel()
        
    #si opcion = 2, se solicitan datos del restaurante y luego se ingresa a la base de datos
    elif (opcion==2):

        nombre_restaurante=input("Ingresar nombre del restaurante: ")
        ubicacion=input ("Ingrese datos 1: ")
        precio=input ("Ingrese datos 2: ")
        tipo=input ("Ingrese datos 3: ")

        nombre_restaurante=nombre_restaurante.lower()
        ubicacion=ubicacion.lower()
        precio=precio.lower()
        tipo=tipo.lower()
        print ("Ingreso el nuevo restaurante en la base de datos en curso")
        agregar_restaurante(nombre_restaurante,ubicacion,precio,tipo)
        
    elif (opcion==3):
        print("recomendacion")
        nombre_restaurante=input("Ingrese nombre de su restaurante favorito: ")
        recomendacion(nombre_restaurante)
    elif (opcion==4):
        print("pendiente")
    elif (opcion==5):
        print("pendiente")
    elif (opcion==6): 
        ciclo=False
    else:
        print ("Ha ingresado un valor invalido, reinicie el programa")
        ciclo=False
        
        

        
        




