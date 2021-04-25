import random
from random import randint
print("Моделирование игры в виде консольного приложения")
print("Участниками являются Компьютер и Игрок")
print("Последовательность шагов определяется случайным образом(сильный удар, нормальный удар, исцеление")
print("У каждого из игроков одинаковое количество здоровья - 100 единиц)")
print("Когда здоровье Компьютера достигает 35% его шанс на использование исцеления повышается до 70%")

# Создаем список вероятности нанесения определенного шага
class ProbabilitySteps:
    powerHit = 90
    normalHit = 90
    healing = 10

# Создаем список количества единиц здоровья игроков
class HealthPlayers:
    player = 100
    computer = 100


class RangeHit(object):
   # Создаем функцию расчета диапазона силы шага
    def __init__(self,minimum_value, maximum_value):
        self.random = random.randint(minimum_value,maximum_value)
        
# Создаем класс действия Игрока
class PlayerAction():
      # Создаем функцию расчета нанесения определенного шага
      def method(self):
        # Задаем вероятность для кажого дейсвия
        ran = random.choices(['p','n', 'h'], \
            weights=[45,45,10])
        if ran == ['p']:
           power = RangeHit(18,25) 
           x = HealthPlayers.computer - power.random
           HealthPlayers.computer = x
           # Визуально выводим значение здоровье 0 на последний удар
           if x < 0:
                x = 0
           # Возвращаем строку в зависимости от выбранного действия с уроном и здроровем  
           return ' [сильный удар] ' + 'и нанес ' + str(power.random) + ' урона ' + \
             " \n --- Здоровье компютера " + str(x) + " очков"
        elif ran == ['n']: 
             normal = RangeHit(10,30)
             x = HealthPlayers.computer - normal.random
             HealthPlayers.computer = x
             if x < 0:
                x = 0
             # Повторим для каждого варианта действия   
             return  ' [номальный удар] ' + 'и нанес ' + str(normal.random) + ' урона ' + \
             " \n --- Здоровье компютера " + str(x) + " очков"
        else: 
             healing = RangeHit(18,25)
             x = HealthPlayers.player + healing.random
             HealthPlayers.player = x
             if x < 0:
                x = 0
             return  ' [исцеление]' + ' востонавливает ' + str(healing.random) + ' очков здоровья' + \
             " \n ---- Здоровье игрока " + str(x) + " очков"
# Создаем класс действия Компьютера
class ComyterAction():

      def method(self):
        # Создаем условие при котором Компьютер имеет повышенный шанс исцеления
        if HealthPlayers.computer <= 35:
            ProbabilitySteps.powerHit = 15
            ProbabilitySteps.normalHit = 15
            ProbabilitySteps.healing = 70
            print(" *** Шанс исцеление компютера равен 70 %")
        else:  
            ProbabilitySteps.powerHit = 90
            ProbabilitySteps.normalHit = 5
            ProbabilitySteps.healing = 5 
        ran = random.choices(['p','n', 'h'], \
            weights=[ProbabilitySteps.powerHit,ProbabilitySteps.normalHit,ProbabilitySteps.healing])
        if ran == ['p']:
           power = RangeHit(18,25) 
           x = HealthPlayers.player - power.random
           HealthPlayers.player = x
           if x < 0:
                x = 0
           return ' [сильный удар] ' + 'и нанес ' + str(power.random) + ' урона ' + \
             " \n --- Здоровье игрока " + str(x) + " очков"
        elif ran == ['n']: 
             normal = RangeHit(10,30)
             x = HealthPlayers.player - normal.random
             HealthPlayers.player = x
             if x < 0:
                x = 0
             return  ' [номальный удар] ' + 'и нанес ' + str(normal.random) + ' урона ' + \
             " \n --- Здоровье игрока " + str(x) + " очков"
        else: 
             healing = RangeHit(18,25)
             x = HealthPlayers.computer + healing.random
             HealthPlayers.computer = x
             if x < 0:
                x = 0
             return  ' [исцеление]' + ' востонавливает ' + str(healing.random) + ' очков здоровья' + \
             " \n --- Здоровье комютера " + str(x) + " очков"



# Создадим класс выполнения действия для каждого из участников
class RoundPlayer:

    def hit(self):
  
        return '\n >>> Игрок использовал' + str(b.method()) 

class RoundComputer:            
    def hit(self):
  
        return ' >>> Компютер использовал' + str(c.method())


i = 0
# Определяем последовательность первого хода
random_number = randint(0, 1)
if random_number == 0:
   print("\n +++ Игрок ходит первый\n") 
   # Создадим условный оператор с условием
   while i == 0:
     a = RoundPlayer()
     f = RoundComputer()
     b = PlayerAction()
     c = ComyterAction()
     print(a.hit())
     # Создадим условие прекрощенния боя   
     if HealthPlayers.computer <= 0:
       
       print("\n Игра окончена победил Игрок\n")
       break
     print(f.hit())
     if HealthPlayers.player <= 0:

       print("\n Игра окончена победил Компьютер\n")   
       break  
else:
    print("\n +++ Компьютер ходит первый\n")
   
    while i == 0 :
     a = RoundPlayer()
     f = RoundComputer()
     b = PlayerAction()
     c = ComyterAction()
    
     print(f.hit())
    
     if HealthPlayers.player <= 0:
        
        print("\n Игра окончена победил Компьютер\n") 
        break
     print(a.hit())

     if HealthPlayers.computer <= 0:
       print("\n Игра окончена победил Игрок\n")
         
       break; 
       
    


   
 