# UTN-Programacion1-TrabajoIntegrador
Entrega de trabajo integrador de Alejo Matias Dreiszigacker y Santiago Naranja

## 1. Descripción del programa
Este programa en Python permite administrar un archivo CSV llamado `paises.csv` que contiene información de países. Si el archivo no existe, el programa lo crea con el encabezado correspondiente. A partir de ahí, ofrece un menú interactivo para:

- Agregar nuevos países al CSV.
- Actualizar población y superficie de un país existente.
- Buscar países por nombre completo o parcial.
- Filtrar países por distintos criterios (continente, población, superficie o densidad).
- Ordenar los países por diferentes campos.
- Mostrar estadísticas generales (cantidad de países, totales, promedios, máximos y mínimos).

Todo se almacena de forma persistente en el CSV, por lo que los datos quedan guardados entre ejecuciones.

---

## 2. Instrucciones de uso
1. **Requisitos previos**:
   - Python 3 instalado.
   - Estar en la misma carpeta donde está el archivo `.py` del programa.

2. **Ejecución**:
   ```bash
   python Trabajo_Integrador_Santiago_Naranja_y_Alejo_Matias_Dreiszigacker.py

3. Al ejecutarse se mostrara un menu como este:
    
       ===GESTIÓN DE DATASET DE PAISES===
         Ingrese 1 para Ingresar un país con sus datos
         Ingrese 2 para Actualizar los datos de población y superficie de un pais
         Ingrese 3 para Buscar un pais por nombre
         Ingrese 4 para Filtrar paises
         Ingrese 5 para Ordenar países
         Ingrese 6 para Mostrar estadísticas
         Ingrese 7 para Salir

      El usuario debe ingresar el número de opción y seguir las instrucciones en pantalla.

4. El programa cuenta con las siguientes validaciones:
     - No permite dejar campos vacíos en los datos obligatorios.
     - Para población, superficie y densidad solo acepta valores numéricos positivos.
     - Si se intenta agregar un país que ya existe, pide otro nombre.
     - Si se intenta actualizar un país que no existe, lo informa.

## 3. Ejemplos de entrada y salida

EJEMPLO 1:
1. Al ingresar la opción 1 y completarla con los siguientes datos:

         Ingresar el nombre del pais a almacenar: Argentina
         Ingresar la población del pais 'Argentina': 46000000
         Ingresar la superficie del pais 'Argentina': 2780000
         Ingresar el continente del pais 'Argentina': América
    
3. La salida en la consola ser:

         =======
         El pais 'Argentina' fue ingresado correctamente con una poblacion de 46000000, una superficie de 2780000, y el continente América.
         =======
         Se agreggo el pais correctamente al CSV con todos sus datos.
         ==========================================

    
4. El contenido del CSV luego de esto sera:

         nombre,poblacion,superficie,continente
         Argentina,46000000,2780000,América

EJEMPLO 2:
1. Otro ejmeplo, caso de que ingresen opción 6.

2. La salida de la consola sera:

         ====== ESTADÍSTICAS ======
         Cantidad de países: 3
         Población total: 410000000
         Población promedio: 136666666.67
         Superficie total: 14000000
         Superficie promedio: 4666666.67
         Mayor población: Estados Unidos (330000000)
         Menor población: Uruguay (3500000)
         Mayor superficie: Estados Unidos (9834000)
         Menor superficie: Uruguay (176215)
         Densidad promedio: 45.2378 hab/km²
         Mayor densidad: Uruguay (19.8654 hab/km²)
         Menor densidad: Argentina (16.9061 hab/km²)
         ===========================


    

## 4. Paritipación de los integrantes
  El trabajo se desarrollo en conjunto entre Santiago Naranja y Alejo Matias Dreiszigacker.
