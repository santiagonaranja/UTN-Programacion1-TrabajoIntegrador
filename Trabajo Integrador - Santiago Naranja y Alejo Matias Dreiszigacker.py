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

def main(): #Funcion principal que contiene el menu iterativo, de esta forma evitamos variables globales
    
    paises= crear_o_cargar_CSV()
    opcion= ""   
        
    while opcion!= "8":
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
                pass
                    
            case "5": 
                pass
                
            case "6": 
                pass
                
            case "7":
                print("Cerrando programa...")
                
            case _:
                print("Opción invalida. Por favor elegir una opción del 1 al 8 como ves en el menu") 
                print(" ")
                
                
if __name__ == "__main__":
    main()