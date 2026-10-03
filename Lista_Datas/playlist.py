from datetime import timedelta

class PlayList:
    def __init__(self, i: int, n: str, d: str):
        self.__id = i
        self.__nome = n
        self.__descricao = d

    def get_id(self) -> int:
        return self.__id
    def set_id(self, i: int):
        self.__id = i
    def get_nome(self) -> str:
        return self.__nome
    def set_nome(self, n: str):
        self.__nome = n
    def get_descricao(self) -> str:
        return self.__descricao
    def set_descricao(self, d: str):
        self.__descricao = d


    def TempoTotal(self, itens: list = None, musicas: list = None) -> timedelta:
        """
        Recebe a lista de PlayListItem e Musica para somar a duração 
        das músicas que pertencem a esta playlist.
        """
        tempo_total = timedelta()
        
        if not itens or not musicas:
            return tempo_total

        mapa_musicas = {m.get_id(): m for m in musicas}
        for item in itens:
            if item.get_id_playlist() == self.__id:
                id_musica = item.get_id_musica()
                if id_musica in mapa_musicas:
                    tempo_total += mapa_musicas[id_musica].get_duracao()

        return tempo_total

    def __str__(self) -> str:
        return f"ID: {self.__id} | Nome: {self.__nome} | Descrição: {self.__descricao}"


class Musica:
    def __init__(self, i: int, t: str, art: str, alb: str, d: timedelta):
        self.__id = i
        self.__titulo = t
        self.__artista = art
        self.__album = alb
        self.__duracao = d

    def get_id(self) -> int:
        return self.__id
    def set_id(self, i: int):
        self.__id = i
    def get_titulo(self) -> str:
        return self.__titulo
    def set_titulo(self, t: str):
        self.__titulo = t
    def get_artista(self) -> str:
        return self.__artista
    def set_artista(self, art: str):
        self.__artista = art
    def get_album(self) -> str:
        return self.__album
    def set_album(self, alb: str):
        self.__album = alb
    def get_duracao(self) -> timedelta:
        return self.__duracao
    def set_duracao(self, d: timedelta):
        self.__duracao = d
    def __str__(self) -> str:
        return f"ID: {self.__id} | Título: {self.__titulo} | Artista: {self.__artista} | Álbum: {self.__album} | Duração: {self.__duracao}"


class PlayListItem:
    def __init__(self, i: int, ip: int, im: int, d: datetime, s: int):
        self.__id = i
        self.__id_playlist = ip
        self.__id_musica = im
        self.__data_inclusao = d
        self.__sequencia = s

    def get_id(self) -> int:
        return self.__id
    def set_id(self, i: int):
        self.__id = i
    def get_id_playlist(self) -> int:
        return self.__id_playlist
    def set_id_playlist(self, ip: int):
        self.__id_playlist = ip
    def get_id_musica(self) -> int:
        return self.__id_musica
    def set_id_musica(self, im: int):
        self.__id_musica = im
    def get_data_inclusao(self) -> datetime:
        return self.__data_inclusao
    def set_data_inclusao(self, d: datetime):
        self.__data_inclusao = d
    def get_sequencia(self) -> int:
        return self.__sequencia
    def set_sequencia(self, s: int):
        self.__sequencia = s

    def __str__(self) -> str:
        dt_str = self.__data_inclusao.strftime("%d/%m/%Y %H:%M")
        return f"Item ID: {self.__id} | Playlist ID: {self.__id_playlist} | Música ID: {self.__id_musica} | Data: {dt_str} | Seq: {self.__sequencia}"


