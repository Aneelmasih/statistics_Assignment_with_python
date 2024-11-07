
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/content/drive/MyDrive/Datasets/supermarket_sales.csv')


def plot_multiple_line_graphs(
        data,
        x_col,
        y_col,
        category_col,
        title='Line Graph for Multiple Cities',
        xlabel='X-axis',
        ylabel='Y-axis'):
    """
    Plots multiple line graphs for different categories (e.g., cities).

    Parameters:
    data (DataFrame): DataFrame containing data for the plot.
    x_col (str): The column to be used for the x-axis.
    y_col (str): The column to be used for the y-axis.
    category_col (str): The column used to separate different line graphs (e.g., City).
    title (str): Title of the plot.
    xlabel (str): Label for the x-axis.
    ylabel (str): Label for the y-axis.
    """
    plt.figure(figsize=(14, 8))

    # Ensure datetime format and sort by x_col
    data[x_col] = pd.to_datetime(data[x_col])
    data = data.sort_values(by=x_col)

    # Plot line graphs for each category
    for category in data[category_col].unique():
        subset = data[data[category_col] == category]
        plt.plot(subset[x_col], subset[y_col], marker='o', label=category)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(title=category_col)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_bar_chart(
        data,
        x_col,
        y_col,
        title='Bar Chart',
        xlabel='X-axis',
        ylabel='Y-axis'):
    """
    Plots a bar chart using the given data and adds the count on top of each bar.

    Parameters:
    data (DataFrame): Filtered DataFrame containing data for the plot.
    x_col (str): The column to be used for the x-axis (categorical data).
    y_col (str): The column to be used for the y-axis (numerical data).
    title (str): Title of the plot.
    xlabel (str): Label for the x-axis.
    ylabel (str): Label for the y-axis.
    """
    plt.figure(figsize=(12, 6))
    bar_data = data.groupby(x_col)[y_col].sum().sort_values()
    ax = bar_data.plot(kind='bar', color='skyblue')

    # Add counts on top of each bar
    for p in ax.patches:
        ax.annotate(
            f'{p.get_height():.0f}',
            (p.get_x() +
             p.get_width() /
             2,
             p.get_height()),
            ha='center',
            va='bottom',
            fontsize=10)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_box_plot(
        data,
        x_col,
        y_col,
        title='Box Plot',
        xlabel='X-axis',
        ylabel='Y-axis'):
    """
    Plots a box plot using the given data, with different colors for each box.

    Parameters:
    data (DataFrame): DataFrame containing data for the plot.
    x_col (str): The column to be used for the x-axis (categorical data).
    y_col (str): The column to be used for the y-axis (numerical data).
    title (str): Title of the plot.
    xlabel (str): Label for the x-axis.
    ylabel (str): Label for the y-axis.
    """
    plt.figure(figsize=(12, 6))
    unique_values = data[x_col].unique()
    palette = sns.color_palette('pastel', len(unique_values))
    sns.boxplot(
        x=x_col,
        y=y_col,
        data=data,
        palette=palette,
        hue='Product line')

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


df['Date'] = pd.to_datetime(df['Date'])

# Filter data for the 'Sports and travel' product line
health_beauty_data = df[df['Product line'] == 'Sports and travel']

# Aggregate total sales per day for each city
health_beauty_aggregated = health_beauty_data.groupby(
    ['Date', 'City'])['Total'].sum().reset_index()
health_beauty_aggregated = health_beauty_aggregated.sort_values(by='Date')
# Plot the line graph for total sales for 'Sports and travel' in each city
plot_multiple_line_graphs(
    health_beauty_aggregated,
    x_col='Date',
    y_col='Total',
    category_col='City',
    title='Total Sales Over Time for Sports and travel by City',
    xlabel='Date',
    ylabel='Total Sales')

# Filter data for a specific product line or category if needed
filtered_data = df[df['Product line'] == 'Health and beauty']

# Plot the bar chart
plot_bar_chart(
    filtered_data,
    x_col='City',
    y_col='Total',
    title='Total Sales by City for Health and Beauty',
    xlabel='City',
    ylabel='Total Sales in $')

# Box plot of total sales by product line
plot_box_plot(
    df,
    x_col='Product line',
    y_col='Total',
    title='Distribution of Total Sales by Product Line',
    xlabel='Product Line',
    ylabel='Total Sales')
