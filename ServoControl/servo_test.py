from machine import Pin, PWM
import utime

pwm = PWM(Pin(15))
pwm.freq(50)

#min 1700
#max 8420
#90 deg = 4900


# pwm.duty_u16(4900)

# duty = 1700

# while(duty <= 8420):
#   pwm.duty_u16(duty)
#   utime.sleep(0.5)
#   duty += 20
#   print(f"duty:{duty}")

while True:
    pwm.duty_u16(1700)
    utime.sleep(1.0)
    pwm.duty_u16(4900)
    utime.sleep(0.5)
    pwm.duty_u16(8420)
    utime.sleep(1.0)
    pwm.duty_u16(4900)
    utime.sleep(0.5)
    

