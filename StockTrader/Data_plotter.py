import matplotlib.pyplot as plt


def plot_regimes(data):
    x = data[0, :]
    y = data[1, :]
    c = data[2, :]

    plt.scatter(x, y, s=None, c=c, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None,
                verts=None, edgecolors=None, hold=None, data=None)
    plt.show()
    return

