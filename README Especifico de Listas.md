# Sistema de Optimización de Rutas en Envíos  
### Primera Etapa – 12/09/2025

## Integrantes
- Angel Camilo Sierra Carvajal – 2242007  
- Juan Esteban Gómez Ayala – 2243465  
- Juan David Ortiz Ochoa – 2242038  

---

## Descripción del Problema
El proyecto aborda la necesidad de gestionar eficientemente una red de rutas de envío entre distintas ubicaciones.  
Se requiere una estructura de datos que permita:

- Almacenar las ubicaciones.  
- Registrar rutas entre ellas.  
- Consultar y actualizar la información.  
- Facilitar la planificación y optimización de entregas o transportes.

La solución se implementa usando listas enlazadas, que permiten agregar ubicaciones, vincular rutas con distancias y realizar búsquedas ordenadas dentro de la red.

---

## Contexto del Proyecto
Este sistema fue desarrollado en el marco de la asignatura de Estructuras de Datos.  
El objetivo general es gestionar y visualizar rutas posibles utilizando listas enlazadas simples como estructura principal.

El sistema permite:

- Agregar ubicaciones.  
- Registrar rutas entre ubicaciones.  
- Verificar si la red está vacía.  
- Contar las ubicaciones registradas.  
- Buscar ubicaciones mediante un método de ordenamiento.  
- Imprimir la red completa de rutas.

Cada ubicación es representada como un nodo, y cada nodo contiene una lista enlazada de rutas hacia otras ubicaciones, lo que permite modelar dinámicamente una red de transporte.

---

## Funciones Implementadas
Conforme a lo solicitado en la entrega, el sistema incluye:

- Verificar si la lista está vacía.  
- Contar los elementos de la lista.  
- Imprimir los elementos.  
- Agregar elementos al inicio de la lista.  
- Buscar elementos usando ordenamiento (Bubble Sort).  

---

## Descripción del Proyecto
El sistema gestiona puntos o ubicaciones, almacenados en una lista enlazada.  
Cada ubicación puede estar conectada con otras por medio de rutas, incluyendo su distancia correspondiente.

- Las ubicaciones funcionan como nodos.  
- Las rutas representan conexiones entre nodos.  
- Toda la red se modela como una lista enlazada dinámica.

El programa presenta un menú que permite:

1. Agregar ubicaciones.  
2. Agregar rutas entre ubicaciones.  
3. Mostrar la red completa de rutas.  
4. Verificar si la red está vacía.  
5. Contar ubicaciones.  
6. Buscar y ordenar ubicaciones.  
7. Salir.

### Funcionamiento General

- Al agregar una ubicación, se crea un nodo solicitando el nombre al usuario.  
- Para agregar una ruta, se seleccionan dos ubicaciones registradas y se indica la distancia entre ellas.  
- Al mostrar la red, se imprime cada ubicación junto con sus rutas y distancias.  
- La búsqueda ordenada permite localizar rápidamente una ubicación específica.

---

## Conclusión
Este sistema permite administrar e indexar rutas de envío, ofreciendo una estructura clara y ordenada para la toma de decisiones en la planificación de entregas.  
La implementación mediante listas enlazadas ofrece flexibilidad y un manejo dinámico de la red de transporte.

---
