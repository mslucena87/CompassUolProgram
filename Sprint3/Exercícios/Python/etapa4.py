from collections import defaultdict
import operator

contagem_filmes = defaultdict(int)

with open(r'C:\Users\user\Projetos\CompassUolProgram\Sprint3\Exercícios\Python\actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

    linhas = linhas[1:]

    for linha in linhas:
        campos = linha.strip().split(',')
        filme = campos[4] 
        contagem_filmes[filme] += 1

contagem_filmes_ordenada = dict(sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0])))

with open('resultado.txt', 'w') as arquivo_saida:
    for i, (filme, quantidade) in enumerate(contagem_filmes_ordenada.items(), start=1):
        arquivo_saida.write(f"{i} - O filme '{filme}' aparece {quantidade} vez(es) no dataset.\n")

print("Resultados escritos no arquivo 'resultado.txt'.")
