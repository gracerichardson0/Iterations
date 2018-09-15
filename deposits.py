def deposits(balance, numDep) :
    for count in range (1, n+1) :
        amount = float (input ("Enter deposit #", count))
        balance += amount
    return balance

balance = float (input ("enter initial balance $"))
print ("Original balance: $", balance)
n = int (input ("Enter # deposits: "))

print ("Original balance: $", balance, "\nAfter ",n, " deposits, final balance: $", deposits(balance, n))