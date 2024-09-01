import json
import os

class CreateSettings:
    def __init__(self):
        pass
    
    def create_settings_file(self, file_path):
        # Verificar si el archivo ya existe
        if os.path.exists(file_path):
            print(f"El archivo {file_path} ya existe. No se realizará ninguna acción.")
            return
        
        # Verificar si la carpeta existe, si no, crearla
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Directorio {directory} creado.")

        data = {
            "bootstrap": {
                "node_id": 2,
                "node_address": "192.168.230.69",
                "node_port": 50052,
                "reference_node_id": 3,
                "reference_node_ip": "192.168.230.1",
                "reference_node_port": 50053
            },
            "finger_table": {
                "index": [
                    1,
                    2,
                    3,
                    4
                ],
                "node_id": [
                    0,
                    1,
                    3,
                    8
                ],
                "node_address": [
                    "127.0.0.1",
                    "127.0.0.2",
                    "127.0.0.3",
                    "127.0.0.4"
                ],
                "node_port": [
                    50051,
                    50051,
                    50051,
                    50051
                ],
                "range_start": [
                    1,
                    2,
                    4,
                    8
                ],
                "range_end": [
                    8,
                    9,
                    11,
                    0
                ],
                "successor": [
                    1,
                    2,
                    4,
                    9
                ]
            },
            "ports": [
                {
                    "download_port": 50052,
                    "upload_port": 50053
                }
            ],
            "file_information": {
                "source_locations": "../sources/",
                "file_list": [
                    {
                        "file_name": "file1.txt"
                    },
                    {
                        "file_name": "file2.txt"
                    },
                    {
                        "file_name": "file3.txt"
                    }
                ]
            }
        }

        # Guardar la data en un archivo JSON
        with open(file_path, 'w') as archivo_json:
            json.dump(data, archivo_json, indent=4)
        print(f"Archivo creado en el directorio {file_path}.")
