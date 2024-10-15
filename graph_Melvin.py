import csv
import matplotlib.pyplot as plt
import numpy as np

def read_csv(filename):
    targets = []
    execution_times = []
    num_coins_used = []
    answers = []
    
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            targets.append(int(row['Target']))
            execution_times.append(float(row['Execution Time']))
            num_coins_used.append(int(row['Number of Coins Used']))
            answers.append(row['Answer'])
    
    return num_coins_used, execution_times, answers

def plot_data(num_coins_used, execution_times, answers, output_filename):
    plt.figure(figsize=(10, 6))
    
    # Set minimum Y value for visibility
    min_y = min(execution_times) if min(execution_times) > 0 else 1e-5
    plt.ylim(min_y, max(execution_times) * 1.1)  # Padding for upper limit
    
    # Plotting points based on answers
    for coins, time, answer in zip(num_coins_used, execution_times, answers):
        if answer == 'Yes':
            plt.scatter(coins, time, color='blue', marker='o', s=100, alpha=0.8, label='Yes' if 'Yes' not in plt.gca().get_legend_handles_labels()[1] else "")
        else:
            plt.scatter(coins, time, color='red', marker='s', s=150, alpha=0.8, label='No' if 'No' not in plt.gca().get_legend_handles_labels()[1] else "")
    
    # Line of best fit
    num_coins_used_array = np.array(num_coins_used)
    execution_times_array = np.array(execution_times)

    # Calculate the coefficients for the linear regression
    coefficients = np.polyfit(num_coins_used_array, execution_times_array, 1)
    polynomial = np.poly1d(coefficients)
    
    # Generate x values for the fitted line
    x_fit = np.linspace(min(num_coins_used_array), max(num_coins_used_array), 100)
    y_fit = polynomial(x_fit)

    # Plotting the line of best fit
    plt.plot(x_fit, y_fit, color='green', linestyle='--', label='Line of Best Fit')

    # Format the equation of the line of best fit with more decimal places
    slope, intercept = coefficients
    equation_text = f'y = {slope:.6f}x + {intercept:.6f}'
    
    # Add the equation text to the plot
    plt.text(0.05, 0.95, equation_text, transform=plt.gca().transAxes, fontsize=12,
             verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

    plt.xlabel('Number of Coins Used')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs Number of Coins Used')
    
    plt.grid(True)
    plt.legend()
    plt.savefig(output_filename)
    plt.show()

# Main code
num_coins_used, execution_times, answers = read_csv('timing_data.csv')
plot_data(num_coins_used, execution_times, answers, 'plot_Melvin.png')
