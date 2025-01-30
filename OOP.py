# #                             Объекто-ориентированное программирование!
#
# # Обстракция выделение существенных свойств объекта, отличающих его от других объектов.
#
# # Программа - множество объектов (моделей),
# # каждый из которых обладает своими свойствами и поведением, но его внутреннее устройство скрыто от других объектов.
#
#
# # Объектно-ориенгтированный анализ (ООА)
#
# # * Выделить объекты
# # * Определить их существующшие свойства
# # * Описать поведение  (команды, которые они могут выполнять)
#
#
# # Объект - то что имеет четкие границы и обладает состоянием и поведением
#
# # Класс - это множество объектов, имеющих общую структуру и общее поведение
#
#
# # Описани класса
# class Cat:
#     color = "Зеленый"
#     name = "ХАЛК"
#     weight = "Все семерки"
#     height = "Все семерочки"
#     gasses_color = "Черные"
#     age = 0
#     def inf(self):
#         print(f"Имя {self.name}:, цвет {self.color}:, возраст {self.age}")
#
#
# # Объект класса
# cat1 = Cat()
#
# # Вывод объекта во внутреннем формате
# # print(cat1)
# # Вывод свойств объекта
# # print(cat1.age, cat1.name)
#
# # Изменение свойств объекта
# cat1.name = "Лаура"
# cat1.color = "Красивый"
# cat1.age = 16
#
#
# cat1.inf()
#
#
# cat2 = Cat()
#
# cat2.name = "Макс"
# cat2.color = "Крутой"
# cat2.age = 17
#
# cat2.inf()
#
#
# cat3 = Cat()
#
# cat3.name = "Илья Олегович"
# cat3.color = "Учительский"
# cat3.age = 2
#
# cat3.inf()
#







# Защитв нутр данных
# Для проверкивходных данных на коректность
# Изменение устройства с сохранением интерфейса

#  инкапстуляция - скрытие внутреннего устройства объектов


# Изначально все члены класса public
# Имена скрытых полей начинаются с двух знаков подчеркивания private


# class Tpen:
#     def __init__(self):
#         self.__color = "000000"
#         self.__size = 1
#
#
#     def __get_color(self):
#         return self.__color
#
#
#     def __get_size(self):
#         return self.__size
#
#     def __hex(self, x):
#         A = "0123456789ABCDEF"
#         x = x.upper()
#         for i in x:
#             if i in A:
#                 continue
#             else:
#                 return False
#         return True
#
#
#     def __set_color(self, new_color):
#         if type(new_color) is str:
#             if len(new_color) == 6:
#                 if self.__hex(new_color):
#                     self.__color = new_color
#
#
#     def __set_size(self, new_size):
#         if type(new_size) is int:
#             if new_size > 0:
#                 self.__size = new_size
#
#     color = property(__get_color, __set_color)
#     size = property(__get_size, __set_size)
#
# pen1 = Tpen()
# pen1.color = "123456"
# pen1.size = 9
# print(pen1.color, pen1.size)


# pen1.set_color("1234AB")
# pen1.set_size(9)
# print(pen1.get_color())
# print(pen1.get_size())


#
# # print(pen1.__color)
# print()
#
#


# Свойство - способ доступа к внутреннему состоянию объекта, имитирующий обращение его к внутренней переменной








#
# class LampRow:
#     def __init__(self):
#         self.__state = "00000000"
#
#
#     def __get_state(self):
#         return self.__state
#
#
#     def __set_state(self, new_state):
#         if type(new_state) is str:
#             if len(new_state) == 8:
#                 if sum([1 for x in new_state if x in '01']) == 8:
#                     self.__state = new_state
#
#     states = property(__get_state, __set_state)
#
#     def show(self):
#         print(self.__state.replace("0", "-").replace("1", "*"))
#
#
# Lamps = LampRow()
# Lamps.show()
# Lamps.states = "10101010"
# print(Lamps.states)
# Lamps.show()
#



