import pandas as pd
import logging

logger = logging.getLogger("gc_data_hub")

def clean_fuel_data(raw_data):
    if not raw_data:
        raise ValueError("No hay datos para transformar.")

    logger.info("Transformando datos del Ministerio...")
    df = pd.DataFrame(raw_data)
    
    # Mapeo exacto de la API (Ojo a las tildes y espacios)
    columns_map = {
        'Rótulo': 'estacion',
        'Municipio': 'municipio',
        'Localidad': 'localidad',
        'Precio Gasolina 95 E5': 'gasolina_95',
        'Precio Gasoleo A': 'diesel',
        'Dirección': 'direccion'
    }
    
    # Verificamos qué columnas han llegado realmente para no fallar
    available_cols = [c for c in columns_map.keys() if c in df.columns]
    df = df[available_cols].rename(columns=columns_map)
    
    if df.empty:
        raise ValueError("El DataFrame resultante está vacío tras el filtrado.")

    # Limpieza de precios (coma por punto)
    for col in ['gasolina_95', 'diesel']:
        if col in df.columns:
            df[col] = df[col].str.replace(',', '.').pipe(pd.to_numeric, errors='coerce')
    
    df = df.dropna(subset=['gasolina_95', 'diesel'])
    
    # Análisis rápido para el log
    if not df.empty:
        avg_gc = df['gasolina_95'].mean()
        logger.info(f"📊 Media Las Palmas (95): {avg_gc:.3f}€")
        
        # Filtro Agaete (Case insensitive)
        df_agaete = df[df['municipio'].str.contains('AGAETE', case=False, na=False)]
        if not df_agaete.empty:
            avg_agaete = df_agaete['gasolina_95'].mean()
            logger.info(f"📍 Media Agaete (95): {avg_agaete:.3f}€")
            
    return df