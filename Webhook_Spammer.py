import requests, time
from colorama import init, Fore
init()

red, reset, magenta, cyan, green = Fore.RED, Fore.RESET, Fore.MAGENTA, Fore.CYAN, Fore.GREEN

w = input(f"{red}URL Del Webhook{reset} >>> {green}")
data = {
        "content": input(f"{red}Contenido Del Mensaje{reset} >>> {green}")
}
for i in range(int(input(f"{red}Cuantos Mensajes Mandara El Webhook{reset} >>> {green}"))):
    r =  requests.post(w, data=data)
    print(f"{green}-> {cyan}Mensaje numero {magenta}{i}{cyan} Enviado{reset}")
    try:
        time.sleep(r.json()["retry_after"]/1000)
    except:
        pass
