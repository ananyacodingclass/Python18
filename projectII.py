guess = input("At n = 1000, o(n^2) takes how many steps? ")

input("Watch o(n) and o(n^2) grow. Please Enter ")
for n in [10, 100, 1000]:
    input("n = " + str(n) + " Press Enter ")
    print(" o(n) =", n, " 0(n^2) =", n * n)

print(" your guess:", guess)
input("Full ladder at n = 1000. Press Enter ")
print(" o(1)=1 o(log n)=10 o(n)=1000 o(n^2)=1,000,000")