#
#
# class Product:    def __init__(self):
#         self.__name = ''        self.__jir = 0.0
#         self.__bel = 0.0        self.__ugl = 0.0
#         self.__call = 0.0
#     def __get_name(self):        return self.__name
#     def __get_jir(self):
#         return self.__jir
#     def __get_bel(self):        return self.__bel
#     def __get_ugl(self):
#         return self.__ugl
#     def __get_call(self):        return self.__call
#     def __set_name(self, newname):
#         if type(newname) is str:            self.__name = newname
#     def __set_jir(self, newjir):
#         if type(newjir) is float:            if 0.0 <= newjir <= 100.0:
#                 self.__jir = newjir
#     def __set_bel(self, newbel):        if type(newbel) is float:
#             if 0.0 <= newbel <= 100.0:                self.__bel = newbel
#     def __set_ugl(self, newugl):
#         if type(newugl) is float:            if 0.0 <= newugl <= 100.0:
#                 self.__ugl = newugl
#     def __set_call(self, newcall):        if type(newcall) is float:
#             if 0.0 <= newcall:                self.__call = newcall
#     name = property(__get_name, __set_name)
#     jir = property(__get_jir, __set_jir)    bel = property(__get_bel, __set_bel)
#     ugl = property(__get_ugl, __set_ugl)    call = property(__get_call, __set_call)
#     def __str__(self):
#         return f'Продукт - {self.name}, жиры - {self.jir}г, белки - {self.bel}г, углеводы - {self.ugl}г, калорийность - {self.call}.'
# a = open('food.csv').readlines()
# a.pop(0)for i in range(len(a)):
#     a[i] = a[i].replace(',', '.').split(';')[:5]    a[i][1] = float(a[i][1])
#     a[i][2] = float(a[i][1])    a[i][3] = float(a[i][1])
#     a[i][4] = float(a[i][1])
# for i in range(len(a)):    product = Product()
#     product.name = a[i][0]    product.jir = a[i][1]
#     product.bel = a[i][2]    product.ugl = a[i][3]
#     product.call = a[i][4]
# #    print(product)
# product2 = Product()product2.name = 'еда'
# product2.jir = 1.5
# product2.bel = '5.1'product2.ugl = 120.1
# product2.call = -1.5print(product2)
#


#
# class Product:
#     def __init__(self,prod,gir,bel,ugl,kal):
#         self.__prod = prod
#         self.__gir = gir
#         self.__bel = bel
#         self.__ugl = ugl
#         self.__kal = kal
#
#     def __get_prod(self):
#         return self.__prod
#
#     def __get_gir(self):
#         return self.__gir
#
#     def __get_bel(self):
#         return self.__bel
#
#     def __get_ugl(self):
#         return self.__ugl
#
#     def __get_kal(self):
#         return self.__kal
#
#     def __set_prod(self, new_prod):
#         if type(new_prod) is str:
#             self.__prod = new_prod
#
#     def __set_gir(self, new_gir):
#         if type(new_gir) is float:
#             if 0 <= new_gir <= 100:
#                 self.__gir = new_gir
#
#     def __set_bel(self, new_bel):
#         if type(new_bel) is float:
#             if 0 <= new_bel <= 100:
#                 self.__bel = new_bel
#
#     def __set_ugl(self, new_ugl):
#         if type(new_ugl) is float:
#             if 0 <= new_ugl <= 100:
#                 self.__ugl = new_ugl
#
#     def __set_kal(self, new_kal):
#         if type(new_kal) is float:
#             self.__kal = new_kal
#
#     prod = property(__get_prod, __set_prod)
#     gir = property(__get_gir, __set_gir)
#     bel = property(__get_bel, __set_bel)
#     ugl = property(__get_ugl, __set_ugl)
#     kal = property(__get_kal, __set_kal)
#
#     def __str__(self):
#         return f"Продукт - {self.__prod}, Жиры - {self.__gir}, Белки - {self.__bel}, Углеводы - {self.__ugl} Калории - {self.__kal}"
#
# a = open("food ().csv").readlines()
# for i in range(len(a)):
#     a[i] = a[i].replace(",", ".")
#     # a[i] = a[i].replace(";", "")
#     a[i] = a[i].split(";")
#     a[i] = a[i][:5]
#     a[i][0] = str(a[i][0])
#     a[i][1] = float(a[i][1])
#     a[i][2] = float(a[i][2])
#     a[i][3] = float(a[i][3])
#     a[i][4] = float(a[i][4])
#
# o=[]
# a.pop(0)
# for i in range(len(a)):
#     l=Product(*a[i])
#     o.append(l)
# o.sort(key=lambda l: l[5])
# print(o)












# a = open("7U9TE3JMA.txt").readline()
# a = a.replace("-", " ")
# a = a.replace("*", " ")
# a = a.replace("B", " ")
# a = a.replace("C", " ")
# a = a.replace("D", " ")
# while "++" in a or " +" in a or "+ " in a or "A+" in a:
#     a = a.replace("++", " ")
#     a = a.replace(" +", " ")
#     a = a.replace("+ ", " ")
#     a = a.replace("A+", " ")
#     a = a.replace("A", " A")
# a = a.split()
# mx = 0
# for x in a:
#     if len(x) > 1 and x[0] == "A":
#         x = x[1:]
#         mx = max(mx, eval(x))
# print(mx)













################################ИЕРАРХИЯ КЛАССОВ

# Разделение изучаемых классов на группы (классы), объединенные общими признаками
#            ФРУКТ
#          /  |  |  \
#        /    |  |   \
#  Яблоко Груша Банан Апельсин

