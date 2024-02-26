from sys import displayhook
import pandas as pd
import plotly.express as px

 # Passo 1º Importar base de dados
      # Detalhes do codigo anterior -> Usei a letra "r" antes do caminho do arquivo por que o vscode interpretou o \ como outra coisa além do caminho do arquivo.
      # , encoding='latin1' -> Escrevi esse código para não dar erro na leitura de caracteres especiais.
tabela = pd.read_csv(r'C:\Users\dougl\Developer Projects\2 - Analise do por que varios clientes estao cancelando o cartão de credito\ClientesBanco.csv', encoding='latin1')


# Passo 2º Vizualizar e tratar essa base de dados.
      # .drop -> é usado para retirar uma informação de uma tabela.
      # axis=() -> o eixo (axis = 0 se for uma linha, axis = 1 se for uma coluna).
# Aqui eu exclui uma coluna inutil, ela tinha as informações do ID dos clientes, ou seja, inutil para essa analise.
tabela = tabela.drop("CLIENTNUM", axis=1)
displayhook(tabela)


# Passo 3º Olhar as informações da tabela.
            # tabela.dropna() -> exclui do display as linhas que estão com informações vazias
# Aqui eu exclui uma linha que estava faltando informação em alguma coluna.
tabela = tabela.dropna()


            # tabela.info() -> me retorna informação de todas as categorias das colunas e me fala quantas linhas tem e o Dtype delas
displayhook(tabela.info())


            # tabela.describe() -> me retorna informação de:
                  # 1. (count) -> A quantidade de linhas analisadas 
                   # 2. (mean) -> A média
                    # 3. (std) -> O desvio padrão
                     # 4. (min) -> O minimo
                      # 5. (%) -> A porcentagem (25% tem 41 anos de idade ou menos)
                        # 6. (max) -> O máximoda
            # .round() -> esse código me permite escolher a quantide de casas decimais eu quero que apareça.
displayhook(tabela.describe().round(1))


            # tabela ['titulo da coluna'] -> me permite receber somente informação daquela coluna.
              # .value_counts() -> resume as informações da coluna.
qtde_categoria = tabela ['Categoria'].value_counts()
displayhook(qtde_categoria)


            # normalize = True -> Isso aqui me permite vizualizar a porcentagem, o quanto daquilo representa em comparação ao todo.
qtde_categoria_perc = tabela ['Categoria'].value_counts(normalize = True)
displayhook(qtde_categoria_perc)


   # Passo 4º Temos várias formas de descobrir o motivo do cancelamento.
      # ---> Podemos olhar a comparação entre Clientes x Cancelados de cada uma das nossas colunas da base de dados
      # for 'x' in 'y' ---> O que eu disse para o python aqui? Para cada coluna na minha tabela, execute esse código. No python, o for sempre ira percorrer as colunas, se você quiser que ele leia as colunas você precisa colocar o seguinte código: for linhas in tabela.index:
      # plotly.express -> O que essa biblioteca faz? ela gera gráficos. Você ira colocar a fonte de dados (tabela), o eixo y vai ser minhas colunas da base de dados, e o eixo x vai ser as informações da base de dados que será usado como comparativo.
      # a parte for COLUNA in tabela, a COLUNA vira o nome de cada coluna da tabela, já que se não alterado o for le as colunas ao invés das linhas.
for coluna in tabela:
      grafico = px.histogram(tabela, x=coluna, color='Categoria')
      grafico.show()


   # Passo 5º Para finalizar o processo o que será feito? Analisar os padrões dos cancelados e dos não cancelados.