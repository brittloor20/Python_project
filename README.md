# Scraping Web de Productos.
Este proyecto realiza scraping de datos de productos de un sitio web, limpia y analiza loo datos, y los guarda en archivos CSV.
## Requisitos
- Python 3.7
- pandas
- beautifulsoup4
- requests
- matplotlib
- time
- logging

## Instalacion 

Para instalar las dependencias creamos un archivo "txt" el cual guardamos todas las dependecias para una rapida instalacion. Su metodo de uso es utilizando PIP y es con el comando siguiente.

`pip install -r .\dep.txt`

## Estructura de carpetas

```plaintext
Python
|-- data/
|   |-- raw/
|   |   |-- products.csv
|   |-- processed/
|       |-- cleaned_products.csv
|-- notebooks/
|   |-- exploration.ipynb
|-- src/
|   |-- analysis/
|   |   |-- __init__.py
|   |   |-- analysis.py
|   |-- decorators/
|   |   |-- __init__.py
|   |   |-- decorators.py
|   |-- scraping/
|       |-- __init__.py
|       |-- scraper.py
|__ dep.txt
|__ README.md
|__ requirements.txt


## Ejecucion de Scraper

Para ejecutar el scraper lo que hay que realizar es.

`python .\src\scraping\scraper.py`

Esto nos va a generar un CSV en la carpeta "RAW" dentro de la carpeta "DATA" llamado "products.csv"

## Ejecucion para analisis de datos 

Para ejecutar el script para analisis de datos lo que hay que realizar es.

`python .\src\analysys\analysis.py`

Esto nos va a generar un CSV en la carpeta "PROCESSED" dentro de la carpeta "DATA" llamado "cleaned_products.csv"

### Brittany Loor 
### loorbrittany20@gmail.com



