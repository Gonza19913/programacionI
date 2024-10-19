class Musico:
    def instrumento(self):
        pass

class Guitarrista(Musico):
    def instrumento(self):
        return "Toco la guitarra."

class Baterista(Musico):
    def instrumento(self):
        return "Toco la batería."

musicos = [Guitarrista(), Baterista()]

for musico in musicos:
    print(musico.instrumento())
