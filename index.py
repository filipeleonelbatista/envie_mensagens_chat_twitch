import socket
import time
import random

SERVER = "irc.chat.twitch.tv"
PORT = 6667
NICKNAME = "username" # Coloque seu username          
TOKEN = "oauth:seu_token" # Coloque o seu token de autenticação
CHANNEL = "#CANAL" # COLOQUE O CANAL DESEJADO COM A HASHTAG NO INICIO        
INTERVAL = 5 # Intervalo entre as mensagens
DURATION = 15 # Duração do processo de envio

# Um array de strings que ele pegará aleatoriamente as mensagens e enviará no chat
commands = [
    "Minhas mensagens aparecerão no chat"
]

def main():
    irc = socket.socket()
    irc.connect((SERVER, PORT))
    
    irc.send(f"PASS {TOKEN}\r\n".encode("utf-8"))
    irc.send(f"NICK {NICKNAME}\r\n".encode("utf-8"))
    irc.send(f"JOIN {CHANNEL}\r\n".encode("utf-8"))
    
    print("Conectado ao chat da Twitch!")
    
    start_time = time.time()
    while time.time() - start_time < DURATION:
        comando = random.choice(commands) 
        mensagem = f"PRIVMSG {CHANNEL} :{comando}\r\n"
        irc.send(mensagem.encode("utf-8"))
        print(f"Enviado: {comando}")
        time.sleep(INTERVAL)
    
    print("Duração do envio atingida. Serviço interrompido.")


if __name__ == "__main__":
    main()
