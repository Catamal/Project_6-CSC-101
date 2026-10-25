# Project 6: Bar Chart Display

This program reads grouped records from a plain-text data file and displays a horizontal bar chart for each group. Fields in the text files are separated by commas. The program sorts each group's records by their numeric values and shows the requested number of highest-valued records.

## Requirements

- Python 3
- Matplotlib

Install Matplotlib if needed:

```text
python -m pip install matplotlib
```

## Data file format

Use a plain-text file such as `cities.txt`, `countries.txt`, or `brands.txt`. Each data row contains comma-separated fields. Groups must appear consecutively, and values must be whole numbers.

Some files put a single number before each group to indicate how many records follow. The program skips these group-count lines automatically. They are separate from introductory/header lines at the start of the file.

For example:

```
4
Year,City,Country,Population,Region
2018,Tokyo,Japan,38194,East Asia
2018,Delhi,India,27890,South Asia
2019,Tokyo,Japan,37400,East Asia
```

## Run the program

Run `Project6.py`, then answer its prompts:

1. Enter the text filename (or its full path) and how many bars each chart should show.
2. Enter how many introductory/header lines to skip. For the provided Princeton data files, enter `3` (3 lines about the database; all blank lines after are skipped)
3. Enter the chart title (name), value-axis label (units), and data source (source if you don't want to display the file name). `Press Enter to use a default response`
4. Check the preview of the first data row. For `countries.txt`, it looks like:

   ```text
   Column 1: 1950-01-01
   Column 2: Afghanistan
   Column 3: Southern Asia
   Column 4: 7752
   Column 5: Asia
   ```

   Enter the column numbers when prompted:

   ```text
   Group column: 1
   Name column: 2
   Value column: 4
   Category column: 5
   ```

   Check the selected fields shown by the program, then enter `Y` to continue or `N` to choose the columns again.
5. Enter how many seconds each chart should stay on screen before advancing. Press Enter for `.01` seconds; decimal values above `0` are accepted.
6. To stop the chart sequence early, click the chart window and press `Q` or `Esc`. You can also press Ctrl+C in the terminal which will stop through a `KeyboardInterrupt`.

The program reads one group at a time, sorts its records from highest to lowest, and displays a static chart before moving to the next group. It leaves the final chart window open until you close it.

## Files

- `Project6.py` reads, groups, sorts, and displays the input records.
- `BarChart.py` provides the chart-drawing class.
- `brands.txt`, `cities.txt`, and `countries.txt` are sample data files from the Princeton bar chart assignment.
