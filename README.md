#  RoboWifi – Comunicação Sem Fio

Robô móvel de duas rodas controlado remotamente via **Wi-Fi**, usando um **Raspberry Pi**, dois **servomotores de rotação contínua** e uma interface web em **Flask**. O controle é feito pelo navegador, de qualquer dispositivo conectado na mesma rede.

##  Visão geral

O Raspberry Pi gera sinais PWM (50 Hz) nos pinos GPIO para acionar os servos esquerdo e direito. Combinando o sentido de giro de cada roda, o robô se move para frente, para trás, vira à esquerda, vira à direita ou para.

O projeto traz duas formas de controle, além de scripts auxiliares de teste e calibração:

| Arquivo | Função |
|---|---|
| `WebServoMotor.py` | Servidor web Flask que recebe comandos do navegador e aciona os servos |
| `CLI_WebServo.py` | Controle pelo terminal, com comandos digitados e um percurso pré-programado |
| `TesteServo.py` | Teste rápido dos servos por menu numérico |
| `Calibrar_Parada.py` | Ajuda a encontrar o valor de PWM em que cada servo fica parado |

##  Hardware necessário

- Raspberry Pi com Wi-Fi e GPIO (modelo: `[preencher]`)
- 2 servomotores de rotação contínua
- Chassi com duas rodas (e apoio/roda boba)
- Alimentação adequada para os servos (fonte/bateria separada do Pi, se necessário)

### Ligações (numeração BCM)

| Componente | Pino GPIO |
|---|---|
| Servo esquerdo | GPIO 18 |
| Servo direito | GPIO 27 |

> Lembre-se de ligar o GND dos servos ao GND do Raspberry Pi.

##  Como funciona o controle

Os servos de rotação contínua interpretam o *duty cycle* do PWM como velocidade/sentido, e não como ângulo:

| Ação | Duty cycle |
|---|---|
| Parar | `7.5` |
| Frente | `6.5` |
| Trás | `8.5` |

Esses valores são pontos de partida. Cada servo tem um ponto de parada ligeiramente diferente, por isso o script `Calibrar_Parada.py` existe: ajuste as constantes `PARAR`, `FRENTE` e `TRAS` no topo dos scripts conforme a sua calibração.

##  Instalação

```bash
git clone https://github.com/William-S-Oliveira/RoboWifi_Comunicacao_Sem_Fio.git
cd RoboWifi_Comunicacao_Sem_Fio
pip install flask RPi.GPIO
```

> Os scripts usam `RPi.GPIO`, portanto só funcionam em um Raspberry Pi.

##  Uso

### 1. Calibrar os servos (recomendado na primeira vez)

```bash
python3 Calibrar_Parada.py
```

Digite valores entre `7.0` e `8.0` para cada motor até que os dois parem. O script informa os valores encontrados no final.

### 2. Testar os servos

```bash
python3 TesteServo.py
```

Menu numérico: `1` frente, `2` trás, `3` esquerda, `4` direita, `5` parar, `0` sair.

### 3. Controle pelo terminal

```bash
python3 CLI_WebServo.py
```

Comandos aceitos: `frente`, `tras`, `esquerda`, `direita`, `parar`, `percurso` e `sair`. O comando `percurso` executa uma sequência de movimentos pré-definida.

### 4. Controle pelo navegador (Wi-Fi)

```bash
python3 WebServoMotor.py
```

O servidor sobe na porta **5002**. No navegador de um dispositivo na mesma rede, acesse:

```
http://<IP-DO-RASPBERRY>:5002
```

Para descobrir o IP do Raspberry Pi, use `hostname -I` no terminal dele.

#### Endpoints

| Rota | Método | Descrição |
|---|---|---|
| `/` | GET | Página de controle (`templates/index.html`) |
| `/move` | POST | Recebe o campo `direcao` (`frente`, `tras`, `esquerda`, `direita` ou `parar`) e aciona os motores |

Exemplo de requisição direta:

```bash
curl -X POST -d "direcao=frente" http://<IP-DO-RASPBERRY>:5002/move
curl -X POST -d "direcao=parar"  http://<IP-DO-RASPBERRY>:5002/move
```

## 📁 Estrutura do projeto

```
RoboWifi_Comunicacao_Sem_Fio/
├── WebServoMotor.py     # Servidor Flask (controle via Wi-Fi)
├── CLI_WebServo.py      # Controle pelo terminal
├── TesteServo.py        # Teste dos servos
├── Calibrar_Parada.py   # Calibração do ponto de parada
├── templates/
│   └── index.html       # Interface web de controle
└── README.md
```

##  Observações

- O servidor escuta em `0.0.0.0` e **não tem autenticação**. Use apenas em redes locais confiáveis.
- Ao encerrar os scripts, o PWM é interrompido e os GPIOs são liberados automaticamente (`GPIO.cleanup()`).
- Se o robô "andar sozinho" quando deveria estar parado, refaça a calibração do valor de parada.

##  Possíveis melhorias

- Controle de velocidade (variando o duty cycle)
- Autenticação na interface web
- Streaming de vídeo de uma câmera
- Sensores de obstáculo



Desenvolvido por: **William da Silva Oliveira** – [GitHub](https://github.com/William-S-Oliveira)
