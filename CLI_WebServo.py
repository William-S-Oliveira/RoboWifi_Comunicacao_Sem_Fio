import RPi.GPIO as GPIO
import time

# Configuração dos pinos
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

SERVO_ESQUERDA = 18
SERVO_DIREITA = 27

GPIO.setup(SERVO_ESQUERDA, GPIO.OUT)
GPIO.setup(SERVO_DIREITA, GPIO.OUT)

# Inicializa PWM com 50Hz
pwm_esq = GPIO.PWM(SERVO_ESQUERDA, 50)
pwm_dir = GPIO.PWM(SERVO_DIREITA, 50)

pwm_esq.start(0)
pwm_dir.start(0)

# Duty cycles
PARAR = 7.5
FRENTE = 6.5
TRAS = 8.5

# Funções de movimento
def frente():
    pwm_esq.ChangeDutyCycle(TRAS)
    pwm_dir.ChangeDutyCycle(FRENTE)
    print("Movendo para frente")

def tras():
    pwm_esq.ChangeDutyCycle(FRENTE)
    pwm_dir.ChangeDutyCycle(TRAS)
    print("Movendo para trás")

def esquerda():
     pwm_esq.ChangeDutyCycle(TRAS)
     pwm_dir.ChangeDutyCycle(TRAS)
     print("Virando à esquerda")

def direita():
    pwm_esq.ChangeDutyCycle(FRENTE)
    pwm_dir.ChangeDutyCycle(FRENTE)
    print("Virando à direita")

def parar():
    pwm_esq.ChangeDutyCycle(PARAR)
    pwm_dir.ChangeDutyCycle(PARAR)
    print("Parado")

def percurso():
    frente()
    frente()
    esquerda()
    tras()
    direita()
    tras()
    frente()
    print("Realizando Percurso")
# Loop de controle via terminal
try:
    while True:
        comando = input("Digite comando (frente, tras, esquerda, direita, parar, sair): ").strip().lower()
        if comando == "frente":
            frente()
        elif comando == "tras":
            tras()
        elif comando == "esquerda":
            esquerda()
        elif comando == "direita":
            direita()
        elif comando == "parar":
            parar()
        elif comando == "percurso":
            percurso()
        elif comando == "sair":
            break
        else:
            print("Comando inválido.")
        time.sleep(0.5)  # Pequena pausa para dar tempo ao servo
        pwm_esq.ChangeDutyCycle(0)
        pwm_dir.ChangeDutyCycle(0)

finally:
    pwm_esq.stop()
    pwm_dir.stop()
    GPIO.cleanup()
    print("GPIO liberado. Encerrado.")
