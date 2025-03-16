# Twitch Chat Bot

Este projeto é um script Python simples para enviar mensagens automaticamente no chat da Twitch. Ele se conecta ao servidor IRC da Twitch, autentica-se utilizando um token OAuth, junta-se a um canal e envia mensagens de forma aleatória conforme os intervalos e a duração configurados.

## Funcionalidades

- Conecta-se ao servidor IRC da Twitch.
- Realiza autenticação utilizando token OAuth.
- Junta-se a um canal especificado.
- Envia mensagens aleatórias definidas em um array a intervalos regulares.
- Permite configurar o tempo de envio das mensagens.

## Pré-Requisitos

- Python 3 instalado.
- Conta no Twitch.
- Token de autenticação OAuth.

## Configuração

Antes de executar o script, edite as seguintes variáveis no arquivo:

- **NICKNAME**: Seu nome de usuário no Twitch.
- **TOKEN**: Seu token OAuth de autenticação.
- **CHANNEL**: Canal ao qual deseja se conectar (deve começar com `#`).
- **INTERVAL**: Intervalo entre cada mensagem (em segundos).
- **DURATION**: Duração total do processo de envio (em segundos).
- **commands**: Lista de mensagens que serão enviadas no chat.

Exemplo de configuração:
```python
NICKNAME = "seu_username"        # Seu nome de usuário no Twitch
TOKEN = "oauth:seu_token"         # Seu token de autenticação OAuth
CHANNEL = "#CANAL"                # Canal de destino (ex.: #exemplo)
INTERVAL = 5                      # Intervalo de 5 segundos entre mensagens
DURATION = 15                     # Envio ativo por 15 segundos
```

## Como Obter o Token de Autenticação e Criar uma Conta no Twitch Dev

### 1. Criar Conta no Twitch

- Se você ainda não tem uma conta, acesse [Twitch](https://www.twitch.tv/) e clique em "Inscrever-se" para criar uma nova conta.

### 2. Acessar o Console de Desenvolvedores do Twitch

- Visite o [Twitch Developer Console](https://dev.twitch.tv/console).
- Faça login com sua conta Twitch.

### 3. Registrar um Novo Aplicativo

- No console de desenvolvedores, clique em **"Register Your Application"** (ou **"Criar Aplicativo"**).
- Preencha os campos solicitados:
  - **Nome da Aplicação**: Um nome descritivo para o seu projeto (ex.: "Twitch Chat Bot").
  - **OAuth Redirect URL**: Pode ser um URL dummy, como `http://localhost`.
  - **Categoria**: Escolha a categoria que melhor representa o uso (ex.: "Chat Bot").
- Clique em **"Registrar"** para criar o aplicativo.

### 4. Obter o Token OAuth

- Após registrar o aplicativo, você terá acesso ao **Client ID**.
- Para gerar o token OAuth, você pode usar ferramentas online como o [Twitch Token Generator](https://twitchtokengenerator.com/) ou seguir as instruções da [documentação oficial da Twitch](https://dev.twitch.tv/docs/authentication/).
- Siga os passos para autorizar e gerar um token com as permissões necessárias (geralmente `chat:read` e `chat:edit`).
- Copie o token gerado e substitua o valor da variável `TOKEN` no script (lembre-se de incluir o prefixo `oauth:`).

## Execução

1. Salve o arquivo do script como, por exemplo, `twitch_chat_bot.py`.
2. Abra o terminal e navegue até o diretório onde o arquivo foi salvo.
3. Execute o script com o Python:
   ```bash
   python twitch_chat_bot.py
   ```
4. O script se conectará ao chat do canal especificado e enviará as mensagens conforme configurado.

## Observações

- **Regras do Twitch**: Certifique-se de seguir as diretrizes e políticas do Twitch para evitar comportamentos que possam ser interpretados como spam.
- **Personalização**: Você pode adicionar mais mensagens ao array `commands` ou ajustar os valores de `INTERVAL` e `DURATION` conforme necessário para seu caso de uso.

## Contribuição

Contribuições, sugestões e melhorias são muito bem-vindas!  
Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
