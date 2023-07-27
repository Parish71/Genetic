import random
import string

ALVO = "H0000"
CARACTERES = string.ascii_letters + string.digits + " !@#$%^&*()_+-=[]{}|;:,.<>?/"  # Conjunto ampliado

TAMANHO_POPULACAO = 2000
TAXA_MUTACAO = 0.01  # Adjust the mutation rate as needed
LIMITE_GERACOES = 6000
TAMANHO_TORNEIO = 1  # Tamanho do torneio para a seleção por torneio

def gerar_individuo():
    individuo = ''.join(random.choice(CARACTERES) for _ in range(len(ALVO)))
    return individuo

def calcular_aptidao(individuo):
    aptidao = sum(1 for i in range(len(ALVO)) if individuo[i] == ALVO[i])
    return aptidao / len(ALVO)

def selecionar_pais(populacao):
    # Seleção por torneio
    torneio = random.sample(populacao, TAMANHO_TORNEIO)
    melhor_individuo = max(torneio, key=calcular_aptidao)
    return melhor_individuo

def cruzar(pai1, pai2):
    filho = ''.join(pai1[i] if random.random() < 0.5 else pai2[i] for i in range(len(ALVO)))
    return filho

def mutar(individuo, forcar_mutacao=False):
    novo_individuo = list(individuo)
    for i in range(len(ALVO)):
        if forcar_mutacao or random.random() < TAXA_MUTACAO:
            novo_individuo[i] = random.choice(CARACTERES)
    return ''.join(novo_individuo)

if __name__ == "__main__":
    populacao = [gerar_individuo() for _ in range(TAMANHO_POPULACAO)]
    melhor_aptidao = 0.1
    melhor_individuo = "Hello"

    geracoes = 0
    while melhor_aptidao < 1.0 and geracoes < LIMITE_GERACOES:
        nova_populacao = []
        # Elitism - Preserve the best individual in the new population
        nova_populacao.append(melhor_individuo)

        while len(nova_populacao) < TAMANHO_POPULACAO:
            pai1 = selecionar_pais(populacao)
            pai2 = selecionar_pais(populacao)
            filho = mutar(cruzar(pai1, pai2))
            nova_populacao.append(filho)

        # Update the population for the next generation
        populacao = nova_populacao
        geracoes += 1

        # Find the best individual in the current population
        melhor_individuo = max(populacao, key=calcular_aptidao)
        melhor_aptidao = calcular_aptidao(melhor_individuo)

        # Print the best individual in this generation
        print(f"Melhor indivíduo encontrado após {geracoes} gerações: {melhor_individuo}")

    print(f"Melhor indivíduo encontrado após {geracoes} gerações: {melhor_individuo}")
