from Classes import *
import os

def ver_quartos():
    while True:
        try:
            os.system("cls")
            print("Esses são os quartos disponiveis: ")
            print("[01] - AP Simples")
            print("[02] - AP Simples Casal")
            print("[03] - AP Duplo")
            print("[04] - AP Duplo Casal")
            print("[05] - AP Luxo")
            print("[06] - AP Master")
            print("[07] - voltar")
            menu_quartos = input("Digite o número correspondente a opção que deseja: ")
            match menu_quartos:
                
                case "1":
                    ap_simples = Ap_Simples
                    ap_simples.informações()

                case "2":
                    ap_simples_casal = Ap_Simples_casal
                    ap_simples_casal.informações()

                case "3":
                    ap_duplo = Ap_Duplo
                    ap_duplo.informações()

                case "4":
                    ap_duplo_casal = Ap_Duplo_casal
                    ap_duplo_casal.informações()

                case "5":
                    ap_luxo = Ap_luxo
                    ap_luxo.informações()

                case "6":
                    ap_Master = Ap_Master
                    ap_Master.informações()

                case "7":
                    print("Voltando...")
                    os.system("pause")
                    break

                case _:
                    print ("Opção inválida")
                    os.system("pause")
                    os.system("cls")
        except:
            print("Erro, opção inválida. Tente novamente.")
            os.system("pause")
            os.system("cls")


def hospedagem():
    os.system("cls")
    print()

def main():
    while True:
        try:
        # Tratamento de erro
            os.system("cls") 
            print("Bem-vindos a um refúgio de elegância e conforto ")
            print("[01] - Ver quartos")
            print("[02] - Realizar Hospedagem")
            print("[03] - Sair")

            menu=input("Digite o número correspondente a opção que deseja: ")
          
            match menu:
                case "1":
                    ver_quartos()
                case "2":
                    print("Você escolheu a opção pra realizar a hospedagem de um quarto \n esses são os quartos disponiveis \n")
                case "3":
                    print("Saindo...")
                    os.system("pause")
                    break
                    
                case _:
                    print ("Opção inválida")
                    os.system("pause")
                    os.system("cls") 
                # Tratamento de erro, ou seja, caso ocorra um erro fazer:

        except:
            print("Erro, opção inválida. Tente novamente.")
            os.system("pause")
            os.system("cls")