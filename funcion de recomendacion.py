def recomendacion(nombre_restaurante):
    #Encontramos la ubicacion del restaurante
    try:
        location = "MATCH (n:Database {nombre:'"+nombre_restaurante+"'}) RETURN n.ubicacion"  
    except Exception:
        print("")
    #Hacemos lista con restaurantes que tiene el primer dato (ubicacion)
    try:
        query = "MATCH (n:Database {ubicacion:'"+location+"'}) RETURN n.nombre"
        results = db.query(query, data_contents=True)
        a = results.rows
        restaurantes1 = []
        for x in a:
            if x not in restaurantes1:
                b.append(x)   
    except Exception:
        print("")

    #Encontramos el segundo dato
    try:
        price = "MATCH (n:Database {nombre:'"+nombre_restaurante+"'}) RETURN n.precio"    
    except Exception:
        print("")
    #Hacemos lista de restaurante que tienen su segundo dato
    try:
        query = "MATCH (n:Database {precio:'"+price+"'}) RETURN n.nombre"
        results = db.query(query, data_contents=True)
        a = results.rows
        restaurantes2 = []
        for x in a:
            if x not in restaurantes2:
                b.append(x)   
    except Exception:
        print("")
  
    #Encontramos el tercer dato de restaurante 
    try:
        class = "MATCH (n:Database {nombre:'"+nombre_restaurante+"'}) RETURN n.tipo"        
    except Exception:
        print("")

    try:
        query = "MATCH (n:Database {tipo:'"+class+"'}) RETURN n.nombre"
        results = db.query(query, data_contents=True)
        a = results.rows
        restaurantes3 = []
        for x in a:
            if x not in restaurantes3:
                b.append(x)   
    except Exception:
        print("")

    lista_recomendacion=[]
    for i in pelicul1:
        if i in restaurantes2:
            lista_recomendacion.append(i)
    for i in restaurantes1:
        if i in restaurantes3:
            if i not in lista_recomendacion:
                lista_recomendacion.append (i)