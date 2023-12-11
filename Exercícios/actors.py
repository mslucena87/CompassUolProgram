import pandas as pd

nome_arquivo = r'C:\Users\user\Projetos\CompassUolProgram\Sprint7\Exercícios\actors.csv'
data_frame = pd.read_csv(nome_arquivo)

# print(data_frame)

ator_com_mais_filmes = data_frame.loc[data_frame['Number of Movies'].idxmax()]['Actor']
numero_de_filmes = data_frame['Number of Movies'].max()

print(f'O ator/atriz com mais filmes é {ator_com_mais_filmes}, com {numero_de_filmes} filmes.')

media_numero_filmes = data_frame['Number of Movies'].mean()

print(f'A média da coluna "Number of Movies" é: {media_numero_filmes:.2f}.')

ator_com_maior_media = data_frame.loc[data_frame['Average per Movie'].idxmax()]['Actor']

print(f'O ator/atriz com a maior média por filme é {ator_com_maior_media}.')

frequencia_filmes = data_frame['#1 Movie'].value_counts()
filme_mais_frequente = frequencia_filmes.idxmax()
frequencia_mais_frequente = frequencia_filmes.max()

print(f'O filme mais frequente é "{filme_mais_frequente}" com uma frequência de {frequencia_mais_frequente}.')
# ator_com_mais_filmes = dados['Actor'].value_counts().idxmax()
# numero_de_filmes = dados['Number of Movies'].value_counts().max()
# print(f'O ator/atriz com mais filmes é {ator_com_mais_filmes}, com {numero_de_filmes} filmes.')


# media_filmes = dados['Number of Movies'].mean()
# print(f'A média da coluna "Número de Filmes" é {media_filmes}.')


# media_por_filme = dados.groupby('Actor')['Number of Movies'].mean()
# ator_maior_media_por_filme = media_por_filme.idxmax()
# maior_media_por_filme = media_por_filme.max()
# print(f'O ator/atriz com a maior média por filme é {ator_maior_media_por_filme}, com uma média de {maior_media_por_filme} filmes por participação.')


# filmes_mais_frequentes = dados['#1 Movie'].value_counts()
# filme_mais_frequente = filmes_mais_frequentes.idxmax()
# frequencia_filme_mais_frequente = filmes_mais_frequentes.max()
# print(f'O filme mais frequente é "{filme_mais_frequente}" com uma frequência de {frequencia_filme_mais_frequente}.')




