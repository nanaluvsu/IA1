# ANÁLISE COMPLETA: BUSCA GULOSA (BEST-FIRST SEARCH)
## Mapa da Romênia: Arad → Bucareste

---

## a) ANÁLISE DETALHADA DO CÓDIGO

### 1. **PARÂMETROS CONSIDERADOS**

#### 1.1 Grafo (Distâncias Reais)
O código representa o mapa da Romênia como um **dicionário de adjacência ponderado**:
```
grafo = {
    'Arad': [('Sibiu', 140), ('Zerind', 75), ('Timisoara', 118)],
    'Sibiu': [('Arad', 140), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    ...
}
```
- **Chave**: cidade (nó)
- **Valor**: lista de tuplas (cidade_vizinha, distância_real_em_km)
- **Significado**: Armazena as conexões reais entre cidades com suas distâncias

#### 1.2 Heurística (Distâncias em Linha Reta)
A heurística é um dicionário com a **distância em linha reta até Bucareste**:
```
h = {
    'Arad': 366,      # Distância reta até Bucareste
    'Sibiu': 253,
    'Zerind': 374,
    'Bucharest': 0,   # Objetivo → h = 0
    ...
}
```
- **Função h(n)**: Estima o custo futuro de um nó até o objetivo
- **Características**: 
  - Heurística **admissível** (nunca sobrestima)
  - Baseada em geometria (distância euclidiana)
  - Guia o algoritmo na direção correta

### 2. **SISTEMAS DE ARMAZENAMENTO E VERIFICAÇÃO**

#### 2.1 Fronteira (Fila de Prioridade)
```python
fronteira = []  # heapq (min-heap)
heapq.heappush(fronteira, (h_valor, contador, nodo, caminho))
```
**Estrutura**: `(h(n), contador, nó, [caminho_completo])`
- **h(n)**: Heurística do nó (prioridade)
- **contador**: Desempate quando heurísticas são iguais
- **nó**: Nó atual
- **[caminho]**: Sequência de nós visitados até aqui

**Operação**:
- `heappush()`: Insere nó na fila com sua prioridade
- `heappop()`: Extrai o nó com **menor h(n)** (nó mais promissor)

**Propriedade**: A fila sempre retira o nó com a heurística mais baixa

#### 2.2 Conjunto de Visitados
```python
visitados = set()
```
**Propósito**: 
- Evita revisitar nós já explorados
- Impede ciclos infinitos
- Reduz redundância na busca

**Operação**:
- `visitados.add(nodo)`: Marca nó como explorado
- `if nodo not in visitados`: Verifica antes de adicionar vizinhos

### 3. **HEURÍSTICA E SELEÇÃO DO MELHOR CAMINHO**

#### 3.1 Como a Heurística é Usada

A Busca Gulosa segue o princípio:
> **"Sempre expanda o nó que parece mais próximo do objetivo segundo h(n)"**

```
Processo:
1. h(Arad) = 366
   ├─→ Expande Arad
   ├─→ Gera vizinhos: Sibiu (253), Zerind (374), Timisoara (329)
   
2. Próximo: Sibiu com h = 253 (menor entre os na fronteira)
   ├─→ Expande Sibiu
   ├─→ Gera vizinhos: Fagaras (178), Rimnicu Vilcea (193)
   
3. Próximo: Fagaras com h = 178
   ├─→ Expande Fagaras
   ├─→ Gera vizinho: Bucharest (0) ← OBJETIVO!
```

#### 3.2 Seleção do "Melhor" Caminho

Diferentemente de algoritmos otimizados (como A*), a Busca Gulosa:
- **NÃO** calcula custo acumulado (g(n))
- **Apenas** considera a heurística h(n)
- Pode encontrar um caminho **não-ótimo**

**Exemplo**: O caminho Arad → Sibiu → Fagaras → Bucharest
- Distância total: 140 + 99 + 211 = **450 km**
- Caminho ótimo: Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest
- Distância ótima: 140 + 80 + 97 + 101 = **418 km**

### 4. **FLUXO DO ALGORITMO**

```
Algoritmo Busca_Gulosa(inicio, objetivo):
    
    1. INICIALIZAR:
       - fronteira = [(h(inicio), 0, inicio, [inicio])]
       - visitados = {}
       - contador = 1
    
    2. ENQUANTO fronteira não estiver vazia:
       a. nodo = fronteira.extrai_minimo()
       
       b. SE nodo == objetivo:
          - RETORNE caminho
       
       c. MARCAR nodo como visitado
       
       d. PARA CADA vizinho de nodo:
          - SE vizinho NÃO visitado:
             - ADICINAR a fronteira
             - fronteira.insere((h(vizinho), contador++, vizinho, novo_caminho))
    
    3. SE fronteira vazia E objetivo não encontrado:
       - RETORNE "Falha"
```

---

## b) ÁRVORE DE DECISÃO DO MAPA DA ROMÊNIA

