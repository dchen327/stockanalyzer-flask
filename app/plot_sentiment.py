import matplotlib.pyplot as plt
from matplotlib import colors, cm


def plot_score(score):
    fig, ax = plt.subplots(figsize=(12, 2))
    fig.subplots_adjust(bottom=0.5)

    cmap = cm.bwr_r
    norm = colors.Normalize(vmin=-100, vmax=100)

    text_scales = ['Sell!', 'Consider Selling',
                   'Consider Holding', 'Consigder Buying', 'Buy!']
    font = {'size': 10}
    for i in range(len(text_scales)):
        plt.text(-100 + 50*i, 110, text_scales[i], fontdict=font, ha='center')

    plt.axvline(x=39, color='black')

    plt.show(fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap),
                          cax=ax, orientation='horizontal', label='Stock Sentiment Score'))


if __name__ == "__main__":
    plot_score(45)
