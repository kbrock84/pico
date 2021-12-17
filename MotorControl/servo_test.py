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
    utime.sleep(1)
    pwm.duty_u16(8000)
    utime.sleep(1)
    pwm.duty_u16(10000)
    utime.sleep(1)
    pwm.duty_u16(20000)
    utime.sleep(1)
    pwm.duty_u16(30000)
    utime.sleep(1)
    pwm.duty_u16(0)
    utime.sleep(1)



    

