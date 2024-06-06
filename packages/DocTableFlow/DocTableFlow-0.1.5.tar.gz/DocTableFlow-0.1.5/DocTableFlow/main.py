import os

import pandas as pd
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdftypes import resolve1
from ._docTableExtractor import _docTableExtractor


def tableToExcel(input_path, output_dir, filename):
    filename = filename + '.xlsx'
    output_path = os.path.join(output_dir, filename)

    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Create an Excel writer object
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')

    df = _docTableExtractor(input_path)

    # Write the DataFrame to the specified sheet
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Save the workbook
    writer.close()


def tableToJson(input_path, output_dir, filename):
    filename = filename + '.json'

    output_path = os.path.join(output_dir, filename)

    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = _docTableExtractor(input_path)

    df.to_json(output_path)


def tableToDataframe(input_path):
    df = _docTableExtractor(input_path)
    return df


def tableToCSV(input_path, output_dir, filename):
    filename = filename + '.csv'
    output_path = os.path.join(output_dir, filename)

    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = _docTableExtractor(input_path)

    # Write the DataFrame to a CSV file
    df.to_csv(output_path, index=False, encoding='UTF-8')


def CountPages(input_path):
    file = open(input_path, 'rb')
    parser = PDFParser(file)
    document = PDFDocument(parser)
    total_pages = resolve1(document.catalog['Pages'])['Count']
    return total_pages
