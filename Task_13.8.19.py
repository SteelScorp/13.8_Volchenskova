TicketCount = int(input("Введите количество билетов к покупке:\t"))
AgeList = [int(input(f"Введите возраст для билета №{i+1}:\t")) for i in range(TicketCount)]

FinalPrice = 0

for age in range(len(AgeList)):
    if 18 <= AgeList[age] <= 25:
        FinalPrice += 990
    elif AgeList[age] > 25:
        FinalPrice += 1390

if FinalPrice != 0 and TicketCount > 3:
    FinalPrice -= FinalPrice * 0.1
    print(f"Итоговая стоимость билетов со скидкой 10%: {FinalPrice} ₽")
else:
    print(f"Итоговая стоимость билетов: {FinalPrice} ₽")
