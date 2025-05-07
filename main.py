from aluno import Aluno
import questionary
import json
# Lista de alunos cadastrados
alunos = []

def encontrar_aluno(matricula):
    for aluno in alunos:
        if aluno.matricula == matricula:
            return aluno
    return None

while True:
    acao = questionary.select(
        "Escolha uma ação:",
        choices=[
             ("1. Cadastrar aluno"),
             ("2. Lançar nota"),
             ("3. Exibir boletim"),
             ("4. Exibir alunos"),
             ("5. Salvar dados"),
             ("6. Sair")
        ]
    ).ask()

    if acao == "1. Cadastrar aluno":
        nome = input("Nome do aluno: ")
        matricula = input("Matrícula: ")
        curso = questionary.select(
            "Escolha o curso:",
            choices= [
                ("1. Informática"),
                ("2. Edificações"),
                ("3. Administração"),
                ("4. Agropecuária"),
            ]
        ).ask()
        aluno = Aluno(nome, matricula, curso)
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")

    elif acao == "2. Lançar nota":
        matricula = input("Informe a matrícula do aluno: ")
        aluno = encontrar_aluno(matricula)
        if aluno.curso == "1. Informática":
            disciplina = questionary.select(
                "Escolha uma matéria",
                choices= [
                    ("Sistemas Operacionais"),
                    ("Programação WEB"),
                    ("Programação Orientada a Objetos"),
                    ("Gestão de Startups"),
                    ("Noções de Robótica"),
                ]
            ).ask()
            nota = float(input("Nota: "))
            if(nota < 0 or nota > 10):
                print("Nota inválida!")
                break
            else:
                aluno.adicionar_nota(disciplina, nota)
                print("Nota lançada com sucesso!")
        elif aluno.curso == "2. Edificações":
            materias = questionary.select(
                "Escolha uma matéria",
                choices = [
                    ("Matéria 1"),
                    ("Matéria 2"),
                    ("Matéria 3"),
                    ("Matéria 4"),
                    ("matéria 5")
                ]
            ).ask()
            nota = float(input("Nota: "))
            if(nota < 0 or nota > 10):
                print("Nota inválida!")
                break
            else:
                aluno.adicionar_nota(disciplina, nota)
                print("Nota lançada com sucesso!")
        elif curso == "3. Administração":
            materias = questionary.select(
                "Escolha uma matéria",
                choices= [
                    ("Matéria 1"),
                    ("Matéria 2"),
                    ("Matéria 3"),
                    ("Matéria 6"),
                    ("Matéria 5")
                ]
            ).ask()
            nota = float(input("Nota: "))
            if(nota < 0 or nota > 10):
                print("Nota inválida!")
                break
            else:
                 aluno.adicionar_nota(disciplina, nota)
                 print("Nota lançada com sucesso!")
        elif curso == "4. Agropecuária":
            materias = questionary.select(
                "Escolha a matéria",
                choices= [
                    ("Matéria 1"),
                    ("Matéria 2"),
                    ("Matéria 3"),
                    ("Matéria 4"),
                    ("Matéria 5")
                ]
            )
            nota = float(input("Nota: "))
            if(nota < 0 or nota > 10):
                print("Nota inválida!")
                break
            else:
                aluno.adicionar_nota(disciplina, nota)
                print("Nota lançada com sucesso!")
        else:
            print("Aluno não encontrado.")

    elif acao == "3. Exibir boletim":
        matricula = input("Informe a matrícula do aluno: ")
        aluno = encontrar_aluno(matricula)
        if aluno:
            aluno.exibir_boletim()
        else:
            print("Aluno não encontrado.")
    elif acao == "4. Exibir alunos":
        if (len(alunos) == 0 ):
            print("Nenhum aluno cadsatrado.")
        else:
            print("Alunos cadastrados:")
            for aluno in alunos:
                print (f"Nome: {aluno.nome} | Matrícula: {aluno.matricula} | Curso: {aluno.curso} \n")
                print("---"*15)

    elif acao == "5. Salvar dados":
        nome_arquivo = input("Digite o nome do arquivo (com .json no final): ")
        alunos_serializaveis = [aluno.__dict__ for aluno in alunos]

        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(alunos_serializaveis, arquivo, indent=4, ensure_ascii=False)

    elif acao == "6. Sair":
        print("Saindo do sistema...")
        break
