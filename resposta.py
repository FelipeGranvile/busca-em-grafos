import networkx as nx
import random
import matplotlib.pyplot as plt
import time

# Função para gerar grafos não direcionados com todos os vértices conectados
def gerarGrafosConectados(opcaoGrafo, numArestas, numVertices):
    
    if opcaoGrafo == 1 and numArestas > numVertices * (numVertices - 1):
        raise ValueError("Número de arestas excede o máximo permitido para grafos direcionados.")
    elif opcaoGrafo == 2 and numArestas > (numVertices * (numVertices - 1)) // 2:
        raise ValueError("Número de arestas excede o máximo permitido para grafos não direcionados.")
    
    if opcaoGrafo == 1:
        GD = nx.DiGraph()
        GD.add_nodes_from(range(numVertices))

        # Passo 1: Conectar todos os vértices com um caminho direcionado
        for i in range(numVertices - 1):
            GD.add_edge(i, i + 1)  # Conectando vértices consecutivos

        # Passo 2: Adicionar arestas aleatórias para garantir maior conectividade
        while len(GD.edges) < numArestas:
            u = random.randint(0, numVertices - 1)
            v = random.randint(0, numVertices - 1)
            if u != v and not GD.has_edge(u, v):
                GD.add_edge(u, v)
        
        return GD
    else:
        G = nx.Graph()
        G.add_nodes_from(range(numVertices))

        # Passo 1: Conectar todos os vértices com um caminho não direcionado
        for i in range(numVertices - 1):
            G.add_edge(i, i + 1)  # Conectando vértices consecutivos

        # Passo 2: Adicionar arestas aleatórias para garantir maior conectividade
        
        while len(G.edges) < numArestas:
            u = random.randint(0, numVertices - 1)
            v = random.randint(0, numVertices - 1)
            if u != v and not G.has_edge(u, v):
                G.add_edge(u, v)
                G.add_edge(v, u)
        
        return G

# Gerando o grafo não direcionado com 10 vértices e 15 arestas
G = gerarGrafosConectados(2, 200, 100)



source = int(input("nó inicial: "))
print(source)

# Busca em largura para arestas e visitação de nós
start_time = time.perf_counter()

busca_largura_arestas = list(nx.bfs_edges(G, source))
end_time = time.perf_counter()

tempo_total_busca_largura = end_time - start_time


nos_visitados_largura = set()
busca_largura_visitacao = []

for u, v in busca_largura_arestas:
    if u not in nos_visitados_largura:
        busca_largura_visitacao.append(u)
        nos_visitados_largura.add(u)
    if v not in nos_visitados_largura:
        busca_largura_visitacao.append(v)
        nos_visitados_largura.add(v)



# Árvore gerada pela BFS
arvore_gerada_BFS = nx.bfs_tree(G, source)

# Exibindo as ordens de visitação e a árvore gerada
print("Arestas da de largura:", busca_largura_arestas)
print("Ordem de visitação dos nós pela BFS:", busca_largura_visitacao)
print ("Tempo gasto: ", tempo_total_busca_largura)
#print("Ordem de visitação das arestas pela BFS:", busca_largura_arestas)
#print("Árvore gerada pela BFS:", list(arvore_gerada_BFS.edges))


""""
# Criando o layout para os dois gráficos no mesmo quadro
fig, axs = plt.subplots(3, 1, figsize=(15, 15))  # 3 linhas, 1 coluna

# 1º gráfico: Plotando o grafo original
axs[0].set_title("Grafo Original")
pos = nx.spring_layout(G)  # Layout para o grafo original
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=10, font_weight='bold', edge_color='gray', ax=axs[0])

# 2º gráfico: Plotando a árvore gerada pela BFS
axs[1].set_title("Árvore Gerada pela BFS")
pos = nx.spring_layout(arvore_gerada_BFS)  # Layout para a árvore
nx.draw(arvore_gerada_BFS, pos, with_labels=True, node_color='lightgreen', node_size=1000, font_size=10, font_weight='bold', edge_color='orange', ax=axs[1])

# 3º gráfico: Exibindo a ordem de visitação dos nós
axs[2].axis('off')  # Desliga os eixos do gráfico
axs[2].text(0.5, 0.5, f'Ordem de visitação dos nós: {busca_largura_visitacao}', ha='center', va='center', fontsize=12, bbox=dict(facecolor='skyblue', alpha=0.5))

# Ajustando o layout para garantir que os gráficos não se sobreponham
plt.tight_layout()

# Exibindo os gráficos
plt.show()

"""


