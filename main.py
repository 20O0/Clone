from os import system
import psutil
from pypresence import Presence
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from cloner import Clone

version = '0.2'


def clearall():
    system('clear')
    print(f"""{Style.BRIGHT}{Fore.GREEN}
 ▄▄▄██▀▀▀▒█████   ▄▄▄       ▒█████   ██ ▄█▀ ██▀███   ██▓  ██████ ▄▄▄█████▓ ▄▄▄       ███▄    █  ██▓
   ▒██  ▒██▒  ██▒▒████▄    ▒██▒  ██▒ ██▄█▒ ▓██ ▒ ██▒▓██▒▒██    ▒ ▓  ██▒ ▓▒▒████▄     ██ ▀█   █ ▓██▒
   ░██  ▒██░  ██▒▒██  ▀█▄  ▒██░  ██▒▓███▄░ ▓██ ░▄█ ▒▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▓██  ▀█ ██▒▒██▒
▓██▄██▓ ▒██   ██░░██▄▄▄▄██ ▒██   ██░▓██ █▄ ▒██▀▀█▄  ░██░  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░██░
 ▓███▒  ░ ████▓▒░ ▓█   ▓██▒░ ████▓▒░▒██▒ █▄░██▓ ▒██▒░██░▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒▒██░   ▓██░░██░
 ▒▓▒▒░  ░ ▒░▒░▒░  ▒▒   ▓▒█░░ ▒░▒░▒░ ▒ ▒▒ ▓▒░ ▒▓ ░▒▓░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▓  
 ▒ ░▒░    ░ ▒ ▒░   ▒   ▒▒ ░  ░ ▒ ▒░ ░ ░▒ ▒░  ░▒ ░ ▒░ ▒ ░░ ░▒  ░ ░    ░      ▒   ▒▒ ░░ ░░   ░ ▒░ ▒ ░
 ░ ░ ░  ░ ░ ░ ▒    ░   ▒   ░ ░ ░ ▒  ░ ░░ ░   ░░   ░  ▒ ░░  ░  ░    ░        ░   ▒      ░   ░ ░  ▒ ░
 ░   ░      ░ ░        ░  ░    ░ ░  ░  ░      ░      ░        ░                 ░  ░         ░  ░  
{Style.RESET_ALL}{Fore.MAGENTA}{Fore.RESET}""")


client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    print(chr(27) + "[2J")
    clearall()
while True:
    token = input(
        f'{Style.BRIGHT}{Fore.MAGENTA}Insira o seu token para prosseguir{Style.RESET_ALL}{Fore.RESET}\n >'
    )
    guild_s = input(
        f'{Style.BRIGHT}{Fore.MAGENTA}Insira o ID do servidor que você deseja replicar{Style.RESET_ALL}{Fore.RESET}\n >'
    )
    guild = input(
        f'{Style.BRIGHT}{Fore.MAGENTA}Insira o ID do servidor de destino para colar o servidor copiado{Style.RESET_ALL}{Fore.RESET}\n>'
    )
    clearall()
    print(f'{Style.BRIGHT}{Fore.GREEN}Os valores inseridos são:')
    print(
        f'{Style.BRIGHT}{Fore.GREEN}Seu token: {Fore.YELLOW}{token}{Style.RESET_ALL}{Fore.RESET}'
    )
    print(
        f'{Style.BRIGHT}{Fore.GREEN}ID do Servidor para replicar: {Fore.YELLOW}{guild_s}{Style.RESET_ALL}{Fore.RESET}'
    )
    print(
        f'{Style.BRIGHT}{Fore.GREEN}ID do Servidor que você deseja colar o servidor copiado: {Fore.YELLOW}{guild}{Style.RESET_ALL}{Fore.RESET}'
    )

    confirm = input(
        f'{Style.BRIGHT}{Fore.MAGENTA}Os valores estão corretos? {Fore.YELLOW}(Y/N){Style.RESET_ALL}{Fore.RESET}\n >'
    )

    if confirm.upper() == 'Y':
        if not guild_s.isnumeric():
            clearall()
            print(
                f'{Style.BRIGHT}{Fore.RED}O ID do servidor para replicar deve conter apenas números.{Style.RESET_ALL}{Fore.RESET}'
            )
            continue
        if not guild.isnumeric():
            clearall()
            print(
                f'{Style.BRIGHT}{Fore.RED}O ID do servidor de destino deve conter apenas números.{Style.RESET_ALL}{Fore.RESET}'
            )
            continue
        if not token.strip() or not guild_s.strip() or not guild.strip():
            clearall()
            print(
                f'{Style.BRIGHT}{Fore.RED}Um ou mais campos estão em branco.{Style.RESET_ALL}{Fore.RESET}'
            )
            continue
        if len(token.strip()) < 3 or len(guild_s.strip()) < 3 or len(
                guild.strip()) < 3:
            clearall()
            print(
                f'{Style.BRIGHT}{Fore.RED}Um ou mais campos têm menos de 3 caracteres.{Style.RESET_ALL}{Fore.RESET}'
            )
            continue
        break
    elif confirm.upper() == 'N':
        clearall()
    else:
        clearall()
        print(
            f'{Style.BRIGHT}{Fore.RED}Opção inválida. Por favor, insira Y ou N.{Style.RESET_ALL}{Fore.RESET}'
        )

