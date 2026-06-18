import pandas as pd
import pywhatkit
import pyautogui
import time

while True:

    print("\n=== SISTEMA DE DIZIMISTAS ===")
    print("1 - Listar Dizimistas")
    print("2 - Enviar WhatsApp Teste")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        dados = pd.read_excel("CadastroAcevemistas.xlsx")

        print("\n=== LISTA DE DIZIMISTAS ===")

        print(dados.to_string(index=False))
        
    elif opcao == "2":

         dados = pd.read_excel("CadastroAcevemistas.xlsx")
         
         for index, linha in dados.iterrows():
            nome = linha["Nome"]
            telefone = str(linha["Telefone"])
            
            print(f"\nEnviando para {nome}")
            
            mensagem = f"Olá {nome}! Esta é uma mensagem de teste da ACVM"
            
            print("Telefone:", telefone)
            print("Mensagem:", mensagem)
            
            pywhatkit.sendwhatmsg_instantly(
                "+55" + telefone,
                mensagem,
                wait_time=15
            )
            
    elif opcao == "3":
        print("Sistema encerrado.")
        break
    else:

        print("Opção inválida!")