# parte da busca por profundidade

start_time_profundidade = time.perf_counter()
busca_profundidade_arestas = list(nx.dfs_edges(G, source))
end_time_profundiade = time.perf_counter()
tempo_total_busca_profundidade = end_time_profundiade - start_time_profundidade

print("Arestas da profundidade: ", busca_profundidade_arestas)

nos_visitados_profundidade = set()
busca_profundidade_visitacao = []

for u, v in busca_profundidade_arestas:
    if u not in nos_visitados_profundidade:
        busca_profundidade_visitacao.append(u)
        nos_visitados_profundidade.add(u)
    if v not in nos_visitados_profundidade:
        busca_profundidade_visitacao.append(v)
        nos_visitados_profundidade.add(v)

print("Ordem de visitação dos nós pela DFS:", busca_profundidade_visitacao)
print ("Tempo gasto: ", tempo_total_busca_profundidade)



# Comparação dos tempos de execução
tempos = [tempo_total_busca_largura, tempo_total_busca_profundidade]
metodos = ['BFS', 'DFS']

# Criando subplots para os dois gráficos e o texto
fig, axs = plt.subplots(3, 1, figsize=(10, 10))  # 3 linhas, 1 coluna

# 1º Gráfico: Comparação dos tempos de execução
axs[0].bar(metodos, tempos, color=['skyblue', 'lightgreen'])
axs[0].set_title('Comparação dos Tempos de Execução', fontsize=14)
axs[0].set_ylabel('Tempo (s)', fontsize=12)
axs[0].set_xlabel('Métodos de Busca', fontsize=12)

# Adicionando os valores colados às barras
for i, v in enumerate(tempos):
    axs[0].text(i, v - 0.0001, f'{v:.5f}', ha='center', fontsize=10, color='black')

# 2º Gráfico: Sequência de Nós Visitados
axs[1].plot(busca_largura_visitacao, label='BFS', marker='o', color='blue')
axs[1].plot(busca_profundidade_visitacao, label='DFS', marker='x', color='green')
axs[1].set_title('Sequência de Nós Visitados', fontsize=14)
axs[1].set_ylabel('Nós Visitados', fontsize=12)
axs[1].set_xlabel('Passo', fontsize=12)
axs[1].legend(loc='upper left', fontsize=10)

# 3º Gráfico: Sequência de Visitação Formatada com Quebra de Linhas
axs[2].axis('off')  # Desativa os eixos
max_chars_per_line = 80  # Limite de caracteres por linha

# Função para quebrar o texto em várias linhas
def format_sequence(sequence):
    seq_str = ' -> '.join(map(str, sequence))
    return '\n'.join([seq_str[i:i + max_chars_per_line] for i in range(0, len(seq_str), max_chars_per_line)])

# Sequências formatadas para BFS e DFS
sequencia_bfs = format_sequence(busca_largura_visitacao)
sequencia_dfs = format_sequence(busca_profundidade_visitacao)

texto_visita = f"Sequência BFS:\n{sequencia_bfs}\n\nSequência DFS:\n{sequencia_dfs}"
axs[2].text(0.5, 0.5, texto_visita, ha='center', va='center', fontsize=10, bbox=dict(facecolor='lightgray', alpha=0.5))

# Ajustando layout para evitar sobreposição
plt.tight_layout()

# Exibindo os gráficos
plt.show()