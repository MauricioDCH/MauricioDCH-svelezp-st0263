

"""
class Peer2PeerServicer(peerCommunications_pb2_grpc.Peer2PeerServiceServicer):
    def __init__(self):
        pass

    def HandleBootstrap(self, request, context):
        pass

    def obtener_ip_global(self):
        try:
            # Realizar una solicitud HTTP a un servicio que devuelve la IP pública
            response = requests.get('https://api.ipify.org?format=json')
            response.raise_for_status()  # Verifica que la solicitud fue exitosa
            # Parsear la respuesta JSON para obtener la IP
            ip_address = response.json()['ip']
            return ip_address
        except requests.RequestException as e:
            print(f"Error al obtener la IP global: {e}")
            return "IP no disponible"

    def QueryFileList(self, request, context):
        pass

    def UploadFile(self, request, context):
        pass

    def DownloadFile(self, request, context):
        pass

    def Ping(self, request, context):
        pass
"""

from concurrent import futures
import grpc
import peerCommunications_pb2
import peerCommunications_pb2_grpc
import json
import requests
import os


class Peer2PeerServicer(peerCommunications_pb2_grpc.Peer2PeerServiceServicer):
    def __init__(self, shared_files_dir, chord_address):
        self.shared_files_dir = shared_files_dir
        self.shared_files = os.listdir(shared_files_dir)
        self.ip_global = self.obtener_ip_global()  # Obtener IP global al inicializar la clase
        self.chord_address = chord_address  # Dirección del nodo Chord al que se conectará para HandleBootstrap
        self.node_id = self.HandleBootstrap('50051')  # ID del nodo actual
        
    def obtener_ip_global(self):
        try:
            # Realizar una solicitud HTTP a un servicio que devuelve la IP pública
            response = requests.get('https://api.ipify.org?format=json')
            response.raise_for_status()  # Verifica que la solicitud fue exitosa

            # Parsear la respuesta JSON para obtener la IP
            ip_address = response.json()['ip']
            return ip_address
        except requests.RequestException as e:
            print(f"Error al obtener la IP global: {e}")
            return "IP no disponible"



    def HandleBootstrap(self, port):
        with grpc.insecure_channel(self.chord_address) as channel:
            stub = peerCommunications_pb2_grpc.Peer2PeerServiceStub(channel)
            try:
                bootstrap_request = peerCommunications_pb2.BootstrapRequest(
                    node_ip=self.ip_global,
                    node_port=int(port)
                )
                response = stub.HandleBootstrap(bootstrap_request)

                if response is None:
                    print("La respuesta fue None")
                    return None

            # Imprimir detalles del nodo
                print(f"ID del nodo asignado: {response.node_id_client}")
                print(f"ID del nodo Chord: {response.id_chord_node}")
                print(f"ID del predecesor: {response.node_id_predeccesor}")
                print(f"ID del sucesor: {response.node_id_succesor}")

                # Usa el campo correcto en la respuesta
                return response.id_chord_node
            except grpc.RpcError as e:
                print(f'Error al comunicar con el nodo Chord: {e.details()}')
                return None

def serve(shared_files_dir, chord_address):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1000))
    server_servicer = Peer2PeerServicer(shared_files_dir, chord_address)
    peerCommunications_pb2_grpc.add_Peer2PeerServiceServicer_to_server(server_servicer, server)
    server.add_insecure_port(f'[::]:50051')
    server.start()
    print(f'Servidor iniciado en el puerto 50051')
    server.wait_for_termination()  # Mantiene el servidor en ejecución



if __name__ == '__main__':
    serve('../sources', 'localhost:50051')