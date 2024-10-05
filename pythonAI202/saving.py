import numpy as np
import matplotlib.pyplot as plt

#saving account with initial balance a0 = 1000, interest rate %1, withdraw 50 every month, how many moths until the balance hits zero?

def saving(a0, interest_rate_percent , withdraw, N):
    a = np.empty(N+1, dtype=float)
    a[0] = a0
    n = [0]

    for i in range(1, N+1):
        a[i] = a[i-1] + interest_rate_percent/100 * a[i-1] - withdraw
        n.append(i)

    n = np.array(n)

    for j in range (1, N+1):
        print("Month: ", n[j], "Balance:", a[j])


    plt.plot(n, a)
    plt.grid(True)
    plt.xlabel('Month')
    plt.ylabel('Balance')
    plt.savefig('saving.png')
    plt.show()

if __name__ == "__main__":
    saving(1000,1,50,30)





