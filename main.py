import os
from operacoes.soma import soma
from operacoes.subtracao import subtracao
from operacoes.multiplicacao import multiplicacao
from operacoes.divisao import divisao

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        limpar_tela()
        print("Calculadora")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        
        opcao = input("Digite sua opção: ")
        
        if opcao == "1":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = soma(num1, num2)
            print(f"{num1} + {num2} = {resultado}")
            input("Pressione Enter para continuar...")
        elif opcao == "2":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = subtracao(num1, num2)
            print(f"{num1} - {num2} = {resultado}")
            input("Pressione Enter para continuar...")
        elif opcao == "3":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = multiplicacao(num1, num2)
            print(f"{num1} × {num2} = {resultado}")
            input("Pressione Enter para continuar...")
        elif opcao == "4":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if num2 != 0:
                resultado = divisao(num1, num2)
                print(f"{num1} ÷ {num2} = {resultado}")
            else:
                print("Erro: divisão por zero!")
            input("Pressione Enter para continuar...")
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Por favor, tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()