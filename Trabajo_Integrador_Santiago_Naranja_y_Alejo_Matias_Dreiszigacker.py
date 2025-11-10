#Entrega Trabajo Integrador - Santiago Naranja y Alejo Matias Dreiszigacker

def crear_o_cargar_CSV(): #Esta funcion busca crear el CSV con el encabezado si no existe el archivo inicial, o si existe, te levanta la información de ese archivo

    with open("paises.csv", "a") as archivo:
        if archivo.tell() == 0:                 
            archivo.write("nombre,poblacion,superficie,continente\n")
    
    paises=[]
    with open("paises.csv", "r") as archivo:
        
        for i, linea in enumerate(archivo):
            linea = linea.strip()

            
            if i == 0 and linea.lower().replace(" ", "") == "nombre,poblacion,superficie,continente":
                continue
            if not linea.strip():
                continue

            
            partes = linea.split(",")
            if len(partes) != 4:
                continue  
            nombre = partes[0].strip()
            poblacion = int(partes[1].strip())
            superficie = int(partes[2].strip())
            continente = partes[3].strip()
            paises.append({"NOMBRE": nombre, "POBLACION": poblacion, "SUPERFICIE": superficie, "CONTINENTE": continente })
                   
    return paises

def agregar_pais(nombre, poblacion, superficie, continente): #Funcion para agregar un pais solo al CSV

    with open("paises.csv", "a") as archivo:
        
        archivo.write(f"{nombre},{poblacion},{superficie},{continente}\n")
        
    print("=======")    
    print(f"El pais '{nombre}' fue ingresado correctamente con una poblacion de {poblacion}, una superficie de {superficie}, y el continente {continente}.")
    print("=======")

def indice_pais(paises, nombre):
    nombre_lower = nombre.lower().strip()
    for i, item in enumerate(paises):
        if isinstance(item, dict):
            if str(item.get("NOMBRE", "")).lower().strip() == nombre_lower:
                return i
    return -1

def existe_pais(paises, nombre_pais):  #Funcion para ver si un pais existe o no
    pais_lower = nombre_pais.lower().strip()
    return any(
        isinstance(item, dict) and str(item.get("NOMBRE", "")).lower().strip() == pais_lower
        for item in paises
    )
    
def buscar_paises(paises, nombre_parcial): #Funcion para la busqueda entera o parcial
    
    buscado = nombre_parcial.lower().strip()
    coincidencias = []

    for item in paises:
        if not isinstance(item, dict):
            continue

        nombre = str(item.get("NOMBRE", "")).lower().strip()

        if buscado in nombre:
            coincidencias.append(item)

    return coincidencias
    
def asignar_poblacion_superficie_CSV(indice, nueva_poblacion, nueva_superficie): #Funcion para nueva poblacion y superficie
    
    with open("paises.csv", "r") as archivo:
        lineas = archivo.readlines()

    header = lineas[0].strip()   
    datos = lineas[1:]         
   
    linea = datos[indice].strip()       
    partes = linea.split(",")        
    
    nombre = partes[0].strip()
    continente = partes[3].strip()
    
    nueva_poblacion = int(nueva_poblacion) #por las dudas los convierto a int
    nueva_superficie = int(nueva_superficie) #por las dudas los convierto a int
        
    datos[indice] = f"{nombre},{nueva_poblacion},{nueva_superficie},{continente}\n"

    with open("paises.csv", "w") as archivo:
        archivo.write(header + "\n")
        archivo.writelines(datos)

def printpaises(paises):
    if not paises:
        print("No hay países para mostrar.")
        return
    print("=======")
    for p in paises:
        print(f"NOMBRE: {p['NOMBRE']}, POBLACION: {p['POBLACION']}, SUPERFICIE: {p['SUPERFICIE']}, CONTINENTE: {p['CONTINENTE']}")
    print("=======")