```
                                NÍVEL 0
                                  |
                                [ARAD]
                              h=366 km
                                  |
                    ________________|________________
                   |                |                |
                NÍVEL 1
                   |
         [ZERIND]  [SIBIU]  [TIMISOARA]
         h=374     h=253    h=329
            ↓
    ESCOLHIDO (menor h)
            |
    ______________________|_______________________________
    |                     |                               |
  NÍVEL 2
    |
[ORADEA]            [FAGARAS]              [RIMNICU VILCEA]
h=380              h=178                    h=193
    ↓
    Expandir Fagaras (h=178, menor valor)
    |
    ______________|___________
    |                         |
  NÍVEL 3
    |
[SIBIU]                    [BUCHAREST] ← OBJETIVO!
(visitado)                  h=0
                            ↓
                        ENCONTRADO!
                        Retornar caminho:
                        Arad → Sibiu → Fagaras → Bucharest
```

### Ordem de Expansão Detalhada

```
1. Expandir: ARAD (h=366)
   Vizinhos gerados:
   ├─ Sibiu (h=253)      ← Mais promissor
   ├─ Zerind (h=374)
   └─ Timisoara (h=329)

2. Expandir: SIBIU (h=253) ← Selecionado (menor h)
   Vizinhos gerados:
   ├─ Arad (visitado - ignorar)
   ├─ Fagaras (h=178)    ← Mais promissor
   └─ Rimnicu Vilcea (h=193)

3. Expandir: FAGARAS (h=178) ← Selecionado (menor h)
   Vizinhos gerados:
   ├─ Sibiu (visitado - ignorar)
   └─ Bucharest (h=0)    ← OBJETIVO!

4. Expandir: BUCHAREST (h=0)
   ✓ OBJETIVO ENCONTRADO!
   
Caminho Final: Arad → Sibiu → Fagaras → Bucharest
Distância percorrida: 140 + 99 + 211 = 450 km
Número de nós visitados: 4
Número de nós gerados: 7
```

---

## c) PASSO A PASSO DA EXECUÇÃO

### **FASE 1: INICIALIZAÇÃO**

```
Estado Inicial:
├─ Nó de início: Arad
├─ Nó objetivo: Bucharest
├─ h(Arad) = 366 km
├─ Fronteira: [(366, 0, 'Arad', ['Arad'])]
└─ Visitados: {}
```

---

### **FASE 2: ITERAÇÃO 1 - EXPANDIR ARAD**

```
PASSO 1:
├─ Nó extraído: Arad
├─ h(Arad) = 366
├─ Caminho até agora: Arad
├─ É objetivo? NÃO
│
├─ MARCADO COMO VISITADO: {Arad}
│
├─ VIZINHOS DE ARAD:
│  ├─ Sibiu (distância real = 140 km)
│  │  └─ h(Sibiu) = 253 km
│  │  └─ Adicionado à fronteira
│  │
│  ├─ Zerind (distância real = 75 km)
│  │  └─ h(Zerind) = 374 km
│  │  └─ Adicionado à fronteira
│  │
│  └─ Timisoara (distância real = 118 km)
│     └─ h(Timisoara) = 329 km
│     └─ Adicionado à fronteira
│
└─ ESTADO APÓS ITERAÇÃO 1:
   ├─ Fronteira (por h): [(253, 1, 'Sibiu', ['Arad', 'Sibiu']),
   │                     (329, 3, 'Timisoara', ...),
   │                     (374, 2, 'Zerind', ...)]
   └─ Visitados: {Arad}

DECISÃO: Próximo nó = Sibiu (h=253 é o mínimo)
```

---

### **FASE 3: ITERAÇÃO 2 - EXPANDIR SIBIU**

```
PASSO 2:
├─ Nó extraído: Sibiu
├─ h(Sibiu) = 253
├─ Caminho até agora: Arad → Sibiu
├─ É objetivo? NÃO
│
├─ MARCADO COMO VISITADO: {Arad, Sibiu}
│
├─ VIZINHOS DE SIBIU:
│  ├─ Arad (VISITADO - IGNORAR)
│  │
│  ├─ Fagaras (distância real = 99 km)
│  │  └─ h(Fagaras) = 178 km
│  │  └─ Adicionado à fronteira ← MAIS PROMISSOR!
│  │
│  └─ Rimnicu Vilcea (distância real = 80 km)
│     └─ h(Rimnicu Vilcea) = 193 km
│     └─ Adicionado à fronteira
│
└─ ESTADO APÓS ITERAÇÃO 2:
   ├─ Fronteira (por h): [(178, 4, 'Fagaras', ...),
   │                     (193, 5, 'Rimnicu Vilcea', ...),
   │                     (329, 3, 'Timisoara', ...),
   │                     (374, 2, 'Zerind', ...)]
   └─ Visitados: {Arad, Sibiu}

ANÁLISE:
Fagaras tem h(Fagaras) = 178 km - MUITO mais promissor
que Rimnicu Vilcea (h=193)! A heurística está guiando bem!

DECISÃO: Próximo nó = Fagaras (h=178 é o mínimo)
```

---

### **FASE 4: ITERAÇÃO 3 - EXPANDIR FAGARAS**

