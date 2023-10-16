maior_numero_de_filmes = {
    'ator/atriz': None,
    'quantidade': 0
}

def try_parse_float(value):
    try:
        float(value)
        return True
    except:
        return False


with open(r'C:\Users\user\Projetos\CompassUolProgram\Sprint3\Exercícios\Python\actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

    linhas = linhas[1:]

    for linha in linhas:
        campos = linha.strip().split(',')
        ator_ou_atriz = campos[0]
        print(ator_ou_atriz)

        if try_parse_float(campos[1]):
            quantidade_de_filmes = float(campos[2])
        else:
            quantidade_de_filmes = float(campos[3])

        if quantidade_de_filmes > maior_numero_de_filmes['quantidade']:
            maior_numero_de_filmes['ator/atriz'] = ator_ou_atriz
            maior_numero_de_filmes['quantidade'] = quantidade_de_filmes

print(f"O ator/atriz com o maior número de filmes é {maior_numero_de_filmes['ator/atriz']} com {maior_numero_de_filmes['quantidade']} filmes.")
