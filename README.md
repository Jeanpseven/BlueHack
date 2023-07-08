# BlueHack
faz um flood de solicitações de conexão em dispositivos bluetooth

disconecta dispositivos de outros dispositivos bluetooth

_________________________
# bthack2.py

O novo script combina funcionalidades de dois scripts anteriores. Ele permite interagir com dispositivos Bluetooth por meio do comando hciconfig e também fornece recursos adicionais para realizar o "flood" de desconexão e desconectar diretamente dispositivos Bluetooth.

O script inicia exibindo um menu de opções disponíveis, incluindo comandos hciconfig, como exibir dispositivos locais, consultar dispositivos remotos, exibir informações detalhadas e iniciar/encerrar o processo de consulta periódica.

Além disso, o script também possui as seguintes opções adicionais:

Realizar o "flood" de desconexão em um dispositivo específico: Essa opção exibe os dispositivos próximos e permite selecionar um dispositivo pelo número correspondente para realizar o "flood" de desconexão, usando a função flood_disconnect_single. Isso envia várias solicitações de desconexão para o dispositivo selecionado.

Realizar o "flood" de desconexão em todos os dispositivos próximos: Essa opção usa a função flood_disconnect_all para realizar o "flood" de desconexão em todos os dispositivos próximos. Isso envia várias solicitações de desconexão para cada dispositivo encontrado.

Desconectar um dispositivo específico e se conectar a ele: Essa opção desconecta o dispositivo especificado usando o comando hcitool dc. Em seguida, o script tenta reconectar ao dispositivo usando o comando hcitool cc. Isso é útil quando você deseja desconectar um dispositivo e estabelecer uma nova conexão com ele.

O script também inclui uma função get_device_ip para obter o endereço IP do dispositivo automaticamente.
_________________________
# brhack3.py

O script é um utilitário em Python que permite realizar várias operações relacionadas a dispositivos Bluetooth. Ele oferece um menu interativo onde você pode escolher diferentes opções, como exibir dispositivos locais, consultar dispositivos remotos, realizar desconexões em dispositivos, enviar keystrokes para um dispositivo conectado, entre outras funcionalidades.

O script utiliza bibliotecas como subprocess, bluetooth e socket para executar comandos do sistema, descobrir dispositivos Bluetooth próximos, obter informações sobre os dispositivos e estabelecer conexões. Além disso, utiliza a biblioteca pyautogui para enviar keystrokes para o dispositivo selecionado.

O menu exibe as opções disponíveis e solicita a entrada do usuário para escolher uma opção. Dependendo da escolha, o script executa a função correspondente para realizar a operação desejada. Por exemplo, é possível exibir dispositivos locais, listar dispositivos remotos pareados, realizar desconexões em dispositivos específicos, enviar keystrokes para um dispositivo conectado, entre outras ações.

O script também fornece informações adicionais, como o endereço IP do dispositivo em que está sendo executado.

