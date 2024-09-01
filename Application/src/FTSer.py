from concurrent import futures
import grpc
import peerCommunications_pb2
import peerCommunications_pb2_grpc
import json
import os

class Peer2PeerServicer(peerCommunications_pb2_grpc.Peer2PeerServiceServicer):
    def __init__(self):
        self.shared_files_dir = '../sources'
        self.shared_files = os.listdir(self.shared_files_dir)
        self.nodes = []  # Lista para mantener la información de los nodos
        self.node_id = 0  # Asignar un ID inicial al nodo
        self.node_ip = 'localhost'
        self.node_port = 50051
        self.crear_archivo_json()

    def crear_archivo_json(self):
        url = f'{self.node_ip}:{self.node_port}'
        node_0 = {"NodeID": self.node_id, "URL": url, "Predecessor": self.node_id, "Successor": self.node_id}
        self.nodes.append(node_0)
        os.makedirs('../configs', exist_ok=True)
        with open('../configs/settings_Chord_Node.json', 'w') as f:
            json.dump(node_0, f, indent=4)
        print("Archivo JSON creado.")

    def load_nodes(self):
        try:
            with open('../configs/settings_Chord_Node-P.json', 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {e}")
            return []
        except FileNotFoundError as e:
            print(f"Archivo JSON no encontrado: {e}")
            return []

    def QueryFingerTable(self, request, context):
        # Cargar nodos desde el archivo JSON
        nodes = self.load_nodes()

        # Crear un mapa de node_id a URL
        node_urls = {}
        for node_id in request.node_ids:
            node_data = next((node for node in nodes if node['NodeID'] == node_id), None)
            if node_data:
                node_urls[node_id] = node_data['URL']
            else:
                node_urls[node_id] = ''  # Asignar cadena vacía si no se encuentra el nodo

        # Construir la respuesta
        response = peerCommunications_pb2.FTResponse(
            node_urls=node_urls
        )

        return response

# Función principal para iniciar el servidor gRPC
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    peer2peer_servicer = Peer2PeerServicer()
    peerCommunications_pb2_grpc.add_Peer2PeerServiceServicer_to_server(peer2peer_servicer, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Servidor gRPC corriendo en puerto 50051')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
