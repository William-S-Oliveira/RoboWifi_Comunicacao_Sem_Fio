import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PINO_ESQUERDO = 18
PINO_DIREITO = 27

GPIO.setup(PINO_ESQUERDO, GPIO.OUT)
GPIO.setup(PINO_DIREITO, GPIO.OUT)

pwm_esq = GPIO.PWM(PINO_ESQUERDO, 50)
pwm_dir = GPIO.PWM(PINO_DIREITO, 50)

pwm_esq.start(0)
pwm_dir.start(0)

parar_esq = None
parar_dir = None

try:
    print("Iniciando calibração dos dois servos.")
    print("Tente valores entre 7.0 e 8.0. Ex: 7.5 para tentativa de parada.")

    while parar_esq is None or parar_dir is None:
        val_esq = float(input("Digite valor para motor ESQUERDO: "))
        val_dir = float(input("Digite valor para motor DIREITO: "))

        pwm_esq.ChangeDutyCycle(val_esq)
        pwm_dir.ChangeDutyCycle(val_dir)

        time.sleep(1.5)

        pwm_esq.ChangeDutyCycle(0)
        pwm_dir.ChangeDutyCycle(0)

        resposta = input("Os dois motores pararam corretamente? (s/n): ").strip().lower()

        if resposta == 's':
            parar_esq = val_esq
            parar_dir = val_dir
            break
        else:
            print("Continuando testes...\n")

    print("\n Calibração concluída!")
    print(f"Valor de PARAR motor ESQUERDO: {parar_esq}")
    print(f"Valor de PARAR motor DIREITO: {parar_dir}")

except KeyboardInterrupt:
    print("\nInterrompido pelo usuário.")
finally:
    pwm_esq.stop()
    pwm_dir.stop()
    GPIO.cleanup()
