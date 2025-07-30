from PyPDF2 import PdfMerger

merger = PdfMerger()
for pdf in ["A.pdf", "B.pdf"]:
    merger.append(pdf)
merger.write("AB.pdf")
merger.close()