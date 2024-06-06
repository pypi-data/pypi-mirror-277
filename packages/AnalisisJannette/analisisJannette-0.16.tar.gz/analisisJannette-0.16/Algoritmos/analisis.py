from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


try:
    import sys
    import subprocess
    import os
    import pandas as pd
    import unicodedata
    import difflib
    
    
    print("Las librerías pandas, unicodedata y difflib ya están instaladas.")
except ImportError as e:
    print(f"Falta instalar la librería: {str(e)}")
    print("Instalando las librerías faltantes...")
    
    # Obtener el nombre de la librería faltante del mensaje de error
    missing_library = str(e).split("'")[1]
    
    # Instalar la librería faltante
    subprocess.check_call([sys.executable, "-m", "pip", "install", missing_library])
    
    print("Instalación completada.")






def eliminar_tildes(texto):
    return ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))

def normalizar_texto(texto):
    return eliminar_tildes(texto).lower().strip() if isinstance(texto, str) else ''

def buscar_coincidencia(nombre, nombres_normalizados, df, columna_original):
    coincidencias_exactas = df[df[columna_original + ' normalizado'] == nombre][columna_original].values
    if len(coincidencias_exactas) > 0:
        return coincidencias_exactas[0]
    else:
        coincidencias_similares = difflib.get_close_matches(nombre, nombres_normalizados, n=1, cutoff=0.0)
        if coincidencias_similares:
            mejor_coincidencia = coincidencias_similares[0]
            return df[df[columna_original + ' normalizado'] == mejor_coincidencia][columna_original].values[0]
        else:
            return None

class ExcelProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def process_excel(self):
        # Verificar la extensión del archivo
        _, extension = os.path.splitext(self.file_path)
        if extension.lower() != '.xlsx':
            raise ValueError("El archivo debe tener la extensión .xlsx")

        # Cargar los archivos
        Archivo = self.file_path
        Base = os.path.join(settings.STATIC_ROOT, 'scr', 'Base.xlsx')
        df_Retrasadas = pd.read_csv(Archivo, sep=';')
        df_PS = pd.read_excel(Base, sheet_name='PS')
        df_Est_DEIS = pd.read_excel(Base, sheet_name='Establecimientos DEIS')

        # Añadir nombres de columnas a df_Est_DEIS si no tiene
        if df_Est_DEIS.columns.isnull().all():
            df_Est_DEIS.columns = ['columna_' + str(i) for i in range(df_Est_DEIS.shape[1])]

        # Procesar df_Retrasadas
        df_Retrasadas['Auxiliar'] = df_Retrasadas.iloc[:, 3].astype(int).map(df_PS.set_index('n°PS')['num-nombre corto PS'])
        df_Retrasadas['NÚMERO PROBLEMA DE SALUD'] = df_Retrasadas['Auxiliar']
        df_Retrasadas.drop(columns=['Auxiliar'], inplace=True)

        # Normalizar nombres en df_Est_DEIS
        df_Est_DEIS['SS Nombre corto normalizado'] = df_Est_DEIS['SS Nombre corto'].apply(normalizar_texto)
        df_Est_DEIS['Nombre establecimiento DEIS normalizado'] = df_Est_DEIS['Nombre establecimiento DEIS'].apply(normalizar_texto)

        # Procesar coincidencias para la primera columna
        df_Retrasadas['Nombre_SS_normalizado'] = df_Retrasadas.iloc[:, 1].apply(normalizar_texto)
        nombres_normalizados_SS = df_Est_DEIS['SS Nombre corto normalizado'].tolist()
        df_Retrasadas['Nombre_SS_DEIS'] = df_Retrasadas['Nombre_SS_normalizado'].apply(
            lambda x: buscar_coincidencia(x, nombres_normalizados_SS, df_Est_DEIS, 'SS Nombre corto'))

        # Reemplazar valores en la primera columna
        df_Retrasadas.iloc[:, 1] = df_Retrasadas['Nombre_SS_DEIS']

        # Procesar coincidencias para la segunda columna
        df_Retrasadas['Nombre_SS_normalizado_2'] = df_Retrasadas.iloc[:, 2].apply(normalizar_texto)
        nombres_normalizados_est = df_Est_DEIS['Nombre establecimiento DEIS normalizado'].tolist()
        df_Retrasadas['Nombre_SS_DEIS_2'] = df_Retrasadas['Nombre_SS_normalizado_2'].apply(
            lambda x: buscar_coincidencia(x, nombres_normalizados_est, df_Est_DEIS, 'Nombre establecimiento DEIS'))

        # Reemplazar valores en la segunda columna
        df_Retrasadas.iloc[:, 2] = df_Retrasadas['Nombre_SS_DEIS_2']

        # Crear nuevas columnas Rut y Dv a partir de RUT-DV
        df_Retrasadas[['Rut', 'Dv']] = df_Retrasadas['RUT-DV'].str.split('-', expand=True)

        # Limpiar columnas auxiliares
        df_Retrasadas.drop(columns=['Nombre_SS_normalizado', 'Nombre_SS_DEIS', 'Nombre_SS_normalizado_2', 'Nombre_SS_DEIS_2'], inplace=True)

        # Modificaciones adicionales
        df_Retrasadas['Intervencion Sanitaria (Corregido)'] = ''
        df_Retrasadas['Alerta (NEW)'] = ''
        df_Retrasadas['Estado Garantia1'] = ''
        df_Retrasadas['Estado GO Nueva Nomenclatura'] = ''
        df_Retrasadas['Documento Cierre GO'] = ''
        df_Retrasadas['Causal Excepcion Go'] = ''
        df_Retrasadas['Cantidad Garantias (NEW)'] = ''
        df_Retrasadas['Doc Termino Go'] = ''
        df_Retrasadas['Fecha Nueva Limite'] = ''
        df_Retrasadas.drop(columns=['PROBLEMA DE SALUD SIGGES'], inplace=True)

        column_names_original = df_Retrasadas.columns.to_list()
        column_names_renamed = [
            'Fecha reporte',
            'Servicio de Salud (Corregido)',
            'Establecimiento (Corregido)',
            'Problema de Salud (Corregido)',
            'Problema Generico',
            'Nombre de la Garantía',
            'Intervencion Sanitaria (Corregido)',
            'Fecha inicio GO',
            'Fecha límite GO',
            'Fecha término GO',
            'Nombre',
            'Rut',
            'Dv',
            'Rut-DV',
            'Alerta (NEW)',
            'Estado Caso',
            'Fecha de creación del caso',
            'Estado Garantia',
            'Estado Garantia1',
            'Estado GO Nueva Nomenclatura',
            'Fecha Digita Inicio',
            'Fecha Digita Termino',
            'Cod Establecimiento',
            'Documento Cierre GO',
            'Sexo',
            'Edad',
            'Grupo Ingreso',
            'Causal Excepcion Go',
            'Comuna Establecimiento',
            'Cantidad Garantias (NEW)',
            'Doc Termino Go',
            'Fecha Nueva Limite'
        ]

        column_names_original[0] = column_names_renamed[0]
        column_names_original[1] = column_names_renamed[1]
        column_names_original[2] = column_names_renamed[2]
        column_names_original[3] = column_names_renamed[3]
        column_names_original[4] = column_names_renamed[4]
        column_names_original[7] = column_names_renamed[5]
        column_names_original[43] = column_names_renamed[6]
        column_names_original[10] = column_names_renamed[7]
        column_names_original[11] = column_names_renamed[8]
        column_names_original[13] = column_names_renamed[9]
        column_names_original[5] = column_names_renamed[10]
        column_names_original[41] = column_names_renamed[11]
        column_names_original[42] = column_names_renamed[12]
        column_names_original[6] = column_names_renamed[13]
        column_names_original[44] = column_names_renamed[14]
        column_names_original[8] = column_names_renamed[15]
        column_names_original[9] = column_names_renamed[16]
        column_names_original[12] = column_names_renamed[17]
        column_names_original[45] = column_names_renamed[18]
        column_names_original[46] = column_names_renamed[19]
        column_names_original[24] = column_names_renamed[20]
        column_names_original[25] = column_names_renamed[21]
        column_names_original[36] = column_names_renamed[22]
        column_names_original[47] = column_names_renamed[23]
        column_names_original[16] = column_names_renamed[24]
        column_names_original[17] = column_names_renamed[25]
        column_names_original[18] = column_names_renamed[26]
        column_names_original[48] = column_names_renamed[27]
        column_names_original[23] = column_names_renamed[28]
        column_names_original[49] = column_names_renamed[29]
        column_names_original[50] = column_names_renamed[30]
        column_names_original[51] = column_names_renamed[31]

        # Renombrar columnas column_names_original
        df_Retrasadas.columns = column_names_original

        # Seleccionar columnas en el orden de column_names_renamed
        df_Retrasadas = df_Retrasadas[column_names_renamed]

        # Guardar el DataFrame en un nuevo archivo Excel en la carpeta media
        processed_file_path = 'Cumplimiento_Actualizado.xlsx'
        full_path = os.path.join(settings.MEDIA_ROOT, processed_file_path)
        df_Retrasadas.to_excel(full_path, index=False)

        # Devolver la URL del archivo procesado para su descarga
        return settings.MEDIA_URL + processed_file_path

    def download_excel(self):
        # Leer el archivo Excel procesado desde la carpeta media
        processed_file_path = 'Cumplimiento_Actualizado.xlsx'
        full_path = os.path.join(settings.MEDIA_ROOT, processed_file_path)
        with open(full_path, 'rb') as file:
            content = file.read()

        # Crear un archivo temporal para la descarga
        temp_file = ContentFile(content)
        file_name = default_storage.save('temp_file.xlsx', temp_file)
        file_url = default_storage.url(file_name)

        return file_url
    def __init__(self, file_path):
        self.file_path = file_path
    def eliminar_tildes(texto):
        return ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))
    def normalizar_texto(texto):
        return eliminar_tildes(texto).lower().strip() if isinstance(texto, str) else ''
    def buscar_coincidencia(nombre, nombres_normalizados, df, columna_original):
        coincidencias_exactas = df[df[columna_original + ' normalizado'] == nombre][columna_original].values
        if len(coincidencias_exactas) > 0:
            return coincidencias_exactas[0]
        else:
            coincidencias_similares = difflib.get_close_matches(nombre, nombres_normalizados, n=1, cutoff=0.0)
            if coincidencias_similares:
                mejor_coincidencia = coincidencias_similares[0]
                return df[df[columna_original + ' normalizado'] == mejor_coincidencia][columna_original].values[0]
            else:
                return None

class ExcelProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def process_csv(self):
        # Cargar los archivos
        Archivo = self.file_path
        Base = os.path.join(settings.STATIC_ROOT, 'scr', 'Base.xlsx')
        df_Retrasadas = pd.read_csv(Archivo, sep=';')
        df_PS = pd.read_excel(Base, sheet_name='PS')
        df_Est_DEIS = pd.read_excel(Base, sheet_name='Establecimientos DEIS')

        # Añadir nombres de columnas a df_Est_DEIS si no tiene
        if df_Est_DEIS.columns.isnull().all():
            df_Est_DEIS.columns = ['columna_' + str(i) for i in range(df_Est_DEIS.shape[1])]

        # Procesar df_Retrasadas
        df_Retrasadas['Auxiliar'] = df_Retrasadas.iloc[:, 3].astype(int).map(df_PS.set_index('n°PS')['num-nombre corto PS'])
        df_Retrasadas['NÚMERO PROBLEMA DE SALUD'] = df_Retrasadas['Auxiliar']
        df_Retrasadas.drop(columns=['Auxiliar'], inplace=True)

        # Normalizar nombres en df_Est_DEIS
        df_Est_DEIS['SS Nombre corto normalizado'] = df_Est_DEIS['SS Nombre corto'].apply(normalizar_texto)
        df_Est_DEIS['Nombre establecimiento DEIS normalizado'] = df_Est_DEIS['Nombre establecimiento DEIS'].apply(normalizar_texto)

        # Procesar coincidencias para la primera columna
        df_Retrasadas['Nombre_SS_normalizado'] = df_Retrasadas.iloc[:, 1].apply(normalizar_texto)
        nombres_normalizados_SS = df_Est_DEIS['SS Nombre corto normalizado'].tolist()
        df_Retrasadas['Nombre_SS_DEIS'] = df_Retrasadas['Nombre_SS_normalizado'].apply(
            lambda x: buscar_coincidencia(x, nombres_normalizados_SS, df_Est_DEIS, 'SS Nombre corto'))

        # Reemplazar valores en la primera columna
        df_Retrasadas.iloc[:, 1] = df_Retrasadas['Nombre_SS_DEIS']

        # Procesar coincidencias para la segunda columna
        df_Retrasadas['Nombre_SS_normalizado_2'] = df_Retrasadas.iloc[:, 2].apply(normalizar_texto)
        nombres_normalizados_est = df_Est_DEIS['Nombre establecimiento DEIS normalizado'].tolist()
        df_Retrasadas['Nombre_SS_DEIS_2'] = df_Retrasadas['Nombre_SS_normalizado_2'].apply(
            lambda x: buscar_coincidencia(x, nombres_normalizados_est, df_Est_DEIS, 'Nombre establecimiento DEIS'))

        # Reemplazar valores en la segunda columna
        df_Retrasadas.iloc[:, 2] = df_Retrasadas['Nombre_SS_DEIS_2']

        # Crear nuevas columnas Rut y Dv a partir de RUT-DV
        df_Retrasadas[['Rut', 'Dv']] = df_Retrasadas['RUT-DV'].str.split('-', expand=True)

        # Limpiar columnas auxiliares
        df_Retrasadas.drop(columns=['Nombre_SS_normalizado', 'Nombre_SS_DEIS', 'Nombre_SS_normalizado_2', 'Nombre_SS_DEIS_2'], inplace=True)

        # Modificaciones adicionales
        df_Retrasadas['Intervencion Sanitaria (Corregido)'] = ''
        df_Retrasadas['Alerta (NEW)'] = ''
        df_Retrasadas['Estado Garantia1'] = ''
        df_Retrasadas['Estado GO Nueva Nomenclatura'] = ''
        df_Retrasadas['Documento Cierre GO'] = ''
        df_Retrasadas['Causal Excepcion Go'] = ''
        df_Retrasadas['Cantidad Garantias (NEW)'] = ''
        df_Retrasadas['Doc Termino Go'] = ''
        df_Retrasadas['Fecha Nueva Limite'] = ''
        df_Retrasadas.drop(columns=['PROBLEMA DE SALUD SIGGES'], inplace=True)

        column_names_original = df_Retrasadas.columns.to_list()
        column_names_renamed = [
            'Fecha reporte',
            'Servicio de Salud (Corregido)',
            'Establecimiento (Corregido)',
            'Problema de Salud (Corregido)',
            'Problema Generico',
            'Nombre de la Garantía',
            'Intervencion Sanitaria (Corregido)',
            'Fecha inicio GO',
            'Fecha límite GO',
            'Fecha término GO',
            'Nombre',
            'Rut',
            'Dv',
            'Rut-DV',
            'Alerta (NEW)',
            'Estado Caso',
            'Fecha de creación del caso',
            'Estado Garantia',
            'Estado Garantia1',
            'Estado GO Nueva Nomenclatura',
            'Fecha Digita Inicio',
            'Fecha Digita Termino',
            'Cod Establecimiento',
            'Documento Cierre GO',
            'Sexo',
            'Edad',
            'Grupo Ingreso',
            'Causal Excepcion Go',
            'Comuna Establecimiento',
            'Cantidad Garantias (NEW)',
            'Doc Termino Go',
            'Fecha Nueva Limite'
        ]

        column_names_original[0] = column_names_renamed[0]
        column_names_original[1] = column_names_renamed[1]
        column_names_original[2] = column_names_renamed[2]
        column_names_original[3] = column_names_renamed[3]
        column_names_original[4] = column_names_renamed[4]
        column_names_original[7] = column_names_renamed[5]
        column_names_original[43] = column_names_renamed[6]
        column_names_original[10] = column_names_renamed[7]
        column_names_original[11] = column_names_renamed[8]
        column_names_original[13] = column_names_renamed[9]
        column_names_original[5] = column_names_renamed[10]
        column_names_original[41] = column_names_renamed[11]
        column_names_original[42] = column_names_renamed[12]
        column_names_original[6] = column_names_renamed[13]
        column_names_original[44] = column_names_renamed[14]
        column_names_original[8] = column_names_renamed[15]
        column_names_original[9] = column_names_renamed[16]
        column_names_original[12] = column_names_renamed[17]
        column_names_original[45] = column_names_renamed[18]
        column_names_original[46] = column_names_renamed[19]
        column_names_original[24] = column_names_renamed[20]
        column_names_original[25] = column_names_renamed[21]
        column_names_original[36] = column_names_renamed[22]
        column_names_original[47] = column_names_renamed[23]
        column_names_original[16] = column_names_renamed[24]
        column_names_original[17] = column_names_renamed[25]
        column_names_original[18] = column_names_renamed[26]
        column_names_original[48] = column_names_renamed[27]
        column_names_original[23] = column_names_renamed[28]
        column_names_original[49] = column_names_renamed[29]
        column_names_original[50] = column_names_renamed[30]
        column_names_original[51] = column_names_renamed[31]

        # Renombrar columnas column_names_original
        df_Retrasadas.columns = column_names_original

        # Seleccionar columnas en el orden de column_names_renamed
        df_Retrasadas = df_Retrasadas[column_names_renamed]

        # Guardar el DataFrame en un nuevo archivo Excel en la carpeta media
        processed_file_path = 'Cumplimiento_Actualizado.xlsx'
        full_path = os.path.join(settings.MEDIA_ROOT, processed_file_path)
        df_Retrasadas.to_excel(full_path, index=False)

        # Devolver la URL del archivo procesado para su descarga
        return settings.MEDIA_URL + processed_file_path

    def download_excel(self):
        # Leer el archivo Excel procesado desde la carpeta media
        processed_file_path = 'Cumplimiento_Actualizado.xlsx'
        full_path = os.path.join(settings.MEDIA_ROOT, processed_file_path)
        with open(full_path, 'rb') as file:
            content = file.read()

        # Crear un archivo temporal para la descarga
        temp_file = ContentFile(content)
        file_name = default_storage.save('temp_file.xlsx', temp_file)
        file_url = default_storage.url(file_name)

        return file_url