# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
print(banana)


# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""

# так як в умові сказано щоб було зрозуміло дитині з 2го класу
# окрім розрахунків виведу ще пояснення

appletree = 4
peartree = appletree+5
plumtree = appletree-2
alltrees = appletree + peartree + plumtree

print("Так як ми знаєм що ми посадили 4 яблуні а груш НА 5 БІЛЬШЕ то ми виконуєм додавання щоб взнати скільки буде груш")
print(f"Отож кількість груш буде 4+5={peartree}")
print(" ")
print("Так як ми знаєм що ми посадили 4 яблуні а слив НА 2 МЕНШЕ то ми виконуєм віднімання щоб взнати скільки буде слив")
print(f"Отож кількість слив буде 4-2={plumtree}")
print("А щоб взнати загальну кількість дерев потрібно тепер виконати додавання всіх дерев")
print(f"Отож загальна кількість дерев буде 4+9+2={alltrees}" )

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
morning_temperature = 0 + 5
afternoon_temperature = morning_temperature - 10
evening_temperature = afternoon_temperature + 4


print("Для початку взнаєм температуру зранку")
print(f"для цього додаєм до нуля 5, 0+5={morning_temperature}")
print("")
print("Тепер взнаєм температуру після обіду")
print(f"для цього віднімаям 10 від температури зранку {morning_temperature}-10={afternoon_temperature}")
print("")
print("Тепер взнаєм температуру ввечері")
print(f"для цього додаєм 4 до температури після обіду {afternoon_temperature}+4={evening_temperature}")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys_quantity = 24
girls_quantity = boys_quantity / 2
today_boys_quantity = boys_quantity - 1
today_girls_quantity = girls_quantity-2
today_members_quantity = today_boys_quantity+today_girls_quantity

print("Для початку потрібно взнати кількість дівчаток взагалі")
print(f"отже ділимо 24 на 2, 24/2={girls_quantity}")
print("")
print(f"Тепер взнаєм скільки хлопчиків прийшло сьогодні {boys_quantity}-1={today_boys_quantity}")
print(f"також взнаєм скільки дівчаток прийшло сьогодні {girls_quantity}-2={today_girls_quantity}")
print(f"і взнаєм скільки дітей прийшло сьогодні, для цього виконуєм додавання {today_boys_quantity}+{today_girls_quantity}={today_members_quantity}")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book_price = 8
second_book_price = first_book_price+2
third_book_price = (first_book_price+second_book_price)/2
common_book_price = first_book_price+second_book_price+third_book_price

print(f"Спочатку взнаєм скільки коштує друга книжка, виконуєм додавання {first_book_price}+2={second_book_price}")
print("далі взнаєм скільки коштує третя книжка, виконуєм додавання першої і другої книжки а потім ділимо результат на 2")
print(f"({first_book_price}+{second_book_price})/2={third_book_price}")
print(f" і виконуєм додавання всіх книжок{first_book_price}+{second_book_price}+{third_book_price}={common_book_price}")
