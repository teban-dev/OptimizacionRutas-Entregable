
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

## Descripción del Proyecto
Este proyecto implementa un sistema de gestión de rutas de envío utilizando una **estructura de árbol**.  
Cada ubicación se representa como un nodo dentro de una red que parte desde un nodo raíz llamado **Centro_Distribucion**.  
A partir de este nodo principal se pueden agregar nuevas ubicaciones y establecer rutas entre ellas indicando la distancia que las separa.

La red conforma una estructura jerárquica donde cada nodo puede tener varios destinos asociados, permitiendo organizar los puntos de entrega y entender sus conexiones.

---

## Funcionalidades del Sistema
El sistema cuenta con un menú interactivo que permite realizar las siguientes operaciones:

- Agregar ubicaciones independientes.  
- Crear rutas entre ubicaciones con su distancia correspondiente.  
- Mostrar toda la red de rutas en forma jerárquica.  
- Verificar si la red está vacía.  
- Contar todas las ubicaciones existentes.  
- Buscar una ubicación específica.  
- Listar todas las ubicaciones en orden alfabético.  
- Calcular la ruta más corta entre dos ubicaciones determinadas.

Cuando se agrega una ubicación, se crea un nuevo nodo dentro del árbol.  
Cuando se agrega una ruta, se establece una conexión entre origen y destino con la distancia registrada.

---

## Visualización y Búsqueda
El programa permite mostrar la estructura jerárquica completa, facilitando la visualización de las relaciones entre ubicaciones.

También es posible:

- Buscar una ubicación por su nombre.  
- Mostrar su información asociada.  
- Indicar la distancia desde su punto de origen, si está disponible.

---

# Cálculo de la Ruta Más Corta

## Descripción del Algoritmo
La función `ruta_mas_corta()` implementa un algoritmo que determina la ruta más eficiente entre dos ubicaciones del árbol.

### Pasos del Proceso
1. **Identificación de los nodos:** se localizan los nodos correspondientes al origen y destino.  
2. **Obtención de los caminos:** se genera la lista de nodos desde la raíz hasta cada ubicación.  
3. **Ancestro común más cercano:** se comparan ambos caminos para identificar el punto donde se separan.  
4. **Construcción de la ruta completa:**  
   - Ascenso desde el origen hasta el ancestro común.  
   - Descenso desde el ancestro común hasta el destino.  
5. **Cálculo de la distancia total:** se suman todas las distancias de los tramos que componen la ruta.

El sistema finalmente muestra el recorrido completo y la distancia total aproximada.

---

## Conclusión
Este programa ofrece una herramienta estructurada y funcional para la gestión y análisis de redes de rutas de envío.  
Permite registrar ubicaciones, conectar puntos mediante distancias y determinar rutas óptimas dentro de una estructura arbórea, facilitando la planificación logística.

