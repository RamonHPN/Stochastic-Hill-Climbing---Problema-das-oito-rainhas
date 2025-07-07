import random
import time
from statistics import mean, stdev

NUM_QUEENS = 8
MAX_ITERATIONS = 1000

# Gera uma solução aleatória (um array de 8 posições)
def random_solution():
    return [random.randint(0, 7) for _ in range(NUM_QUEENS)]

# Calcula a aptidão (número de conflitos negativos)
def fitness(state):
    conflicts = 0
    for i in range(NUM_QUEENS):
        for j in range(i + 1, NUM_QUEENS):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return -conflicts  # Negativo pois menor número de conflitos é melhor

# Gera todos os vizinhos com 1 movimento vertical em qualquer coluna
def get_neighbors(state):
    neighbors = []
    for col in range(NUM_QUEENS):
        for row in range(8):
            if state[col] != row:
                neighbor = state.copy()
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

# Algoritmo Stochastic Hill Climbing
def stochastic_hill_climbing():
    current = random_solution()
    current_fitness = fitness(current)
    start = time.time()

    for iteration in range(1, MAX_ITERATIONS + 1):
        neighbors = get_neighbors(current)
        better_neighbors = [n for n in neighbors if fitness(n) > current_fitness]

        if not better_neighbors:
            break

        current = random.choice(better_neighbors)
        current_fitness = fitness(current)

        if current_fitness == 0:
            break

    elapsed = time.time() - start
    return iteration, elapsed, current

# Executa o algoritmo 50 vezes e armazena estatísticas
iterations, times, solutions = [], [], []

for _ in range(50):
    it, t, sol = stochastic_hill_climbing()
    iterations.append(it)
    times.append(t)
    if sol not in solutions:
        solutions.append(sol)
    if len(solutions) >= 5:
        break

# Estatísticas
media_iter = mean(iterations)
std_iter = stdev(iterations)
media_time = mean(times)
std_time = stdev(times)

# Exibição dos resultados
print("\n Estatísticas:")
print(f"Média de iterações: {media_iter:.2f}")
print(f"Desvio padrão das iterações: {std_iter:.2f}")
print(f"Média do tempo: {media_time:.4f} s")
print(f"Desvio padrão do tempo: {std_time:.4f} s")

print("\n 5 Melhores Soluções Distintas:")
for i, sol in enumerate(solutions[:5]):
    print(f"{i+1}: {sol}")
