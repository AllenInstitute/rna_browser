import matplotlib.pyplot as plt
import numpy as np


class RNAplotter(object):

    def __init__(self):
        ...

    def comparison_hist(self, user_data, all_data, tube_prefix: str, num_bins=None):

        if num_bins is None:
            num_bins = 50
        else:
            pass

        amplified_quantity_bins = np.linspace(0, 80, num_bins)
        percent_cdna_bins = np.linspace(0, 100, num_bins)
        marker_sum_bins = np.linspace(0, 1.5, num_bins)

        fig, axs = plt.subplots(3, 1, figsize=(12, 6))

        axs[0].hist(user_data.amplified_quantity_ng,
                    amplified_quantity_bins, alpha=0.5, label= tube_prefix, density=True)
        axs[0].hist(all_data.amplified_quantity_ng,
                    amplified_quantity_bins, alpha=0.5, label="All tubes", density=True)
        axs[0].set_title('RNA yield')
        axs[0].set_xlabel('Amplified quantity (ng)')
        axs[0].set_ylabel('Probability density')
        axs[0].legend(loc='upper right')

        axs[1].hist(user_data.percent_cdna_longer_than_400bp*100,
                    percent_cdna_bins, alpha=0.5, label= tube_prefix, density=True)
        axs[1].hist(all_data.percent_cdna_longer_than_400bp*100,
                    percent_cdna_bins, alpha=0.5, label="All tubes", density=True)
        axs[1].set_title('RNA length')
        axs[1].set_xlabel('Percent cDNA greater than 400 bp')
        axs[1].set_ylabel('Probability density')
        axs[1].legend(loc='upper left')

        axs[2].hist(user_data.marker_sum_norm_label,
                    marker_sum_bins, alpha=0.5, label= tube_prefix, density=True)
        axs[2].hist(all_data.marker_sum_norm_label,
                    marker_sum_bins, alpha=0.5, label="All tubes", density=True)
        axs[2].set_title('RNA mapping')
        axs[2].set_xlabel('NMS score')
        axs[2].set_ylabel('Probability density')
        axs[2].legend(loc='upper left')

        plt.tight_layout()
        plt.show()