```
PASSO 3:
├─ Nó extraído: Fagaras
├─ h(Fagaras) = 178
├─ Caminho até agora: Arad → Sibiu → Fagaras
├─ É objetivo? NÃO
│
├─ MARCADO COMO VISITADO: {Arad, Sibiu, Fagaras}
│
├─ VIZINHOS DE FAGARAS:
│  ├─ Sibiu (VISITADO - IGNORAR)
│  │
│  └─ Bucharest (distância real = 211 km)
│     └─ h(Bucharest) = 0 km ← é o OBJETIVO!
│     └─ Adicionado à fronteira
│
└─ ESTADO APÓS ITERAÇÃO 3:
   ├─ Fronteira (por h): [(0, 6, 'Bucharest', ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']),
   │                     (193, 5, 'Rimnicu Vilcea', ...),
   │                     (329, 3, 'Timisoara', ...),
   │                     (374, 2, 'Zerind', ...)]
   └─ Visitados: {Arad, Sibiu, Fagaras}

DECISÃO: Próximo nó = Bucharest (h=0 é o MÍNIMO absoluto)
```

---

### **FASE 5: ITERAÇÃO 4 - ENCONTRAR OBJETIVO**

```
PASSO 4:
├─ Nó extraído: Bucharest
├─ h(Bucharest) = 0
├─ Caminho até agora: Arad → Sibiu → Fagaras → Bucharest
├─ É objetivo? SIM! ✓
│
└─ RETORNAR CAMINHO ENCONTRADO:
   
   ✓ SUCESSO!
   ├─ Caminho: Arad → Sibiu → Fagaras → Bucharest
   ├─ Comprimento: 4 cidades (3 etapas)
   ├─ Distância total: 140 + 99 + 211 = 450 km
   ├─ Nós visitados: 4
   ├─ Nós gerados na fronteira: 7
   └─ Eficiência: Encontrado em 4 iterações!
```

---

## d) COMPARAÇÃO COM O CAMINHO ÓTIMO

### Caminho Encontrado pela Busca Gulosa
```
Arad (h=366)
 ↓ [140 km]
Sibiu (h=253)          ← Escolhido por ter h menor
 ↓ [99 km]
Fagaras (h=178)        ← Escolhido por ter h menor
 ↓ [211 km]
Bucharest (h=0)        ✓ Encontrado!

TOTAL: 450 km em 3 etapas
```

### Caminho Ótimo (Distância Mínima)
```
Arad
 ↓ [140 km]
Sibiu
 ↓ [80 km]
Rimnicu Vilcea (h=193)
 ↓ [97 km]
Pitesti (h=98)
 ↓ [101 km]
Bucharest

TOTAL: 418 km em 4 etapas
```

### **ANÁLISE COMPARATIVA**

| Aspecto | Busca Gulosa | Caminho Ótimo | Diferença |
|---------|-------------|--------------|-----------|
| **Distância Total** | 450 km | 418 km | +32 km (7.7% pior) |
| **Número de Cidades** | 4 | 5 | -1 (mais direto) |
| **Iterações até Objetivo** | 4 | - | - |
| **Caminho** | A→Si→Fa→B | A→Si→RV→P→B | - |

### **Por Que a Busca Gulosa não Encontrou o Ótimo?**

1. **Greedy (Guloso)**: A algoritmo toma a decisão **localmente ótima** a cada passo
    - Em SIBIU: Fagaras (h=178) parece melhor que Rimnicu Vilcea (h=193)
    - **MAS**: Rimnicu Vilcea leva a Pitesti (h=98) que é melhor ainda!

2. **Falta de Visão Global**: Não considera o custo acumulado
    - Fagaras tem distância real GRANDE (211 km) até Bucharest
    - Rimnicu Vilcea → Pitesti tem distância MENOR (97+101=198 km)

3. **Quando Usar Busca Gulosa**:
    - ✓ Quando boa solução (não necessariamente ótima) é suficiente
    - ✓ Quando há muitos nós (precisa explorar menos)
    - ✗ Quando solução ótima é CRÍTICA (usar A*)

---

## e) CONCLUSÃO

### Características do Código

**Pontos Positivos:**
✓ Implementação clara e bem estruturada
✓ Heurística admissível (distância reta)
✓ Usa fila de prioridade (eficiente)
✓ Evita nós revisitados
✓ Encontra solução rapidamente

**Limitações:**
✗ Não garante solução ótima (é guloso)
✗ Pode ficar preso em mínimos locais
✗ Sem memória de nós já explorados

### Aplicações da Busca Gulosa

- Roteamento de GPS (precisa de resultado rápido)
- Planejamento com tempo limitado
- Sistemas embarcados com pouca memória
- Quando "bom o suficiente" é aceitável

### Para Solução Ótima: Use A*

A* = Busca Gulosa + Custo Acumulado
$$f(n) = g(n) + h(n)$$

Onde:
- $g(n)$ = custo real acumulado (0 → n)
- $h(n)$ = heurística (n → objetivo)

---

**FIM DA ANÁLISE**
