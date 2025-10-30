import socket
import time

HOST = '127.0.0.1'  # localhost
PORT = 5000         # puerto del maestro

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(2)  # Espera a dos esclavos
    print("🕒 Maestro iniciado. Esperando conexiones de esclavos...")

    connections = []
    clocks = []
    master_time = 100.0  # tiempo inicial del maestro (simulado en segundos)

    while len(connections) < 2:
        conn, addr = server.accept()
        print(f"✅ Conectado esclavo desde {addr}")
        connections.append(conn)

    # Enviar hora actual del maestro a los esclavos
    for conn in connections:
        conn.sendall(str(master_time).encode())

    # Recibir tiempos de los esclavos
    for conn in connections:
        data = conn.recv(1024).decode()
        slave_time = float(data)
        clocks.append(slave_time)
        print(f"⏱️  Hora recibida del esclavo: {slave_time}s")

    # Calcular ajuste promedio
    diffs = [t - master_time for t in clocks]
    avg_adjustment = sum(diffs) / (len(clocks) + 1)
    new_time = master_time + avg_adjustment

    print(f"\n🧮 Ajuste promedio: {avg_adjustment:+.2f}s")
    print(f"🕓 Nuevo tiempo sincronizado: {new_time:.2f}s")

    # Enviar tiempo ajustado a todos los esclavos
    for conn in connections:
        conn.sendall(str(new_time).encode())

    # Actualizar reloj del maestro
    master_time = new_time

    print("\nTiempos finales sincronizados:")
    print(f"   Maestro: {master_time:.2f}s")
    for i, t in enumerate(clocks):
        print(f"   Esclavo {i+1}: {new_time:.2f}s")

    # Cerrar conexiones
    for conn in connections:
        conn.close()
    server.close()

    print("\n✅ Sincronización completada correctamente.")

if __name__ == "__main__":
    main()
