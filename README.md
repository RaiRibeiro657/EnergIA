   ***EnergIA* – Assistente Inteligente de Energia**
___
- Pedro Henrique Lisboa – RM: 565722
- Pedro Henrique dos Santos Cardoso - RM: 563268
- Gabriel Gibin Leoncio – RM: 565462
- Rafael do Nascimento Silva – RM: 566263
- Rai Augusto Ribeiro – RM: 562870
___

O **EnergIA** é um sistema completo de gerenciamento de energia, desenvolvido para monitorar e controlar o consumo de cargas elétricas críticas e secundárias em tempo real. O projeto integra três camadas principais:  

1. **Backend (API Flask)** – Mantém o estado da bateria e das cargas, processa atualizações e fornece endpoints para consulta e controle.  
2. **Interface Visual (Streamlit)** – Painel interativo que mostra status da bateria, histórico de consumo e permite controle manual das cargas.  
3. **Assistente de Voz (Python)** – Permite interação por comandos de voz, possibilitando ligar/desligar cargas e consultar o status da bateria sem precisar tocar no computador.  

O sistema foi projetado para **simular o gerenciamento de energia de uma residência ou micro-usina**, com foco em automação e monitoramento inteligente.

___

## **Funcionamento do Backend**

O **backend** é responsável por manter o estado do sistema e processar ações automáticas. Ele contém a classe `EnergyManager` que:  

- **Armazena o nível de bateria** e o estado de cada carga (crítica e secundária).  
- **Calcula o consumo de energia** com base nas cargas ligadas.  
- **Permite atualização manual ou automática das cargas**.  

A API expõe dois endpoints principais:  

1. **`/status`** – Retorna o estado atual da bateria e das cargas em formato JSON.  
2. **`/update`** – Permite ligar ou desligar cargas específicas através de requisições POST.

___

## **Funcionamento da Interface Visual (Streamlit)**

O **painel Streamlit** funciona como uma **central de monitoramento**, permitindo:  

- Visualizar **o nível da bateria em tempo real** com barras de progresso.  
- Consultar o **estado das cargas críticas e secundárias** com métricas visuais.  
- Controlar manualmente cargas através de **botões interativos**.  
- Observar o **histórico de consumo** em gráficos, facilitando análise de padrões de uso.  

O Streamlit consome os dados diretamente da API Flask, garantindo que **qualquer alteração via interface ou assistente de voz seja refletida imediatamente**.

___

## **Funcionamento do Assistente de Voz**

O **assistente de voz** permite que o usuário interaja com o sistema **falando comandos**, sem usar o teclado.  

- Utiliza **SpeechRecognition** para capturar comandos do microfone.  
- Utiliza **pyttsx3** para respostas de áudio, confirmando ações e informando status.  
- Integra diretamente com a API Flask para:  
  - Consultar status da bateria e cargas.  
  - Ligar ou desligar a carga crítica.  
  - Ligar ou desligar a carga secundária.  

**Comandos de exemplo:**  
- `"status"` → consulta bateria e estado das cargas.  
- `"desligar carga secundária"` / `"ligar carga secundária"`  
- `"desligar carga crítica"` / `"ligar carga crítica"`  
- `"sair"` ou `"parar"` → encerra o assistente.

___

> Observação: ´sounddevice` substitui o PyAudio, garantindo funcionamento do assistente de voz sem problemas de instalação no Windows.
>
> ___
>
> Vídeo YouTube: https://youtu.be/voaITdt1LSg
