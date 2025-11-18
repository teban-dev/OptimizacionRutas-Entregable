## TERCERA ENTREGA

# Sistema de Optimización de Rutas en Envíos - Versión Final (Grafos)

## Contexto del Problema

El sistema de distribución y logística requiere una correcta
administración de las rutas de envío entre distintas ubicaciones. La
planificación adecuada de estas rutas impacta directamente en los
tiempos de entrega, costos operativos y eficiencia general del proceso
logístico.

Este proyecto implementa un **sistema de optimización de rutas**
utilizando **grafos**, donde cada ubicación se modela como un nodo y
cada ruta como una conexión con un peso asociado (distancia). Además, se
integran estructuras como **listas de adyacencia, matriz de adyacencia,
lista de aristas y diccionarios**, con el objetivo de representar la red
de forma flexible y eficiente.

El sistema permite: - Registrar nuevas ubicaciones. - Crear rutas
dirigidas entre ubicaciones con su distancia. - Visualizar toda la red
de rutas. - Ordenar las ubicaciones alfabéticamente. - Buscar
ubicaciones específicas. - Calcular la **ruta más corta** aplicando el
algoritmo de Dijkstra.

Esta implementación consolida los conceptos vistos en clase sobre
estructuras de datos avanzadas y su aplicación en soluciones reales.

------------------------------------------------------------------------

## Integrantes del Proyecto

-   Juan David Ortiz Ochoa (2242038)
-   Juan Esteban Gomez Ayala (2243465)
-   Ángel Sierra (2242007)

**Profesora:** Nury Farelo\
**Fecha:** 17/11/2025

------------------------------------------------------------------------

## Estructuras de Datos Utilizadas

### ✔ Listas de Adyacencia

Permiten modelar de forma eficiente qué rutas salen desde cada ubicación
y hacia dónde se dirigen.

### ✔ Matriz de Adyacencia

Implementada como parte del análisis para ver la conectividad global del
grafo.

### ✔ Lista de Aristas

Registro lineal de las rutas creadas y sus distancias.

### ✔ Diccionarios

Base del grafo que permite acceso rápido a cada ubicación.

------------------------------------------------------------------------

## Descripción del Sistema

La clase **`GrafoRutas`** administra toda la red mediante un diccionario
donde cada clave es una ubicación y su valor es la lista de rutas
salientes.

### Funciones Principales

-   **`agregar_ubicacion(nombre)`**: Agrega un nodo.
-   **`agregar_ruta(origen, destino, distancia)`**: Crea una conexión
    dirigida con peso.
-   **`mostrar_red()`**: Imprime la red completa.
-   **`esta_vacia()` y `contar_ubicaciones()`**: Estado general del
    grafo.
-   **`buscar_ubicacion(nombre)`**: Muestra rutas salientes de una
    ubicación.
-   **`ordenar_ubicaciones()`**: Orden alfabético.
-   **`ruta_mas_corta(origen, destino)`**: Implementa **Dijkstra**
    usando `heapq`.

------------------------------------------------------------------------

## Estructura del Menú Interactivo

1.  Agregar ubicación\
2.  Agregar ruta\
3.  Mostrar la red completa\
4.  Verificar si la red está vacía\
5.  Contar ubicaciones\
6.  Buscar ubicación\
7.  Ordenar ubicaciones\
8.  Calcular ruta más corta\
9.  Salir

------------------------------------------------------------------------

## Clonar el Repositorio

``` bash
git clone https://github.com/usuario/sistema-optimizacion-rutas.git
cd sistema-optimizacion-rutas
```

### Ejecutar el Programa

``` bash
python main.py
```

------------------------------------------------------------------------

## Conclusión

El sistema basado en **grafos** ofrece mayor flexibilidad y eficiencia
para representar redes de rutas reales en comparación con las
estructuras previas del proyecto:

-   **Listas enlazadas:** Adecuadas para secuencias simples, pero no
    para múltiples conexiones entre ubicaciones.
-   **Árboles:** Útiles para jerarquías, pero no permiten ciclos y
    limitan las relaciones múltiples.
-   **Grafos:** Son ideales para redes de transporte, permiten múltiples
    conexiones, ciclos, rutas alternativas y soportan algoritmos como
    **Dijkstra**, esenciales para encontrar caminos óptimos.

Gracias a estas capacidades, la versión final del sistema representa de
manera fiel escenarios reales de logística y distribución.
