
# Duck typing : - it is a concept where the type of an object is determined
# by its behaviouor , not by its class

class InkjetPrinter:
    def PrintDocument(self,document):
        print("Inkjet Printer printing : ", document)

class LaserPrinter:
    def PrintDocument(self,document):
        print("Laser Printer printing : ", document)

class PDFWriter:
    def PrintDocument(self,document):
        print(f"Saving : {document} as PDF")


def StartPrinting(Device):
    Device.PrintDocument("Marvellous Notes")

def main():
    StartPrinting(InkjetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())
main()

