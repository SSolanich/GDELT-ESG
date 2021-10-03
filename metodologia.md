## Parte I.    Preprocesamiento y análisis de datos

### a) Extraer reportes
1. Obtener listado de reportes por empresa, en formato de texto o pdf.
2. Parsear el contenido, aplicar preprocesamiento de texto.

### b) Topic modelling
1. Definir stopwords
2. Calcular term-frequency de unigramas y bigramas
3. Entrenar modelo LDA, variar cantidad de topicos a encontrar
4. Extraer las top N palabras que describen cada tópico
5. Definir los nombres de cada tópico
6. Visualizar cada tópico y las palabras que lo representan via wordclouds
7. Clasificar cada oracion del corpus dentro de algun tópico, junto con su probabilidad de pertenecer a él
8. Crear tabla de frecuencia para empresas/topicos
9. Calcular histograma de la distribución de probabilidad de topicos
10. Extraer las oraciones principales por cada tópico

### c) Iniciativas ESG principales
1. Encontrar cantidad optima de clusters (metodo del codo)
2. Realizar clustering, K-means
3. Asignar cada oracion al cluster correspondiente
4. Encontrar las principales estrategias ESG especificas por compañía


## Parte II.   ESG Score

### a) Descarga de datos GDELT
1. Extraer datos GDELT para las regiones de interes, utilizar curl o bigQuery
2. Parsear los eventos GDELT utilizando libreria externa
3. Graficar la frecuencia de eventos en el tiempo

### b) Extraer registros relevantes
1. Hacer un diccionario de mappeo para los nombres de organizaciones
2. Definir funciones que filtren las busquedas exclusivamente a tematicas relacionadas a ECON, ENV y UNGP.
3. Almacenar en tabla con columnas: publishDate, organisation, documentIdentifier, themes, tone
4. Visualizar filtrando por organizacion

### c) Crear vista agregada por organizacion
1. Utilizando la tabla anterior, crear nueva tabla agrupando por fecha, organizacion y tema

### d) Crear score ESG interno
1. Calcular sentimiento medio de la industria
2. Comparar sentimiento de cada organizacion respecto a la media
3. definir el score ESG como la diferencia entre el sentimiento particular y el promedio de la industria

### e) Crear un score ESG basado en redes
1. Crear los dataframes conteniendo los nodos (organizaciones) y las conexiones
2. Crear objeto Graph para representar la red de nodos
3. Utilizar algoritmo PageRank o Shortest Path para asignar influencias
4. Filtrar el grafo por los nodos menos influyentes, o de menor conexiones
5. Otener la importancia de las conexiones
6. Guarda tabla de conexiones
7. Visualizar las conexiones mas influyentes/importantes por cada organizacion
8. Calcular el score ESG como la ponderacion de influencia con el puntaje calculado anteriormente