Em resumo, o script oferece um conjunto de funcionalidades para interagir com dispositivos Bluetooth, facilitando a descoberta, conexão e controle de dispositivos próximos.

                                                       =%%%%%%%%.=%%%%%%##%+                                                                          
                               #@%:                   #%%%%%%%%%.  =%%%%%%%##.                                                                        
                              =@@@+                  #%%%%%%%%%%.   .*%%%%%%%%.                                                                       
                            +#=@@+                  *%%%%%%%%%%%.  .  .+%%%%%%#                 -=-.                                                  
                           =@@@@@@#+               .%%%%%= :*%%%.  *#.   =%%%%%-               *@@@#                                                  
                          -@@@@@@@@@=              =%%%%%=   :#@.  +%+   .#%%%%*               =@@@#                       ...                        
                          %@@@@@@@@@#              *%%#%%%#=.  -.  -.  :*%%%%%%%               .#@@#:.                   :%@@@%.                      
                          *@%@@@@@%@#       .....  #%%#%%%%%%+.      -#%%%%%%%%%  ......    :#@@@@@@@@@%=                *@@@@@%                      
                            @@@@@@%#@:......    .  %%%%%%%%%%%%.    +%%%%%%%%%%@. ...   ..:#@@@@@@@@@@@@@                #@@@@@%.                     
                            @@@@@@@=#-  .....:.    #%%%%%%%%%+       -*%%%%%%%%@     .....:-@@@@@@@@@@@@@.              %@@@@@@#.                     
                        .::+@@@@@@@%##:.     ..:-  *%%%%%%%=   =.  -.  .*%%%%%%%  -::..    :@@@@@@@@@@@@@+:.           +@@@@@@@@@%*=:.                
                    .::-:  =@@@@@@@@=:    .:-:.    +%%#%%=   :#%.  *%=   :#%%%%*     .:-:.  =#@@@@@@@@@@@  :--:.     +@@@@@@@@@@@@@@@@%               
        ...      .:-:.     -@@@#%@@@:  .:--.       .%%#%%=.:*%%%.  **.  .=#%%#%-        .:-::=@@@@@@@@@@=     .:-:. .@@@@@@@@@@@@@@@@@@-              
      :#@@@+  .:--.       -#@@@-.@@@+.---:          +%%%%%%%%%%%.  .  .*%%%%%##           :--@@@@@@@@@@@=-.      .-=%@@@@@@@@@@@@@@@@@@@              
      *@@@@@@*--.       :--+@@@. *@@:--:-            %%%%%%%%%%%.   .*%%%%%%%%.            -+@@@@@@@@@@@*--:      :@@@@@@@@@@@@@@@@@@@@@:             
      =@@@@@@%%%*+-    :---:*@%  .%@:--:-:            *%%%#%%%%%. .+%%%%%%%%#.            :-+%@@@@%@@@%*+-:-:     %@@@@@@@@@@@@@@@@@@@@@*             
      .@@@@@@#=*%@@@#. ---::-@=   .@=.----:.           :#%%%%%%%-*%%%%#%%%#-            .----+@@@+:@@@= .----.    :#@@#%@@@@@@@@@@@@@@@@@             
      =@@@@@@@@@@@@@+ .--:--=@:    #@%:.-----:.          :+#%%%%%%%%%%%#+-           .:-----: @@@= %@@= -----.         +@@@@@@@@@@@@@@@@@.            
      :%@@@@@@@@@%-    :-:-*@%.      -:   .:-----::...        .:::::.          ..::-----:.    @@@. =@@*:--:--          *@@@@@@@@@@@@@@@@@:            
      -#@@@@@@@@@@.     :--==-:               ..::--------::::::....::::::--------::..       :@@@  .@@@=:--:          :@@@@@@@@@@@@@@@@@@:            
      -%@@@@@@@@@@%      :------:.                   ...:::::::::-::::::::::...              -@@# .=@@@*--.           +@@@@@@@@@@@@@@@@@@:            
      -#@@@@@@@@@@@%+=*#-  .:------::.                                                       =@@*--=@@@*.             %@@@@@@@@@@@@@@@@@@-            
      :%@@@@@@@@@@@@@#++%++**+=:--------:..                                              ..:=%@@=---@@@              -@@@@@@@@@@@@@@@@@@@-            
       #@@@@@@@@@@@@@@@@@@@@@@@- ..:---------::::..                              ..::::---=#@@%#-.. #@%             .#@@@@@@@@@@@@@@@@@@@:.           
       +*=*#@@@@@@@@@@@@@@@@@@@%      ..:::------------::::::::::::::::::::::----------------.      %@*           .:---#@@@@@@@@@@@@@@@@@@@           
       *=+@@@@@@@@@@@@@%##%+#@@@#:           ...::::----------------------------::::...                         :------#@@@@@@=@@@@@@@@@@@@           
       *+::======-=%=-.   *  =@@@@#:                      ................                                   .:-:--::--+@@@@@@.@@@@@@@@@@@@           
       *-    :--:--%-----:#   .%@@@@#.                                                                   .:-----------:.@@@@@@.@@@@@@@@@@@@           
       *:      .:--%------%--:.:%@@%@@*:   :+-                                                      ..:------------:.   @@@@@@.#@@@@@@@@@@+           
       *:         .%---:--%--:-=@@@@=*@@@@@@@:                                                ..::--:-----------:.      %@@@@@ +@@@@@@@%=             
       *:          #  .:--*-::--%*@@@%@@@*=+:..                                      ...:::-----------------:..         %@@@@@ -@@@@@@:               
       .           =      .:::--=-+###+--==-::-------:::::::....::::....::::::::-----------------------::.              %@@@@@ .@@@@@%                
                                .:::--::---------------------------------------------------:-----::.                    %@@@@@  @@@@@#                
                                       ..::::-------------------------------------------:::..                           *@@@@#  *@@@@*                
                                                  ......::::::::::::::::::::......                                      :@@@@:  +@@@@*                
                                                                                                                       .@@@@*    @@@@#                
                                                                                                                        #@@@%   =@@@@*                

