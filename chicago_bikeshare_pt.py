# coding: utf-8
# Começando com os imports
# Projeto 1 - Curso FDSI
# Autor: Ricardo Albuquerque - Brasília-DF
import csv
import matplotlib.pyplot as plt
#from functools import reduce

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

def imprimir_amostras(lista):
    """
    Função imprimir_amostras
          Finalidade: Receber uma lista e gera uma impressão do conteúdo dela.

          Argumentos:
              lista: Lista a ser impressa
          Retorna:
              None.
    """
    nr_linha = 0
    for linha in lista:
        nr_linha += 1
        print("linha {0}: {1}".format(nr_linha, linha))

# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
#imprimir_amostras(1,21,0)
imprimir_amostras(data_list[1:21])
# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras para gênero")
nova_lista = list(genero[6] for genero in data_list[:20]) #Expressão geradora
imprimir_amostras(nova_lista)
# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
# Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
def column_to_list(lista, index):
    """
    Função column_to_list
          Finalidade: Receber uma lista e um índice para que seja gerada uma nova lista pelo index referenciado.

          Argumentos:
              lista: Lista com todas as features
              index: Índice para ser a referência da nova lista a ser gerada
          Retorna:
              column_list: Lista com a feature referenciada
    """
    column_list = []
    for perfil in lista:
        column_list.append(perfil[index])

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
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
def contador_genero(lista):
    """
    Função contador_genero
          Finalidade: Receber uma lista e contabilizar por gênero. Utiliza-se de duas variáveis cujo
                      escopo é global, então, necessário se faz declará-las, aqui, com a palavra
                      reservada "global".

          Argumentos:
              lista: Lista com todas as features
          Retorna:
              Uma lista com o total para male, em primeiro e, em segundo, total para female.
    """
    global male, female
    
    for genero in lista:
        if genero == "Male":
            male += 1
        elif genero == "Female":
            female += 1
            
    return [male, female]
            
contador_genero(genero[6] for genero in data_list) #Expressão geradora

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(lista):
    """
    Função count_gender
          Finalidade: Receber uma lista e contabilizar por gênero. Utiliza-se de duas variáveis (male e female, ambas locais).

          Argumentos:
              lista: Lista com todas as features
          Retorna:
              Uma lista com o total para male, em primeiro e, em segundo, total para female.
    """
    male = 0
    female = 0
    for genero in lista:
        if genero[-2] == "Male":
            male += 1
        elif genero[-2] == "Female":
            female += 1
            
    return [male, female]
    
print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list)) #Expressão geradora

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(lista):
    """    
    Função most_popular_gender
          Finalidade: Receber uma lista e realizar a contagem para cada gênero de pessoa. Para isso,
                      uma função (count_gender) será chamada para que seja retornada uma lista composta por totais do 
                      gênero "masculino" e gênero "feminino". De posse dessa nova lista, essa função irá
                      compará-los para, então, indicar qual o gênero obteve maior ocorrência na lista primária.
                      Ao final, um literal será retornado para indicar qual o gênero obteve maior
                      frequência.

          Argumentos:
              data_list: Lista com todas as features
          Retorna:
              answer: Atributo que terá o gênero de maior ocorrência .    
    """
    answer = "Equal"
    
    lista_male_female = count_gender(lista)
    if lista_male_female [0] < lista_male_female [1]:
        answer = "Female"
    elif lista_male_female [0] > lista_male_female [1]:
        answer = "Male"
    
    return answer

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
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

def count_user_type(lista, user_type_list):
    """    
    Função count_user_type
          Finalidade: Receber uma lista com várias features e separar a feature "user_type_list" para
                      contabilizar as ocorrências para cada "user_type". Faz-se uma seleção por
                      user_type para realizar a contagem por esse atributo. Ao final, retornar uma
                      lista que irá conter o total de ocorrência para cada "user_type".

          Argumentos:
              lista: Lista com todas as features
              user_type_list: Lista com os tipos existentes de data_list para que se possa
                              realizar a contagem por esses tipos.
          Retorna:
              answer: Uma lista com os totais por user_type .    
    """

    user_lista = column_to_list(lista, -3)
    
    contador0 = 0
    contador1 = 0
    contador2 = 0
    
    for user_type in user_lista:
        if user_type == user_type_list[0]:
            contador0 += 1
        elif user_type == user_type_list[1]:
            contador1 += 1
        elif user_type == user_type_list[2]:
            contador2 += 1
    
    return [contador0, contador1, contador2]
        
