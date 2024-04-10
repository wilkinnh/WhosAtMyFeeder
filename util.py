import os
import sqlite3

import yaml


def load_config():
    file_path = os.getenv("CONFIG_PATH", "./config/config.yml")
    with open(file_path, "r") as config_file:
        config = yaml.safe_load(config_file)
    return config


def setupdb():
    config = load_config()
    conn = sqlite3.connect(config["database"]["path"])
    cursor = conn.cursor()
    cursor.execute(
        """    
        CREATE TABLE IF NOT EXISTS detections (    
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            detection_time TIMESTAMP NOT NULL,  
            detection_index INTEGER NOT NULL,  
            score REAL NOT NULL,  
            display_name TEXT NOT NULL,  
            category_name TEXT NOT NULL,  
            frigate_event TEXT NOT NULL UNIQUE,
            camera_name TEXT NOT NULL 
        )    
    """
    )
    conn.commit()
    conn.close()