input_guild_id = guild_s
output_guild_id = guild
token = token
clearall()


@client.event
async def on_ready():
    try:
        print(
            f"{Style.BRIGHT}{Fore.GREEN} A autenticação na conta foi bem-sucedida"
        )
        print(
            f"{Style.BRIGHT}{Fore.BLUE} Versão do Clonador: {Fore.YELLOW}{version}{Style.RESET_ALL}{Fore.RESET}"
        )
        print(
            f"{Style.BRIGHT}{Fore.BLUE} Versão da API Discord.py em uso: {Style.BRIGHT}{Fore.YELLOW}{discord.__version__}{Style.RESET_ALL}{Fore.RESET}"
        )
        print(
            f"{Style.BRIGHT}{Fore.BLUE} Olá, {Fore.YELLOW}{client.user.name}!{Fore.BLUE} A clonagem começará em instantes...{Style.RESET_ALL}{Fore.RESET}"
        )
        print(f"\n")
        guild_from = client.get_guild(int(input_guild_id))
        guild_to = client.get_guild(int(output_guild_id))
        await Clone.guild_edit(guild_to, guild_from)
        await Clone.roles_delete(guild_to)
        await Clone.channels_delete(guild_to)
        await Clone.roles_create(guild_to, guild_from)
        await Clone.categories_create(guild_to, guild_from)
        await Clone.channels_create(guild_to, guild_from)
        print(f"{Style.BRIGHT}{Fore.GREEN}O servidor foi copiado com êxito!")
        print(
            f"{Style.BRIGHT}{Fore.BLUE}Visite nosso servidor do Discord: {Fore.YELLOW}https://discord.gg/Qvf5NUtqMg{Style.RESET_ALL}"
        )
        print(
            f"{Style.BRIGHT}{Fore.BLUE}Finalizando processo e encerrando a sessão na conta {Fore.YELLOW}{client.user}"
        )
        await client.close()  #fecha o codigo
    except discord.LoginFailure:
        print(
            "Não foi possível autenticar na conta. Verifique se o token está correto."
        )
    except discord.Forbidden:
        print(
            "Não foi possível realizar a clonagem devido a permissões insuficientes."
        )
    except discord.HTTPException:
        print("Ocorreu um erro na comunicação com a API do Discord.")
    except discord.NotFound:
        print(
            "Não foi possível encontrar algum dos elementos da cópia (canais, categorias, etc.)."
        )
    except Exception as e:
        print(f"Erro na função on_ready: {e}")


client.run(token, bot=False)
