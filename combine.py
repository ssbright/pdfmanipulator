import PyPDF2


inputs = ['dummy.pdf', 'twopage.pdf', 'wtr.pdf']
print(inputs)

def pdf_combiner(pdf_list):
  merger = PyPDF2.PdfFileMerger()
  for pdf in pdf_list:
    print(pdf)
    merger.append(pdf)
  merger.write('combined.pdf')

pdf_combiner(inputs)
