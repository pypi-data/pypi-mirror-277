
# DocTableFlow

**DocTableFlow** is a Python package designed to fetch tablular data from PDF files and save them in various formats such as Excel, JSON, CSV, and DataFrame. It simplifies the process of converting tabular data from PDFs into structured formats for easy analysis and manipulation.

## Features

- Fetch tablular data from PDF files.
- Save extracted tables as Excel files.
- Save extracted tables as JSON files.
- Save extracted tables as CSV files.
- Return extracted tables as Pandas DataFrames.
- Count the number of pages in a PDF document.

## Installation

Install DocTableFlow using pip:

```bash
pip install DocTableFlow
```

## Usage

Here's a quick guide on how to use DocTableFlow:

### Extract Tables to Excel

```python
from DocTableFlow import tableToExcel

input_path = 'path/to/input.pdf'
output_dir = 'path/to/output/dir'
tableToExcel(input_path, output_dir)
```

### Extract Tables to JSON

```python
from DocTableFlow import tableToJson

input_path = 'path/to/input.pdf'
output_dir = 'path/to/output/dir'
tableToJson(input_path, output_dir)
```

### Extract Tables to CSV

```python
from DocTableFlow import tableToCSV

input_path = 'path/to/input.pdf'
output_dir = 'path/to/output/dir'
tableToCSV(input_path, output_dir)
```

### Extract Tables as DataFrame

```python
from DocTableFlow import tableToDataframe

input_path = 'path/to/input.pdf'
df = tableToDataframe(input_path)
print(df)
```

### Count Pages in PDF

```python
from DocTableFlow import CountPages

input_path = 'path/to/input.pdf'
page_count = CountPages(input_path)
print(f"Total pages: {page_count}")
```

## Example

```python
from DocTableFlow import tableToExcel, tableToJson, tableToCSV, tableToDataframe, CountPages

# Extract to Excel
tableToExcel('/path/to/input.pdf', '/path/to/output/dir')

# Extract to JSON
tableToJson('/path/to/input.pdf', '/path/to/output/dir')

# Extract to CSV
tableToCSV('/path/to/input.pdf', '/path/to/output/dir')

# Extract to DataFrame
df = tableToDataframe('/path/to/input.pdf')
print(df)

# Count pages
page_count = CountPages('/path/to/input.pdf')
print(f"Total pages: {page_count}")
```

## Dependencies

DocTableFlow requires the following libraries:

- cffi
- chardet
- charset-normalizer
- contourpy
- cryptography
- cycler
- Deprecated
- deprecation
- et-xmlfile
- fonttools
- img2pdf
- importlib_resources
- joblib
- kiwisolver
- lxml
- markdown-it-py
- matplotlib
- mdurl
- numpy
- ocrmypdf
- packaging
- pandas
- pdfminer
- pdfminer.six
- pikepdf
- pillow
- pluggy
- pycparser
- pycryptodome
- Pygments
- pyparsing
- pypdf
- PyPDF2
- python-dateutil
- pytz
- reportlab
- rich
- scikit-learn
- scipy
- six
- threadpoolctl
- typing_extensions
- tzdata
- wrapt
- XlsxWriter
- zipp

These dependencies will be automatically installed when you install DocTableFlow using pip.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any questions or suggestions, feel free to contact the author:

- **Name**: Rohit Sahoo
- **Email**: rohitsahoo741@gmail.com