# Класс Б ялвляется наследником класса А, сели можэно сказать, что Б - это разновидность А.

# Объектно ариентированноен программирование - это такой подход к программированию, при котором программа представляет собой множество взаимодействующих объектов, каждый из которых является экземпляром определенного класса, а классы образуют иерархию наследованияю








# class Pet:
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight
#         if hasattr(self, "sound"):
#             pass
#         else:
#             raise NotImplementedError("ЭУУУ, ты! Нельзя создать такой объект!!!!!")
#     def pr(self):
#         return f"Имя имеет: {self.name}, Цвет имеет: {self.color}"
#
#
# class Cat(Pet):
#     def __init__(self, name, color, weight, count):
#         Pet.__init__(self, name, color, weight)
#         self.count = count
#     def sound(self):
#         return "МЯЯЯЯЯЯЯЯЯЯУУУУУУ!!!!!!!"
#
# pat1 = Pet(4 ,5, 6)

# cat1 = Cat("Лешик", "Красивый", 4, 10)
# print(cat1.sound())















# Абстрактный класс - класс, содержащий хотя бы один абстрактный метод
# Абстрактный метод - метод класса, который объявляется, но не реализуется в классе


# class Pet:
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight
#         if hasattr(self, "sound"):
#             pass
#         else:
#             raise NotImplementedError("ЭУУУ, ты! Нельзя создать такой объект!!!!!")
#     def pr(self):
#         return f"Имя имеет: {self.name}, Цвет имеет: {self.color}"
#
#
# class Dog(Pet):
#     def __init__(self, name, color, weight, numder):
#         Pet.__init__(self, name, color, weight)
#         self.number = numder
#     def sound(self):
#         return "ГАААВВ!"
#
#
# class Cat(Pet):
#     def __init__(self, name, color, weight, count):
#         Pet.__init__(self, name, color, weight)
#         self.count = count
#     def sound(self):
#         return "МЯЯЯЯЯЯЯЯЯЯУУУУУУ!!!!!!!"
#
#
# class Parrot(Pet):
#     def __init__(self, name, color, weight, color_or_cletka):
#         super().__init__(name, color, weight)
#         self.color_or_cletka = color_or_cletka
#     def sound(self):
#         return "Лешка дурак!!!!!!"
#
#
# cat1 = Cat("Лаурик", "Красивый", 4, 10)
# dog1 = Dog("Максим", "Классный", 30, 13)
# parrot1 = Parrot("Лешка", "Глупый", 0, "Страшная")
# print(cat1.pr())
# print(cat1.sound())
# print(dog1.pr())
# print(dog1.sound())
# print(parrot1.pr())
# print(parrot1.sound())


# Полимарфизм = это возможность классов-наследников по-разному реализовать метод с одним и тем же именем



class TLogElement:
    """Базовый класс для логического элемента."""
    def __init__(self):
        self.__in1 = 0
        self.__in2 = 0
        self._res = 0
        if hasattr(self, "_calc"):
            pass
        else:
            raise NotImplementedError("Нелья создать такой объект!!!")

    def __setIn1(self, newIn1):
        if newIn1 in (0,1):
            self.__in1 = newIn1
            self._calc()

    def __setIn2(self, newIn2):
        if newIn2 in (0,1):
            self.__in2 = newIn2
            self._calc()

    In1 = property(lambda x: x.__in1, __setIn1)
    In2 = property(lambda x: x.__in2, __setIn2)
    Res = property(lambda x: x._res)


class TNot(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = int(not(self.In1))


class TAnd(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = self.In1 * self.In2


class TOr(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        if self.In1 + self.In2 == 0:
            self._res = 0
        else:
            self._res = 1


class TEk(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        if (self.In1 + self.In2) % 2 == 0:
            self._res = 1
        else:
            self._res = 0


class TAndNot(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        if (self.In1 + self.In2) == 2:
            self._res = 0
        else:
            self._res = 1


class TOrNot(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        if (self.In1 + self.In2) == 0:
            self._res = 1
        else:
            self._res = 0


class TXor(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)
    def _calc(self):
        if (self.In1 + self.In2) % 2 == 0:
            self._res = 0
        else:
            self._res = 1


class TImp(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)
    def _calc(self):
        if not(self.In1) <= self.In2:
            self._res = 0
        else:
            self._res = 1


class TTriger(TLogElement):
    def __init__(self, Q):
        TLogElement.__init__(self)
        self.Q = Q
    def _calc(self):
        if self.Q == 0:
            if self.In1 >= self.In2 and self.In1 + self.In2 > 0:
                self._res = 1
            else:
                self._res = 0
        elif self.Q == 1:
            if self.In1 < self.In2:
                self._res = 0
            else:
                self._res = 1


# И НЕ
# И ИЛИ НЕ



















