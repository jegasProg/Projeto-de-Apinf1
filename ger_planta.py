from math import ceil

class Aluno:
	def __init__(self, nome, media, miopia=False, conversador=False):
		self.nome = nome
		self.media = media
		self.miopia = miopia
		self.conversador = conversador

def gerar_planta(alunos):
	if not alunos:
		return []

	ordenados = sorted(alunos, key=lambda aluno: aluno.media)
	conversadores = []
	nao_conversadores = []
	for aluno in ordenados:
		if aluno.conversador:
			conversadores.append(aluno)
		else:
			nao_conversadores.append(aluno)
	grupos = []
	while conversadores and nao_conversadores:
		# Um conversador só partilha o par com um aluno não conversador.
		grupos.append([nao_conversadores.pop(0), conversadores.pop()])
	for aluno in conversadores + nao_conversadores:
		grupos.append([aluno])

	grupos.sort(key=lambda grupo: not any(aluno.miopia for aluno in grupo))

	# Cada lugar é identificado por uma coordenada (fila, coluna), começando em 1.
	lugares = {}
	for indice_grupo, grupo in enumerate(grupos):
		fila = indice_grupo // 3 + 1
		primeira_coluna = (indice_grupo % 3) * 2 + 1
		for deslocamento, aluno in enumerate(grupo):
			lugares[(fila, primeira_coluna + deslocamento)] = aluno

	planta = []
	for numero_fila in range(1, (len(grupos) + 2) // 3 + 1):
		fila = []
		for coluna in range(1, 7):
			fila.append(lugares.get((numero_fila, coluna)))
		planta.append(fila)
	return planta


def mostrar_planta(planta):
	if not planta:
		print("Não há alunos para apresentar.")
		return

	print("\nPlanta da sala (frente da sala na Fila 1):")
	print("       " + " | ".join(f"Col. {n}" for n in range(1, 7)))
	print("       " + " | ".join("------" for _ in range(6)))
	for numero, fila in enumerate(planta, start=1):
		lugares = [aluno.nome if aluno else "—" for aluno in fila]
		print(f"Fila {numero}: " + " | ".join(f"{nome:<6}" for nome in lugares))


def main():
	while True:
		try:
			quantidade = int(input("Número de alunos: "))
			if quantidade < 0:
				raise ValueError
			break
		except ValueError:
			print("Introduza um número inteiro não negativo.")

	alunos = []
	for numero in range(1, quantidade + 1):
		nome = input(f"Nome do aluno {numero}: ").strip() or f"Aluno {numero}"
		while True:
			try:
				media = float(input(f"Média anual de {nome}: ").replace(",", "."))
				if 0 <= media <= 200:
					break
				print("Média inválida. Introduza um valor entre 0 e 200.")
			except ValueError:
				print("Média inválida. Introduza um valor entre 0 e 200.")
		while True:
			resposta = input(f"{nome} tem miopia? (s/n): ").strip().lower()
			if resposta in {"s", "sim", "n", "não", "nao"}:
				break
			print("Resposta inválida. Introduza s ou n.")
		while True:
			conversador = input(f"{nome} é conversador? (s/n): ").strip().lower()
			if conversador in {"s", "sim", "n", "não", "nao"}:
				break
			print("Resposta inválida. Introduza s ou n.")
		alunos.append(Aluno(nome, media, resposta in {"s", "sim"}, conversador in {"s", "sim"}))

	mostrar_planta(gerar_planta(alunos))


if __name__ == "__main__":
	main()
