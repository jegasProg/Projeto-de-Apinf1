import random
import math

class Alunos:
    def __init__(self, nome, dupla, coluna_na_dupla, linha, media, caracteristicas=None):
        self.nome = nome
        self.dupla = dupla
        self.coluna_na_dupla = coluna_na_dupla
        self.linha = linha
        self.media = media
        self.caracteristicas = caracteristicas if caracteristicas else []


def obter_dados_turma():
    while True:
        try:
            alunos_na_turma = int(input("Quantos alunos tem a turma? "))
            if alunos_na_turma > 0:
                break
            print("A turma deve ter pelo menos um aluno.")
        except ValueError:
            print("Introduza um número inteiro válido e maior que zero.")

    alunos = []
    for numero in range(1, alunos_na_turma + 1):
        nome = input("Nome: ").strip()
        while not nome:
            nome = input("O nome não pode ficar vazio. Nome: ").strip()

        while True:
            try:
                media = float(input("Média (0 a 20): ").replace(",", "."))
                if 0 <= media <= 20:
                    break
                print("A média deve estar entre 0 e 20.")
            except ValueError:
                print("Introduza uma média numérica válida entre 0 e 20.")

        dificuldades = input(
            "Características/dificuldades (separadas por vírgulas; Enter se não houver): "
        )
        caracteristicas = []
        for i in dificuldades.split(","):
            caracteristica = i.strip()
            if caracteristica:
                caracteristicas.append(caracteristica)
        alunos.append(Alunos(nome, None, None, None, media, caracteristicas))

    return alunos


def tem_miopia(aluno):
    texto = " ".join(aluno.caracteristicas).lower()
    return "miopia" in texto or "míope" in texto


def atribuir_lugares(turma):
    """Emparelha a menor média com a maior, a segunda menor com a segunda maior, etc."""
    numero_colunas = 6
    numero_filas = math.ceil(len(turma) / numero_colunas)

    for aluno in turma:
        aluno.linha = None
        aluno.coluna_na_dupla = None
        aluno.dupla = None

    ordenados = sorted(turma, key=lambda aluno: aluno.media)
    maiores = list(reversed(ordenados))

    # A formação dos pares é feita explicitamente do pior para o melhor:
    # 2 fica com 20, 4 fica com 18, e assim sucessivamente.
    pares = []
    for indice, aluno_pior in enumerate(ordenados):
        aluno_melhor = maiores[indice]
        if aluno_pior is aluno_melhor:
            pares.append([aluno_pior])
        elif not any(aluno_melhor in par for par in pares):
            pares.append([aluno_pior, aluno_melhor])

    lugares_ocupados = set()

    # Coloca até seis alunos com miopia na fila da frente.
    coluna = 0
    for par in pares:
        if coluna >= numero_colunas:
            break
        aluno_miopia = next((aluno for aluno in par if tem_miopia(aluno)), None)
        if aluno_miopia is not None:
            aluno_miopia.linha = 0
            aluno_miopia.coluna_na_dupla = coluna
            aluno_miopia.dupla = coluna + 1
            lugares_ocupados.add((0, coluna))

            for parceiro in par:
                if parceiro is not aluno_miopia:
                    parceiro.linha = 1
                    parceiro.coluna_na_dupla = coluna
                    parceiro.dupla = coluna + 1
                    lugares_ocupados.add((1, coluna))
            coluna += 1

    # Coloca os pares restantes na mesma coluna, em filas consecutivas.
    for par in pares:
        if all(aluno.linha is not None for aluno in par):
            continue

        coluna = next(
            (c for c in range(numero_colunas)
             if all((fila, c) not in lugares_ocupados for fila in range(numero_filas))),
            None,
        )
        if coluna is None:
            for c in range(numero_colunas):
                if all(aluno.coluna_na_dupla != c for aluno in par if aluno.coluna_na_dupla is not None):
                    coluna = c
                    break

        if coluna is None:
            continue

        for aluno in par:
            if aluno.linha is not None:
                continue
            for fila in range(1, numero_filas):
                lugar = (fila, coluna)
                if lugar not in lugares_ocupados:
                    aluno.linha = fila
                    aluno.coluna_na_dupla = coluna
                    aluno.dupla = coluna + 1
                    lugares_ocupados.add(lugar)
                    break

    # Caso excepcional de turma sem lugar restante, completa a grelha.
    for fila in range(numero_filas):
        for c in range(numero_colunas):
            lugar = (fila, c)
            if lugar in lugares_ocupados:
                continue
            aluno = next((a for a in turma if a.linha is None), None)
            if aluno is not None:
                aluno.linha = fila
                aluno.coluna_na_dupla = c
                aluno.dupla = c + 1
                lugares_ocupados.add(lugar)


def mostrar_planta(turma):
    print("\nPLANTA DA SALA (vista da frente para trás)")
    print("Frente da sala")

    numero_filas = math.ceil(len(turma) / 6)
    for fila in range(numero_filas):
        lugares = [None] * 6
        for aluno in turma:
            if aluno.linha == fila:
                lugares[aluno.coluna_na_dupla] = aluno

        texto = []
        for lugar in lugares:
            if lugar is None:
                texto.append("[Lugar vazio]")
            else:
                texto.append(f"[{lugar.nome}]")
        print(f"Fila {fila + 1}: {'  |  '.join(texto)}")

    sem_lugar = [aluno for aluno in turma if aluno.linha is None]
    if sem_lugar:
        print("Sem lugar atribuído:", ", ".join(aluno.nome for aluno in sem_lugar))


if __name__ == "__main__":
    turma = obter_dados_turma()
    atribuir_lugares(turma)

    for aluno in turma:
        caracteristicas = ", ".join(aluno.caracteristicas) or "Nenhuma indicada"
        print(f"{aluno.nome} | Média: {aluno.media:g} | Características/dificuldades: {caracteristicas}")

    mostrar_planta(turma)
