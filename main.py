try:
    
    #stetic
    
    from termcolor import colored
    from colorama import init
    
    #functional
    
    import math
    import time
    from datetime import datetime
    
    #My own Modules
    
    from exceptions import ErrorDeValor
    
except ImportError:
    
    print(colored('Debes importar los modulos requridos en requeriments.txt', 'light_red'))
    
    
# main

while True:
    
    print(colored('<------------------------------------------------------>\n', 'red'))
    print(colored('                 Calculadora Python\n', 'light_yellow'))
    print(colored('<------------------------------------------------------>\n', 'red'))
    
    
    fecha = f'{datetime.now().day} / {datetime.now().month} / {datetime.now().year}:'
    
    importante = input(colored('Selecciona una opción:\n1.Sumar\n2.Restar\n3.Dividir\n4.Multiplicar\n5.Raíz Cuadrada\n6.Salir\n', 'light_blue'))
    
    if importante == '1':
        while True:
            
            try:
                
                op1 = int(input(
                    colored(
                        'Dime el primer número:\n', 'red'
                        )
                    )   
                )
                
                op2 = int(
                    input(
                        colored(
                            'Dime el segundo número:\n', 'red'
                        )
                    )
                )
                
                print(
                    colored(
                        '{} Cargando resultado...'.format(fecha), 'red'
                    )
                )
                
                time.sleep(2)
                
                print(colored('Respuesta = {}\n'.format(sum([op1, op2])), 'red'))
                
            except:
                
                try:
                    
                    raise ErrorDeValor(
                        colored (
                            
                            '*No escribas Letras*\n', 'red'
                            
                        )
                    )
                
                except:
                    
                    None    
                
                continue
            
            else:
                
                break
            
    elif importante == '2':
        
        while True:
            
            try:
                
                op1 = int(input(
                    colored(
                        'Dime el primer número:\n', 'red'
                        )
                    )   
                )
                
                op2 = int(
                    input(
                        colored(
                            'Dime el segundo número:\n', 'red'
                        )
                    )
                )
                
                print(
                    colored(
                        '{} Cargando resultado...\n'.format(fecha), 'red'
                    )
                )
                
                time.sleep(2)
                
                print(colored('Respuesta = {}\n'.format(op1 - op2), 'red'))
                
            except:
                
                try:
                    
                    raise ErrorDeValor(
                        colored (
                            
                            '*No escribas Letras*\n', 'red'
                            
                        )
                    )
                
                except:
                    
                    None    
                
                continue
            
            else:
                
                break
            
    elif importante == '3':
        
        while True:
            
            try:
                
                op1 = int(input(
                    colored(
                        'Dime el primer número:\n', 'red'
                        )
                    )   
                )
                
                op2 = int(
                    input(
                        colored(
                            'Dime el segundo número:\n', 'red'
                        )
                    )
                )
                
                
                if op1 != 0 and op2 != 0:
                    
                    print(
                        colored(
                            '{} Cargando resultado...\n'.format(fecha), 'red'
                        )
                    )
                
                    time.sleep(2)
                        
                    print(colored('Respuesta = {}\n'.format(op1 / op2), 'red'))
                
                else:
                    
                    print(
                        colored(
                            'No puedes dividir entre 0\n', 'red'
                        )
                    )
                    
                    continue    
                
            except:
                
                try:
                    
                    raise ErrorDeValor(
                        colored (
                            
                            '*No escribas Letras*\n', 'red'
                            
                        )
                    )
                
                except:
                    
                    None    
                
                continue
            
            else:
                
                break
    
    elif importante == '4':
        
         while True:
            
            try:
                
                op1 = int(input(
                    colored(
                        'Dime el primer número:\n', 'red'
                        )
                    )   
                )
                
                op2 = int(
                    input(
                        colored(
                            'Dime el segundo número:\n', 'red'
                        )
                    )
                )
                
                print(
                    colored(
                        '{} Cargando resultado...'.format(fecha), 'red'
                    )
                )
                
                time.sleep(2)
                
                print(colored('Respuesta = {}\n'.format(op2 * op2), 'red'))
                
            except:
                
                try:
                    
                    raise ErrorDeValor(
                        colored (
                            
                            '*No escribas Letras*\n', 'red'
                            
                        )
                    )
                
                except:
                    
                    None    
                
                continue
            
            else:
                
                break
            
    elif importante == '5':
        
        while True:
            
            try:
                
                num = int(input(
                    colored(
                        'Dime el número:\n', 'red'
                        )
                    )   
                )
                
                time.sleep(2)    
                print(colored('Respuesta = {}\n'.format(math.sqrt(num)), 'red'))
                
            except:
                
                try:
                    
                    raise ErrorDeValor(
                        colored (
                            
                            '*No escribas Letras*\n', 'red'
                            
                        )
                    )
                
                except:
                    
                    None    
                
                continue
            
            else:
                
                break
                
    if importante == '6':
        
        exit = input(colored('Desea Salir del Programa? (y/n)'))
        
        if exit == 'y':
            break
        else:
            continue
        
