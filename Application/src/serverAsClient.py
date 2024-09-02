import time
from bootstrap import Bootstrap
from getData import GetData
from FingerTableGenerator import QueryFingerTable

def serverAsClient():
    print('INICIANDO CLIENTE...')
    
    # BOOTSTRAP
    print("BOOTSTRAP")
    bootstrap = Bootstrap()
    bootResponse = bootstrap.handle_bootstrap()
    print(f"ID del nodo asignado: {bootResponse.node_id_client}")
    
    time.sleep(1)
    
    # GET DATA
    print("\nGET DATA")
    getData = GetData()
    getDataResponse = getData.get_data(bootResponse.node_id_client)
    print(getDataResponse)
    
    time.sleep(1)
    
    # FINGER TABLE
    print("\nFINGER TABLE")
    finger_table = QueryFingerTable(getDataResponse.number_of_nodes_in_network)
    #finger_table = QueryFingerTable(2)
    ftResonse = finger_table.request_finger_table()
    
    print('--------------------------------------------------------------')
    print(f'BOOTS: \n{bootResponse}')
    print(f'GET: \n{getDataResponse}')
    print(f'FT: \n{ftResonse}')
    

if __name__ == '__main__':
    serverAsClient()
