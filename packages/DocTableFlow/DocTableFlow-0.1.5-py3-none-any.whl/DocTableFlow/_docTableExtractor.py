from __future__ import division
from pdfminer.layout import LAParams
import pandas as pd
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
import pdfminer
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import resolve1
from sklearn.cluster import KMeans
from os.path import basename
import re
from pdfminer.pdfparser import PDFParser
import os
import numpy as np
import PyPDF2
import warnings
import sys
from matplotlib import patches
import tempfile

if not sys.warnoptions:
    warnings.simplefilter("ignore")


def _get_pdf_searchable_pages(fname):
    from pdfminer.pdfpage import PDFPage
    searchable_pages = []
    non_searchable_pages = []
    page_num = 0
    with open(fname, 'rb') as infile:

        for page in PDFPage.get_pages(infile):
            page_num += 1
            if 'Font' in page.resources.keys():
                searchable_pages.append(page_num)
            else:
                non_searchable_pages.append(page_num)
    if page_num > 0:
        if len(searchable_pages) == 0:
            return "Nonsearchable"
        elif len(non_searchable_pages) == 0:
            return "searchable"

    else:
        return "Invalid"


def _docTableExtractor(input_file):
    is_searchable = _get_pdf_searchable_pages(input_file)
    tabular_content_all_pages = []
    if is_searchable == "Nonsearchable":
        cmd = "ocrmypdf " + input_file + " " + input_file + " --force-ocr"
        os.system(cmd)

    file = open(input_file, 'rb')
    parser = PDFParser(file)
    document = PDFDocument(parser)
    total_pages = resolve1(document.catalog['Pages'])['Count']
    base_filename = basename(input_file)
    # Create a temporary file for the math log
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_log:
        math_log_filename = temp_log.name

    # print(f"Temporary math log file created at: {math_log_filename}")
    # log_file = open('math_log.txt', 'a', encoding='utf-8')
    table_clusters_list = []
    log_file = open(math_log_filename, 'a', encoding='utf-8')
    for page_number in range(0, total_pages):
        base_filename = base_filename.replace('.pdf', '') + '_pg_' + str(page_number)

        class PdfCoodrinates:
            def __init__(self):
                self.x_positions = []
                self.y_positions = []
                self.extracted_texts = []

            def parse_obj(self, lt_objs):
                for obj in lt_objs:
                    if isinstance(obj, pdfminer.layout.LTTextLine):
                        self.x_positions.append(int(obj.bbox[0]))
                        self.y_positions.append(int(obj.bbox[1]))
                        self.extracted_texts.append(str(obj.get_text()))
                        math_log = str(obj.bbox[0]) + ' ' + str(obj.bbox[1]) + ' ' + str(
                            obj.get_text().replace('\n', '_'))
                        log_file.write(math_log + '\n')

                    if isinstance(obj, pdfminer.layout.LTTextBoxHorizontal):
                        self.parse_obj(obj._objs)

                    elif isinstance(obj, pdfminer.layout.LTFigure):
                        self.parse_obj(obj._objs)

            def parsepdf(self, filename, startpage, endpage):

                # Open a PDF file.
                fp = open(filename, 'rb')

                # Create a PDF parser object associated with the file object.
                parser = PDFParser(fp)

                # Create a PDF document object that stores the document structure.
                document = PDFDocument(parser)

                # Check if the document allows text extraction. If not, abort.
                if not document.is_extractable:
                    raise PDFTextExtractionNotAllowed

                # Create a PDF page aggregator object.
                device = PDFPageAggregator(PDFResourceManager(), laparams=LAParams())

                # Create a PDF interpreter object.
                interpreter = PDFPageInterpreter(PDFResourceManager(), device)

                i = 0
                for page in PDFPage.create_pages(document):
                    if startpage <= i <= endpage:
                        interpreter.process_page(page)
                        layout = device.get_result()
                        self.parse_obj(layout._objs)
                    i += 1

        def table_without_border(pdf_path):
            global text_pos
            pdf_handler = PdfCoodrinates()
            pdf_handler.parsepdf(pdf_path, 0, 0)
            y_positions = pdf_handler.y_positions
            x_positions = pdf_handler.x_positions
            extracted_texts = pdf_handler.extracted_texts

            def list_duplicates(seq):
                tally = defaultdict(list)
                for i, item in enumerate(seq):
                    tally[item].append(i)

                return ((key, locs) for key, locs in tally.items())

            close_pairs = []
            for pos1 in y_positions:
                for pos2 in y_positions:
                    if math.isclose(pos1, pos2, abs_tol=1):
                        close_pairs.append((pos1, pos2))

            for pair in close_pairs:
                for index, value in enumerate(y_positions):
                    if value == pair[0]:
                        y_positions[index] = pair[1]

            l = []
            for dup in sorted(list_duplicates(y_positions), reverse=True):
                l.append(dup)

            # Initialize empty DataFrame and lists to store intermediate results
            final_dataframe = pd.DataFrame()
            current_row = []
            all_rows = []
            cleaned_rows = []

            # Process duplicate y_positions
            for duplicate in sorted(list_duplicates(y_positions), reverse=True):
                for position in duplicate[1]:
                    # Clean and prepare the text
                    cleaned_text = str(extracted_texts[position]).replace('\n', '')
                    current_row.append(cleaned_text)

                all_rows.append(current_row)

                # Remove unwanted characters and spaces
                current_row = [item for item in current_row if item not in [' ', '  ', '   ', '$']]

                cleaned_rows.append(current_row)
                current_row = []

            # Convert all_rows to DataFrame
            for row in all_rows:
                final_dataframe = pd.concat([final_dataframe, pd.Series(row).to_frame().T], ignore_index=True)

            clusters_found = len(max(cleaned_rows, key=len))
            if 15 < clusters_found < 18:
                clusters_found = 20

            table_clusters_list.append(clusters_found)
            if int(math.fabs(table_clusters_list[0] - clusters_found)) == 1:
                clusters_found = table_clusters_list[0]

            kmeans = KMeans(n_clusters=clusters_found)
            x_positions_array = np.array(x_positions).reshape(-1, 1)
            kmeans_output = kmeans.fit(x_positions_array)
            centroids = kmeans_output.cluster_centers_

            # Convert centroids to a sorted list of integers
            sorted_centroids = sorted([int(centroid[0]) for centroid in centroids])

            # Identify pairs of y_positions within a minimum distance for a new line
            close_pairs = [(elem1, elem2) for elem1 in y_positions for elem2 in y_positions if abs(elem1 - elem2) < 6]

            for pair in close_pairs:
                for index, value in enumerate(y_positions):
                    if value == pair[0]:
                        y_positions[index] = pair[1]

            res_table = [' '] * clusters_found
            table_content = []

            table_df = pd.DataFrame([])

            for duplicates in sorted(list_duplicates(y_positions), reverse=True):
                for index in duplicates[1]:
                    # Clean and prepare the text
                    cleaned_text = str(extracted_texts[index]).replace('\n', '').strip()
                    cleaned_text = re.sub(' +', ' ', cleaned_text)
                    cluster_index = min(range(len(sorted_centroids)),
                                        key=lambda i: abs(sorted_centroids[i] - x_positions[index]))

                    leading_spaces = len(cleaned_text) - len(cleaned_text.lstrip())
                    if leading_spaces > 5:
                        cleaned_text = 'temp_text' + '          ' + cleaned_text

                    split_text = cleaned_text.split('   ')
                    split_text_result = [segment.replace('temp_text', '   ') for segment in split_text if
                                         segment != '']
                    cleaned_text = cleaned_text.replace('temp_text', '')

                    if res_table[cluster_index] != ' ':
                        res_table[cluster_index] += cleaned_text
                    elif len(split_text_result) > 1:
                        for i, segment in enumerate(split_text_result):
                            if cluster_index + i < len(res_table):
                                res_table[cluster_index + i] = segment
                            else:
                                res_table.insert(cluster_index + i, segment)
                    else:
                        res_table[cluster_index] = cleaned_text

                res_table.extend([' '] * clusters_found)

                if any(s.strip() for s in res_table):
                    table_content.append(res_table)

                res_table = [' '] * clusters_found

            list_text_positions = []

            # Calculate the number of non-space items in each row and store in list_text_positions
            for row in table_content:
                non_space_count = sum(1 for item in row if item != " ")
                list_text_positions.append(non_space_count)

            # Remove rows from table_content where the corresponding count in list_text_positions is 1
            for text_position in list_text_positions:
                counter = 0
                if text_position == 1:
                    del table_content[counter]
                    counter += 1
                if text_position > 1:
                    break

            # Find the first occurrence of a count greater than 1 and remove all preceding counts
            for item in list_text_positions:
                if item > 1:
                    index = list_text_positions.index(item)
                    break
            del list_text_positions[0:index]

            # Reverse the list and find the first occurrence of a count greater than 1
            list_text_positions.reverse()
            for item in list_text_positions:
                if item > 1:
                    text_pos = list_text_positions.index(item)
                    break
            list_text_positions.reverse()

            # If text_pos is not 0, delete the last text_pos number of items from both lists
            if text_pos != 0:
                del table_content[-text_pos:]
                del list_text_positions[-text_pos:]

            # Remove lines where the count of non-space items is exactly 1 for more than 7 consecutive lines
            # Repeat the process 10 times
            for _ in range(10):
                total_words = 0  # Initialize the counter for consecutive words with value 1
                word_nos = 0  # Initialize the index counter

                # Iterate through each text position in the list
                for text_position in list_text_positions:
                    if text_position == 1:
                        total_words += 1  # Increment the count if the text position is 1

                    if text_position > 1:
                        if total_words < 8:
                            total_words = 0  # Reset the count if there are fewer than 8 consecutive 1s

                        if total_words > 7:
                            break  # Exit the loop if there are more than 7 consecutive 1s

                    word_nos += 1  # Increment the index counter

                start = word_nos - total_words  # Calculate the start position of the consecutive 1s

                if total_words > 7:
                    delete = start + 7  # Determine the position to start deleting from

                    # Delete the elements from table_content and list_text_positions
                    del table_content[delete:word_nos]
                    del list_text_positions[delete:word_nos]

            # Convert remaining table content to a DataFrame and append it to the list
            for record in table_content:
                table_df = pd.concat([table_df, pd.Series(record).to_frame().T], ignore_index=True)

            # Append the DataFrame to the list of all pages' tabular content
            tabular_content_all_pages.append(table_df)

    for page_number in range(0, total_pages):

        pfr = PyPDF2.PdfReader(open(input_file, "rb"))
        orientation = pfr.pages[0].get('/Rotate')
        try:
            pfr.decrypt('')
        except:
            pass

        if orientation == 180 or orientation == 270 or orientation == 90:

            pdf_in = open(input_file, 'rb')
            pdf_reader = PyPDF2.PdfReader(pdf_in)
            pdf_writer = PyPDF2.PdfWriter()

            for pagenum in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]
                page.rotate(360 - orientation)
                pdf_writer.add_page(page)

            pdf_out = open('input_pdf_rotated.pdf', 'wb')
            pdf_writer.write(pdf_out)
            pdf_out.close()
            pdf_in.close()

            pfr = PyPDF2.PdfReader(open("input_pdf_rotated.pdf", "rb"))

            pg9 = pfr.pages[page_number]
            writer = PyPDF2.PdfWriter()

            writer.add_page(pg9)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                NewPDFfilename = temp_pdf.name

            # print(f"Temporary PDF file created at: {NewPDFfilename}")

            # Write to the temporary PDF file
            with open(NewPDFfilename, "wb") as outputStream:
                writer.write(outputStream)

        else:
            pg9 = pfr.pages[page_number]
            writer = PyPDF2.PdfWriter()
            writer.add_page(pg9)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                NewPDFfilename = temp_pdf.name

            # print(f"Temporary PDF file created at: {NewPDFfilename}")

            # Write to the temporary PDF file
            with open(NewPDFfilename, "wb") as outputStream:
                writer.write(outputStream)

        def get_pdf_page_layouts(file_path):
            """
            Retrieves the layout of each page from a PDF file.

            Parameters:
                file_path (str): The path to the PDF file.

            Returns:
                list: A list containing the layout objects of each page in the PDF.
            """
            # Initialize layout analysis parameters
            layout_params = LAParams()

            # Open the PDF file in binary read mode
            with open(file_path, 'rb') as file:
                pdf_parser = PDFParser(file)
                pdf_document = PDFDocument(pdf_parser)

                # Ensure the document allows text extraction
                if not pdf_document.is_extractable:
                    raise PDFTextExtractionNotAllowed

                # Set up resource manager and device for page aggregation
                resource_manager = PDFResourceManager()
                page_aggregator = PDFPageAggregator(resource_manager, laparams=layout_params)
                pdf_interpreter = PDFPageInterpreter(resource_manager, page_aggregator)

                # List to hold the layout of each page
                page_layouts = []

                # Process each page and extract the layout
                for pdf_page in PDFPage.create_pages(pdf_document):
                    pdf_interpreter.process_page(pdf_page)
                    page_layout = page_aggregator.get_result()
                    page_layouts.append(page_layout)

            return page_layouts

        page_layouts = get_pdf_page_layouts(NewPDFfilename)
        TEXT_ELEMENTS = [
            pdfminer.layout.LTTextBox,
            pdfminer.layout.LTTextBoxHorizontal,
            pdfminer.layout.LTTextLine,
            pdfminer.layout.LTTextLineHorizontal
        ]

        def pdf_characters(pdf_element):
            """
            Recursively extracts characters from a given PDF element.

            Parameters:
                pdf_element: An element from a PDF layout, which can be of various types.

            Returns:
                list: A list of extracted LTChar objects.
            """
            if isinstance(pdf_element, pdfminer.layout.LTChar):
                return [pdf_element]

            if isinstance(pdf_element, (list, TEXT_ELEMENTS[0], TEXT_ELEMENTS[1], TEXT_ELEMENTS[2], TEXT_ELEMENTS[3])):
                return [char for sub_element in pdf_element for char in pdf_characters(sub_element)]

            return []

        pdf_table_content_located = list()
        table_figure = page_layouts[0]
        texts = []
        table_rectangle_data = []

        for each_figure in table_figure:
            if isinstance(each_figure, pdfminer.layout.LTTextBoxHorizontal):
                texts.append(each_figure)
            elif isinstance(each_figure, pdfminer.layout.LTRect):
                table_rectangle_data.append(each_figure)
        table_data_chars = pdf_characters(texts)

        def rectangle_table_width(rect):
            x_min, y_min, x_max, y_max = rect.bbox
            return min(x_max - x_min, y_max - y_min)

        def rectangle_table_area(rect):
            x_0, y_0, x_1, y_1 = rect.bbox
            return (x_1 - x_0) * (y_1 - y_0)

        def rectangle_borders(rect):
            x_0, y_0, x_1, y_1 = rect.bbox

            if x_1 - x_0 > y_1 - y_0:
                return (x_0, y_0, x_1, y_0, "H")
            else:
                return (x_0, y_0, x_0, y_1, "V")

        lines = [rectangle_borders(r) for r in table_rectangle_data
                 if rectangle_table_width(r) < 2 and
                 rectangle_table_area(r) > 1]

        xmin, ymin, xmax, ymax = table_figure.bbox

        def is_within_range(x, xmin, xmax):
            return xmin <= x <= xmax

        def find_bounding_rectangle(x, y, lines):
            # Identify vertical lines that intersect with the y-coordinate
            vertical_lines = [line for line in lines if line[4] == "V" and is_within_range(y, line[1], line[3])]

            # Identify horizontal lines that intersect with the x-coordinate
            horizontal_lines = [line for line in lines if line[4] == "H" and is_within_range(x, line[0], line[2])]

            # If there are fewer than 2 intersecting vertical or horizontal lines, return None
            if len(vertical_lines) < 2 or len(horizontal_lines) < 2:
                return None

            # Find vertical lines to the left and right of the x-coordinate
            left_verticals = [v[0] for v in vertical_lines if v[0] < x]
            right_verticals = [v[0] for v in vertical_lines if v[0] > x]

            # If there are no left or right vertical lines, return None
            if not left_verticals or not right_verticals:
                return None

            # Determine the bounding x-coordinates
            x0, x1 = max(left_verticals), min(right_verticals)

            # Find horizontal lines below and above the y-coordinate
            lower_horizontals = [h[1] for h in horizontal_lines if h[1] < y]
            upper_horizontals = [h[1] for h in horizontal_lines if h[1] > y]

            # If there are no lower or upper horizontal lines, return None
            if not lower_horizontals or not upper_horizontals:
                return None

            # Determine the bounding y-coordinates
            y0, y1 = max(lower_horizontals), min(upper_horizontals)

            # Return the coordinates of the bounding rectangle
            return (x0, y0, x1, y1)

        from collections import defaultdict
        import math

        bounding_box_dict = {}
        for char_data in table_data_chars:
            bounding_boxes = defaultdict(int)

            # Get the left coordinates of the character's bounding box
            left_x, left_y = char_data.bbox[0], char_data.bbox[1]
            # Find the bounding rectangle for the left coordinates
            bbox_left = find_bounding_rectangle(left_x, left_y, lines)
            # Increment the count for this bounding rectangle
            bounding_boxes[bbox_left] += 1

            # Calculate the center coordinates of the character's bounding box
            center_x, center_y = math.floor((char_data.bbox[0] + char_data.bbox[2]) / 2), math.floor(
                (char_data.bbox[1] + char_data.bbox[3]) / 2)
            # Find the bounding rectangle for the center coordinates
            bbox_center = find_bounding_rectangle(center_x, center_y, lines)
            # Increment the count for this bounding rectangle
            bounding_boxes[bbox_center] += 1

            # Get the upper coordinates of the character's bounding box
            upper_x, upper_y = char_data.bbox[2], char_data.bbox[3]
            # Find the bounding rectangle for the upper coordinates
            bbox_upper = find_bounding_rectangle(upper_x, upper_y, lines)
            # Increment the count for this bounding rectangle
            bounding_boxes[bbox_upper] += 1

            # Determine the bounding box with the highest count
            if max(bounding_boxes.values()) == 1:
                bbox = bbox_center
            else:
                bbox = max(bounding_boxes.items(), key=lambda item: item[1])[0]

            if bbox is None:
                continue

            if bbox in bounding_box_dict:
                bounding_box_dict[bbox].append(char_data)
            else:
                bounding_box_dict[bbox] = [char_data]

        for x in range(int(xmin), int(xmax), 10):
            for y in range(int(ymin), int(ymax), 10):
                bbox = find_bounding_rectangle(x, y, lines)
                if bbox is None:
                    continue
                if bbox in bounding_box_dict:
                    continue
                bounding_box_dict[bbox] = []

        def concatenate_characters(character_objects):
            """
            Converts a list of characters with bounding box positions into a concatenated string.

            Parameters:
                character_objects (list): A list of character objects with bounding box attributes.

            Returns:
                str: A single string with characters concatenated row by row.
            """
            if not character_objects:
                return ""
            # Extract and sort unique row positions in descending order
            unique_row_positions = sorted({char.bbox[1] for char in character_objects}, reverse=True)
            concatenated_result = ""

            for row_position in unique_row_positions:
                # Filter characters belonging to the current row and sort by horizontal position
                characters_in_current_row = sorted((char for char in character_objects if char.bbox[1] == row_position),
                                                   key=lambda char: char.bbox[0])
                # Concatenate text from characters in the sorted row and append to the result string
                row_text = ''.join(char.get_text() for char in characters_in_current_row)
                concatenated_result += " {}".format(row_text)
            return concatenated_result.strip()

        def idenify_tabular_boxes(boxed_records):
            """
            Converts a dictionary of boxed records into a table format with rows and columns.

            Parameters:
                boxed_records (dict): A dictionary where keys are bounding boxes (tuples) and values are lists of character objects.

            Returns:
                list: A list of lists representing the table content, with each inner list corresponding to a row.
            """
            # Extract the keys which are the bounding boxes
            bounding_boxes = boxed_records.keys()
            # Create a list of unique row indices sorted in descending order
            unique_row_indices = sorted({box[1] for box in bounding_boxes}, reverse=True)
            table_rows = []

            # Group boxes by row and sort them by their column index
            for row_index in unique_row_indices:
                boxes_in_row = sorted((box for box in bounding_boxes if box[1] == row_index), key=lambda box: box[0])
                # Convert the content of each box to a string and add to the current row list
                row_content = [concatenate_characters(boxed_records[box]) for box in boxes_in_row]
                table_rows.append(row_content)

            return table_rows

        pdf_table_content_located.extend(idenify_tabular_boxes(bounding_box_dict))

        if len(pdf_table_content_located) != 0:
            table_df = pd.DataFrame(pdf_table_content_located)
            tabular_content_all_pages.append(table_df)
        else:
            table_without_border(NewPDFfilename)

    dfs = []

    for each_table in tabular_content_all_pages:
        dfs.append(each_table)
        for _ in range(6):
            dfs.append(pd.Series([np.nan]))

    # Concatenate all DataFrames and NaN series
    tabular_content_all_pages_df = pd.concat(dfs, ignore_index=True)

    tabular_content_all_pages = len(tabular_content_all_pages_df.columns.values)

    return tabular_content_all_pages_df




# tableToExcel('/Users/rohitsahoo/Desktop/auto-table-extract/upload/research.pdf','/Users/rohitsahoo/Desktop/auto-table-extract/csv')
