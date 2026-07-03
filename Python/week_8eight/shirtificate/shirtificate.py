from fpdf import FPDF
def main():
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font("Arial", size=24)

    # Center Text
    pdf.cell(0, 20, "CS50 Shirtificate", ln=True, align="C")

    # Add Image
    pdf.image("shirtificate.png", x=20, y=60, w=170)

    # Add Text to the Image
    pdf.set_text_color(255, 255, 255)
    name = input("Name: ") + " took CS50"
    page_width = pdf.w
    text_width = pdf.get_string_width(name)
    x = (page_width - text_width) / 2   # centrado horizontal
    y = 120                            # altura dentro de la camiseta
    pdf.text(x, y, name)


    # Output Image
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
