class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = {}  # chave: disciplina, valor: lista de notas

    def adicionar_nota(self, disciplina, nota):
        if disciplina not in self.notas:
            self.notas[disciplina] = []
        self.notas[disciplina].append(nota)

    def calcular_media(self, disciplina):
        if disciplina in self.notas and len(self.notas[disciplina]) > 0:
            return sum(self.notas[disciplina]) / len(self.notas[disciplina])
        return 0

    def exibir_boletim(self):
        print(f"\n--- Boletim de {self.nome} ---")
        for disciplina, notas in self.notas.items():
            media = self.calcular_media(disciplina)
            print(f"{disciplina}: {notas} | Média: {media:.2f}")
        print("--------------------------")