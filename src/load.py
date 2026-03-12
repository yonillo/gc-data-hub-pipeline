import os
import logging
from datetime import datetime

logger = logging.getLogger("gc_data_hub")

def save_to_parquet(df):
    """
    Guarda el DataFrame en la carpeta 'data' usando el formato profesional Parquet.
    """
    # 1. Crear la carpeta 'data' si no existe
    if not os.path.exists('data'):
        os.makedirs('data')
        logger.info("Carpeta 'data' creada.")

    # 2. Generar nombre de archivo con timestamp (para histórico)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    file_path = f"data/fuel_prices_gc_{timestamp}.parquet"

    logger.info(f"Guardando datos en {file_path}...")
    
    try:
        # 3. Guardar en formato Parquet
        df.to_parquet(file_path, index=False, engine='pyarrow')
        logger.info("✅ Archivo guardado correctamente.")
        
        # También guardamos una versión 'latest' para facilitar el uso en Dashboards
        df.to_parquet("data/fuel_prices_latest.parquet", index=False, engine='pyarrow')
        
    except Exception as e:
        logger.error(f"❌ Error al guardar en Parquet: {e}")
        raise