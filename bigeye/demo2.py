import matplotlib.pyplot as plt

plt.ion()
plt.figure()
for i in range(100):
    plt.plot([i], [i], 'o')
    plt.draw()
    plt.pause(0.05)
raw_input("done >>")
