import pylab
import scipy.special
import seaborn


def nchoosek(n, k):
    a = scipy.special.comb(n, k, exact=True)
    return a * (1/6)**k * (5/6)**(n-k)


def make_plot(x_vals, y_vals, title, x_label, y_label):
    # pylab.figure()
    pylab.title(title)
    # pylab.xlabel(x_label)
    # pylab.ylabel(y_label)
    seaborn.barplot(x_vals, y_vals)


def throw_dice(n):
    x_vals, y_vals = [], []
    for k in range(2, n+1):
        x_vals.append(k)
        y_vals.append(nchoosek(k, 2))
    make_plot(x_vals, y_vals, 'The Probability of Getting 3 Exactly Twice', 'number of roll die', 'probability')
    pylab.xlim(0, n)
    pylab.ylim(0.0, 0.35)
    pylab.savefig('saikoro/images/nchoose2')


pylab.figure(figsize=(15,10))
seaborn.set_style('whitegrid')
throw_dice(50)