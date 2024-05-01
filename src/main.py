#
# Actividad, Estructura de Datos Tipo Pila
#
# Alumno: José Fernando Usui
#

import os

# Tarea: Limpiar consola
clear = lambda: os.system("cls")

class Nodo:
    def __init__(self, caracter):
        self.caracter = caracter
        self.siguiente = None

class Stack:
    def __init__(self):
        self.puntero = None
    def apilar(self, nodo):
        if self.esta_vacio(self.puntero):
            self.puntero = nodo
        else:
            nodo.siguiente = self.puntero
            self.puntero = nodo
    def vaciar(self):
        if self.esta_vacio(self.puntero):
            return None
        else:
            while not self.esta_vacio(self.puntero):
                aux = self.puntero
                self.puntero = self.puntero.siguiente
                if not self.esta_vacio(aux.siguiente):
                    aux.siguiente = None
                aux = None
    def obtener_cadena_de_caracteres(self):
        aux = self.puntero
        cadena = ''
        while not self.esta_vacio(aux):
            cadena = cadena + aux.caracter
            aux = aux.siguiente
        return cadena
    # La estrategia es la siguientes:
    # 1. Buscar el elemento 1 e ir sumando lo elemento que coincidan
    # 2. Buscar el elemento 2 e ir sumando lo elemento que coincidan
    # 3. Por ultimo comparar la igualdad (primer paréntesis "(" y segundo paréntesis ")")
    def buscar_elementos(self, elemento_1, elemento_2):
        elementos_encontrados = [0, 0]
        aux = self.puntero
        while not self.esta_vacio(aux):
            if aux.caracter == elemento_1:
                elementos_encontrados[0] = elementos_encontrados[0] + 1
            if aux.caracter == elemento_2:
                elementos_encontrados[1] = elementos_encontrados[1] + 1
            aux = aux.siguiente
        return elementos_encontrados[0] == elementos_encontrados[1]
    def esta_vacio(self, puntero):
        return puntero == None
    
def controlar_opcion(opcion):
    lista_de_opcion = [1, 2, 3, 4]
    for x in lista_de_opcion:
        if opcion == x:
            return True
    return False

def main():
    pila__de_caracteres = Stack()

    while True:
        print('------------------------------------------------')
        print('Informacion General:')
        cadena_de_caracteres = pila__de_caracteres.obtener_cadena_de_caracteres()
        if cadena_de_caracteres == '':
            print('\tCaracteres Apilados: No hay caracteres apilados')
            print('\tCaracteres Apilados(Inverso): No hay caracteres')
        else:
            print(f'\tCaracteres Apilados: {cadena_de_caracteres}')
            print(f'\tCaracteres Apilados(Inverso): {cadena_de_caracteres[::-1]}')
        print('------------------------------------------------')
        print('Menu:')
        print('1> Cargar un carácter a la pila')
        print('2> Iniciar proceso de análisis de la expresión aritmética')
        print('3> Borrar todos los nodos de la pila')
        print('4> Salir')
        print()
        opcion = int(input('Ingrese una opcion: '))
        print()
        if controlar_opcion(opcion):
            if opcion == 1:
                clear()
                pila__de_caracteres.apilar(Nodo(input('Ingresar un caracter: ')[0:1]))
                clear()
            elif opcion == 2:
                clear()
                print('---------------------------------------------------------------')
                print('Coincidencias:')
                if cadena_de_caracteres == '':
                    print('\tNo hay elementos apilados')
                else:
                    estado_del_analisis_en_general = [0, 0, 0] 
                    if cadena_de_caracteres.find('(') != -1 or cadena_de_caracteres.find(')') != -1: 
                        if pila__de_caracteres.buscar_elementos('(', ')'):
                            print('\tLos paréntesis están equilibrados')
                            estado_del_analisis_en_general[0] = 1
                        else:
                            print('\tLos paréntesis no están equilibrados')
                            estado_del_analisis_en_general[0] = -1
                    else:
                        print('\tNo se encontró en la pila elementos que coincida con un "paréntesis"')
                        estado_del_analisis_en_general[0] = -2
                    if cadena_de_caracteres.find('[') != -1 or cadena_de_caracteres.find(']') != -1:
                        if pila__de_caracteres.buscar_elementos('[', ']'):
                            print('\tLos corchetes están equilibrados')
                            estado_del_analisis_en_general[1] = 1
                        else:
                            print('\tLos corchetes no están equilibrados')
                            estado_del_analisis_en_general[1] = -1
                    else:
                        print('\tNo se encontró en la pila elementos que coincida con un "corchete"')
                        estado_del_analisis_en_general[1] = -2
                    if cadena_de_caracteres.find('{') != -1 or cadena_de_caracteres.find('}') != -1:
                        if pila__de_caracteres.buscar_elementos('{', '}'):
                            print('\tLas llaves están equilibrados')
                            estado_del_analisis_en_general[2] = 1
                        else:
                            print('\tLas llaves no están equilibrados')
                            estado_del_analisis_en_general[2] = -1
                    else:
                        print('\tNo se encontró en la pila elementos que coincida con una "llave"')
                        estado_del_analisis_en_general[2] = -2
                    print()
                    print('\tResultado del Análisis:')
                    estado_final = True
                    for x in estado_del_analisis_en_general:
                        if x == -1:
                            print('\t\t- La expresión aritmética esta DESEQUILIBRADA')
                            estado_final = False
                            break
                    if estado_del_analisis_en_general[0] == -2 and estado_del_analisis_en_general[1] == -2 and estado_del_analisis_en_general[2] == -2:
                        print('\t\t- No hay elementos "()[]{}" en la expresión aritmética para analizar')
                        estado_final = False
                    if estado_final:
                        print('\t\t- La expresión aritmética esta EQUILIBRADA')
                print('---------------------------------------------------------------')
                input('Presione cualquier tecla para continuar...')
                clear()
            elif opcion == 3:
                pila__de_caracteres.vaciar()
                clear()
            elif opcion == 4:
                break
        else:
            print('La opcion ingresada no existe')
            input('Presione cualquier tecla para continuar...')
            clear()
if __name__ == '__main__':
    main()