def filtrar_paises(paises): ## Funcion para filtrar paises segun diferentes criterios.

    if not paises:
        print("No hay países cargados para filtrar.")
        return []

    while True:
        print("=== FILTROS ===")
        print("1) Por continente")
        print("2) Por población ")
        print("3) Por superficie")
        print("4) Por densidad")
        print("5) Volver")
        opc = input("Opción: ").strip()

        while not opc.isdigit() or opc=="":
            print("=======")
            print(f"No ingresaste una opcion correcta. Tiene que ser un valor del 1 al 5 según los filtros disponibles:")
            print("=== FILTROS ===")
            print("1) Por continente")
            print("2) Por población ")
            print("3) Por superficie")
            print("4) Por densidad")
            print("5) Volver")
            opc= input(f"Ingresa nuevamente su opción: ")

        if opc == "1":
            parte = input("Ingrese continente (entero o parcial, ej: 'amer' para América): ").lower().strip()
            res = [
                p for p in paises
                if parte in str(p.get("CONTINENTE", "")).lower()
            ]
            printpaises(res)
            return res

        elif opc == "2":
            minimo = input("Población mínima (o enter para omitir): ").strip()
            
            while not minimo.isdigit() and minimo != "":
                print("=======")
                print("No ingresaste un valor de poblacion correcto. Tiene que ser un valor numerico positivo")
                minimo= input(f"Ingresa nuevamente la población mínima: ")
            
            maximo = input("Población máxima (o enter para omitir): ").strip()
            
            while not maximo.isdigit() and maximo != "":
                print("=======")
                print("No ingresaste un valor de poblacion correcto. Tiene que ser un valor numerico positivo")
                maximo= input(f"Ingresa nuevamente la población maxima: ")
            
            min_val = int(minimo) if minimo.isdigit() else None
            max_val = int(maximo) if maximo.isdigit() else None

            def ok(val):
                if min_val is not None and val < min_val: return False
                if max_val is not None and val > max_val: return False
                return True

            res = [p for p in paises if ok(p["POBLACION"])]
            printpaises(res)
            return res

        elif opc == "3":
            minimo = input("Superficie mínima (o enter para omitir): ").strip()
            
            while not minimo.isdigit() and minimo != "":
                print("=======")
                print("No ingresaste un valor de superficie correcto. Tiene que ser un valor numerico positivo")
                minimo= input(f"Ingresa nuevamente la superficie mínima: ")
            
            maximo = input("Superficie máxima (o enter para omitir): ").strip()
            
            while not maximo.isdigit() and maximo != "":
                print("=======")
                print("No ingresaste un valor de superficie correcto. Tiene que ser un valor numerico positivo")
                maximo= input(f"Ingresa nuevamente la superficie maxima: ")
            
            min_val = int(minimo) if minimo.isdigit() else None
            max_val = int(maximo) if maximo.isdigit() else None

            def ok(val):
                if min_val is not None and val < min_val: return False
                if max_val is not None and val > max_val: return False
                return True

            res = [p for p in paises if ok(p["SUPERFICIE"])]
            printpaises(res)
            return res

        elif opc == "4":
            def densidad(p):
                sup = p["SUPERFICIE"]
                return p["POBLACION"] / sup if sup > 0 else 0

            minimo = input("Densidad mínima (o enter para omitir): ").strip()
            
            while not minimo.isdigit() and minimo != "":
                print("=======")
                print("No ingresaste un valor de densidad correcto. Tiene que ser un valor numerico positivo")
                minimo= input(f"Ingresa nuevamente la densidad mínima: ")
            
            maximo = input("Densidad máxima (o enter para omitir): ").strip()
            
            while not maximo.isdigit() and maximo != "":
                print("=======")
                print("No ingresaste un valor de densidad correcto. Tiene que ser un valor numerico positivo")
                maximo= input(f"Ingresa nuevamente la densidad maxima: ")
            

            min_val = float(minimo) if minimo.replace(".", "", 1).isdigit() else None
            max_val = float(maximo) if maximo.replace(".", "", 1).isdigit() else None

            def ok(d):
                if min_val is not None and d < min_val: return False
                if max_val is not None and d > max_val: return False
                return True

            res = [p for p in paises if ok(densidad(p))]
            printpaises(res)
            return res

        elif opc == "5":
            return paises
        else:
            print("Opción inválida de filtro.")

