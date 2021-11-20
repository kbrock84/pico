import machine
import utime
from ssd1306 import SSD1306_I2C
from mpu9250 import MPU9250

def format_nums(nums):
    ret_strs = ["", "", ""]
    for n in range(3) :
        ret_strs[n] = "{:.1f}".format(nums[n])
        
    return ret_strs

            

sda=machine.Pin(16)
scl=machine.Pin(17)

Hardi2c=machine.I2C(0, sda=sda, scl=scl, freq=200000)

sensor = MPU9250(Hardi2c)
print(sensor.acceleration)
print(sensor.gyro)
print(sensor.magnetic)
print(sensor.temperature)

print(f"Hardi2C{Hardi2c.scan()}")

oled = SSD1306_I2C(128, 64, Hardi2c)


for n in range(200):
    oled.fill(0)
    accNums = format_nums(sensor.magnetic)
    oled.text(f"x: {accNums[0]}", 0, 0)
    oled.text(f"y: {accNums[1]}", 0, 20)
    oled.text(f"z: {accNums[2]}", 0, 40)
    oled.show()
    
oled.poweroff()
