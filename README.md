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
