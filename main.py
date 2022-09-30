import numpy as np
import matplotlib.pyplot as plt

la = np.linalg

verbose = False
quiet = False
if not verbose:
    def info(msg):
        pass
else:
    def info(msg):
        print(msg)

if quiet:
    def say(msg):
        pass
else:
    def say(msg):
        print(msg)

N = 8
kron_delta = lambda x, y: x == y and 1 or 0

build_x = lambda n: (1. / np.sqrt(2)) * np.matrix([[
        kron_delta(i, j + 1) * np.sqrt(i) + kron_delta(i, j - 1) * np.sqrt(i + 1)
        for i in range(n)] for j in range(n)]
        )

build_p = lambda n: (1j / np.sqrt(2)) * np.matrix([[
        kron_delta(i, j + 1) * np.sqrt(i) - kron_delta(i, j - 1) * np.sqrt(i + 1)
        for i in range(n)] for j in range(n)]
        )

x = build_x(N)
p = build_p(N)
a = (1. / np.sqrt(2)) * (x + 1j * p)
a_dag = (1. / np.sqrt(2)) * (x - 1j * p)
assert (a_dag == a.getH()).all()
info(f"a:\n{a}\n")
info(f"a_dag:\n{a_dag}\n")

hamil = a_dag @ a + np.diag(np.repeat(1. / 2., N))
info(f"H:\n{hamil}\n")

w, v = la.eig(hamil)
assert np.isreal(w).all()
w = np.vectorize(lambda x: x.real)(w)
idx = w.argsort()
w = w[idx]
v = v[:,idx]
say(f"e: {w}")
info(f"v:\n{v}\n")

def plot(f):
    fig, ax = plt.subplots()
    x = np.linspace(0, 1, 2)
    for e in np.sort(w):
        y = np.repeat(abs(e), 2)
        ax.plot(x,y)
    plt.savefig(f)
    say(f"create: {f}")

f = "output/main.png"
plot(f)
