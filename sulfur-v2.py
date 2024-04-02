
rust = {
    "feijão":{"Polvora": 60},
    "explosivos": {"Polvora": 50, "Sulfur": 10,"---> SulfurT":110},
    "bala explosiva": {"Polvora": 10, "Sulfur": 5, "---> SulfurT":25},
    "peido": {"Granada de Feijao": 4, "---> PolvoraT":240, "---> SulfurT":480},
    "rocket": {"Polvora": 150, "Explosivos": 10, "---> PolvoraT":650, "---> SulfurT":1400},
    "c4": {"Explosivos": 20, "---> PolvoraT":1000, "---> SulfurT":2200}
}
def calcular(receita,quantidade=1):
    total = {}
    for item, qtd in rust[receita].items():
        total[item] = qtd * quantidade
    return total

def exibir (total):
    for item, qtd in total.items():
        print(f"{item}: {qtd}")

def main():
    while True:
        print("Escolha uma receita: ")
        for receita in rust:
            print(receita)
        escolha = input("Digite sua escolha da lista (ou digite 'sair' para encerrar): ")
        if escolha.lower() == "sair":
            break
        if escolha.lower() in rust:
            quantas = int(input("Qual a quantidade que deseja: "))
            full = calcular(escolha, quantas)
            exibir(full)
        else:
            print("Receita não encontrada. Tente novamente.")
if __name__ == "__main__":
    main()