# bthack 2.0

import subprocess
import bluetooth
import socket

# Função para exibir as opções de comando disponíveis
def exibir_opcoes():
    print("Opções disponíveis:")
    print("dev                            - Exibir dispositivos locais")
    print("inq                            - Consultar dispositivos remotos (exibe endereço, offset de clock e classe)")
    print("scan                           - Consultar dispositivos remotos (exibe nome do dispositivo)")
    print("name <bdaddr>                  - Exibir nome do dispositivo remoto com o endereço bdaddr")
    print("info <bdaddr>                  - Exibir nome, versão e recursos suportados do dispositivo remoto com o endereço bdaddr")
    print("spinq                          - Iniciar processo de consulta periódica (sem exibir resultados)")
    print("epinq                          - Encerrar processo de consulta periódica")
    print("flood <bdaddr>                 - Realizar o flood de desconexão para o dispositivo com o endereço bdaddr")
    print("disconnect <bdaddr>            - Desconectar o dispositivo com o endereço bdaddr")

# Executar o comando hciconfig com base nos argumentos fornecidos
def executar_comando(args):
    try:
        output = subprocess.check_output(["hciconfig"] + args).decode("utf-8")
        print(output)
    except subprocess.CalledProcessError as e:
        print("Ocorreu um erro ao executar o comando:", e)

# Função para obter o endereço IP do dispositivo
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

# Função para desconectar um dispositivo Bluetooth
def disconnect_device(device_address):
    try:
        subprocess.check_call(["hcitool", "dc", device_address])
        print(f"Dispositivo {device_address} desconectado com sucesso.")
    except Exception as e:
        print(f"Erro ao desconectar dispositivo {device_address}: {str(e)}")

# Loop principal
while True:
    entrada = input("Digite um comando (ou 'q' para sair): ").split()
    
    if not entrada:
        continue
    
    comando = entrada[0]
    
    if comando == "q":
        break
    
    if comando == "dev":
        executar_comando([])
    elif comando == "inq":
        executar_comando(["inq"])
    elif comando == "scan":
        executar_comando(["scan"])
    elif comando == "name":
        if len(entrada) < 2:
            print("Endereço Bluetooth não especificado. Uso: name <bdaddr>")
        else:
            executar_comando(["name", entrada[1]])
    elif comando == "info":
        if len(entrada) < 2:
            print("Endereço Bluetooth não especificado. Uso: info <bdaddr>")
        else:
            executar_comando(["info", entrada[1]])
    elif comando == "spinq":
        executar_comando(["spinq"])
    elif comando == "epinq":
        executar_comando(["epinq"])
    elif comando == "flood":
        if len(entrada) < 2:
            print("Endereço Bluetooth não especificado. Uso: flood <bdaddr>")
        else:
            flood_disconnect_single(entrada[1])
    elif comando == "disconnect":
        if len(entrada) < 2:
            print("Endereço Bluetooth não especificado. Uso: disconnect <bdaddr>")
        else:
            disconnect_device(entrada[1])
    else:
        print("Comando inválido. Digite 'q' para sair ou consulte as opções disponíveis:")
        exibir_opcoes()

# Obtém o endereço IP do dispositivo
device_ip = get_device_ip()
print("Endereço IP do dispositivo:", device_ip)
