#1
roy = [1, 2, 3, 4, 5]
print(f"Sonlar ro'yxati: {roy}")

natija = list(map(lambda el: el * 2, roy))
print(natija)


#2
roy = [10, 20, 30, 40]
print(f"Sonlar ro'yxati: {roy}")

natija = list(map(lambda el: el - 5, roy))
print(natija)


#3
roy = ["apple", "banana", "cherry"]
print(f"Ro'yxat: {roy}")

natija = list(map(lambda el: el.upper(), roy))
print(natija)


#4
roy = ["salom", "dunyo", "python"]
print(f"Ro'yxat: {roy}")

natija = list(map(lambda el: len(el), roy))
print(natija)


#5
roy = [3, 6, 9, 12]
print(f"Ro'yxat: {roy}")

natija = list(map(lambda el: el ** 2, roy))
print(natija)
