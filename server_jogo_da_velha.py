from ast import Break
import socket
import time

jogo = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def printJogo():
    return '\r\n   1     2     3\r\n1  '+str(jogo[0][0])+'  |  '+str(jogo[0][1])+'  |  '+str(jogo[0][2])+'\r\n------------------\r\n2  '+str(jogo[1][0])+'  |  '+str(jogo[1][1])+'  |  '+str(jogo[1][2])+'\r\n------------------\r\n3  '+str(jogo[2][0])+'  |  '+str(jogo[2][1])+'  |  '+str(jogo[2][2])+'\r\n'


def checar():
    for x in jogo:
        if (x == ['X', 'X', 'X']):
            return 'X'
        if (x == ['O', 'O', 'O']):
            return 'O'
    for x in range(3):
        if (jogo[0][x] == jogo[1][x] and jogo[2][x] == jogo[1][x] and jogo[0][x] == 'X'):
            return 'X'
        if (jogo[0][x] == jogo[1][x] and jogo[2][x] == jogo[1][x] and jogo[0][x] == 'O'):
            return 'O'
    if (jogo[0][0] == jogo[1][1] and jogo[2][2] == jogo[1][1] and jogo[0][0] == 'X'):
        return 'X'
    if (jogo[0][0] == jogo[1][1] and jogo[2][2] == jogo[1][1] and jogo[0][0] == 'O'):
        return 'O'
    if (jogo[0][2] == jogo[1][1] and jogo[2][0] == jogo[1][1] and jogo[0][2] == 'X'):
        return 'X'
    if (jogo[0][2] == jogo[1][1] and jogo[2][0] == jogo[1][1] and jogo[0][2] == 'O'):
        return 'O'
    completo = 'E'
    for x in range(3):
        for y in range(3):
            if (jogo[x][y] == ' '):
                completo = '0'
    return completo


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
s.bind(('', 5050))
s.listen(2)

ws, addr = s.accept()
print('Conectado a', addr)
data = ws.recv(2000).decode('utf-8')

P = data.split(' ')  # GET / HTTP/1.0 -> [GET, /, HTTP/1.0]
if P[0] == 'GET':
    if P[1] == '/':
        ws.send(str.encode('Aguardando adversário...'))

ws2, addr2 = s.accept()
print('Conectado a', addr2)
data2 = ws2.recv(2000).decode('utf-8')

print('\r\n')

P = data2.split(' ')  # GET / HTTP/1.0 -> [GET, /, HTTP/1.0]
if P[0] == 'GET':
    if P[1] == '/':
        ws.send(str.encode('Adversário conectado!'))
        ws.sendall(str.encode(printJogo()))
        ws2.sendall(str.encode(printJogo()))

try:
    sair = 0
    while (sair == 0):
        while True:
            ws2.sendall(str.encode('Aguardando jogada do adversário...'))
            acabou = False
            while True:
                ws.sendall(str.encode('vez'))
                jogada = ws.recv(2000).decode('utf-8')
                if (jogo[int(jogada[2])-1][int(jogada[0])-1] == ' '):
                    break
            jogo[int(jogada[2])-1][int(jogada[0])-1] = 'O'
            print('Jogador O:')
            print(printJogo())
            ws.sendall(str.encode(printJogo()))
            ws2.sendall(str.encode(printJogo()))
            if (checar() == 'E'):
                ws.sendall(str.encode('Empate, não houve vencedor'))
                ws2.sendall(str.encode('Empate, não houve vencedor'))
                print('Empate, não houve vencedor')
                acabou = True
            else:
                if (checar() == 'O'):
                    ws.sendall(str.encode('Jogador O venceu!'))
                    ws2.sendall(str.encode('Jogador O venceu!'))
                    print('Jogador O venceu!')
                    acabou = True
                else:
                    if (checar() == 'X'):
                        ws.sendall(str.encode('Jogador X venceu!'))
                        ws2.sendall(str.encode('Jogador X venceu!'))
                        print('Jogador X venceu!')
                        acabou = True
            if (acabou == True):
                print('jogar novamente? digite 1 para SIM, 0 para NÃO')
                resp = input()
                if (resp == '1'):
                    jogo = [[' ', ' ', ' '], [
                        ' ', ' ', ' '], [' ', ' ', ' ']]
                    ws.sendall(str.encode(printJogo()))
                    ws2.sendall(str.encode(printJogo()))
                    break
                else:
                    print('JOGO FINALIZADO')
                    time.sleep(5)
                    sair = 1
                    break
            ws.sendall(str.encode('Aguardando jogada do adversário...'))

            while True:
                ws2.sendall(str.encode('vez'))
                jogada = ws2.recv(2000).decode('utf-8')
                if (jogo[int(jogada[2])-1][int(jogada[0])-1] == ' '):
                    break
            jogo[int(jogada[2])-1][int(jogada[0])-1] = 'X'
            print('Jogador X:')
            print(printJogo())
            ws.sendall(str.encode(printJogo()))
            ws2.sendall(str.encode(printJogo()))
            if (checar() == 'E'):
                ws.sendall(str.encode('Empate, não houve vencedor'))
                ws2.sendall(str.encode('Empate, não houve vencedor'))
                print('Empate, não houve vencedor')
                acabou = True
            else:
                if (checar() == 'O'):
                    ws.sendall(str.encode('Jogador O venceu!'))
                    ws2.sendall(str.encode('Jogador O venceu!'))
                    print('Jogador O venceu!')
                    acabou = True
                elif (checar() == 'X'):
                    ws.sendall(str.encode('Jogador X venceu!'))
                    ws2.sendall(str.encode('Jogador X venceu!'))
                    print('Jogador X venceu!')
                    acabou = True
            if (acabou == True):
                print('jogar novamente? digite 1 para SIM, 0 para NÃO')
                resp = input()
                if (resp == '1'):
                    jogo = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
                    ws.sendall(str.encode(printJogo()))
                    ws2.sendall(str.encode(printJogo()))
                    break
                else:
                    print('JOGO FINALIZADO')
                    time.sleep(5)
                    sair = 1
                    break

except KeyboardInterrupt:
    print("\r\nTerminado pelo usuário")
    ws.close()
    ws2.close()
    s.close()
except IndexError:
    print("\r\nTerminado pelo usuário")
    ws.close()
    ws2.close()
    s.close()
except ConnectionResetError:
    print("\r\nTerminado pelo usuário")
    ws.close()
    ws2.close()
    s.close()
