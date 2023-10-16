total_receita_bruta = 0.0
total_filmes = 0

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

        if try_parse_float(campos[5]):
            receita_bruta = float(campos[5])
        else:                  
            receita_bruta = float(campos[6])

        total_receita_bruta += receita_bruta

print(total_receita_bruta)

media_receita_bruta = total_receita_bruta / len(linhas)

print(f"A média de receita bruta dos principais filmes é de ${media_receita_bruta:.2f} milhões de dólares.")
