#duck Typing : It is a concept where the type of an object is determined 
#by its behaviour not by its class.

class InkJetPrinter:
    def PrintDocument(self, document):
        print("Ink Jet Printer printing : " , document)

class LaserPrinter:
    def PrintDocument(self, document):
        print("Laser Printer printing : " , document)

class PDFWriter:
    def PrintDocument(self, document):
        print(f"Saving {document} as PDF")

def StartPrinting(Device):
    Device.PrintDocument("Marvellous Notes")

def main():
    StartPrinting(InkJetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())

main()