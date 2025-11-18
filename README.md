
# Sistema de Optimización de Rutas en Envíos - Versión con Arboles (SEGUNDA ENTREGA)

## Contexto del Problema
Las empresas de envío enfrentan constantemente el reto constante de optimizar sus rutas de distribución para reducir tiempos, costos de transporte y mejorar la eficiencia logística.  
Este proyecto busca resolver ese problema mediante un **sistema de optimización de rutas**, que representa la red de ubicaciones y conexiones entre ellas utilizando **estructuras de datos tipo árbol**, el cual en un futuro será actualizado usando grafos.

El sistema permite:
- Registrar nuevas ubicaciones dentro de una red de distribución.  
- Conectar ubicaciones mediante rutas con una distancia asociada.  
- Visualizar la red completa de manera jerárquica.  
- Consultar rutas, buscar ubicaciones y calcular caminos más cortos entre dos puntos.  

Este enfoque permite modelar de forma jerárquica la distribución —desde el **Centro de Distribución principal** hasta los distintos puntos de entrega—, mejorando la toma de decisiones en la planificación de envíos.

---

## Integrantes del Proyecto
- Juan David Ortiz Ochoa (2242038)  
- Juan Esteban Gomez Ayala (2243465)  
- Ángel Sierra (2242007)  

**Profesora:** Nury Farelo  
**Fecha:** 24/10/2025

---

## Herramientas Utilizadas

### Lenguaje de Programación: Python 3
Se utiliza por su facilidad para el manejo de estructuras de datos, su sintaxis clara y su amplia disponibilidad de librerías útiles para la manipulación de árboles y grafos.

---

## Librerías Utilizadas

### bigtree
**Función:** Facilita la creación y visualización de estructuras jerárquicas (árboles).  
**Uso en el proyecto:**
- Se utiliza la clase `Node` para representar cada ubicación o punto dentro de la red de rutas.  
- Se emplea la función `print_tree()` para mostrar gráficamente la estructura de la red con las distancias entre ubicaciones.  

**Instalación (desde terminal o Colab):**
```bash
pip install bigtree
```

**Ejemplo de uso:**
```python
from bigtree import Node, print_tree

raiz = Node("Centro_Distribucion")
ciudad = Node("Bogotá", parent=raiz, distancia=20)
print_tree(raiz)
```

---

## Entorno de Desarrollo

### Google Colab
Se usó como entorno principal de desarrollo, ya que permite ejecutar código Python en la nube sin necesidad de configuración local, además de facilitar la instalación de librerías mediante comandos `pip` y permite el trabajo de todos de forma asincronica.

### GitHub
Utilizado como repositorio para documentar y compartir el código. Debe contener:
- Carpeta con la primera versión del proyecto (sin árboles).  
- Carpeta con la versión actual implementada con árboles.  
- Archivo `README.md` con la descripción, dependencias e instrucciones de ejecución.  


#TERCERA ENTREGA
# Sistema de Optimización de Rutas en Envíos - Versión con final con Grafos (TERCERA ENTREGA)

## Contexto del Problema
El sistema de distribución y logística requiere una correcta administración de las rutas de envío entre distintas ubicaciones. La planificación adecuada de estas rutas impacta directamente en los tiempos de entrega, costos operativos y eficiencia general del proceso logístico.

Este proyecto implementa un **sistema de optimización de rutas** utilizando un **grafos**, donde cada ubicación se modela como un nodo y cada ruta como una conexión con un peso asociado (distancia). Además, se integran estructuras como **listas de adyacencia, matriz de adyacencia, lista de aristas y diccionarios**, con el objetivo de representar la red de forma flexible y eficiente.

El sistema permite:
- Registrar nuevas ubicaciones.
- Crear rutas dirigidas entre ubicaciones con su distancia.
- Visualizar toda la red de rutas.
- Ordenar las ubicaciones alfabéticamente.
- Buscar ubicaciones específicas.
- Calcular la **ruta más corta** aplicando el algoritmo de Dijkstra.

Esta implementación consolida los conceptos vistos en clase sobre estructuras de datos avanzadas y su aplicación en soluciones reales.

---

## Integrantes del Proyecto
- Juan David Ortiz Ochoa (2242038)
- Juan Esteban Gomez Ayala (2243465)
- Ángel Sierra (2242007)

