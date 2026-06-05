import pymupdf
import pymupdf.layout

import pymupdf4llm

doc = pymupdf.open('odel_report.pdf')

pageOne = doc[0]
# allTables = pageOne.find_tables()
# table1 = allTables.tables[0]

print(pageOne.get_text())
