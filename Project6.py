# Project 6: Bar Chart Display
# 10/21/2026
# Kingsley Wickstrom
# Read and display data from a file in a bar chart format.


# 1. Ask the user for the data file and how many bars to display.
# 2. Skip the header lines in the file.
# 3. Read data from a file into a Dictionary. (Read in only one group, not the whole file.)
# 4. Sort the Dictionary by the value of each record (1 record = 1 line of data).
# 5. Create and display a (static, not moving) bar chart.
# 6. Pause a bit.
# 7. Repeat steps 3–6 until the file is done.

def main():
    # Step 1: Ask the user for the data file and how many bars to display.
    data_file = input("Enter the name of the data file: ")
    num_bars = int(input("Enter the number of bars to display: "))

    # Step 2: Skip the header lines in the file.
    with open(data_file, 'r') as file:
        # Assuming the first line is a header
        next(file)  # Skip the header line

        while True:
            # Step 3: Read data from a file into a Dictionary.
            data_dict = {}
            for _ in range(num_bars):
                line = file.readline()
                if not line:
                    break  # End of file
                key, value = line.strip().split(',')
                data_dict[key] = float(value)

            if not data_dict:
                break  # No more data to read

            # Step 4: Sort the Dictionary by the value of each record.
            sorted_data = dict(sorted(data_dict.items(), key=lambda item: item[1], reverse=True))

            # Step 5: Create and display a (static, not moving) bar chart.
            print("\nBar Chart:")
            for key, value in sorted_data.items():
                print(f"{key}: {'#' * int(value)} ({value})")

            # Step 6: Pause a bit.
            input("\nPress Enter to continue...")