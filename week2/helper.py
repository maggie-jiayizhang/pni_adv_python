# helper functions for plotting variance explained

import numpy as np
import matplotlib.pyplot as plt

# plot cumulative variance explained by the first n pc's
# plot a visual guide at thresh
def plot_cum_var_explained(variance, n=10, thresh=0.9):
    cum_var = np.cumsum(variance) # cumulative var explained
    
    plt.bar(range(n), cum_var[:n])
    plt.ylabel("Cumulative Variance Explained", fontsize='x-large')
    plt.xlabel("# PC", fontsize='x-large')
    plt.ylim(0, 1)
    plt.xticks(range(n), range(n))
    plt.axhline(y=thresh, label="%d%% var"%(thresh*100), ls="--", color="black")
    plt.legend()


# plot variance explained by the first n pc's
# plot a visual guide at thresh
def plot_var_explained(variance, n=10, thresh=0.9):
    
    plt.bar(range(n), variance[:n])
    plt.ylabel("Variance Explained", fontsize='x-large')
    plt.xlabel("# PC", fontsize='x-large')
    plt.ylim(0, 1)
    plt.xticks(range(n), range(n))
    plt.axhline(y=thresh, label="%d%% var"%(thresh*100), ls="--", color="black")
    plt.legend()