user_type_lista = list(set(column_to_list(data_list, -3)))
print("\nTAREFA 7: Verifique o gráfico!")
print("\nLista para User Type: ", user_type_lista)
print("\n{0}: {1}".format(user_type_lista[0], count_user_type(data_list, user_type_lista)[0]))
print("\n{0}: {1}".format(user_type_lista[1], count_user_type(data_list, user_type_lista)[1]))
print("\n{0}: {1}".format(user_type_lista[2], count_user_type(data_list, user_type_lista)[2]))

types = user_type_lista
quantity = count_user_type(data_list, user_type_lista)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('User type')
plt.xticks(y_pos, types)
plt.title('Quantidade por User type')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque não foram contabilizados os gêneros em branco."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua própria resposta!.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().

def monta_lista(lista, index):
    """    
    Função monta_lista
          Finalidade: Receber uma lista e separar a feature por, também, um índice recebido.
                      De posse desse índice, gerar uma nova lista que irá conter somente uma feature com
                      suas respectivas ocorrências.

          Argumentos:
              lista: Lista com todas as features
              index: Índice que referencia a feature a ser extraída de data.
          Retorna:
              nova_lista: Uma lista com o tempo expresso em tipo inteiro utilizado pelo usuário no trajeto inicial e final com
              o uso da bicicleta locada.
    """
    
    nova_lista = []
    for tempo in lista:
        if tempo[index]!="":
            nova_lista.append(int(tempo[index]))

    return nova_lista

def somar_viagem(lista):
    """    
    Função somar_viagem
          Finalidade: Receber uma lista e realiza a soma de seus elementos e retorna o valor desse somatório.
          
          Argumentos:
              lista: Lista com todas a feature tempo de viagem
          Retorna:
              soma: O somatório do tempo de viagem.
    """    
    soma = 0
    for viagem in lista:
        soma += viagem
        
    return soma

trip_duration_list = monta_lista(data_list, 2)
trip_duration_list.sort()
min_trip = trip_duration_list[0]
max_trip = trip_duration_list.pop()
mean_trip = somar_viagem(trip_duration_list)/len(trip_duration_list)
"""
mean_trip = reduce(lambda x,y: x+y, trip_duration_list)/len(trip_duration_list)
-------------------------------------------------------------------------------
                                      ^
                                      |
                                      |
Essa técnica com uma função anônima(lambda) funcion
ou bem, mas segundo o meu revisor, devo utilizar 
uma função de usuário (somar_viagem) para realizar o somatório total do tempo de percurso.
"""
if (len(trip_duration_list)%2) != 0:
    median_trip = trip_duration_list[round(len(trip_duration_list)/2)]
else:
    median_trip = (trip_duration_list[int(len(trip_duration_list)/2)] + 
                  trip_duration_list[int(len(trip_duration_list)/2+1)]) / 2

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
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.
"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    """    
    Função count_items
          Finalidade: Receber uma lista com várias features e separar a feature "user_type" para
                      contablizá-las. Ao final, retornar duas listas: uma que irá conter os
                      tipos existentes e a outra o total de ocorrência para cada tipo.
                      
          Argumentos:
              column_list: Lista com a feature selecionada, no caso o tipo de usuário.
          Retorna:
              item_types: Tipos de usuário existentes na lista column_list.
              count_types: totais por tipo de usuário constante da lista column_list.
    """
    
    lista_temp = column_to_list(data_list, -3)
    item_types = list(set(lista_temp))
    count_items = []
    for item in item_types:
        count_items.append(lista_temp.count(item))
        
    print(item_types)
    print(count_items)

    return item_types, count_items

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------