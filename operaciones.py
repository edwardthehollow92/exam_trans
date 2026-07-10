def guardar_arreglos(arreglos):
    arreglos = {
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno']
}


    try:
        cantidad= int(input(f"cantidad de arreglos{arreglos}"))
    except:
        print("debe ingresar un valor correcto por ejemplo FLO1")
        return
    
    for i in range(cantidad):
        arreglos = input(f"arreglos {i+1}:").strip().lower()
        cantidad.append(cantidad)
        print("arreglo guardado")



def unidades_arreglos(arreglos):
    if not arreglos:
        print("no hay arreglos registrados")
        return
    
    for posicion, arreglo in enumerate (arreglos,1):
        arreglos = ",".join([arreglo.title()for arreglo in arreglos["arreglos"]])
        print(f"\n arreglo{posicion}")
        print(f"\n tipo:{arreglo['tipo'].title()}")
        print(f"\n color:{arreglo['color']}")
        print(f"\n tamaño:{arreglo['tamaño']}")
        print(f"\n temporada:{arreglo}")

def busqueda_precios(arreglos):
    bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6]
   }
    

def precio_Actualizar(arreglos):
    try:
        precio= int(input(f"el precio es de {bodega},desea actualizarlo?:(s/n)"))
    except:
        print(f"el precio es de {bodega},desea actualizarlo? (s/n)")
        return
    


