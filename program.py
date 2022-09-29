from math import sqrt


message = ['Добро пожаловать в самую лучшую программу для вычисления',
          'квадратного корня из заданного числа']

def  Calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)

def calc(your_number) :
    if your_number <= 0:
        return    
     
    root = 0
    answer = Calculate_square_root(your_number)
    print(f'Мы вычислили корень квадратный из введенного вами числа. Это будет: {answer}')