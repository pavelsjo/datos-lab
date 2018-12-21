<a href="https://es.wikipedia.org/wiki/C%C3%B3rdoba_(Argentina)"><img src="./images/Screenshot_2018-12-21 JupyterLab.png" alt="Provincia de Córdoba" width="400px"  align="right"></a>

# Densidad Poblacional -- Argentina, Córdoba.

**Referencia:** [Toda la población del mundo cabe en Argentina](https://medium.com/datos-argentina/toda-la-poblaci%C3%B3n-del-mundo-cabe-en-argentina-215e59353871)

**Objetivo:** Exploración y experimentación con datos.

Para visualizar la distribución de la población de la Provincia de Córdoba, trabajaremos con un [shapefile](https://es.wikipedia.org/wiki/Shapefile) sobre un mapa con los datos del Instituto Nacional de Estadística y Censos de la República Argentina [INDEC](https://www.indec.gov.ar/codgeo.asp).

 
 ## Datos 
 [Link: Shapefile -- Provincia de Córdoba](https://www.indec.gov.ar/ftp/cuadros/territorio/codgeo/Codgeo_Cordoba_con_datos.zip)
 
 Descripción:
 
 - **toponimo_i:** Identificación única propia del archivo
 - **link:** ID del Radio Censal
 - **varon:** cantidad de varones en dicho radio censal
 - **mujer:** cantidad de mujeres en dicho radio censal
 - **totalpobl:** población total
 - **hogares:** cantidad total de hogares
 - **viviendasp:** total de viviendas particulares
 - **viv_part_h:** total de viviendas particulares habitadas
 - **geometry:** información geográfica para hacer la visualización del mapa.

 
## Main Workflow
 
- **[Radios Censales 1 - R](https://github.com/pavelsjo/datos-lab/tree/python_version/radios-censales-1-R)**. Trabajar con datos a nivel de radio censal en R.

- **[Radios Censales 1 - Python](https://github.com/pavelsjo/datos-lab/tree/python_version/radios-censales-1-Python)**. Trabajar con datos a nivel de radio censal en Python.

## Intalación 

### Uso en R

```R
# Instalamos los paquetes si no están instalados en nuestras computadoras
install.packages("tidyverse")
install.packages("sf")
```

### Uso en Python

Este código ha sido probado con Python 3.5, es posible que funcione correctamente con Python 2.7 y otras versionnes anteriores. Los paquetes necesarios para trabajar con este repositorio están listados en [requirements.txt](requirements.txt).

Para instalar los requerimientos en [conda](http://conda.pydata.org), ejecuta la siguiente línea de comandos en la terminal:


```
$ conda install --file requirements.txt
```

Si quieres crear un entorno aislado ``datos_lab`` con Python 3.5 y todos los paquetes requeridos, ejecuta el siguiente código:

```
$ conda create -n datos_lab python=3.5 --file requirements.txt
```