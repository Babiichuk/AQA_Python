alice_in_wonderland = """ "Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don\'t much care where ——" said Alice.
"Then it doesn\'t matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough." """

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

black_sea_area = 436_402
azov_sea_area = 37_800
all_seas_area = black_sea_area + azov_sea_area
print(f"Площа Азовського та Чорного моря разом становить {all_seas_area} кілометрів квадратних")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

all_stores_goods_quantity = 375_291
first_and_second_store_goods_quantity = 250_449
second_and_third_store_goods_quantity = 222_950
first_store_goods_quantity = all_stores_goods_quantity - second_and_third_store_goods_quantity
third_store_goods_quantity = all_stores_goods_quantity - first_and_second_store_goods_quantity
first_and_third_store_goods_quantity = first_store_goods_quantity + third_store_goods_quantity
second_store_goods_quantity = all_stores_goods_quantity - first_and_third_store_goods_quantity

print(f"""На першому складі перебуває {first_store_goods_quantity} товарів 
на другому складі перебуває {second_store_goods_quantity} товарів
на третьому складі перебуває {third_store_goods_quantity} товарів""")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

one_month_payment_quantity = 1179
loan_period_month = 18
total_price = one_month_payment_quantity * loan_period_month

print(f"Загальна вартість компьютера становить {total_price} гривень")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
remainder_variant_a = 8019 % 8
remainder_variant_b = 9907 % 9
remainder_variant_c = 2789 % 5
remainder_variant_d = 7248 % 6
remainder_variant_e = 7128 % 5
remainder_variant_f = 19224 % 9

print(f"""Остача від ділення 8019 на 8  становить {remainder_variant_a}
остача від ділення  9907 на 9  становить {remainder_variant_b} 
остача від ділення  2789 на 5  становить {remainder_variant_c} 
остача від ділення  7248 на 6  становить {remainder_variant_d} 
остача від ділення  7128 на 5  становить {remainder_variant_e} 
остача від ділення  19224 на 9  становить {remainder_variant_f} """)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_pizza_price = 274
middle_pizza_price = 218
juice_price = 35
pie_price = 350
water_prise = 21

big_pizza_quantity = 4
middle_pizza_quantity = 2
juice_quantity = 4
pie_quantity = 1
water_quantity = 3

total_big_pizza_price = big_pizza_price * big_pizza_quantity
total_middle_pizza_price = middle_pizza_price * middle_pizza_quantity
total_juice_price = juice_price * juice_quantity
total_pie_price = pie_price * pie_quantity
total_water_price = water_prise * water_quantity

cost_of_celebration = total_big_pizza_price + total_middle_pizza_price + total_juice_price + total_pie_price + total_water_price

print(f"На святкування дня народження Іринці потрібно {cost_of_celebration} гривень")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photo_quantity = 232
one_page_capacity = 8
album_pages_quantity = all_photo_quantity //one_page_capacity

if (all_photo_quantity % one_page_capacity) > 0: album_pages_quantity += 1

print(f"Для розміщення всіх його фото Ігору знадобиться {album_pages_quantity} сторінок")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

journey_length = 1600
fuel_liter_on_100_km = 9
tank_capacity = 48

journey_fuel_quantity = journey_length // 100 * fuel_liter_on_100_km
refill_stops_quantity = journey_fuel_quantity // tank_capacity

print(f"Для подорожі знадобиться {journey_fuel_quantity} літрів бензину \n {refill_stops_quantity} разів потрібно зупинитися для заправки ")