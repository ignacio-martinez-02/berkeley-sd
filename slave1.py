import socket
import random

HOST = '127.0.0.1'
PORT = 5000

def main(initial_time):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Recibir hora del maestro
    data = client.recv(1024).decode()
    master_time = float(data)

    print(f"Conectado al maestro. Hora del maestro: {master_time}s")

    # Enviar hora local (simulada con un desfase aleatorio)
    print(f"Mi hora local (antes de sincronizar): {initial_time}s")
    client.sendall(str(initial_time).encode())

    # Recibir nuevo tiempo sincronizado
    data = client.recv(1024).decode()
    new_time = float(data)

    print(f"Hora sincronizada recibida: {new_time}s")
    print("✅ Sincronización exitosa.\n")

    client.close()

if __name__ == "__main__":
    my_time = float(input("Ingrese el tiempo actual del esclavo (en segundos): "))
    main(my_time)