import logging
import sys

def setup_logger():
    # Ensure Windows console streams support UTF-8 characters and emojis
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    logger = logging.getLogger("gc_data_hub")
    logger.setLevel(logging.INFO)
    
    # Format: Timestamp - Name - Level - Message
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
    return logger