amount = int(input("Enter the Amount:"))


if amount % 100 != 0:
 print("Error: Amount should be multiple of 100")

else:
 note_2000 = amount//2000
 amount %= 2000

 note_500 = amount//500
 amount %= 500

 note_100 = amount//100
 amount %= 100

 print("Currency note to be given:")
 print(f"2000_note:{note_2000}")
 print(f"500_note:{note_500}")
 print(f"100_note:{note_100}")


amount = int(input("Enter the Amount: "))
if amount % 100 != 0: 
   print("Error: Amount should be multiple of 100")
else:
    for n in [2000, 500, 100]:
        print(n,"_note:", amount // n)
        amount %= n
