import pymupdf
import pymupdf.layout
import pymupdf4llm

import camelot
import os, sys, time

# Pymupdf
def pymupdfFunc():
    doc = pymupdf.open("odel_report.pdf")
    pageThree = doc[3]

    allTables = pageThree.find_tables()
    table1 = allTables.tables[0]

    markdown = table1.to_markdown()

    with open("results/pymupdf.md", "w", encoding="utf-8") as f:
        f.write(markdown)

# Pymupdf4llm
def pymupdf4llmFunc():
    md = pymupdf4llm.to_markdown("odel_report.pdf")

    with open("results/pymupdf4llm.md", "w", encoding="utf-8") as f:
        f.write(md)

# Camelot
def camelotFunc():
    pdf_path = "odel_report.pdf"

    with pymupdf.open(pdf_path) as document:
        pageCount = document.page_count

    tables = camelot.read_pdf(pdf_path, pages=f"1 - {pageCount}", flavor="stream")
    print(tables[3].to_csv("results/camelot.csv"))

pymupdfFunc()
