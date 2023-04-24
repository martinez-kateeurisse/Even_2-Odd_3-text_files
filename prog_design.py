#Import colorama
from colorama import Back, Fore, Style 

#Define header design
def double_triple_header():
    print(Fore.GREEN, """
                                ──────▄▀▄─────▄▀▄
                                ─────▄█░░▀▀▀▀▀░░█▄ 
                                ─▄▄──█░░░░░░░░░░░█──▄▄
                                █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█"""+ Fore.LIGHTMAGENTA_EX,"""  
                   █▀▀ █ █░░ █▀▀ ▄▄ █░█ ▄▀█ █▄░█ █▀▄ █░░ █ █▄░█ █▀▀
                   █▀░ █ █▄▄ ██▄ ░░ █▀█ █▀█ █░▀█ █▄▀ █▄▄ █ █░▀█ █▄█""")
    print(Fore.WHITE,  "="* 18 + "Squaring Even Integers & Cubing Odd Integers" + "="* 18 ,"\n")
