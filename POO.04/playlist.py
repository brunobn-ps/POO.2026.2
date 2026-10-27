class Musica:
    def __init__(self, titulo, artista, album):
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)
    def set_titulo(self, t):
        self.__titulo = t
    def set_artista(self, a):
        self.__artista = a
    def set_album(self, al):
        self.__album = al
    def get_titulo(self):
        return self.__titulo
    def get_artista(self):
        return self.__artista
    def get_album(self):
        return self.__album
    def ToString(self):
        return f"Título da Música: {self.__titulo}  ---  Artista do Título: {self.__artista}  ---  Album da Música: {self.__album}"
    def __str__(self):
        return self.ToString()
    
class Playlist:
    def __init__(self, nome, descricao):
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.__musicas = []
    def set_nome(self, nome): self.__nome = nome
    def set_descricao(self, descricao): self.__descricao = descricao
    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao
    def Inserir(self, m: Musica):
        self.__musicas.append(m)
    def Listar(self):
        return self.__musicas
    def ToString(self):
        qtd = len(self.__musicas)
        return f"A Playlist {self.__nome} tem {qtd} música(s)"
    def __str__(self):
        return self.ToString()


class PlaylistUI:
    @staticmethod
    def menu():
        print("\n---MENU---")
        print("1 - Criar uma playlist")
        print("2 - Inserir música em uma playlist")
        print("3 - Listar músicas em uma playlist")
        print("4 - Fim do Programa")
        opcao = int(input("Escolha uma das opções: "))
        return opcao

    @staticmethod
    def main():
        playlists = []

        op = PlaylistUI.menu()
        while op != 4:
            if op == 1:
                nome = input("Digite o nome da playlist: ")
                desc = input("Digite a descrição da playlist: ")
                
                pl = Playlist(nome, desc)
                playlists.append(pl)
            elif op == 2:
                if not playlists:
                    print("Nenhuma playlist cadastrada!")
                else: 
                    print("\nPlaylists cadastradas: ")
                    for i, pl in enumarate(playlists):
                        
            elif op == 3:
