from classes import Knight

knight1 = Knight("Sir Lancelot", 10, army=10000)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20, army=20000)  # Высокий уровень умения

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("Все битвы закончились!")
