#  Python Excel to CSV Converter

This is a Python script that converts specific columns from an Excel file to a CSV file.

## Requirements

- Python 3
- openpyxl library (install using `pip install openpyxl`)

## Usage

1. Ensure that your Excel file is in the same directory as the script.
2. Modify the `input_file` variable in the script to specify the name of your input Excel file.
3. Update the `column_names` list in the script to include the names of the columns you want to extract.
4. Run the script using `python csv-converter.py `.
5. The extracted column data will be saved to a CSV file named "output.csv" in the same directory.
6. Run the csv output using `python output-view.py`.

## Example

Suppose you have an Excel file named "input.xlsx" with the following columns:

| Name    | Age | Location |
|---------|-----|----------|
| Thens    | 19  | USA   |
| Kesavan  | 23  | UK    |
| Pradeep  | 50  | UAE   |

To extract the "Name" and "Location" columns, update the `column_names` list as follows:

```python
column_names = ['Name', 'Location']
Name,Location
Thens,USA
Kesavan,UK
Pradeep,UAE
