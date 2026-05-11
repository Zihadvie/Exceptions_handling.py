
try:
    N1 = int(input("Give me a number : "))
    N2 = int(input("Give me a number : "))
    result=N1/N2
    print(f"{result:.2f}")
except Exception as e:                                #all type of exception(ValueError,TypeError,ZeroDivision etc) its work able
   print(f"You can not divide by string{e}")

finally:
    print("Congratulations!")
