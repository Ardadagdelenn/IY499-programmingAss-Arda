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
# Draw the histogram
def draw_histogram(grouped_df, class_width):
    try:
        plt.bar(grouped_df['Midpoint'], grouped_df['Frequency'], width=class_width, color='green', edgecolor='black', alpha=0.7)
        plt.xlabel('Midpoint')
        plt.ylabel('Frequency')
        plt.title('Grouped Data Histogram')
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.show()
    except Exception as e:
        print("Error in drawing histogram:", e)

# Calculate and display statistics
def show_statistics(data):
    print("\n--- Statistics ---")
    print(f"Mean: {np.mean(data):.2f}")
    print(f"Median: {np.median(data):.2f}")
    print(f"Minimum: {min(data)}")
    print(f"Maximum: {max(data)}")
    print(f"Count: {len(data)}")

# Save user-entered data into CSV
def save_data_to_csv(data, filename='sampleData.csv'):
    try:
        df = pd.DataFrame(data, columns=["Value"])
        df.to_csv(filename, index=False)
        print(f"\nData saved to {filename}")
    except Exception as e:
        print("Failed to save file:", e)

# Read data from CSV
def read_data_from_csv(filename='sampleData.csv'):
    try:
        df = pd.read_csv(filename)
        return df["Value"].tolist()
    except Exception as e:
        print("Failed to read file:", e)
        return []
        # Main menu
def main():
    while True:
        print("\n***** Grouped Data Application *****")
        print("1. Enter Data and Save in CSV")
        print("2. Show Statistics")
        print("3. Draw Histogram")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            user_input = input("Enter numbers separated by commas: ")
            try:
                data = [int(x.strip()) for x in user_input.split(',')]
                save_data_to_csv(data)
            except ValueError:
                print("Invalid input. Please enter only numbers.")
        
        elif choice == '2':
            data = read_data_from_csv()
            if data:
                show_statistics(data)
        
        elif choice == '3':
            data = read_data_from_csv()
            if data:
                class_width = int(input("Enter class width (e.g., 5): "))
                grouped_df = group_data(data, class_width)
                if grouped_df is not None:
                    print(grouped_df)
                    draw_histogram(grouped_df, class_width)
        
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
