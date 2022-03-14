import socket
# tralha na placa de rede

import sys

def main ():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou')
        print('Erro: {}'.format(e))
        sys.exit()
    print('Socket criado com sucesso.')

    hostAlvo = input('Digite o host ou ip a ser conecado: ')
    portaAlvo = input('Digite a porta ser conecada: ')

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print('Cliente conectado com sucesso no host: ' + hostAlvo + ' , na porta: ' + portaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print('A conexão falhou')
        print('Erro:  {}'.format(e))
        sys.exit()

if __name__ == '__main__':
    main()

