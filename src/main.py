from utils.logger import setup_logger
from extract import fetch_fuel_prices
from transform import clean_fuel_data
from load import save_to_parquet

def run_pipeline():
    logger = setup_logger()
    logger.info("🚀 INICIANDO PIPELINE DE CARBURANTES GRAN CANARIA")
    
    try:
        # E - EXTRAER
        raw_data = fetch_fuel_prices()
        
        # T - TRANSFORMAR
        df_cleaned = clean_fuel_data(raw_data)
        
        # L - CARGAR
        save_to_parquet(df_cleaned)
        
        logger.info("✨ PROCESO COMPLETADO EXITOSAMENTE ✨")
        
    except Exception as e:
        logger.error(f"💥 FALLO CRÍTICO: {e}")

if __name__ == "__main__":
    run_pipeline()