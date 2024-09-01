import math

def find_next_active_node(successor, listaNodosActivos):
    """Encuentra el siguiente nodo activo que sea mayor o igual al sucesor"""
    for node in listaNodosActivos:
        if node >= successor:
            return node
    return listaNodosActivos[0]

def FingerTable(numberOfNodes, listaNodosActivos):
    """Crea la finger table para cada nodo en la red"""
    fingerTables = {}
    totalIndexFingerTable = math.ceil(math.log2(numberOfNodes))
    
    for i in range(numberOfNodes):
        fingerTables[i] = {}
        for j in range(1, totalIndexFingerTable + 1):
            successor = (i + 2**(j - 1)) % numberOfNodes
            fingerTables[i][j] = find_next_active_node(successor, listaNodosActivos)
    
    return fingerTables

if __name__ == "__main__":
    numberOfNodes = 16
    listaNodosActivos = [0, 2, 5, 8, 10, 13]
    listaNodosActivos.sort()
    fingerTable = FingerTable(numberOfNodes, listaNodosActivos)
    
    for i in listaNodosActivos:
        print(f"Node {i} Finger Table: {fingerTable[i]}")
