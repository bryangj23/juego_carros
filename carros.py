class Carro:

    def __init__(self, jugador):
        self.jugador=jugador
        self.posicion=0

    def set_pos(self, posicion):
        self.posicion=posicion

    def get_pos(self):
        return self.posicion

    def getKm(self):
        return self.get_pos()/1000