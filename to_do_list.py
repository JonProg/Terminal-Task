#--Importações necessárias--
 
import colorama
import json
from colorama import Fore

colorama.init(autoreset=True)
#---------------------------------

bar = f'{Fore.YELLOW}|'
print(Fore.MAGENTA + '-'*14)
print(f'{Fore.RED}--|{Fore.CYAN}COMANDOS{Fore.RED}|--')
print(Fore.MAGENTA + '-'*14)

print(Fore.YELLOW + '-'*22)
print(f'{Fore.YELLOW}|{Fore.LIGHTRED_EX}Sair -- e{bar:>17}')
print(f'{Fore.YELLOW}|{Fore.LIGHTMAGENTA_EX}Listar Tarefas -- lt{bar:>5}')
print(f'{Fore.YELLOW}|{Fore.LIGHTYELLOW_EX}Desfazer -- d{bar:>13}')
print(f'{Fore.YELLOW}|{Fore.LIGHTGREEN_EX}Refazer -- r{bar:>14}')
print(Fore.YELLOW + '-'*22)
print()

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        print(f'Nenhuma tarefa encontrada em {caminho_arquivo}')
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(tarefas, arquivo, indent=2)

CAMINHO_ARQUIVO = 'tarefas.json'
tasks = ler([], CAMINHO_ARQUIVO)
tasks_exclude = []


while True:
    salvar(tasks, CAMINHO_ARQUIVO)
    task = input('Nova Tarefa:').strip()

    if len(task) <=2:
        if task == 'lt':
            for indice in range(len(tasks)):
                print(f'{Fore.CYAN}{indice+1}. {Fore.LIGHTMAGENTA_EX}{tasks[indice].lower()}')
            if tasks == []:
                print(f'{Fore.RED}Nada a listar')
            continue
        
        elif task == 'd':
            try:
                tasks_exclude.append(tasks[-1])
                tasks.remove(tasks[-1])
            except IndexError:
                print(f'{Fore.RED}NADA a desfazer!')
            continue

        elif task == 'r':
            try:
                tasks.append(tasks_exclude[-1])
                tasks_exclude.clear()
            except IndexError:
                print(f'{Fore.RED}NADA a refazer!')
            continue

        elif task == 'e':
            break
    else:
        tasks.append(task)



    


