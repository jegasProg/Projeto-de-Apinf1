import random

class Alunos:
    def __init__(self, nome, coluna, linha, caracteristicas=None):
        self.nome = nome
        self.coluna = coluna
        self.linha = linha
        self.caracteristicas = caracteristicas if caracteristicas else []

    def mostrar_posição(self):
        return f"O {self.nome} está na fila {self.coluna} e coluna {self.linha}(dificuldades: {self.caracteristicas})"

Turma = []
numero_de_alunos = int(input("Numero de alunos na turma"))
tamanho_da_linha = (numero_de_alunos + 5) / 6
dados_alunos = []

lugares_disponiveis = []
for linha in range(1, round(tamanho_da_linha) + 1):
    for coluna in range(1, 7):
        lugares_disponiveis.append((linha, coluna))

random.shuffle(lugares_disponiveis)

for i in range(numero_de_alunos):
    nome = input("Nome do aluno:  ")
    resposta = input("Dificuldades do seu aluno separado por (,) ou pressione enter para continuar sem dificuldades.").lower().split(",")
    dados_alunos.append((nome, resposta))

    # coluna_aleatoria, linha_aleatoria = lugares_disponiveis.pop()
    # novo_aluno = Alunos(nome, coluna_aleatoria, linha_aleatoria, resposta)
    # Turma.append(novo_aluno)

lugares_frente = []
lugares_laterais = []

for lugares in lugares_disponiveis:
    if lugares[0] == 1:
        lugares_frente.append(lugares)
    elif lugares[1] in (1, 6):
        lugares_laterais.append(lugares)

alunos_sem_lugar = []

for nome, dificuldades in dados_alunos:
    texto_junto = " ".join(dificuldades)
    if ("miopia" in texto_junto or "audição" in texto_junto) and lugares_frente:
        lugar = lugares_frente.pop()
        lugares_disponiveis.remove(lugar)
        Turma.append(Alunos(nome, lugar[0], lugar[1], dificuldades))
    
    elif "autismo" in texto_junto and lugares_laterais:
        lugar = lugares_laterais.pop()
        lugares_disponiveis.remove(lugar)
        Turma.append(Alunos(nome, lugar[0], lugar[1], dificuldades))

    else:
        alunos_sem_lugar.append((nome, dificuldades))

for nome, dificuldades in alunos_sem_lugar:
    lugar = lugares_disponiveis.pop()
    Turma.append(Alunos(nome, lugar[0], lugar[1], dificuldades))

print("---Planta---")
for alunos in Turma:
    print(alunos.mostrar_posição())