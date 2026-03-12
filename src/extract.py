import requests
import logging

logger = logging.getLogger("gc_data_hub")

def fetch_fuel_prices():
    URL = "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/"
    
    logger.info("Conectando a la API del Ministerio de Industria...")
    
    try:
        # Añadimos un Header de User-Agent por si acaso el servidor bloquea peticiones básicas
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(URL, headers=headers, timeout=25)
        response.raise_for_status()
        
        data = response.json()
        stations = data.get('ListaEESSPrecio', [])
        
        # Filtramos por IDProvincia '35' (Las Palmas)
        # Importante: El ID suele venir como string en esta API
        gc_data = [s for s in stations if s.get('IDProvincia') == '35']
        
        if not gc_data:
            logger.warning("⚠️ No se encontraron estaciones con IDProvincia '35'. Intentando por nombre...")
            gc_data = [s for s in stations if "PALMAS" in s.get('Provincia', '').upper()]

        logger.info(f"✅ Descarga completada. {len(gc_data)} estaciones encontradas.")
        return gc_data

    except Exception as e:
        logger.error(f"❌ Error en la descarga: {e}")
        raise