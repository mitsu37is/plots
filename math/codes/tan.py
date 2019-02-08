import pylab
import numpy as np
import seaborn

pylab.figure(figsize=(6,4))
pylab.title("tan(x)")
pylab.tick_params(labelbottom=False, labelleft=True, labelright=False, labeltop=False)
t = np.arange(0, 10*np.pi, 0.4)
pylab.ylim(-10.0, 10.0)
seaborn.barplot(t, np.tan(t))
# seaborn.barplot(t, np.sin(t - np.pi)*2)

pylab.savefig('sample/images/tan_x2')