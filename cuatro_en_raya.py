class CuatroEnRaya:
    """
    Esta clase contiene una simulación de la reglas del juego cuatro en raya.
    Su constrictor se basa en el numero de filas y columnas para generar un tablero,
    al cual se le aplicaran funciones.
    """
    def __init__(self,num_filas, num_columnas):
        self.num_filas = num_filas
        self.num_columnas = num_columnas
        self.tablero = self.crear_tablero()

    def crear_tablero(self):
        """
        Esta función genera un tablero con el número de filas y columnas.
        """
        tablero=[]
        for i in range(self.num_filas):
            fila=[]
            tablero.append(fila)
            for j in range(self.num_columnas):
                fila.append("•")
        return tablero
    
    def obtener_tablero(self):

        """
        Esta función devuelve el tablero de la clase para que este pueda ser
        consumido extrernamente. 
        """
        return self.tablero
    
    def introducir_fichas(self,columna,color):
        """
        Esta función tiene la responsabilidad de introducir la ficha del juego, y
        verifica si la inserción es exitosa en el tablero.
        Argumentos:
        <columna> Posición de la columna en que será insertada la ficha.
        <color> La ficha que será insertada en el tablero.
        """
        if columna < 0 or columna >= self.num_columnas:
            return False , "columna_rango"
        elif self.tablero[0][columna] != "•":
            return False , "columna_llena"
        else:
            for i in range(self.num_filas-1,-1,-1):
                if self.tablero[i][columna]=="•":
                    self.tablero[i][columna]=color
                    return True, None
        return False, "error_inesperado"

    def revisar_filas(self, color):
        """
        Esta función revisa si hay una suma de 4 de la misma ficha o color en las filas.
        Argumentos:
        <color> La ficha que será evaluada.
        """
        contador=0 
        for i in self.tablero:
            contador=0
            for j in i:
                if j == color:
                    contador+=1
                    if contador == 4:
                        return True
                else:
                    contador = 0
        return False

    def revisar_columnas(self, color):
        """
        Esta función revisa si hay una suma de 4 de la misma ficha o color en las columnas.
        Argumentos:
        <color> La ficha que será evaluada.
        """
        contador=0
        for i in range(self.num_columnas): 
            contador=0
            for j in self.tablero:
                if j[i]==color:
                    contador+=1
                    if contador==4:
                        return True
                else:
                    contador = 0
        return False         

    def revisar_diagonal_derecha(self, color):
        """
        Esta función revisa si hay una suma de 4 de la misma ficha o color en las diagonales derechas.
        Argumentos:
        <color> La ficha que será evaluada.
        """
        for i in range(self.num_filas-3):
            for j in range(self.num_columnas-3):
                contador=0
                for escalera in range(4):
                    if self.tablero[i+escalera][j+escalera]==color:
                        contador+=1
                    else:
                        break
                if contador==4:
                    return True
        return False

    def revisar_diagonal_izquierda(self, color):
        """
        Esta función revisa si hay una suma de 4 de la misma ficha o color en las diagonales izquierdas.
        Argumentos:
        <color> La ficha que será evaluada.
        """
        for i in range(self.num_filas-3):
            for j in range(3, self.num_columnas):
                contador=0
                for escalera in range(4):
                    if self.tablero[i+escalera][j-escalera]==color:
                        contador+=1
                    else:
                        break
                if contador==4:
                    return True
        return False

    def revisar_ganador(self, color):
        """
        Esta función revisa si hay algun True en las funciones que revisan filas, columnas, diagonales en bisca
        de una suma de 4 fichas consecutivas.
        Argumentos:
        <color> La ficha que será evaluada.
        """
        if self.revisar_filas(color)==True:
            return True
        elif self.revisar_columnas(color)==True:
            return True
        elif self.revisar_diagonal_derecha(color)==True:
            return True
        elif  self.revisar_diagonal_izquierda(color)==True:
            return True
        else:
            return False

    def cambiar_turno(self, turno_actual):
        """
        Esta función intercambia los turnos del juego actual.
        Argumnetos:
        <turno_actual> El tyurno que será evaluado para el cambio de juego. 
        """
        return "Y" if turno_actual == "X" else "X"


def mostrar_tablero(tablero):
    """
    Esta función imprime el una lista de manera más ordenada, simulando un tablero.
    Argumentos:
    <tablero> Una lista que contiene listas y simula un tablero.
    """
    for num in range(len(tablero[0])):
        print(num, end='  ')
    for i in tablero:
        print("")
        for casilla in i:
            print(casilla, end="  ")
    print("")

        
def juego_cuatro_en_raya():
    """
    Esta función simula la lógica del juego cuatro en raya utilizando los métodos de la clase CuatroEnRaya.
    En este contexto, se intenta simular una interfaz dentro de la consola, separando la lógica de la vista
    por medio de este controlador, donde se muestra la retroalimentación, la entrad y salida de los datos. 
    """
    mensajes = {
        "columna_rango" : "¡Error! La columna esta fuera del rango del tablero.",
        "columna_llena" : "¡Error! La columna {columna} esta llena.",
        "error_inesperado" : "¡Error inesperado!",
        "titulo" : "¡Cuatro en raya!",
        "columnas" : "¿Cuántas columnas tendrá el tablero? ",
        "filas" : "¿Cuántas filas tendrá el tablero? ",
        "ganador" : "¡El juego ha terminado! ¡El ganador fue el participante del turno {turno}.!",
        "empate" : "El número de intentos ha llegado a su límte. ¡Ha  sido un empate.!",
        "columna_turno" : "¿En que columna deseas poner la ficha: ",
        "elegir_turno" : "Elige X o Y como tu ficha para jugar. ",
        "error_insercion" : "Por favor, ingresa un número válido."
        } 
    print(mensajes["titulo"])
    num_columnas=int(input(mensajes["columnas"]))
    num_filas=int(input(mensajes["filas"]))
    limite = num_filas * num_columnas
    juego = CuatroEnRaya(num_filas,num_columnas)
    turno = input(mensajes["elegir_turno"])
    if turno not in ["X", "Y"]:
        print("Ficha inválida. Se asignará X por defecto.")
        turno = "X"
    contador_de_intentos = 0
    while contador_de_intentos != limite:
        mostrar_tablero(juego.obtener_tablero())
        print(f"Es el turno de {turno}. ")
        try:
            col = int(input(mensajes["columna_turno"]))
        except ValueError:
            print(mensajes["error_insercion"])
            continue
        exito, opcion = juego.introducir_fichas(col, turno)
        if not exito:
            print(mensajes[opcion].format(columna = col))
            continue
        else:
            contador_de_intentos+=1
            if juego.revisar_ganador(turno):
                print(mensajes["ganador"].format(turno = turno))
                mostrar_tablero(juego.obtener_tablero())
                break
            if contador_de_intentos == limite:
                print(mensajes["empate"])
                mostrar_tablero(juego.obtener_tablero())
            else:
                turno = juego.cambiar_turno(turno)


"""
Ejecución del juego.
"""
if __name__ == "__main__":
    juego_cuatro_en_raya()

    


        
