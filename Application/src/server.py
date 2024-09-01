from concurrent import futures
import grpc
import peerCommunications_pb2
import peerCommunications_pb2_grpc
import json
from bootstrap import Bootstrap
from getData import GetData
from createSettings import CreateSettings
from FingerTableGenerator import QueryFingerTable
import os
import time


class Peer2PeerServicer(peerCommunications_pb2_grpc.Peer2PeerServiceServicer):
    def __init__(self):
        self.shared_files_dir = '../sources'
        self.shared_files = os.listdir(self.shared_files_dir)
        bootstrap = Bootstrap()
        self.ip_global = bootstrap.obtener_ip_global()  # Obtener IP global al inicializar la clase
        self.chord_address = 'localhost:50051'
        self.node_id = None  # Inicializa en None, se asignará después con HandleBootstrap





def serve():
    print('INICIANDO SERVIDOR...')
    create_settings = CreateSettings()
    create_settings.create_settings_file('../configs/settings.json')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_servicer = Peer2PeerServicer()
    peerCommunications_pb2_grpc.add_Peer2PeerServiceServicer_to_server(server_servicer, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print(f'Servidor iniciado en el puerto 50051 \n')
    time.sleep(1)
    # Llama a HandleBootstrap después de iniciar el servidor
    print("BOOTSTRAP")
    bootstrap = Bootstrap()
    bootResponse = bootstrap.handle_bootstrap()
    print(f"ID del nodo asignado: {bootResponse.node_id_client}")
    #print(server_servicer.node_id)
    time.sleep(1)
    
    print("\nGET DATA")
    getData = GetData()
    getDataResponse = getData.get_data(bootResponse.node_id_client)
    
    time.sleep(1)
    print("\nFINGER TABLE")
    finger_table = QueryFingerTable(getDataResponse.number_of_nodes_in_network)
    finger_table.request_finger_table()

if __name__ == '__main__':
    serve()