import lcddriver
import time

if __name__ == '__main__':
    
    "variables"
    lcd = lcddriver.lcd()#object
    loading,loading2 = "",""
    
    lcd.lcd_clear()
    lcd.lcd_display_string("Menu de Opciones",1)
    while loading<=("."*8):
        lcd.lcd_display_string(f"Cargando{loading}",2)
        loading+= "."
        time.sleep(0.3)
    lcd.lcd_clear()
    
    lcd.lcd_display_string("Elige una opcion",1)
    while loading2<=("."*8):
        lcd.lcd_display_string(f"Cargando{loading2}",2)
        loading2+= "."
        time.sleep(0.3)
    lcd.lcd_clear()
        
    lcd.lcd_display_string("1(+) 2(-) o(or)",1)
    lcd.lcd_display_string("3(*) 4(/) &(and)",2)
    
    op = input("Elige una Opcion: ")
    
    if op =='1':
        lcd.lcd_clear()
        lcd.lcd_display_string("Digite valor1",1)
        num1 = int(input("num1 : "))
        lcd.lcd_display_string(f"Ingresaste {num1}",2)
        time.sleep(0.9)
        
        lcd.lcd_clear()
        lcd.lcd_display_string("Digite valor2:",1)
        num2 = int(input("num2 : "))
        lcd.lcd_display_string(f'Ingresaste {num2}',2)
        time.sleep(0.9)
        
        lcd.lcd_clear()
        lcd.lcd_display_string(f"Resultado : {num1+num2}",1)
        lcd.lcd_display_string(f"Cargando...",2)
        time.sleep(3)
        
    elif op =='2':
        lcd.lcd_clear()
        lcd.lcd_display_string("Digite valor1",1)
        num1 = int(input("num1 : "))
        lcd.lcd_display_string(f"Ingresaste {num1}",2)
        time.sleep(0.9)
        
        lcd.lcd_clear()
        lcd.lcd_display_string("Digite valor2:",1)
        num2 = int(input("num2 : "))
        lcd.lcd_display_string(f'Ingresaste {num2}',2)
        time.sleep(0.9)
        
        lcd.lcd_clear()
        lcd.lcd_display_string(f"Resultado : {num1-num2}",1)
        lcd.lcd_display_string(f"Cargando...",2)
        time.sleep(3)
    elif op =='3':
        lcd.lcd_clear()
        lcd.lcd_display_string("Digite valor1",1)
        num1 = int(input("num1 : "))
        lcd.lcd_display_string(f"Ingresaste {num1}",2)
        time.sleep(0.9)
        
        lcd.lcd_clear()
        lcd.lcd_display_string("Digite valor2:",1)
        num2 = int(input("num2 : "))
        lcd.lcd_display_string(f'Ingresaste {num2}',2)
        time.sleep(0.9)
        
        lcd.lcd_clear()
        lcd.lcd_display_string(f"Resultado : {num1*num2}",1)
        lcd.lcd_display_string(f"Cargando...",2)
        time.sleep(3)
    elif op =='4':
        lcd.lcd_clear()
        lcd.lcd_display_string("Digite valor1",1)
        num1 = float(input("num1 : "))
        lcd.lcd_display_string(f"Ingresaste {num1}",2)
        time.sleep(0.9)
        
        lcd.lcd_clear()
        lcd.lcd_display_string("Digite valor2:",1)
        num2 = float(input("num2 : "))
        lcd.lcd_display_string(f'Ingresaste {num2}',2)
        time.sleep(0.9)
        
        lcd.lcd_clear()
        lcd.lcd_display_string(f"Resultado : {num1/num2}",1)
        lcd.lcd_display_string(f"Cargando...",2)
        time.sleep(3)
    elif op.lower() =='o':
        lcd.lcd_clear()
        lcd.lcd_display_string("Entrada 1",1)
        num1 = int(input("num1 : "))
        lcd.lcd_display_string(f"Ingresaste {num1}",2)
        time.sleep(0.9)
        
        lcd.lcd_clear()
        lcd.lcd_display_string("Entrada 2:",1)
        num2 = int(input("num2 : "))
        lcd.lcd_display_string(f'Ingresaste {num2}',2)
        time.sleep(0.9)
        
        lcd.lcd_clear()
        lcd.lcd_display_string(f"Resultado : {num1 or num2}",1)
        lcd.lcd_display_string(f"Cargando...",2)
        time.sleep(3)
    elif op.lower() =='&':
        lcd.lcd_clear()
        lcd.lcd_display_string("Entrada 1",1)
        num1 = int(input("num1 : "))
        lcd.lcd_display_string(f"Ingresaste {num1}",2)
        time.sleep(0.9)
        
        lcd.lcd_clear()
        lcd.lcd_display_string("Entrada 2:",1)
        num2 = int(input("num2 : "))
        lcd.lcd_display_string(f'Ingresaste {num2}',2)
        time.sleep(0.9)
        
        lcd.lcd_clear()
        lcd.lcd_display_string(f"Resultado : {num1 and num2}",1)
        lcd.lcd_display_string(f"Cargando...",2)
        time.sleep(3)
    else:
        lcd.lcd_clear()
        lcd.lcd_display_string(f'Opcion Invalida',1)
        lcd.lcd_display_string(f"Regresando...",2)
        time.sleep(3)
        
        
             
    
    lcd.lcd_clear()
    lcd.lcd_display_string(f'Fin Programa..',1)
    print('Fin del Programa')
    