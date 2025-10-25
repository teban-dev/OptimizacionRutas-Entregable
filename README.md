<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Optimización de Rutas en Envíos</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; color: #222;">

    <h1>Sistema de Optimización de Rutas en Envíos - Versión 2</h1>

    <h2>Contexto del Problema</h2>
    <p>
        Las empresas de envío enfrentan el reto constante de optimizar sus rutas de distribución
        para reducir tiempos, costos de transporte y mejorar la eficiencia logística. Este proyecto
        busca resolver ese problema mediante un sistema de optimización de rutas, que representa la
        red de ubicaciones y conexiones entre ellas utilizando estructuras de datos tipo árbol.
    </p>

    <p>
        El sistema permite:
        <ul>
            <li>Registrar nuevas ubicaciones dentro de una red de distribución.</li>
            <li>Conectar ubicaciones mediante rutas con una distancia asociada.</li>
            <li>Visualizar la red completa de manera jerárquica.</li>
            <li>Consultar rutas, buscar ubicaciones y calcular caminos más cortos entre dos puntos.</li>
        </ul>
    </p>

    <p>
        Este enfoque facilita modelar de forma jerárquica la distribución —desde el Centro de Distribución principal
        hasta los distintos puntos de entrega—, mejorando la toma de decisiones en la planificación de envíos.
    </p>

    <h2>Integrantes del Proyecto</h2>
    <ul>
        <li>Juan David Ortiz Ochoa (2242038)</li>
        <li>Juan Esteban Gomez Ayala (2243465)</li>
        <li>Ángel Sierra (2242007)</li>
    </ul>
    <p><strong>Profesora:</strong> Nury Farelo<br>
       <strong>Fecha:</strong> 24/10/2025</p>

    <h2>Herramientas Utilizadas</h2>
    <h3>Lenguaje de Programación: Python 3</h3>
    <p>
        Se utiliza por su facilidad para el manejo de estructuras de datos, su sintaxis clara
        y su amplia disponibilidad de librerías útiles para la manipulación de árboles y grafos.
    </p>

    <h2>Librerías Utilizadas</h2>

    <h3>bigtree</h3>
    <p>
        <strong>Función:</strong> Facilita la creación y visualización de estructuras jerárquicas (árboles).<br>
        <strong>Uso en el proyecto:</strong>
    </p>
    <ul>
        <li>Se utiliza la clase <code>Node</code> para representar cada ubicación o punto dentro de la red de rutas.</li>
        <li>Se emplea la función <code>print_tree()</code> para mostrar gráficamente la estructura de la red con las distancias entre ubicaciones.</li>
    </ul>

    <p>
        <strong>Instalación:</strong>
    </p>
    <pre><code>!pip install -U bigtree</code></pre>

    <p>
        <strong>Ejemplo de uso:</strong>
    </p>
    <pre><code>from bigtree import Node, print_tree

raiz = Node("Centro_Distribucion")
ciudad = Node("Bogotá", parent=raiz, distancia=20)
print_tree(raiz)
    </code></pre>

    <h2>Entorno de Desarrollo</h2>

    <h3>Google Colab</h3>
    <p>
        Se usó como entorno principal de desarrollo, ya que permite ejecutar código Python en la nube
        sin necesidad de configuración local, además de facilitar la instalación de librerías mediante comandos <code>pip</code>.
    </p>

    <h3>GitHub</h3>
    <p>
        Utilizado como repositorio para documentar y compartir el código. Debe contener:
    </p>
    <ul>
        <li>Carpeta con la primera versión del proyecto (sin árboles).</li>
        <li>Carpeta con la versión actual implementada con árboles.</li>
        <li>Archivo <code>README.html</code> o <code>README.md</code> con la descripción, dependencias e instrucciones de ejecución.</li>
    </ul>

    <h2>Conclusión</h2>
    <p>
        El proyecto demuestra cómo el uso de árboles jerárquicos puede aplicarse a la optimización de rutas en empresas de envíos.
        La estructura basada en nodos permite una gestión ordenada, búsqueda rápida de ubicaciones y visualización clara de las conexiones,
        haciendo el sistema escalable y entendible.
    </p>

</body>
</html>
