bal = input('what is the initial balance on the account?: ')
per = input('what % are you expecting annually?: ')
time = input('for how many years yo you want to invest?: ')

def interestEarn(balance, rate):
    return balance * (rate / 100.)

def compound(balance, rate):
    return balance + interestEarn(balance, rate)

for i in range(0,time):
    bal = compound(bal, per)
print 'after', time, 'years the balance is', bal
