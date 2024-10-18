# instalar 'deep_translator' (pip install deep_translator)
# importar a biblioteca Deep Translator

import os
import time
from deep_translator import GoogleTranslator


tradutor = GoogleTranslator(source="auto", target="pt")


print("Programa que traduz qualquer texto em outras línguas para Português")

if __name__ == '__main__':
    while True:
        try:
            print('''
                  [1] - Traduzir texto.
                  [2] - Sair do programa.
                  ''')
            opcao = input("Opção desejada: ")

            os.system("cls")
            
            match opcao:
                case "1":
                    texto_original = input("Digite o texto a ser traduzido: \n")
                    
                    texto_traduzido = tradutor.translate(texto_original)
                    

                    print(f"\nTradução = {texto_traduzido}")
                    continue
                case "2":
                    print("Saindo do programa.")
                    time.sleep(1.5)
                    break
                case _: 
                    print("Opção inválida.")
                    continue

        except Exception as e:
            print(f"Não foi possível traduzir o texto. {e}.")