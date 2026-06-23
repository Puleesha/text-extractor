import pymupdf
# import pymupdf.layout
# import pymupdf4llm

import camelot
import os, sys, time

# Pymupdf
def pumupdfFunc():
    doc = pymupdf.open("odel_report.pdf")
    pageOne = doc[1]

    # allTables = pageOne.find_tables()
    # table1 = allTables.tables[0]

    print(pageOne.get_text())

# Camelot
def camelotFunc():
    pdf_path = "odel_report.pdf"

    with pymupdf.open(pdf_path) as document:
        pageCount = document.page_count

    tables = camelot.read_pdf(pdf_path, pages=f"1 - {pageCount}", flavor="stream")
    print(tables[2])

camelotFunc()