def ordenar_paises(paises): ## Funcion para ordenar paises segun diferentes criterios
    if not paises:
        print("No hay países cargados para ordenar.")
        return []

    print("=== CRITERIOS DE ORDEN ===")
    print("1) NOMBRE")
    print("2) POBLACION")
    print("3) SUPERFICIE")
    print("4) CONTINENTE")
    print("5) DENSIDAD (población/superficie)")
    opc = input("Opción: ").strip()

    def clave_nombre(p):
        return str(p["NOMBRE"]).lower()

    def clave_poblacion(p):
        return p["POBLACION"]

    def clave_superficie(p):
        return p["SUPERFICIE"]

    def clave_continente(p):
        return str(p["CONTINENTE"]).lower()

    def clave_densidad(p):
        return (p["POBLACION"] / p["SUPERFICIE"]) if p["SUPERFICIE"] > 0 else float("inf")

    clave = None
    if opc == "1":
        clave = clave_nombre
    elif opc == "2":
        clave = clave_poblacion
    elif opc == "3":
        clave = clave_superficie
    elif opc == "4":
        clave = clave_continente
    elif opc == "5":
        clave = clave_densidad
    else:
        print("Opción inválida.")
        return paises

    sentido = input("Orden ascendente (A) o descendente (D): ").strip().lower()
    
    while sentido != "a" and sentido != "d" :
                print("=======")
                print("No ingresaste un valor de orden correcto.")
                sentido= input(f"Ingresa nuevamente - Orden ascendente (A) o descendente (D):  ")
    
    reverse = (sentido == "d")
    ordenada = sorted(paises, key=clave, reverse=reverse)
    printpaises(ordenada)
    return ordenada

def mostrar_estadisticas(paises): ## Funcion para mostrar estadisticas de los paises cargados
    if not paises:
        print("No hay países cargados para estadísticas.")
        return

    def clave_poblacion(p):
        return p["POBLACION"]

    def clave_superficie(p):
        return p["SUPERFICIE"]

    def clave_densidad(x):
        return x[1]

    n = len(paises)
    pobl_total = sum(p["POBLACION"] for p in paises)
    sup_total = sum(p["SUPERFICIE"] for p in paises)
    prom_pobl = pobl_total / n if n else 0
    prom_sup = sup_total / n if n else 0

    mayor_pob = max(paises, key=clave_poblacion)
    menor_pob = min(paises, key=clave_poblacion)
    mayor_sup = max(paises, key=clave_superficie)
    menor_sup = min(paises, key=clave_superficie)

    densidades = [(p["NOMBRE"], (p["POBLACION"] / p["SUPERFICIE"]) if p["SUPERFICIE"] > 0 else 0) for p in paises]
    dens_prom = sum(d for _, d in densidades) / n if n else 0
    d_max = max(densidades, key=clave_densidad)
    d_min = min(densidades, key=clave_densidad)

    print("====== ESTADÍSTICAS ======")
    print(f"Cantidad de países: {n}")
    print(f"Población total: {pobl_total}")
    print(f"Población promedio: {prom_pobl:.2f}")
    print(f"Superficie total: {sup_total}")
    print(f"Superficie promedio: {prom_sup:.2f}")
    print(f"Mayor población: {mayor_pob['NOMBRE']} ({mayor_pob['POBLACION']})")
    print(f"Menor población: {menor_pob['NOMBRE']} ({menor_pob['POBLACION']})")
    print(f"Mayor superficie: {mayor_sup['NOMBRE']} ({mayor_sup['SUPERFICIE']})")
    print(f"Menor superficie: {menor_sup['NOMBRE']} ({menor_sup['SUPERFICIE']})")
    print(f"Densidad promedio: {dens_prom:.4f} hab/km²")
    print(f"Mayor densidad: {d_max[0]} ({d_max[1]:.4f} hab/km²)")
    print(f"Menor densidad: {d_min[0]} ({d_min[1]:.4f} hab/km²)")
    print("===========================")


