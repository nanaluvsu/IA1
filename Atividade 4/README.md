# Agentes Inteligentes

Esse repositório contém o código base relacionado ao exercício sobre o tópico
de agentes inteligentes e algoritmos de busca, para a disciplina de Inteligência 
Artificial e Machine Learning na PUC Campinas.

As instruções para executar o exercício estão disponíveis no LMS das aulas.

## Utilização
Abaixo estão as instruções para ambiente linux. Se você utiliza Windows ou Mac, faça 
os ajustes necessários.

1. Criação e ativação de um ambiente virtual

No seu terminal de preferência, execute o comando abaixo para criar um ambiente
virtual.
```
python -m venv env

```
Ative o ambiente virtual.
```
source env/bin/activate
```
2. Instale as dependências necessárias para execução do código.

Com o seu ambiente virtual ativado, instale as dependências com o comando abaixo.
```
python -m pip install -r requirements.txt
```

3. Rodando as demonstrações

Para executar a demonstração do agente vacumm\_cleaner:
```
cd vacumm_cleaner
python main.py
```

Para executar a demonstração do agente no labirinto:
```
cd labirinto
python main.py
```

4. Teste sua implementação do exercício

Para resolver o exercício proposto em sala de aula, você deve modificar o
arquivo `labirinto/exercise.py`.
Após implementar sua solução, ajuste a função main para executar o algoritmo
implementado.
Em seguida, você pode executar o agente com o seguinte comando (assumindo que
já está na pasta labirinto):

```
python exercise.py
```
