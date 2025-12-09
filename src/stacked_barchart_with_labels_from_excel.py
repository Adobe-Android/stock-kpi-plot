# Inspired by https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py

import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import numpy as np
import pandas as pd
import math
import os

# ticker = 'NVDA'
# company_name = 'Nvidia Corporation'
# ticker = 'MRVL'
# company_name = 'Marvell Technology, Inc.'
# revenue = {}
ticker = 'AVGO'
company_name = 'Broadcom Inc.'
revenue = {}

cwd = os.getcwd()
folder_excel_read_path = os.path.join(cwd, 'data', f'{ticker}.xlsx')
folder_image_save_path = os.path.join(cwd, 'images', f'{ticker}-Stacked-Revenue-Segments.png')

def set_revenue_segments(indexes, df, revenue):
    for index in indexes[1:]:
        revenue[index] = df.loc[index].values.tolist()

def main():
    # Read Excel file and map data values to objects
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
    df = pd.read_excel(f'{folder_excel_read_path}', sheet_name='Model', header=None, skiprows=[1], index_col=0)
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
    quarters = df.loc['Reporting Quarter'].values.tolist()
    set_revenue_segments(df.index, df, revenue)

    x = np.arange(len(quarters))  # the label locations
    width = 0.6  # the width of the bars
    bottom = np.zeros(len(quarters))

    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure
    fig, ax = plt.subplots(layout='constrained', num=ticker, figsize = [12, 10])

    for segment, earnings in revenue.items():
        rects = ax.bar(quarters, earnings, width, label=segment, bottom=bottom)
        bottom += earnings
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar_label.html
        ax.bar_label(rects, fmt='${:,g}', label_type='center')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_title(f'{company_name} ({ticker})')
    ax.set_ylabel('Revenue (Millions)')
    ax.set_xlabel('Reporting Date')
    ax.set_xticks(x, quarters)
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
    ax.legend(title='Revenue Segments', loc='best', ncols=2)
    ax.yaxis.set_major_formatter(StrMethodFormatter('${x:,g}'))
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
    plt.savefig(f'{folder_image_save_path}', dpi=300, pad_inches=0.1, bbox_inches='tight', format='png')
    plt.show()

if __name__ == "__main__":
    main()