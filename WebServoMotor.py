from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

SERVO_ESQUERDA = 18
SERVO_DIREITA = 27
 
GPIO.setup(SERVO_ESQUERDA, GPIO.OUT)
GPIO.setup(SERVO_DIREITA, GPIO.OUT)

pwm_esq = GPIO.PWM(SERVO_ESQUERDA, 50)
pwm_dir = GPIO.PWM(SERVO_DIREITA, 50)
pwm_esq.start(0)
pwm_dir.start(0)

app = Flask(__name__)

# Duty cycles (ajuste conforme seus servos)
PARAR = 7.5
FRENTE = 6.5
TRAS = 8.5

def frente():
    pwm_esq.ChangeDutyCycle(FRENTE)
    pwm_dir.ChangeDutyCycle(FRENTE)

def tras():
    pwm_esq.ChangeDutyCycle(TRAS)
    pwm_dir.ChangeDutyCycle(TRAS)

def esquerda():
    pwm_esq.ChangeDutyCycle(TRAS)
    pwm_dir.ChangeDutyCycle(FRENTE)

def direita():
    pwm_esq.ChangeDutyCycle(FRENTE)
    pwm_dir.ChangeDutyCycle(TRAS)

def parar():
    pwm_esq.ChangeDutyCycle(PARAR)
    pwm_dir.ChangeDutyCycle(PARAR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    direcao = request.form['direcao']
    if direcao == 'frente':
        frente()
    elif direcao == 'tras':
        tras()
    elif direcao == 'esquerda':
        esquerda()
    elif direcao == 'direita':
        direita()
    elif direcao == 'parar':
        parar()
    return ('', 204)

try:
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5002)
finally:
    pwm_esq.stop()
    pwm_dir.stop()
    GPIO.cleanup()
