import logging
import sys

def setup_logger():
    logger = logging.getLogger("gc_data_hub")
    logger.setLevel(logging.INFO)
    
    # Formato profesional: Fecha - Nombre - Nivel - Mensaje
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Salida a consola
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(console_handler)
        
    return logger