import numpy as np
import matplotlib.pyplot as plt

#spread of a disease i0 = # of initially infected people p = population
# w= number of weeks, d = duration of disease(weeks), k = correlation coefficient

def SIR_Model(i0, p, w, d, k):
    i = np.empty(w+1, dtype=float)
    i[0] = i0
    r = np.empty(w+1, dtype=float)
    r[0] = 0
    s = np.empty(w+1, dtype=float)
    s[0] = p - i0

    weeks = [0]

    # Loop to calculate S, I, R over time
    for t in range(1,w+1):
        r[t] = r[t-1] + (1/d) * i[t-1]
        i[t] = i[t-1] - (1/d) * i[t-1] + k * s[t-1] * i[t-1]
        s[t] = p - i[t] - r[t]
        weeks.append(t)

    weeks = np.array(weeks)

    for j in range(0, w + 1):
        print(f"Week: {weeks[j]} I: {i[j]} S: {s[j]} R: {r[j]}")

    # Plotting the infected people over time
    plt.figure(figsize=(10,6))

    # Plot for Infected People (I)
    plt.subplot(3, 1, 1)
    plt.plot(weeks, i, 'r-', label='Infected (I)')
    plt.grid(True)
    plt.title('SIR Model Over Time')
    plt.xlabel('Weeks')
    plt.ylabel('Infected')

    # Plot for Susceptible People (S)
    plt.subplot(3, 1, 2)
    plt.plot(weeks, s, 'b-', label='Susceptible (S)')
    plt.grid(True)
    plt.xlabel('Weeks')
    plt.ylabel('Susceptible')

    # Plot for Recovered People (R)
    plt.subplot(3, 1, 3)
    plt.plot(weeks, r, 'g-', label='Removed (R)')
    plt.grid(True)
    plt.xlabel('Weeks')
    plt.ylabel('Removed')

    # Adjust layout and save figure
    plt.tight_layout()
    plt.savefig('SIR_model.png')
    plt.show()

if __name__ == "__main__":
    SIR_Model(5, 1000, 24, 5/3, 0.00140704)
