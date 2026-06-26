import pandas as pd
import pywhatkit
import pyautogui
import pygetwindow as gw
import subprocess
import time
import os

PASTA_IMAGENS = "imagens"

while True:
    print("\n=== SISTEMA DE Divulgação ===")
    print("1 - Listar Dizimistas")
    print("2 - Enviar WhatsApp Teste")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        dados = pd.read_excel("CadastroAcevemistas.xlsx")
        print("\n=== LISTA DE DIZIMISTAS ===")
        print(dados.to_string(index=False))

    elif opcao == "2":
        imagens = os.listdir(PASTA_IMAGENS)
        print("\n=== IMAGENS DISPONÍVEIS ===")
        for i, img in enumerate(imagens):
            print(f"{i+1} - {img}")

        escolha = input("\nEscolha o número da imagem: ")
        imagem_escolhida = imagens[int(escolha) - 1]
        caminho_imagem = os.path.join(PASTA_IMAGENS, imagem_escolhida)
        caminho_completo = os.path.abspath(caminho_imagem)
        print(f"✅ Imagem selecionada: {imagem_escolhida}")

        dados = pd.read_excel("CadastroAcevemistas.xlsx")

        for index, linha in dados.iterrows():
            nome = linha["Nome"]
            telefone = str(linha["Telefone"])

            print(f"\nEnviando para {nome} - {telefone}")

            mensagem  = f"""Olá Acevemista {nome}! Tudo bem?

        A ACVM precisa da sua ajuda!

        Com apenas R$ 10,00 por mês você contribui para manter nossa sede funcionando.

        Pequenos gestos, quando unidos, transformam vidas. ❤️

        📲 Chave PIX:
        coordenacaont@gmail.com
        """

            pywhatkit.sendwhatmsg_instantly(
                "+55" + telefone,
                mensagem,
                wait_time=25,
                tab_close=False
            )

            print("Aguardando mensagem carregar...")
            time.sleep(15)

            try:
                janelas = gw.getWindowsWithTitle("WhatsApp")
                if not janelas:
                    janelas = gw.getWindowsWithTitle("Edge")
                if janelas:
                    janelas[0].activate()
                    time.sleep(2)
            except:
                pass

            print("Enviando mensagem de texto...")
            pyautogui.press("enter")
            time.sleep(3)

            # ✅ Copia a imagem para área de transferência PRIMEIRO
            print("Copiando imagem...")
            subprocess.run([
                "powershell",
                "-command",
                f"Set-Clipboard -Path '{caminho_completo}'"
            ])
            time.sleep(2)

            # ✅ Cola e envia a imagem
            print("Enviando imagem...")
            pyautogui.hotkey("ctrl", "v")  # cola no WhatsApp
            time.sleep(3)
            pyautogui.press("enter")  # envia
            time.sleep(5)

            print(f"✅ Mensagem e imagem enviadas para {nome}!")

    elif opcao == "3":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida!")