maior_media_receita = {
    'ator/atriz': None,
    'media_receita': 0.0
}

with open(r'C:\Users\user\Projetos\CompassUolProgram\Sprint3\Exercícios\Python\actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

    linhas = linhas[1:]

    for linha in linhas:
        campos = linha.strip().split(',')
        ator_ou_atriz = campos[0]
        media_receita = float(campos[3])  

        if media_receita > maior_media_receita['media_receita']:
            maior_media_receita['ator/atriz'] = ator_ou_atriz
            maior_media_receita['media_receita'] = media_receita

print(f"O ator/atriz com a maior média de receita de bilheteria bruta por filme é {maior_media_receita['ator/atriz']} com uma média de ${maior_media_receita['media_receita']:.2f} milhões de dólares por filme.")
