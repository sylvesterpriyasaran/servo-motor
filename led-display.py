"""
https://www.circuitschools.com/interfacing-16x2-lcd-module-with-raspberry-pi-pico-with-and-without-i2c/#Method2_Interfacing_16X2_LCD_display_module_with_Raspberry_Pi_Pico_with_I2C_adapter
"""
from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd


pin12 = machine.Pin(8)
pin13 = machine.Pin(9)

i2c = I2C(0, sda=pin12, scl=pin13, freq=400000)


print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
    print("No i2c device !")
else:
    print('i2c devices found:',len(devices))


I2C_ADDR = devices[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
while True:
  print(I2C_ADDR, "| Hex:",hex(I2C_ADDR))
  print()
  lcd.move_to(0,0)
  lcd.putstr("I2CAddress:"+hex(I2C_ADDR)+"\n")
  lcd.move_to(0,1)
  lcd.putstr("CircuitSchools.")
