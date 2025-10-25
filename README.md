
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

---
