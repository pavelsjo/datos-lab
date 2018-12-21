import os
from urllib.request import urlretrieve
import pandas as pd
import numpy as np
import geopandas as gpd

import zipfile


#DATOS PRINCIPALES
URL = r'https://www.indec.gov.ar/ftp/cuadros/territorio/codgeo/Codgeo_Cordoba_con_datos.zip'
FILENAME = r'./data/Codgeo_Cordoba_con_datos.zip'

def get_data(filename = FILENAME, url = URL, force_download=False):
    '''    
    PARAMETERS
    ----------
    RETURN
    ------
    EXAMPLES
    --------
    '''
    if force_download or not os.path.exists(filename):
        urlretrieve( url, filename)
    
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(r'./data/')
        
    shapefile = gpd.read_file(r'./data/Cordoba_con_datos.shp')
    
    return shapefile