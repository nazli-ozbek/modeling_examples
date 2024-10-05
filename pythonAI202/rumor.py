import numpy as np
import matplotlib.pyplot as plt

#spreading a rumor to a company of 1000 employees, spread of rumor as a contagious disease
#r0=number of people who started the rumor k=proportionality constant n=number of employees, d=number of days
def rumor(r0, k, n, d):
    spread = np.empty(d+1, dtype=float)
    spread[0] = r0
    days = [0]

    for i in range(1, d+1):
        spread[i] = spread[i-1] + k * spread[i-1] * (n - spread[i-1])
        days.append(i)

    days = np.array(days)

    for j in range(1, d+1):
        print(f"Day: {days[j]} Spread: {spread[j]} Percentage: {(float)(spread[j]/n) * 100}")

    plt.plot(days, spread)
    plt.grid(True)
    plt.title('Rumor Spread Over Time')
    plt.xlabel('Days Passed')
    plt.ylabel('# of people who know about the rumor')
    plt.savefig('rumor.png')
    plt.show()

if __name__ == "__main__":
    rumor(4,0.001,1000,30)

