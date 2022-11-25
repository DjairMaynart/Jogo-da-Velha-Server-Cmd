import socket
#import base64


def printJogo(jogo):
    print('\r\n   1     2     3\r\n1 ', jogo[0][0], ' | ', jogo[0][1], ' | ', jogo[0][2], '\r\n------------------\r\n2 ', jogo[1][0],
          ' | ', jogo[1][1], ' | ', jogo[1][2], '\r\n------------------\r\n3 ', jogo[2][0], ' | ', jogo[2][1], ' | ', jogo[2][2], '\r\n')


print('digite o ip do servidor:')
endIPdest = input()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

s.connect((endIPdest, 5050))
print('Conectado com o servidor!')
s.send('GET / HTTP/1.1'.encode('utf-8'))

try:
    while True:
        recebido = s.recv(2000).decode('utf-8')
        if (recebido == ''):
            print('Conexão terminada')
            break
        else:
            if ('vez' in recebido):
                print(recebido.replace('vez',''))
                while True:
                    digitado = input(
                        "Digite uma jogada válida no formato x,y de 1 a 3: ")
                    if (len(digitado) == 3 and digitado[0].isdigit() and digitado[2].isdigit() and digitado[1] == ','
                            and int(digitado[0]) > 0 and int(digitado[0]) < 4 and int(digitado[2]) > 0 and int(digitado[2]) < 4):
                        break
                s.sendall(str.encode(digitado))

            else:
                print(recebido.replace('vez',''))

except KeyboardInterrupt:
    print("\r\nTerminado pelo usuário")
    s.close()
