
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

Descripción del proyecto:
El código implementa un sistema de gestión de rutas de envío utilizando una
estructura de árbol. Cada ubicación se representa como un nodo dentro de la
red, partiendo desde un nodo raíz denominado “Centro_Distribucion”. A partir
de este
nodo principal se pueden agregar nuevas ubicaciones y establecer rutas entre
ellas, indicando la distancia que las separa. De esta manera, la red conforma una
estructura jerárquica donde cada nodo puede tener varios destinos asociados,
facilitando la organización de los puntos de entrega y sus conexiones.
El programa presenta un menú interactivo que permite realizar diversas
operaciones: agregar ubicaciones independientes, crear rutas entre ubicaciones,
mostrar toda la red de rutas, verificar si la red está vacía, contar las ubicaciones
existentes, buscar una ubicación específica, listar las ubicaciones en orden
alfabético y calcular la ruta más corta entre dos puntos determinados.
Cuando se agrega una ubicación, se crea un nuevo nodo dentro del árbol,
mientras que al agregar una ruta se establece una conexión entre el origen y el
destino con su respectiva distancia. La función para mostrar la red imprime toda
la estructura
jerárquica, permitiendo visualizar cómo se relacionan las ubicaciones. También es
posible buscar una ubicación concreta, mostrando su nombre y, si está disponible,
la distancia desde su punto de origen.
La función que calcula la ruta más corta realiza un recorrido del árbol para
determinar el camino más eficiente entre dos ubicaciones dadas. Primero
identifica ambos nodos (origen y destino) y obtiene sus respectivas rutas dentro
del árbol desde la raíz. Luego, compara los caminos para encontrar el ancestro
común más cercano, es decir, el punto donde las dos rutas se separan. A partir de
este ancestro, el programa construye la ruta total, sumando las distancias tanto
en el ascenso desde el origen hasta el ancestro común como en el descenso
desde este hasta el
destino. Finalmente, muestra en pantalla el recorrido completo y la distancia total
aproximada.
En conjunto, este programa ofrece una herramienta estructurada y funcional para
la gestión y análisis de redes de rutas de envío, permitiendo registrar ubicaciones,
conectar puntos mediante distancias y determinar rutas óptimas para una mejor
planificación logística.
Cálculo de la ruta más corta:
La función “ruta_mas_corta()” implementa un algoritmo que permite determinar el
camino más eficiente entre dos ubicaciones dentro del árbol.
El proceso consiste en los siguientes pasos:
Identificación de nodos: se localizan los nodos correspondientes al origen y destino
dentro de la red.
Obtención de los caminos: se genera la lista de nodos desde la raíz hasta cada uno
(origen y destino).
Determinación del ancestro común más cercano: se compara cada camino hasta
encontrar el nodo en el que ambos se separan, lo que representa el punto
intermedio de conexión entre las dos ubicaciones.
Construcción de la ruta completa:
Se recorre desde el origen hasta el ancestro común (ascenso).
Luego, se continúa desde el ancestro común hasta el destino (descenso).
Cálculo de la distancia total: se suman las distancias de todos los tramos del
recorrido.
Finalmente, el sistema muestra en pantalla el trayecto completo en orden y la
distancia total aproximada del viaje.
Este método permite simular una optimización básica de rutas dentro de una
estructura arbórea, proporcionando una herramienta útil para visualizar y analizar
la eficiencia de las conexiones en una red de distribución.
