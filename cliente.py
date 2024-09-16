import socket

def coneccion_servidor():
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('127.0.0.1', 8080)
    client_socket.connect(server_address)

    return client_socket

def enviar_request(client_socket, request):

    client_socket.sendall(request.encode())

    response = client_socket.recv(1024).decode()
    return response

def main():
    print("Cliente de generación de nombre de usuario/contrasenia")

    cliente_socket = coneccion_servidor()

    while True:
        
        print("Seleccione una opcion:")
        print("1. Generar nombre de usuario")
        print("2. Generar contrasenia")
        print("3. Salir")

        opcion = input("Ingrese su opcion: ")

        if opcion == '3':
            print("Saliendo...")
            break

        if opcion not in ['1', '2']:
            print("Opcion invalida. Intentelo de nuevo.")
            continue

        length = input("Ingrese la longitud deseada: ")

        if opcion == '1':
            request = f"U{length}"
        elif opcion == '2':
            request = f"P{length}"

        response = enviar_request(cliente_socket, request)
        print(f"Respuesta del servidor: {response}")

    cliente_socket.close()

if __name__ == "__main__":
    main()
