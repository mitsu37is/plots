import pylab
import seaborn
import numpy as np
import matplotlib.animation as animation


def make_plot(omega, title, x_label, y_label):
    fig = pylab.figure(figsize=(6,4))
    pylab.title(title)
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    interval = np.arange(0, 10, 0.1)
    pylab.plot(np.sin(omega * interval), np.sin(2*interval))
    pylab.savefig('math/images/lissajous')
    ims = []
    for t in interval:
        ims.append(pylab.plot(np.sin(omega * t), np.sin(2 * t), 'o'))
    ani = animation.ArtistAnimation(fig, ims, interval=100, blit=True, repeat_delay=0)
    ani.save('math/images/lissajous.gif', writer='imagemagick', fps=4)


seaborn.set_style('whitegrid')
make_plot(3, 'Lissajous Curve', 'x = sin(3t)', 'y = sin(2t)')