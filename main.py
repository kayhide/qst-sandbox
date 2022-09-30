import numpy as np
import matplotlib.pyplot as plt

la = np.linalg


N = 8
kron_delta = lambda x, y: x == y and 1 or 0

build_x = lambda n: np.matrix([[
        kron_delta(i, j + 1) * np.sqrt(i) + kron_delta(i, j - 1) * np.sqrt(i + 1)
        for i in range(0, n)] for j in range(0, n)]
        )

build_p = lambda n: np.matrix([[
        kron_delta(i, j + 1) * np.sqrt(i) - kron_delta(i, j - 1) * np.sqrt(i + 1)
        for i in range(0, n)] for j in range(0, n)]
        )

x = build_x(N)
p = build_p(N)
print(x)
print(p)
a = x + 1j * p
a_dag = x - 1j * p
print(a)
assert (a_dag == a.conjugate()).all()
assert (a_dag == a.transpose()).all()

hamil = a @ a_dag + np.diag(np.repeat(1. / 2., N))
print(hamil)


print()
w, v = la.eig(hamil)
print(w)
print(np.sort(abs(w)))
# print(np.nub(np.sort(abs(w))))
# print(v)

def plot(f):
    fig, ax = plt.subplots()
    x = np.linspace(0, 2* np.pi, 200)
    # y = np.sin(x)
    # ax.plot(x,y)
    for e in np.sort(w):
        y = np.repeat(abs(e), 200)
        ax.plot(x,y)
    plt.savefig(f)

plot("output/main.png")