**Profesora:** Nury Farelo  
**Fecha:** 17/11/2025

---

## Estructuras de Datos Utilizadas
El proyecto empleó múltiples estructuras de datos para representar de manera completa la red de rutas:

### ✔ Listas de Adyacencia
Permiten modelar de forma eficiente qué rutas salen desde cada ubicación y hacia dónde se dirigen.  
Son útiles para recorridos, búsquedas y cálculos de rutas.

### ✔ Matriz de Adyacencia
Aunque no usada directamente en el menú, fue implementada como parte del proceso de análisis del grafo.  
Permite ver de forma global qué nodos están conectados entre sí.

### ✔ Lista de Aristas
Facilita el registro lineal de todas las conexiones con sus distancias.

### ✔ Diccionarios en Python
Base de la estructura general del grafo, permitiendo un acceso directo y eficiente a las ubicaciones.

---

## Descripción del Sistema
El sistema está construido alrededor de la clase **`GrafoRutas`**, que administra toda la red mediante un diccionario donde cada clave representa una ubicación y su valor es la lista de rutas salientes.

### Funciones Principales

#### `agregar_ubicacion(nombre)`
Permite registrar un nuevo nodo en el grafo, siempre que no exista previamente.

#### `agregar_ruta(origen, destino, distancia)`
Crea una conexión dirigida entre dos ubicaciones válidas. Cada ruta almacena su distancia como peso.

#### `mostrar_red()`
Imprime la estructura completa del grafo mostrando cada ubicación y las rutas asociadas.

#### `esta_vacia()` y `contar_ubicaciones()`
Permiten evaluar el estado general de la red.

#### `buscar_ubicacion(nombre)`
Muestra las rutas que parten de la ubicación buscada.

#### `ordenar_ubicaciones()`
Lista alfabéticamente todas las ubicaciones registradas.

#### `ruta_mas_corta(origen, destino)`
Implementa el **algoritmo de Dijkstra** para calcular el camino más eficiente entre dos puntos de la red. Utiliza una cola de prioridad (`heapq`).

El algoritmo:
1. Inicializa todas las distancias con infinito.
2. Asigna 0 a la distancia del nodo origen.
3. Usa una cola de prioridad para seleccionar la ruta más corta disponible.
4. Actualiza las distancias hacia los vecinos.
5. Reconstruye el camino final usando un diccionario de predecesores.

---

## Estructura del Menú Interactivo
El programa principal ofrece un menú con las siguientes opciones:

1. **Agregar ubicación**
2. **Agregar ruta**
3. **Mostrar la red completa**
4. **Verificar si la red está vacía**
5. **Contar ubicaciones**
6. **Buscar una ubicación específica**
7. **Mostrar ubicaciones ordenadas**
8. **Calcular la ruta más corta entre dos puntos**
9. **Salir del sistema**

Esto permite interactuar con el grafo de manera dinámica mientras se ejecuta el programa.

---

bash
git clone https://github.com/usuario/sistema-optimizacion-rutas.git
cd sistema-optimizacion-rutas
```

### Ejecutar el programa
Para ejecutar el sistema, simplemente correr el archivo principal:

```bash
python main.py
```

Al inicio se cargará automáticamente el menú para gestionar la red de rutas.

---

## Conclusión
El sistema basado en **grafos** ofrece mayor flexibilidad y eficiencia para representar redes de rutas reales en comparación con estructuras previas trabajadas en el proyecto:


- **Listas enlazadas:** permiten almacenar secuencias lineales, pero no representan bien múltiples conexiones entre ubicaciones ni permiten recorridos eficientes entre nodos no contiguos.
- **Árboles:** funcionan para relaciones jerárquicas, pero limitan las conexiones múltiples entre nodos y no permiten ciclos; esto los hace poco adecuados para redes de transporte donde cada ubicación puede conectarse con varias otras.
- **Grafos:** son la estructura ideal para modelar rutas, permiten múltiples conexiones, ciclos, caminos alternativos y el uso de algoritmos como **Dijkstra**, lo que facilita encontrar rutas óptimas y analizar la red completa.


Gracias a estas capacidades, la versión final del sistema logra una representación más fiel y útil para escenarios reales de logística y distribución.

