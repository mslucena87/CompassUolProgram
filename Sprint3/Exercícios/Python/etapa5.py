atores_e_receitas = []

with open(r'C:\Users\user\Projetos\CompassUolProgram\Sprint3\Exercícios\Python\actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

    linhas = linhas[1:]

    for linha in linhas:
        campos = linha.strip().split(',')
        ator = campos[0]
        receita_bruta_str = campos[1]

        try:
            receita_bruta = float(receita_bruta_str)
        except ValueError:
            print(f"Valor inválido encontrado: {receita_bruta_str}. Linha ignorada.")
            continue

        atores_e_receitas.append((ator, receita_bruta))

atores_e_receitas_ordenados = sorted(atores_e_receitas, key=lambda x: x[1], reverse=True)

with open('resultado2.txt', 'w') as arquivo_saida:
    for ator, receita in atores_e_receitas_ordenados:
        arquivo_saida.write(f"{ator} - ${receita:.2f} milhões\n")

print("Resultados escritos no arquivo 'resultado2.txt'.")


