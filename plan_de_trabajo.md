## Semana 1. 23 - 27 Nov

### Metas:

- [x] Exploración inicial
- [x] Formulación de plan de trabajo
- [x] Extracción de informes de sustentabilidad
- [ ] Descarga de datos GDELT

### Desafíos:

* Redactar un plan de trabajo con plazos adecuados a las metas
* Determinar la mejor manera de extraer los PDF de las memorias anuales
* Encontrar la manera de descargar solo datos relevantes de GDELT

### Factores de riesgo:

* No todas la compañías poseen informe anual
* No es posible hacer descargas filtradas de la base de datos

### Resultados:

* Se tienen todas las dependencias necesarias para comenzar con el proyecto

---

## Semana 2. 30 Nov - 4 Dic

### Metas:

- [ ] Replicar primera parte del articulo
- [ ] Realizar preprocesamiento de texto
- [ ] Realizar Topic Modelling

### Desafíos:

* Familiarizarse con el uso de spark y databricks, junto con las librerías a utilizar
* Ajustar el preprocesamiento a palabras en español

### Factores de riesgo:

* Los modelos ajustados mediante LDA no entregan topicos esperados o interpretables

### Resultados:

* Se determinan los temas principales abordados en los informes anuales
* Se tiene un entendimiento de los terminos más frecuentes por tema
* Se determinan las principales iniciativas de cada empresa

---

## Semana 3. 7 - 11 Dic

### Metas:

- [ ] Replicar segunda parte del articulo
- [ ] Extraer el valor de sentimiento en GDELT y utilizarlo como score ESG
- [ ] Comparar el score de cada empresa respecto al sentimiento promedio
- [ ] Crear un nuevo score basado en redes de importancia (PageRank)
- [ ] Crear el score final a utilizar basado en la ponderación de los scores definidos anteriormente

### Desafíos:

* El codigo se complejiza en este punto
* Familiarizarse con la nueva estructura para representar redes, Graphframes
* Entender el algorimo PageRank y que representa la influencia de cada conexión

### Resultados:

* Se obtienen las relaciones principales entre empresas
* Se determina un puntaje ESG de mayor confianza para cada empresa

---

## Semana 4. 14 - 18 Dic

### Metas:

- [ ] Replicar tercera parte del articulo
- [ ] Utilizar los puntajes ESG para medir riesgo en el mercado
- [ ] Comparar resultados de analisis de sentimiento con el desempeño del mercado

### Resultados:

* Obtener una herramienta mejor que aleatorio, para relacionar los puntajes ESG y el sentimiento con el rendimiento del mercado.