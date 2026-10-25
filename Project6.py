# Project 6: Bar Chart Display
# 10/21/2026
# Kingsley Wickstrom
# Read and display grouped data from a CSV file in bar chart format;
# README for more information.


"""Read grouped records from a CSV file and display them as bar charts."""

import csv
from itertools import groupby

import matplotlib.pyplot as pyplot

from BarChart import BarChart


def get_filename():
    """Ask for a readable CSV filename."""
    while True:
        filename = input("Enter the CSV filename: ")
        try:
            with open(filename, "r", encoding="utf-8", newline=""):
                return filename
        except OSError as error:
            print(f"Could not open that file: {error}")


def get_integer(prompt, minimum):
    """Read an integer from the user that is at least minimum."""
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum:
                return value
            print(f"Enter a number that is at least {minimum}.")
        except ValueError:
            print("Please enter a whole number.")


def get_seconds_with_default(prompt, default):
    """Read a positive number of seconds, using default when left blank."""
    while True:
        response = input(prompt).strip()
        if not response:
            return default
        try:
            seconds = float(response)
            if seconds > 0:
                return seconds
            print("Enter a number greater than 0.")
        except ValueError:
            print("Please enter a number of seconds, such as 0.5 or 2.")


def get_column(prompt):
    """Read a 1-based CSV column number and return its 0-based index."""
    return get_integer(prompt, 1) - 1


def read_records(reader, header_lines, group_column, name_column,
                 value_column, category_column):
    """Yield validated records as group, name, value, category, and line number."""
    line_number = 0
    for _ in range(header_lines):
        if next(reader, None) is None:
            raise ValueError("The file ended before all header lines were skipped.")
        line_number += 1

    columns = (group_column, name_column, value_column, category_column)
    required_column = max(columns)

    while True:
        row = next(reader, None)
        if row is None:
            return
        line_number += 1
        if not row or all(not field.strip() for field in row):
            continue

        if len(row) == 1 and row[0].strip().isdigit():
            record_count = int(row[0].strip())
            if record_count < 1:
                raise ValueError(
                    f"Line {line_number} has an invalid group record count."
                )

            records_read = 0
            while records_read < record_count:
                row = next(reader, None)
                if row is None:
                    raise ValueError(
                        f"Group starting on line {line_number} declares "
                        f"{record_count} records, but the file ended early."
                    )
                line_number += 1
                if not row or all(not field.strip() for field in row):
                    continue
                yield _parse_record(
                    row, required_column, group_column, name_column,
                    value_column, category_column, line_number
                )
                records_read += 1
            continue

        yield _parse_record(
            row, required_column, group_column, name_column,
            value_column, category_column, line_number
        )


def _parse_record(row, required_column, group_column, name_column,
                  value_column, category_column, line_number):
    """Parse and validate one data row."""
    if len(row) <= required_column:
        raise ValueError(
            f"Line {line_number} has fewer columns than the selected column numbers."
        )

    group = row[group_column].strip()
    name = row[name_column].strip()
    category = row[category_column].strip()
    if not group or not name:
        raise ValueError(
            f"Line {line_number} must have a non-empty group and name."
        )

    try:
        value = int(row[value_column].strip().replace(",", ""))
    except ValueError as error:
        raise ValueError(
            f"Line {line_number} has a value that is not a whole number."
        ) from error

    return group, name, value, category, line_number


def main():
    # Step 1: Ask which file to read and how many bars to display.
    filename = get_filename()
    num_bars = get_integer("How many bars should each chart show? ", 1)

    # Step 2: Ask how many introductory/header lines to skip.
    header_lines = get_integer("How many header lines should be skipped? ", 0)

    try:
        # Ask for the fields needed to interpret and label each chart.
        chart_title = input(
            f"Chart title (default: Top {num_bars} Records by Group): "
        ).strip()
        if not chart_title:
            chart_title = f"Top {num_bars} Records by Group"

        x_axis_label = input(
            "Value-axis label (include units, if applicable): "
        ).strip()
        if not x_axis_label:
            x_axis_label = "Value"

        data_source = input(f"Data source (default: {filename}): ").strip()
        if not data_source:
            data_source = f"Source: {filename}"

        group_column = get_column("Group column number (1-based): ")
        name_column = get_column("Name column number (1-based): ")
        value_column = get_column("Value column number (1-based): ")
        category_column = get_column("Category column number (1-based): ")

        pause_seconds = get_seconds_with_default(
            "Seconds to show each chart before advancing [0.2]: ",
            0.2,
        )

        with open(filename, "r", encoding="utf-8", newline="") as data_file:
            reader = csv.reader(data_file)
            records = read_records(
                reader,
                header_lines,
                group_column,
                name_column,
                value_column,
                category_column,
            )
            grouped_records = groupby(records, key=lambda record: record[0])

            chart = None
            print("Displaying charts. Press Ctrl+C in the terminal to stop.")
            # Step 7: Repeat steps 3-6 for each remaining group in the file.
            for group_name, group in grouped_records:
                # Step 3: Store only the current group's records in a dictionary.
                group_data = {
                    index: (name, value, category)
                    for index, (_, name, value, category, _) in enumerate(group)
                }

                # Step 4: Sort this group's records by value, highest first.
                ranked_records = sorted(
                    group_data.values(),
                    key=lambda record: record[1],
                    reverse=True,
                )[:num_bars]

                if chart is None:
                    chart = BarChart(
                        chart_title,
                        x_axis_label,
                        data_source,
                    )
                else:
                    chart.reset()

                # Step 5: Build and display a static chart for this group.
                for name, value, category in ranked_records:
                    chart.add(name, value, category)
                chart.set_caption(group_name)
                chart.draw()

                # Step 6: Pause so the chart can be seen before advancing.
                pyplot.pause(pause_seconds)
        if chart is None:
            print("The file contains no data records after the header.")
        else:
            chart.leave_window_open()
    except (OSError, ValueError) as error:
        print(f"Could not process the CSV file: {error}")


if __name__ == "__main__":
    main()
