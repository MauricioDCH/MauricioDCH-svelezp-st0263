from concurrent import futures
import grpc
import peerCommunications_pb2
import peerCommunications_pb2_grpc
import json
import requests
import os

# Definición de la clase del servidor gRPC
class Peer2PeerServicer(peerCommunications_pb2_grpc.Peer2PeerServiceServicer):
    def __init__(self):
        self.nodes = []  # Lista para mantener la información de los nodos
        self.node_id = 0
        self.node_ip = self.obtener_ip_global()
        self.node_port = 50051
        self.crear_archivo_json()

    def obtener_ip_global(self):
        try:
            response = requests.get('https://api.ipify.org?format=json')
            response.raise_for_status()
            ip_address = response.json()['ip']
            return ip_address
        except requests.RequestException as e:
            print(f"Error al obtener la IP global: {e}")
            return "IP no disponible"

    def crear_archivo_json(self):
        url = f'{self.node_ip}:{self.node_port}'
        node_0 = {"NodeID": self.node_id, "URL": url, "Predecessor": self.node_id, "Successor": self.node_id}
        self.nodes.append(node_0)
        
        #print("Este es el nodo cero: " + str(self.nodes))
        os.makedirs('../configs', exist_ok=True)
        with open('../configs/settings_Chord_Node.json', 'w') as f:
            json.dump(node_0, f, indent=4)
        print("Archivo JSON creado.")


    def HandleBootstrap(self, request, context):
        # Incrementar el ID del nodo
        self.node_id += 1
        node_id_client = self.node_id
        node_ip = request.node_ip
        node_port = request.node_port
        url = f"{node_ip}:{node_port}"
        
        # Modificación del sucesor y predecesor del nodo 0.
        self.nodes[0]['Predecessor'] = node_id_client
        self.nodes[0]['Successor'] = self.nodes[0]['NodeID'] + 1
        # Buscar el nodo predecesor y sucesor
        predecessor = None
        successor = None
        if self.nodes:
            predecessor = self.nodes[-1]['NodeID']  # Ejemplo simplificado
            successor = self.nodes[0]['NodeID']
            self.nodes[-1]['Successor'] = node_id_client

        # Agregar el nuevo nodo a la lista
        
        new_node = {
            "NodeID": node_id_client,
            "URL": url,
            "Predecessor": predecessor,
            "Successor": successor
        }
        
        self.nodes.append(new_node)
        # Mostrar todos los nodos que se va ingresando
        
        for nodo in self.nodes:
            print(nodo)
        #print(f"Nuevo nodo ingresado: {new_node}")
        print()
        with open('../configs/settings_Chord_Node.json', 'w') as f:
            json.dump(self.nodes, f, indent=4)


        # Crear la respuesta
        response = peerCommunications_pb2.BootstrapResponse(
            node_id_client=node_id_client,
            id_chord_node=self.nodes[0]['NodeID'],
            node_id_predeccesor=predecessor if predecessor else 0,
            node_id_succesor=successor if successor else 0,
            node_status=True
        )
        return response


# Función principal para iniciar el servidor gRPC
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1000))
    peer2peer_servicer = Peer2PeerServicer()
    peerCommunications_pb2_grpc.add_Peer2PeerServiceServicer_to_server(peer2peer_servicer, server)
    server.add_insecure_port('0.0.0.0:50051')
    #server.add_insecure_port(f'{peer2peer_servicer.node_ip}:50051')
    server.start()
    print(f"Servidor gRPC corriendo en {peer2peer_servicer.node_ip}:50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
