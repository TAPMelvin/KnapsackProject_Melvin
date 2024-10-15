import csv
import re

def parse_output_file(filename):
    timing_data = []
    with open(filename, 'r') as file:
        content = file.read()
        
        # Split the content by the delimiter
        blocks = content.split('--------------------------------------------------\n')
        
        for block in blocks:
            # Use regex to extract relevant data
            size_match = re.search(r'Problem Size: (\w+)', block)
            target_match = re.search(r'Target: (\d+)', block)
            coins_match = re.search(r'Available coins: \[(.*?)\]', block)
            solution_match = re.search(r'Number of coins used: (\d+)', block)
            time_match = re.search(r'Execution time: ([\d\.]+) seconds', block)
            
            if size_match and target_match and coins_match and time_match:
                problem_size = size_match.group(1)
                target = int(target_match.group(1))
                coins = [int(x) for x in coins_match.group(1).split(', ')]
                execution_time = float(time_match.group(1))

                # Check if the solution match is found to determine the answer
                if solution_match:
                    num_coins = int(solution_match.group(1))
                    answer = 'Yes' if num_coins > 0 else 'No'  # Check if num_coins is greater than 0
                else:
                    num_coins = 0  # No solution found
                    answer = 'No'

                # Append to timing data
                timing_data.append({
                    'Problem Size': problem_size,
                    'Target': target,
                    'Available Coins': coins,
                    'Number of Coins Used': num_coins,
                    'Execution Time': execution_time,
                    'Answer': answer
                })
    
    return timing_data

def write_to_csv(timing_data, output_filename):
    with open(output_filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=timing_data[0].keys())
        writer.writeheader()
        for data in timing_data:
            writer.writerow(data)

# Main code
timing_data = parse_output_file('dataOutput_Melvin.txt')
write_to_csv(timing_data, 'timing_data.csv')
