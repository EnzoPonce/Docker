from partida import Partida
from servicesPartidas import ServicesPartidas
from jugadores import Jugadores

class Ahorcado():

    def un_jugador(self):
        menu = ServicesPartidas()
        player = str(input("Ingrese su nombre >>> "))
        cant = int(input("Ingrese la dificultad >>> "))
        p = menu.iniciar_partida(player, cant, '', '')
        for i in range(0, p.intentos):
            letra = input("\nIngrese la letra >>> ")
            if letra == 'salir':
                return True
            respuesta = menu.intentar_letra(p, letra.upper())
            print(respuesta)
            if respuesta == 'Gano' or respuesta == 'Perdio':
                return True

    def dos_jugadores(self):
        dicc = {}
        menu = ServicesPartidas()
        for j in range(0, 2):
            player = str(input("Ingrese su nombre >>> "))
            cant = int(input("Ingrese la dificultad >>>"))
            palabra = str(input("Ingrese la palabra >>>"))
            tipo = str(input("Ingrese la categoria >>> "))
            p = menu.iniciar_partida(player, cant, palabra, tipo)
            for i in range(0, p.intentos):
                letra = str(input("\nIngrese letra >>> "))
                if letra == 'salir':
                    return True
                respuesta = menu.intentar_letra(p, letra.upper())
                print(respuesta)
                if respuesta == 'Gano' or respuesta == 'Perdio':
                    if j == 0:
                        dicc[player] = p.__dict__
                        break
                    else:
                        dicc[player] = p.__dict__
                        return True