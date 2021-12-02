from fpdf import FPDF


PDF_WIDTH_MM = 297
PDF_HEIGHT_MM = 210
LETTER_WIDTH_MM = 3.4

COLOR_GREEN_1 = (98, 122, 110)
COLOR_GREEN_2 = (99, 129, 113)
COLOR_GREEN_3 = (32, 65, 49)


def txt_to_mm(txt):
    return int(len(txt) * LETTER_WIDTH_MM)


class CertGenerator(FPDF):

    def __init__(self, metadata, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.metadata = metadata

        # Factory
        self.set_up_page()
        self.draw_frame()
        self.draw_header()
        self.draw_name()
        self.draw_body()
        self.draw_footer()

    def set_up_page(self):
        self.add_page()
        self.image('/app/assets/bg1.png', x=0, y=0, w=PDF_WIDTH_MM, h=PDF_HEIGHT_MM)
        self.set_draw_color(*COLOR_GREEN_3)
        self.image('/app/assets/ornament_left.png', x=10, y=10)
        self.image('/app/assets/ornament_right.png', x=PDF_WIDTH_MM-42, y=10)
        self.image('/app/assets/logo_small.png', x=PDF_HEIGHT_MM/2 + 13, y=20)

    def draw_frame(self):
        self.set_line_width(1)

        # top lines
        self.line(5, 5, PDF_WIDTH_MM-5, 5)
        self.line(7, 7, PDF_WIDTH_MM-7, 7)

        # left lines
        self.line(5, 5, 5, PDF_HEIGHT_MM-5)
        self.line(7, 7, 7, PDF_HEIGHT_MM-7)

        # right lines
        self.line(PDF_WIDTH_MM-5, 5, PDF_WIDTH_MM-5, PDF_HEIGHT_MM-5)
        self.line(PDF_WIDTH_MM-7, 7, PDF_WIDTH_MM-7, PDF_HEIGHT_MM-7)

        # bottom lines
        self.line(5, PDF_HEIGHT_MM-5, PDF_WIDTH_MM-5, PDF_HEIGHT_MM-5)
        self.line(7, PDF_HEIGHT_MM-7, PDF_WIDTH_MM-7, PDF_HEIGHT_MM-7)

    def draw_header(self):
        self.set_font('Times', 'I', 32)
        self.text(85, PDF_HEIGHT_MM/2 - 20, 'Certificate of Achievement')

    def draw_name(self):
        self.set_font('Arial', 'B', 32)
        name = self.metadata['full_name']
        offset = PDF_WIDTH_MM/2 - txt_to_mm(name)
        self.text(offset, PDF_HEIGHT_MM/2, name)

    def draw_body(self):
        self.set_font('Times', '', 28)
        self.text(75, PDF_HEIGHT_MM/2 + 20, self.metadata['text'])
        self.text(60, PDF_HEIGHT_MM/2 + 30, self.metadata['tilte'])

    def draw_footer(self):
        self.set_font('Times', '', 20)
        self.text(15, PDF_HEIGHT_MM - 15, self.metadata['date'])
        self.text(PDF_WIDTH_MM - 60, PDF_HEIGHT_MM - 15, self.metadata['uuid'])
