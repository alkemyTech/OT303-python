#COMO: Analista de datos
#QUIERO: Implementar SQL Operator
#PARA: tomar los datos de las bases de datos en el DAG

#Criterios de aceptación:
#Configurar un Python Operators, para que extraiga información de la base de datos utilizando el .sql disponible en el repositorio base de las siguientes universidades:

#Universidad Tecnológica Nacional

#Universidad Nacional De Tres De Febrero

import logging
import os
import pandas as pd
from datetime import datetime

from config.cfg import LOG_ETL, root_csv
from db.db_connection import create_engine_connection
from utils.utils import create_folder, get_src_querys

from db.db_connection import *
#desde la base ppal , indico los nombres sobre los que deseo conectar
DEBUG = True
DATABASES = {
    'training': {
        'ENGINE': create_engine_connection(),
                        'NAME': os.path.join(BASE_DIR, 'db.training'),
    }
}



from .base import *
#trae los registros e inicia el motor
DATABASES =  {
        'ENGINE': 'create_engine_connection()',
        'NAME': 'Universidades_A',
        'USER':  config('USER'),
        'PASSWORD':  config('PASSWORD'),
        'HOST': config('SERVER'),
        'PORT': config('PORT'),
    }
log_name = LOG_ETL + datetime.today().now('%Y-%m-%d')
logger = logging.getLogger(log_name)


def extract_data():

    logger.info('task_extract')
    create_folder(root_csv)

    engine = create_engine_connection()

    sql_files = get_src_querys()

    with engine.connect() as connection:

        for sql_file_name, sql_full_path in sql_files.items():
            with open(sql_full_path) as f:

                query = f.read()
                logger.info('Extracting data from {}'.format(sql_file_name))

                result = connection.execute(query)

                df = pd.DataFrame(result)
                logger.info('Writing information to csv.')

                df.to_csv(os.path.join(
                    ROOT_CSV, f'{sql_file_name[:-4]}.csv'), index=False)
    logger.info('Extracting data from database.')

#transformacion de datos de las universidades
def transform_data():

    logger.info('task_transform')
    logger.info('Transform data from csv.')

#carga de datos de las universidades.
def load_data():

    logger.info('task_load')
    logger.info('Loading data to S3.')


