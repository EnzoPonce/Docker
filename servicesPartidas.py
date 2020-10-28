import random
from palabras import Palabras
from partida import Partida

class ServicesPartidas():

    def iniciar_partida(self, nombre, intentos, palabra, tipo_palabra):
        if palabra == '' and tipo_palabra == '':
            if intentos < 1 or intentos > 10:
                raise ValueError
            else:
                x = Palabras
                k = random.randint(1, len(x.diccionario))
                k -= 1
                y = x.diccionario['%s'% k]
                palabra = y['palabra']
                tipo_palabra = y['tipo_palabra']
                print(": ", tipo_palabra)
                intentosTotales = intentos * len(list(palabra))
                partida = Partida(palabra, intentosTotales, tipo_palabra, nombre)
                print("\nCantidad de letras >>> ", len(palabra))
                print("\n", partida._palabra_aciertos)
                return partida
        else:
            print("\nPista para descifrar la palabra >>> ", tipo_palabra)
            intentosTotales = intentos * len(list(palabra))
            partida = Partida(palabra, intentosTotales, tipo_palabra, nombre)
            print("\nCantidad de letras >>>", len(palabra))
            print("\n", partida._palabra_aciertos)
            return partida

    def get_random_palabra(self):
        x = Palabras
        k = random.randint(0, len(x.diccionario))
        k -= k
        y = x.diccionario['%s'% k]
        return y

    def intentar_letra(self, partida, letra):
        contador = 0
        a = False
        for l in partida._palabra: 
            if l == letra:
                partida._palabra_aciertos[contador] = letra
                a = True  
            contador += 1
        print(partida._palabra_aciertos) 
        if partida._palabra_aciertos == partida._palabra:
            partida.intentos -= 1
            return "Gano"
        elif a != True:
            partida.intentos -= 1 
            if partida.intentos == 0:
                return "Perdio"
            else:
                return "Continua"
        else:
            partida.intentos -= 1
            if partida.intentos == 0:
                return "Perdio"
            else:
                return "Continua"        
