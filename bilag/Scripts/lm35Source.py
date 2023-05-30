from machine import ADC, Pin, PWM
from time import sleep_ms

adcTemp = ADC(Pin(36))             
adcTemp.atten(adcTemp.ATTN_0DB)

adcOffset = 2.1
adc2temp = 120.0 / 4095.0                                  # 10 mV/°C, 1200 mV full range i.e. 120 °C

average = 8

print("LM35 test\n")

while True:
    if average > 1:
        adcVal = 0
        for i in range (average):
            adcVal += adcTemp.read()
            sleep_ms(int(1000 / average))
        adcVal = adcVal / average
    else:
        adcVal = adcTemp.read()
        sleep_ms(1000)
    
    temp = adc2temp * adcVal + adcOffset
    print("ADC: %3d -> %2.1f °C " % (adcVal, temp))
    