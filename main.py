import telnet
import nmea2

result = telnet.TelnetWorkers('127.0.0.1','55555')

for x in range (0,17):
    a = result.connect()

    if (x == 0):
        b = a.split('started...')

        cont = True
        indice = 0
        while cont:
            if(str(b[indice]) != 'Simulator (127.0.0.1 : 55555) '):
                c = b[indice]
                cont = False
            else:
                indice = indice + 1

    else:
        c = a

    imprimir = nmea2.sentence(c)

    if (imprimir != None):
        print imprimir