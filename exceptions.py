
#Error Personalizado

class ErrorDeValor (Exception):
        
    def __init__ (self, error):
            
        print('Error de valor: {}'.format(error))
