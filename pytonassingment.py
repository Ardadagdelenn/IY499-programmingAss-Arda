import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Group the data into class intervals
def group_data(data, class_width):
    try:
        min_val = min(data)
        max_val = max(data)
        bins = np.arange(min_val, max_val + class_width, class_width)
        frequency, bin_edges = np.histogram(data, bins=bins)
        midpoints = [(bin_edges[i] + bin_edges[i+1]) / 2 for i in range(len(bin_edges)-1)]
        freq_times_mid = [frequency[i] * midpoints[i] for i in range(len(frequency))]

        grouped_df = pd.DataFrame({
            'Class Range': [f'{int(bin_edges[i])} - {int(bin_edges[i+1])}' for i in range(len(bin_edges)-1)],
            'Frequency': frequency,
            'Midpoint': midpoints,
            'Freq * Mid': freq_times_mid
        })
        return grouped_df
    except Exception as e:
        print("Error in grouping data:", e)
        return None
