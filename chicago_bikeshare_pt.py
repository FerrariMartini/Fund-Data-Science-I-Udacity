# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for line in data_list[0:20]:
    print(line)

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for gender in data_list[0:20]:
    print(gender[6])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, 
# na mesma ordem
def column_to_list(data, index):
    """ Essa função cria uma lista com elementos de uma coluna (nesse caso a coluna de genero)
    do arquivo data_list atráves de um loop de repetição onde cada elemento da coluna é 
    lido e transferido para a lista column_list.
INPUT: 
    - data: dados do data_list que são importados de um arquivo csv
    - index: é a coluna do arquivo data_list que possui os dados a serem lidos
OUTPUT:
- column_list: uma lista com os elementos (male ou female) transferidos pelo loop de repetição
"""

    column_list = []
    
    for i in data:
        column_list.append(i[index])
    # Dica: Você pode usar um for para iterar sobre as amostras, 
    # pegar a feature pelo seu índice, e dar append para uma lista
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) 
# e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para TODO isso.
male = 0
female = 0
for gender in data_list:
    if gender[6] == "Male":
        male += 1
    elif gender[6] == "Female":
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para TODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """ Realizar contagem de cada elemento distinto da coluna genero do arquivo data_list atráves
    de um loop de repetição e de um estrutura de decisão que analisa cada elemento e realiza sua soma se forem igual.
INPUT: 
    - data_list: dados que são importados de um arquivo csv
OUTPUT:
    - male: somatório dos elementos male transferidos e somados pelo loop de repetição
    - female: somatório dos elementos female transferidos e somados pelo loop de repetição
"""
    male = 0
    female = 0
    for gender in data_list:
        if gender[6] == "Male":
            male += 1
        elif gender[6] == "Female":
            female += 1

    return [male, female]

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """ Por meio de uma estrutura de decisão realiza a comparação de maior e menor entre os valores de
    saída da função count_gender e retorna o maior valor (TRUE) representado por uma string.
INPUT: 
    - data_list: dados que são importados de um arquivo csv
OUTPUT:
    - answer: o maior valor encontrado depois da comparação de valores, sua representação é uma string.  
"""
    answer = ""
    
    if count_gender(data_list)[0] > count_gender(data_list)[1]:
        answer = "Masculino"
    elif count_gender(data_list)[0] < count_gender(data_list)[1]:
        answer = "Feminino"
    else:
        answer = "Igual"
    
    return answer

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)


input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
def count_user_type(data_list):
    """ Realizar contagem de cada elemento distinto da coluna user_type do arquivo data_list atráves
    de um loop de repetição e de um estrutura de decisão que analisa cada elemento e realiza 
    sua soma se forem igual.
INPUT: 
    - data_list: dados que são importados de um arquivo csv
OUTPUT:
    - subscriber: somatório dos elementos subscriber transferidos e somados pelo loop de repetição
    - customer: somatório dos elementos customer transferidos e somados pelo loop de repetição
    - others: somatório dos elementos others transferidos e somados pelo loop de repetição
"""
    subscriber = 0
    customer = 0
    others = 0
    for ut in data_list:
        if ut[-3] == "Subscriber":
            subscriber += 1
        elif ut[-3] == "Customer":
            customer += 1
        else:
            others += 1
    
    return [subscriber, customer, others]
    
print("\nTAREFA 7: Imprimindo o resultado de Tipo de Usuários")
print(count_user_type(data_list))

user_type = column_to_list(data_list, -3)
types = ["Subscriber", "Customer", "Others"]
quantity = count_user_type(data_list) 
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque no universo total de usuários que usam o serviço de bikeshare (data_list) existem cadastro de usuários que não possuem a informação de genero. Quanto realizamos a contagem na função def count_gender estão coletando apenas os generos declarados, ou seja, apenas male e female excluindo os cadastros vazios.\n"
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. 
# Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para TODO isso, como max() e min().

trip_duration_list = column_to_list(data_list, 2)
tdl_num = []

for num in trip_duration_list:
    tdl_num.append(int(num))

tdl_num = sorted(tdl_num)

min_trip = tdl_num[0]
max_trip = tdl_num[-1]
mean_trip = round(sum(tdl_num)/len(tdl_num))
median_trip = 0.

if len(tdl_num) % 2 == 0:
    p1 = tdl_num[round(len(tdl_num)//2) - 1]
    p2 = tdl_num[len(tdl_num)//2]
    median_trip = (p1 + p2)/2
else:
    median_trip = tdl_num[round(len(tdl_num)//2)]

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? 
# Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. 
# Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#    """
#      Função de exemplo com anotações.
#      Argumentos:
#          param1: O primeiro parâmetro.
#          param2: O segundo parâmetro.
#      Retorna:
#          Uma lista de valores x.
#
#      """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"
print(answer)

def count_items(column_list):
    item_types = []
    count_items = []

    item_types =  len(set(column_list))
    count_items = len(column_list)
             
    return item_types, count_items

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------

