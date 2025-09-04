amount = int(input("Enter amount: "))
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 1]

for note in notes:
    if amount >= note:
        count = amount // note
        amount %= note
        print(f"{note} : {count}")
