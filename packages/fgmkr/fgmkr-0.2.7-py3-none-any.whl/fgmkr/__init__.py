from matplotlib import pyplot as plt
import numpy as np
from scipy import stats

# Single Input
def fgmk(n,x,y,xlabel,ylabel, titlestr, figtext = None, glabel = None, grid = None,dim=None):
    # Figure Setup
    if dim is not None:
        plt.figure(n, figsize=dim)
    else:
        plt.figure(n)

    # Data Visualization
    plt.plot(x,y, label = glabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(titlestr)
    plt.text(0.5, -0.18, r'$\bf{Figure\ }$' + str(n) + r': '+ str(figtext), transform=plt.gca().transAxes,
            horizontalalignment='center', verticalalignment='center', fontsize=10)

    # Figure Cleanup
    if grid:
        plt.grid(which='both')
    if glabel is not None:
        plt.legend()

# Double Input
def fgmk2(n, x0, y0, xlabel, ylabel, t,
          l=None, lst='-', c='tab:blue',
          x=None, y=None, l1=None, lst1='-', c1='tab:orange',
          fig=None, grid=1, dim=None):
    # Figure Setup
    if dim is not None:
        plt.figure(n, figsize=dim)
    else:
        plt.figure(n)
    plt.title(t)
    if fig is not None:
        plt.text(0.5, -0.18, r'$\bf{Figure\ }$' + str(n) + r': ' + str(fig), transform=plt.gca().transAxes,
                 horizontalalignment='center', verticalalignment='center', fontsize=10)

    # Data Visualization
    plt.plot(x0, y0, label=l, linestyle=lst, color=c)  # Set 0
    if x is not None and y is not None:  # Set 1
        plt.plot(x, y, label=l1, linestyle=lst1, color=c1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Figure Cleanup
    if grid:
        plt.grid(which='both')
    if l is not None or l1 is not None:
        plt.legend()

# Histogram
def hgmk2(n, data, xlabel, ylabel, t, l=None, lst='-', c='tab:blue', fig=None, grid=1, dim=None,
          conf_intervals=None, mark_values=None, mark_labels=None, average=False, bell_curve=False,
          xmax=None):
    # Filter data based on xmax
    if xmax is not None:
        data = data[data <= xmax]

    # Figure Setup
    if dim is not None:
        plt.figure(n, figsize=dim)
    else:
        plt.figure(n)

    # Calculate histogram
    counts, bins, _ = plt.hist(data, bins=30, color='#214187', alpha=0.7, label=l, linestyle=lst, density=True)

    # Average
    if average:
        avg = np.mean(data)
        plt.axvline(avg, color='black', linestyle='-', label=r'Experimental $\bar{x}_{target}$' + f'\n{avg:.3f}')

    # Confidence intervals
    if conf_intervals:
        for ci_value in conf_intervals:
            if ci_value <= 1:
                lower_bound, upper_bound = np.percentile(data, [(1-ci_value)*50, (1+ci_value)*50])
                plt.axvline(lower_bound, color='red', linestyle=':', label=f'{ci_value*100}% \nCI: [{lower_bound:.2f}, {upper_bound:.2f}]')
                plt.axvline(upper_bound, color='red', linestyle=':')
            else:
                lower_bound, upper_bound = np.percentile(data, [ci_value[0], ci_value[1]])
                plt.axvline(lower_bound, color='red', linestyle=':', label=f'{ci_value[0]}% to {ci_value[1]}% \nCI: [{lower_bound:.2f}, {upper_bound:.2f}]')
                plt.axvline(upper_bound, color='red', linestyle=':')

    # Mark values
    if mark_values and mark_labels:
        colors = ['tab:pink', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:blue', 'tab:gray']
        for value, label, color in zip(mark_values, mark_labels, colors[:len(mark_values)]):
            plt.axvline(value, color=color, linestyle='--', label=label)
            # plt.text(value, max(counts), label, color=color)

    # Bell curve
    if bell_curve:
        x = np.linspace(min(data), max(data), 100)
        mu = np.mean(data)
        sigma = np.std(data)
        pdf = stats.norm.pdf(x, mu, sigma)
        plt.plot(x, pdf, color='orange', linestyle='-')

    # Legend
    legend = plt.legend()
    for text in legend.get_texts():
        text.set_fontsize(8)

    # Plot settings
    plt.title(t)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    if grid:
        plt.grid(which='both')
    if fig is not None:
        plt.text(0.5, -0.18, r'$\bf{Figure\ }$' + str(n) + r': ' + str(fig), transform=plt.gca().transAxes,
                 horizontalalignment='center', verticalalignment='center', fontsize=10)
    plt.show()

# Help
def fgmk_help():
    print('Mandatory: \nFigure Number\nx0\ny0\nx0 Label\ny0 Label\nTitle\n')
    print('Optional Graph Features: \nfig, Figure Text\ngrid, enabled by default\ndim, 1x2 Tuple\n')
    print('Data Set 0: \nl, Label\nlst, \'-\' by default\nc \'tab:blue\' by default\n')
    print('Data Set 1: \nx\ny\nl1, Label\nlst1, \'-\' by default\nc1 \'tab:orange\' by default\n')