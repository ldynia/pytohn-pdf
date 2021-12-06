from fpdf import FPDF

# A4
PDF_WIDTH_MM = 297
PDF_HEIGHT_MM = 210

COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (15, 2, 70)
COLOR_GREEN_1 = (98, 122, 110)
COLOR_GREEN_2 = (99, 129, 113)
COLOR_GREEN_3 = (32, 65, 49)


def txt_to_mm(txt, LETTER_WIDTH_MM=3.4):
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
        # Create page
        self.add_page()

        # Set page color by choosing background image.
        if self.metadata['background'] == 'green':
            self.image('/app/assets/bg1.png', x=0, y=0, w=PDF_WIDTH_MM, h=PDF_HEIGHT_MM)

        # Set graphics
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
        self.set_font('Times', 'I', 46)
        self.text(85, PDF_HEIGHT_MM/2 - 20, self.metadata['header'])

    def draw_name(self):
        self.set_font('Arial', 'B', 32)
        self.set_text_color(*COLOR_BLUE)
        name = self.metadata['full_name']
        offset = PDF_WIDTH_MM/2 - txt_to_mm(name)
        self.text(offset, PDF_HEIGHT_MM/2 + 3, name)

    def draw_body(self):
        # Draw text
        self.set_font('Times', '', 24)
        self.set_text_color(*COLOR_BLACK)
        self.text(97, PDF_HEIGHT_MM/2 + 20, self.metadata['text'])
        # Draw title
        self.set_font('Arial', 'B', 28)
        self.set_text_color(*COLOR_BLUE)
        self.text(75, PDF_HEIGHT_MM/2 + 40, self.metadata['title'])

    def draw_footer(self):
        # Draw date
        self.set_font('Times', '', 20)
        self.set_text_color(*COLOR_BLACK)
        self.text(15, PDF_HEIGHT_MM - 15, self.metadata['date'])

        # Draw uuid
        if self.metadata['uuid']:
            self.text(PDF_WIDTH_MM - 60, PDF_HEIGHT_MM - 15, self.metadata['uuid'])