class UI:
    __playlists = []
    __musicas = []
    __itens = []

    @classmethod
    def Main(cls):
        op = -1
        while op != 0:
            op = cls.Menu()
            if op == 1:
                cls.InserirMusica()
            elif op == 2:
                cls.ListarMusicas()
            elif op == 3:
                cls.AtualizarMusica()
            elif op == 4:
                cls.ExcluirMusica()
            elif op == 5:
                cls.InserirItem()
            elif op == 6:
                cls.ListarItensPlaylist()
            elif op == 7:
                cls.AtualizarItem()
            elif op == 8:
                cls.ExcluirItem()
            elif op == 0:
                print("\nAplicação finalizada!")
            else:
                print("\nOpção inválida!")

    @staticmethod
    def Menu() -> int:
        print("\n" + "="*40)
        print("         GERENCIADOR DE MÚSICAS       ")
        print("="*40)
        print("--- MÚSICAS ---")
        print("1 - Inserir Música")
        print("2 - Listar Músicas")
        print("3 - Atualizar Música")
        print("4 - Excluir Música")
        print("--- ITENS DA PLAYLIST ---")
        print("5 - Adicionar Música à Playlist")
        print("6 - Listar Músicas de uma Playlist")
        print("7 - Atualizar Item da Playlist")
        print("8 - Remover Música da Playlist")
        print("0 - Sair")
        print("="*40)
        try:
            return int(input("Opção: "))
        except ValueError:
            return -1

    @classmethod
    def InserirMusica(cls):
        try:
            i = int(input("ID: "))
            t = input("Título: ")
            art = input("Artista: ")
            alb = input("Álbum: ")
            m = int(input("Duração (Minutos): "))
            s = int(input("Duração (Segundos): "))
            d = timedelta(minutes=m, seconds=s)
            cls.__musicas.append(Musica(i, t, art, alb, d))
            print("Música cadastrada!")
        except ValueError:
            print("Entrada inválida!")

    @classmethod
    def ListarMusicas(cls):
        if not cls.__musicas:
            print("Nenhuma música cadastrada.")
            return
        for m in cls.__musicas:
            print(m)

    @classmethod
    def AtualizarMusica(cls):
        try:
            i = int(input("ID da Música a atualizar: "))
            for m in cls.__musicas:
                if m.get_id() == i:
                    m.set_titulo(input("Novo Título: "))
                    m.set_artista(input("Novo Artista: "))
                    m.set_album(input("Novo Álbum: "))
                    minu = int(input("Novos Minutos: "))
                    segu = int(input("Novos Segundos: "))
                    m.set_duracao(timedelta(minutes=minu, seconds=segu))
                    print("Música atualizada!")
                    return
            print("Música não encontrada.")
        except ValueError:
            print("Entrada inválida!")

    @classmethod
    def ExcluirMusica(cls):
        try:
            i = int(input("ID da Música a excluir: "))
            for m in cls.__musicas:
                if m.get_id() == i:
                    cls.__musicas.remove(m)
                    cls.__itens = [item for item in cls.__itens if item.get_id_musica() != i]
                    print("Música e seus vínculos removidos!")
                    return
            print("Música não encontrada.")
        except ValueError:
            print("Entrada inválida!")

    @classmethod
    def InserirItem(cls):
        try:
            i = int(input("ID do Item: "))
            ip = int(input("ID da Playlist: "))
            im = int(input("ID da Música: "))
            
            if not any(m.get_id() == im for m in cls.__musicas):
                print("Erro: Música não encontrada!")
                return

            seq = int(input("Sequência na Playlist: "))
            dt = datetime.now()
            cls.__itens.append(PlayListItem(i, ip, im, dt, seq))
            print("Música associada à playlist com sucesso!")
        except ValueError:
            print("Entrada inválida!")

    @classmethod
    def ListarItensPlaylist(cls):
        try:
            ip = int(input("Informe o ID da Playlist: "))
            itens_pl = [item for item in cls.__itens if item.get_id_playlist() == ip]
            if not itens_pl:
                print("Nenhum item nesta playlist.")
                return
            
            mapa_m = {m.get_id(): m for m in cls.__musicas}
            print(f"\n--- Músicas da Playlist {ip} ---")
            for item in sorted(itens_pl, key=lambda x: x.get_sequencia()):
                m = mapa_m.get(item.get_id_musica())
                str_musica = f"{m.get_titulo()} - {m.get_artista()}" if m else "Música removida"
                print(f"Seq {item.get_sequencia()} | {str_musica} | Adicionado em: {item.get_data_inclusao().strftime('%d/%m/%Y')}")
        except ValueError:
            print("ID inválido!")

    @classmethod
    def AtualizarItem(cls):
        try:
            i = int(input("ID do Item a atualizar: "))
            for item in cls.__itens:
                if item.get_id() == i:
                    item.set_sequencia(int(input("Nova Sequência: ")))
                    print("Item atualizado!")
                    return
            print("Item não encontrado.")
        except ValueError:
            print("Entrada inválida!")

    @classmethod
    def ExcluirItem(cls):
        try:
            i = int(input("ID do Item a remover: "))
            for item in cls.__itens:
                if item.get_id() == i:
                    cls.__itens.remove(item)
                    print("Item removido da playlist!")
                    return
            print("Item não encontrado.")
        except ValueError:
            print("Entrada inválida!")

if __name__ == "__main__":
    UI.Main()