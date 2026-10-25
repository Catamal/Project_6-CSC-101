# Project 6: Bar Chart Display

This program reads grouped records from a comma-separated data file and displays a horizontal bar chart for each group. Records within each group are sorted by their numeric value, and only the requested number of top records are shown.

## Requirements

- Python 3
- Matplotlib

Install Matplotlib if needed:

```text
python -m pip install matplotlib
```

## Data file format

The input must be a comma-separated file. Groups must appear in consecutive rows; for example, all records for one year should appear together. Values must be whole numbers. A file can use any extension, such as `.csv` or `.txt`.

Some datasets, including Princeton's cities and countries files, put a single number before each group to state how many records follow. The program recognizes and skips these group-count lines automatically. These are separate from the introductory/header lines at the start of the file.

Example:

```csv
Year,City,Population,Region
2018,Tokyo,38194,East Asia
2018,Delhi,27890,South Asia
2018,Shanghai,25779,East Asia
2019,Tokyo,37400,East Asia
2019,Delhi,28500,South Asia
```

The first row is the header. The `Year` column identifies groups, `City` is the bar name, `Population` is the value, and `Region` is the category used to color bars.

## Run the program

Enter the requested information:

1. Enter the data filename and how many bars each chart should show.
2. Enter the number of introductory/header lines to skip. For `cities.txt` and `countries.txt`, enter `4`.
3. Enter the chart title, value-axis label, and data source. Press Enter for a default if you do not want to provide one.
4. Enter the 1-based column numbers for group, name, value, and category. For the Princeton population files, use `1`, `2`, `4`, and `5`, respectively.
5. Enter how many seconds each chart should stay on screen before advancing (press Enter for 0.2 seconds). You can use decimals, such as `0.5` or `2`.

The program reads one group at a time, sorts that group's records from highest to lowest, and displays a static chart before moving on to the next group. It leaves the final chart window open until you close it. Press Ctrl+C in the terminal to stop early.

## Files

- `Project6.py` reads, groups, sorts, and displays the input records.
- `BarChart.py` provides the `BarChart` class used to draw the charts.
