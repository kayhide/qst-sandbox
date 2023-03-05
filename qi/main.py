from qutip import *
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


delta = 0.001
min = -0.35
max = 0.35
xs = np.linspace(min, max, int((max - min) / delta) + 1)
ys = np.linspace(min, max, int((max - min) / delta) + 1)

class Run:
    def __init__(self, name, p, m1, m2):
        self.name = name
        self.p = p
        self.m1 = m1
        self.m2 = m2

        st0 = 1 / np.sqrt(2) * (tensor(basis(2,0), basis(2,0)) + tensor(basis(2,1), basis(2,1)))
        self.rho_0 = (1 - p) * st0 * st0.trans() + p * tensor(qeye(2), qeye(2)) / 4.0

    def value(self, x, y):
        rho = self.rho_0 + x * self.m1 + y * self.m2
        if any(v <= 0 for v in rho.eigenenergies()):
            return 0
        else:
            if any(v < 0 for v in partial_transpose(rho, [True, False]).eigenenergies()):
                return 2
            else:
                return 1

def plot(run):
    fig, ax = plt.subplots()
    zs = np.zeros([len(xs), len(ys)])
    for j, y in enumerate(ys):
        print(f"{y:0.3f} ", end="", flush=True)
        for i, x in enumerate(xs):
            zs[j, i] = run.value(x, y)

    print("")
    ax.pcolor(xs, ys, zs)

    f = f"output/{run.name}.png"
    plt.savefig(f)
    say(f"create: {f}")

run = Run("Case-ex", 0.75,
    tensor(sigmax(), (sigmax() - 2 * sigmaz()) / np.sqrt(5)),
    tensor((sigmay() - 3 * sigmaz())/ np.sqrt(10), sigmay()))
plot(run)

run = Run("Case-1", 0.75, tensor(sigmax(), sigmaz()), tensor(sigmay(), sigmaz()))
plot(run)

run = Run("Case-2", 0.75, tensor(sigmax(), sigmax()), tensor(sigmay(), sigmay()))
plot(run)

run = Run("Case-3", 0.75, tensor(sigmax(), sigmax()), tensor(sigmay(), sigmax()))
plot(run)
