from time import *
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

sleep(0.1) # Wait for USB to become ready

# Дисплей
WIDTH = 128
HEIGHT = 64
i2c = I2C(0,scl=Pin(1),sda=Pin(0),freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

# Кнопки
btn_red = Pin(9, Pin.IN)
btn_blue = Pin(14, Pin.IN)

# Светодиоды
led_red = Pin(7, Pin.OUT)
led_blue = Pin(26, Pin.OUT)

# Моторы
Am1 = Pin(13, Pin.OUT)
Ap1 = Pin(12, Pin.OUT)
Bp1 = Pin(11, Pin.OUT)
Bm1 = Pin(10, Pin.OUT)

Am2 = Pin(21, Pin.OUT)
Ap2 = Pin(20, Pin.OUT)
Bp2 = Pin(18, Pin.OUT)
Bm2 = Pin(19, Pin.OUT)


# функция запуска моторов
def engine(Ap, Am, Bm, Bp):
    
  sleep_ms(1)
  Bm.value(0) # Bm выключить
  Ap.value(1) # Ap включить

  sleep_ms(1)
  Ap.value(0)
  Bp.value(1)

  sleep_ms(1)
  Bp.value(0)
  Am.value(1)

  sleep_ms(1)
  Am.value(0)
  Bm.value(1)


while 1:
  if btn_red.value(): # если нажать на красную кнопку, 
    led_red.toggle() # включится красный светодиод
    oled.text("LED RED is ON", 20, 10) # Вывести информацию на дисплей
    oled.show()
    sleep(0.1)
    if led_red.value() == 1: # если красный светодиод включен, 
      while 1:
        engine(Ap1, Am1, Bm1, Bp1) # включить двигатель 1
        engine(Ap2, Am2, Bm2, Bp2) # включить двигатель 2
        led_blue.value(1) # включить синий светодиод
        # Вывести информацию на дисплей
        oled.text("MOTOR 1 is ON", 20, 10)
        oled.text("MOTOR 2 is ON", 20, 10)
        oled.text("LED BLUE is ON", 20, 10)
        oled.show()
        if btn_blue.value(): # если нажать на синюю кнопку, 
          led_red.toggle() # красный светодиод выключится
          sleep(0.1)
          if led_red.value() == 0: # если красный светодиод выключен
            led_blue.value(0) # выключить синий светодиод
            # Вывести информацию на дисплей
            oled.text("LED RED is OFF", 20, 10)
            oled.text("LED BLUE is OFF", 20, 10)
            oled.text("MOTOR 1 is OFF", 20, 10)
            oled.text("MOTOR 2 is OFF", 20, 10)
            oled.show()
            break # прерывать выполнение цикла
            

