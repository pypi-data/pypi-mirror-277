"""
este es el modulo que incluye la clase de reproductor de musica
"""

class Player:
    """
    este clase crea un reproductor de musica
    """

    def play(self, song):
        """
        reproduce la cancion que recibio en el constructor
        parameters:
        song (str): este es un string con el path de la cancion

        Returns:
        Int: devuelve 1 si reproduce con exito, en caso de fracaso devuelve 0
        """
        print("reproduciendo cancion")

    def stop(self):
        print("stopping")