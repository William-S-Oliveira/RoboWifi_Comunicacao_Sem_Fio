import RPi.GPIO as GPIO
import time

# Configuração dos GPIOs dos servos
SERVO_ESQUERDA = 18
SERVO_DIREITA = 27

# Inicializa GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_ESQUERDA, GPIO.OUT)
GPIO.setup(SERVO_DIREITA, GPIO.OUT)

# PWM com 50Hz (frequência padrão de servo)
pwm_esq = GPIO.PWM(SERVO_ESQUERDA, 50)
pwm_dir = GPIO.PWM(SERVO_DIREITA, 50)

pwm_esq.start(0)
pwm_dir.start(0)

print("Teste de servo - comandos:")
print("[1] Frente")
print("[2] Trás")
print("[3] Esquerda")
print("[4] Direita")
print("[5] Parar")
print("[0] Sair")

try:
    while True:
        cmd = input("Comando: ")
        if cmd == "1":
            pwm_esq.ChangeDutyCycle(6.4)
            pwm_dir.ChangeDutyCycle(6.4)
            print("→ Indo para frente")
        elif cmd == "2":
            pwm_esq.ChangeDutyCycle(8.6)
            pwm_dir.ChangeDutyCycle(8.6)
            print("→ Indo para trás")
        elif cmd == "3":
            pwm_esq.ChangeDutyCycle(7.6)  # parado ou girando devagar
            pwm_dir.ChangeDutyCycle(6.4)  # gira só a direita
            print("→ Virando esquerda")
        elif cmd == "4":
            pwm_esq.ChangeDutyCycle(6.4)
            pwm_dir.ChangeDutyCycle(7.6)
            print("→ Virando direita")
        elif cmd == "5":
            pwm_esq.ChangeDutyCycle(7.5)
            pwm_dir.ChangeDutyCycle(7.5)
            print("→ Parado")
        elif cmd == "0":
            break
        else:
            print("Comando inválido.")

        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    pwm_esq.stop()
    pwm_dir.stop()
    GPIO.cleanup()
    print("GPIO limpo. Teste encerrado.")
