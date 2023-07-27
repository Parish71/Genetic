import random

ALVO = "Hell"
CARACTERES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ, !"

TAMANHO_POPULACAO = 100
TAXA_MUTACAO = 0.05
LIMITE_GERACOES = 20000

def gerar_individuo():
    individuo = ''.join(random.choice(CARACTERES) for _ in range(len(ALVO)))
    return individuo

def calcular_aptidao(individuo):
    aptidao = sum(1 for i in range(len(ALVO)) if individuo[i] == ALVO[i])
    return aptidao / len(ALVO)

def selecionar_pais(populacao):
    return random.choice(populacao)

def cruzar(pai1, pai2):
    filho = ''.join(pai1[i] if random.random() < 0.5 else pai2[i] for i in range(len(ALVO)))
    return filho

def mutar(individuo):
    novo_individuo = list(individuo)
    for i in range(len(ALVO)):
        if random.random() < TAXA_MUTACAO:
            novo_individuo[i] = random.choice(CARACTERES)
    return ''.join(novo_individuo)

if __name__ == "__main__":
    populacao = [gerar_individuo() for _ in range(TAMANHO_POPULACAO)]
    melhor_aptidao = 0.0
    melhor_individuo = ""

    geracoes = 0
    while melhor_aptidao < 1.0 and geracoes < LIMITE_GERACOES:
        for individuo in populacao:
            aptidao = calcular_aptidao(individuo)
            if aptidao > melhor_aptidao:
                melhor_aptidao = aptidao
                melhor_individuo = individuo

        nova_populacao = [mutar(cruzar(selecionar_pais(populacao), selecionar_pais(populacao))) for _ in range(TAMANHO_POPULACAO)]
        populacao = nova_populacao
        geracoes += 1
        
        # Impressão do melhor indivíduo encontrado até o momento
        print(f"Testando o indivíduo encontrado após {geracoes} gerações: {individuo}")
        print(f"Melhor indivíduo encontrado após {geracoes} gerações: {melhor_individuo}")        

