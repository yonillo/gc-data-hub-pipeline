import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import logging

logger = logging.getLogger("gc_data_hub")

def fetch_fuel_prices():
    URL = "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/"
    
    logger.info("Conectando a la API del Ministerio de Industria...")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'application/json',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    }

    session = requests.Session()
    retries = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        raise_on_status=False
    )
    session.mount('https://', HTTPAdapter(max_retries=retries))

    try:
        response = session.get(URL, headers=headers, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        stations = data.get('ListaEESSPrecio', [])
        
        # Filtramos por IDProvincia '35' (Las Palmas)
        gc_data = [s for s in stations if s.get('IDProvincia') == '35']
        
        if not gc_data:
            logger.warning("⚠️ No se encontraron estaciones con IDProvincia '35'. Intentando por nombre...")
            gc_data = [s for s in stations if "PALMAS" in str(s.get('Provincia', '')).upper()]

        logger.info(f"✅ Descarga completada. {len(gc_data)} estaciones encontradas.")
        return gc_data

    except Exception as e:
        logger.error(f"❌ Error en la descarga: {e}")
        raise