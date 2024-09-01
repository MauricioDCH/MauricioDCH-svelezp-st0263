import grpc
import peerCommunications_pb2
import peerCommunications_pb2_grpc
import math

class QueryFingerTable:
    def __init__(self, m_number_of_nodes_in_network):
        self.m_number_of_nodes_in_network = m_number_of_nodes_in_network
    
    
    
    def generate_node_ids(self):
        # Calcula el tamaño de la tabla de finger
        finger_table_size = math.ceil(math.log2(self.m_number_of_nodes_in_network))
        print(f"Tamaño de la tabla de finger: {finger_table_size}")
        
        list_of_node_ids = []
        node_id = 0
        # Genera la lista de node_ids
        for ft_index in range(1, finger_table_size + 1):
            finger_id = (node_id + 2**(ft_index - 1)) % self.m_number_of_nodes_in_network
            list_of_node_ids.append(finger_id)
        
        print(f"Lista de node_ids generada: {list_of_node_ids}")
        return list_of_node_ids

    """
    def generate_node_ids(self):
        # Calcula el tamaño de la tabla de finger
        finger_table_size = math.ceil(math.log2(self.m_number_of_nodes_in_network))
        print(f"Tamaño de la tabla de finger: {finger_table_size}")
        
        list_of_node_ids = []
        node_id = 0
        # Genera la lista de node_ids
        for ft_index in range(1, finger_table_size + 1):
            finger_id = math.ceil(node_id + 2**(ft_index - 1)) % self.m_number_of_nodes_in_network
            list_of_node_ids.append(finger_id)
        
        print(f"Lista de node_ids generada: {list_of_node_ids}")
        return list_of_node_ids
        
    """
    def request_finger_table(self):
        
        # Configura la conexión con el servidor
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = peerCommunications_pb2_grpc.Peer2PeerServiceStub(channel)
            
            # Prepara la solicitud con una lista de node_ids
            request = peerCommunications_pb2.FTRequest(
                number_of_nodes_in_network=self.m_number_of_nodes_in_network,
                node_ids=self.generate_node_ids()
            )
            
            # Envía la solicitud y recibe la respuesta
            try:
                response = stub.QueryFingerTable(request)
                
                sorted_response = dict(sorted(response.node_urls.items()))
                print(f'Respuesta del servidor: \n\n{sorted_response}\n\n')
                # Imprime la respuesta
                print("Respuesta del servidor:")
                for node_id, url in sorted_response.items():
                    print(f"Nodo ID: {node_id}, URL: {url}")
                #return sorted_response
            except grpc.RpcError as e:
                print(f"Error al comunicar con el servidor: {e.details()}")

"""
if __name__ == '__main__':
    
    finger_table = QueryFingerTable(16)
    finger_table.request_finger_table()
"""