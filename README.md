   ***EnergIA* – Assistente Inteligente de Energia**
___
- Pedro Henrique Lisboa – RM: 565722
- Pedro Henrique dos Santos Cardoso - RM: 563268
- Gabriel Gibin Leoncio – RM: 565462
- Rafael do Nascimento Silva – RM: 566263
- Rai Augusto Ribeiro – RM: 562870
___

  O EnergIA é um sistema de automação que simula o gerenciamento inteligente de energia elétrica com suporte a comandos de voz.
Ele combina um backend em Flask para controle do consumo e estado das cargas com um assistente de voz interativo, que entende e responde a comandos naturais.

  **Funcionalidades**

- Monitoramento de energia
Consulta o nível de bateria e o status das cargas críticas e secundárias.

- Gerenciamento de cargas

- Permite ligar ou desligar cargas críticas e secundárias por meio de comandos de voz.

- Assistente de voz interativo

- Reconhece comandos de voz do usuário.

- Responde em voz sintetizada.

- Executa ações automáticas no sistema.

  *API REST (Flask)*
  Disponibiliza rotas simples para:

- Consultar status da energia.

- Atualizar estado das cargas.

___

  **Fluxo de Funcionamento**

- O usuário fala um comando (“Qual o status da energia?”, “Desligar carga secundária”).
- O assistente interpreta a fala e envia a requisição para a API Flask.
- O backend processa a ação, simula os efeitos no consumo de energia e retorna os dados.
- O assistente responde ao usuário em voz.

___

  **Tecnologias Utilizadas**

- Python 3.10+
- Flask → para a API backend
- SpeechRecognition → reconhecimento de voz
- pyttsx3 → síntese de voz (respostas faladas)
- Requests → comunicação entre assistente e backend

___

  **Como executar**
  Após clonar o repositório em sua maquina, será necessário instalar o conteúdo presente no requirements.txt com o comando *pip install -r requirements.txt* no terminal, 
  assim em outro terminal rode o programa com o código python voice/assistant.py


