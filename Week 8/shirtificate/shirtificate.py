from fpdf import FPDF
from requests import get
from os import path
class PDF:
    def __init__(self):
        self.pdf = FPDF()
        if not path.exists('shirtificate.png'):
            print("Downloading main ...")
            with open('shirtificate.png', 'wb') as f:
                res = get("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png")
                f.write(res.content)
                f.close()


    def setup_certificate(self):
        self.pdf.add_page()
        self.pdf.set_font("helvetica", "B", 30)
        self.pdf.cell(0, 50, 'CS50 Certificate', align='C')
        self.pdf.image("shirtificate.png", w=self.pdf.epw)
        self.pdf.set_font_size(20)
        self.pdf.set_text_color(255, 255, 255)

    def add_name(self, name):
        self.pdf.text(x=55, y=125, txt=f"{name} took CS50")

    def save_pdf(self, name):
        self.pdf.output(name)

def main():
    name = input("Name: ")
    if not name:
        print("Invalid name entered.")
        return

    pdf = PDF()
    pdf.setup_certificate()
    pdf.add_name(name)
    pdf.save_pdf("shirtificate.pdf")

if __name__ == "__main__":
    main()
