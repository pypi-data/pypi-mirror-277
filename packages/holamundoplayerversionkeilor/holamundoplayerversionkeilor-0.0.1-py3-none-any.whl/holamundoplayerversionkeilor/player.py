"""
Esta es la documentacion de player:
Este es el modulo que incluye la clase de reproductor de musica
"""

class Player:
    def __init__(self, name, path):
        """
        Este es el contructor de Player recibe dos parametros.
        
        Parameters:
        name (str): Este es un string con el nombre de la cancion.
        path (str): Este es un string con el path de la cancion.
        """
        self.name = name
        self.path = path
        self.reproduciendo = False

    def play(self):
        """
        Reproduce la cancion, que le pasaste en el constructor.
        
        Returns:
        int: Devuelve 1 si reproduce con exito y devuelve 0 si hubo un error.
        """
        try:
            self.reproduciendo = True
            if type(self.name) != str or type(self.path) != str:
                raise ValueError

            print(f"\nReproduciendo la cancion {self.name}.")
            return 1
        
        except ValueError: return 0
        except: return 0

    def stop(self):
        "Pausa la cancion, si se esta reproduciendo."
        if self.reproduciendo == True:
            print(f"\nSe pauso la cancion {self.name}")
            self.reproduciendo = False
        else:
            print(f"\nLa cancion {self.name} no se esta reproduciendo.")

if __name__ == '__main__':
    circles = Player("Circles de Post Malone", "music/Circles.mp3")
    circles.play()
    circles.stop()
    circles.stop()