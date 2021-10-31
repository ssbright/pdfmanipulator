import PyPDF2

with open('dummy.pdf', 'rb') as file:  #needs to be read binary, and not just read mode so that PyPDF2 can read the binary file
  print(file)
  reader = PyPDF2.PdfFileReader(file)
  print(reader)
  print(reader.numPages)
  writer = PyPDF2.PdfFileWriter()

  page = reader.getPage(0)
  page.rotateCounterClockwise(90)
  writer.addPage(page)

  with open('tilted.pdf', 'wb') as tilt_file:
    writer.write(tilt_file)
