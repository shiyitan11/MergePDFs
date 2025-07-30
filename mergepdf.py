from PyPDF2 import PdfMerger

merger = PdfMerger()
for pdf in ["A.pdf", "B.pdf"]: #make sure we have two or more PDF files in the same directory as the script like A.pdf and B.pdf here
    merger.append(pdf)
merger.write("AB.pdf") #After running the code, a new file like AB.pdf here will be created, containing the merged pdf we want
merger.close()
