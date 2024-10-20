import numpy as np
import matplotlib.pyplot as plt
#a_n+1 = r*a_n + b
def lin_dynamical(a0, r,b,k):
    print(f"Calculated a: {b / (1- r)}")
    time = [0]
    res = np.empty(k+1, dtype=float)
    res[0]= a0
    for i in range(1,k+1):
     res[i] = r * res[i-1] + b
     time.append(i)

    time = np.array(time)

    for j in range(1 ,k+1):
        print(f"Time: {time[j]} Result: {res[j]}")

    plt.plot(time, res)
    plt.grid(True)
    plt.title('Linear Dynamical System')
    plt.xlabel('Time')
    plt.ylabel('Result')
    plt.savefig('lin_dynamical.png')
    plt.show()

if __name__ == "__main__":
    lin_dynamical(1000,0.9,1000,500)

#difference between calculated and actual result is due to floating-point precision error