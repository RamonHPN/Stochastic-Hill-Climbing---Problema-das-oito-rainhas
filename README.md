# 🏰 Stochastic Hill Climbing — Problema das 8 Rainhas

Este projeto implementa o algoritmo **Stochastic Hill Climbing** para resolver o clássico problema das 8 rainhas, utilizando uma representação por array onde cada índice representa uma coluna e o valor armazenado representa a linha da rainha naquela coluna.

---

## ✅ Requisitos Atendidos

### Representação
- Cada solução é representada por um vetor de 8 posições.
- O índice do vetor representa a coluna do tabuleiro.
- O valor em cada posição representa a linha da rainha naquela coluna (valores entre 0 e 7).

---

## ⚙️ Parâmetros do Algoritmo

| Parâmetro            | Valor              |
|---------------------|--------------------|
| Tamanho do tabuleiro | 8x8                |
| Máximo de iterações  | 1000               |
| Representação       | Array de 8 posições |
| Critério de parada  | Solução ótima (0 colisões) ou máximo de iterações |

---

## 🎯 Função Objetivo

A função de aptidão avalia o número de pares de rainhas que se atacam (conflitos). O objetivo é minimizar esse número.

- **Fitness** = - (número de conflitos)

A busca termina quando o fitness é 0 (nenhum conflito) ou o número máximo de iterações é atingido.

---

## 📈 Estatísticas Geradas

O algoritmo é executado 50 vezes para obter:

- Média e desvio padrão do número de iterações necessárias para parar.
- Média e desvio padrão do tempo de execução.
- As cinco melhores soluções distintas encontradas.

---

## 📦 Estrutura do Código

- `random_solution()`: Gera uma solução inicial aleatória.
- `fitness(state)`: Calcula o número negativo de conflitos da solução.
- `get_neighbors(state)`: Gera todas as soluções vizinhas que diferem em uma posição.
- `stochastic_hill_climbing()`: Executa o algoritmo Stochastic Hill Climbing até o critério de parada.

---

## ▶️ Como Executar

### Pré-requisitos

- Python 3.x instalado.
- Nenhuma biblioteca externa necessária.

### Rodar o script

```bash
python q1.py