def main(): #Funcion principal que contiene el menu iterativo, de esta forma evitamos variables globales
    
    paises= crear_o_cargar_CSV()
    opcion= ""   
        
    while opcion!= "7":
        print("===GESTIÓN DE DATASET DE PAISES===")
        print("Ingrese 1 para Ingresar un país con sus datos")
        print("Ingrese 2 para Actualizar los datos de población y superficie de un pais")
        print("Ingrese 3 para Buscar un pais por nombre")
        print("Ingrese 4 para Filtrar paises")
        print("Ingrese 5 para Ordenar países")
        print("Ingrese 6 para Mostrar estadísticas")
        print("Ingrese 7 para Salir")
        print(" ")
        print("===INGRESAR OPCIÓN====")
        opcion = input("Opción: ").strip()
        
        match opcion:
            case "1":
                
                ingreso_pais=input("Ingresar el nombre del pais a almacenar: ")
                
                paises= crear_o_cargar_CSV()
        
                while existe_pais(paises, ingreso_pais) == True or ingreso_pais == "":
                    print("=======")
                    print("Pais repetido o en blanco. Por favor, intente nuevamente")
                    ingreso_pais = input("Ingrese nuevamente el nombre de un pais: ").strip()
                    print("=======")
                    
                poblacion = input(f"Ingresar la población del pais '{ingreso_pais}': ")
                    
                while not poblacion.isdigit() or poblacion=="":
                    print("=======")
                    print(f"No ingresaste una cantidad de población para el pais '{ingreso_pais}' correcta, tiene que ser un valor numerico positivo.")
                    poblacion= input(f"Ingresa nuevamente la poblacion: ")
                    
                superficie = input(f"Ingresar la superficie del pais '{ingreso_pais}': ")
                    
                while not superficie.isdigit() or superficie=="" :
                    print("=======")
                    print(f"No ingresaste una cantidad de superficie para el pais '{ingreso_pais}' correcta, tiene que ser un valor numerico positivo.")
                    superficie= input(f"Ingresa nuevamente la superficie: ")
                
                continente = input(f"Ingresar el continente del pais '{ingreso_pais}': ")
                    
                while continente == "":
                    print("=======")
                    print(f"No ingresaste ningun continente para el pais '{ingreso_pais}', el valor no puede estar vacio.")
                    continente= input(f"Ingresa nuevamente el continente: ")
                
                agregar_pais(ingreso_pais, poblacion, superficie, continente)
                paises.append({"NOMBRE": ingreso_pais, "POBLACION": int(poblacion), "SUPERFICIE": int(superficie), "CONTINENTE": continente})
                
                print("Se agreggo el pais correctamente al CSV con todos sus datos.")
                print("==========================================")    
                
                
            case "2":
                if not paises:
                    print("No hay paises ingresados. Primero deben existir paises en el CSV para actualizar los datos de poblacion y superficie de un pais.")
                    continue
                
                seleccion= input(f"Ingrese el país que quiere actualizar su Población y Superficie: ")
                
                pais_lower = seleccion.lower().strip()
                
                posicion=indice_pais(paises, pais_lower)
                
                if posicion == -1:
                    print("No hay coincidencias con el pais ingresado")
                else:
                    poblacion = input(f"Ingresar la población a actualizar del pais '{seleccion}': ")
                    while not poblacion.isdigit():
                        print("=======")
                        print(f"No ingresaste una cantidad correcta, tiene que ser un valor numerico positivo.")
                        print("=======")
                        poblacion= input(f"Ingresa nuevamente la poblacion: ")
                        
                    superficie = input(f"Ingresar la superficie a actualizar del pais '{seleccion}': ")
                    while not superficie.isdigit():
                        print("=======")
                        print(f"No ingresaste una cantidad correcta, tiene que ser un valor numerico positivo.")
                        print("=======")
                        superficie= input(f"Ingresa nuevamente la superficie: ")
                        
                        
                    paises[posicion]["POBLACION"] = int(poblacion)
                    poblacion_nueva= paises[posicion]["POBLACION"]
                    
                    paises[posicion]["SUPERFICIE"] = int(superficie)
                    superficie_nueva= paises[posicion]["SUPERFICIE"]
                    
                    
                    asignar_poblacion_superficie_CSV(posicion,poblacion_nueva, superficie_nueva)
                    print("=======")
                    print(f"El país '{seleccion}' fue actualizado correctamente con la poblacion {poblacion_nueva} y con la superficie {superficie_nueva} en el CSV.")
                    print("=======")
                    
                    
            case "3": 
                if not paises:
                    print("No hay paises ingresados. Primero deben existir paises en el CSV para hacer una busqueda.")
                    continue
                
                busqueda = input(f"Ingresar el nombre entero o parcial del pais a buscar: ")
                
                paises = crear_o_cargar_CSV()
                resultado = buscar_paises(paises, busqueda)

                if resultado:
                    print("=======")
                    print("Se encontro al siguiente pais o listado de paises con coincidencias enteras o parciales:")
                    for p in resultado:
                        print("NOMBRE:",p["NOMBRE"],",","POBLACION:", p["POBLACION"],",","SUPERFICIE:", p["SUPERFICIE"],",","CONTINENTE:", p["CONTINENTE"] )
                else:
                    print("No se encontraron países por coincidencial entera o parcial.")

                
            case "4":
                filtrados = filtrar_paises(paises)               
                    
            case "5": 
                _ = ordenar_paises(paises)
                
            case "6": 
                mostrar_estadisticas(paises)

                
            case "7":
                print("Cerrando programa...")
                
            case _:
                print("Opción invalida. Por favor elegir una opción del 1 al 8 como ves en el menu") 
                print(" ")
                
                
if __name__ == "__main__":
    main()
