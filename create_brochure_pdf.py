#!/usr/bin/env python3
"""
Château Alaverdi Professional Tri-Fold Brochure Generator
Creates print-ready PDF with images, brand colors, and complete content
"""

from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
import os

class ChateauAlaverdiBrochure:
    def __init__(self, output_file="Chateau_Alaverdi_Brochure.pdf"):
        self.output_file = output_file

        # Page setup - 11x8.5 landscape for tri-fold
        self.page_width, self.page_height = landscape(letter)

        # Tri-fold panel width (divide by 3)
        self.panel_width = self.page_width / 3

        # Brand colors
        self.wine_red = HexColor('#651f29')
        self.beige = HexColor('#f5f5dc')
        self.dark_gray = HexColor('#333333')
        self.light_gray = HexColor('#666666')

        # Margins
        self.margin = 0.3 * inch

        # Image paths
        self.photos_dir = "photos"

    def add_bleed_marks(self, c):
        """Add crop marks for printing"""
        c.setStrokeColor(black)
        c.setLineWidth(0.5)
        mark_length = 0.125 * inch

        # Corner marks
        corners = [
            (0, 0), (self.page_width, 0),
            (0, self.page_height), (self.page_width, self.page_height)
        ]

        for x, y in corners:
            if x == 0:
                c.line(x, y, x + mark_length, y)
            else:
                c.line(x, y, x - mark_length, y)
            if y == 0:
                c.line(x, y, x, y + mark_length)
            else:
                c.line(x, y, x, y - mark_length)

    def draw_text_block(self, c, text, x, y, width, font_size=10, color=None,
                       bold=False, italic=False, align='left', leading=None):
        """Draw a text block with word wrapping"""
        if color:
            c.setFillColor(color)
        else:
            c.setFillColor(self.dark_gray)

        c.setFont("Helvetica-Bold" if bold else "Helvetica", font_size)

        if leading is None:
            leading = font_size * 1.3

        # Simple word wrapping
        words = text.split()
        lines = []
        current_line = []

        for word in words:
            test_line = ' '.join(current_line + [word])
            if c.stringWidth(test_line, "Helvetica-Bold" if bold else "Helvetica", font_size) < width - self.margin * 2:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]

        if current_line:
            lines.append(' '.join(current_line))

        # Draw lines
        current_y = y
        for line in lines:
            if align == 'center':
                text_width = c.stringWidth(line, "Helvetica-Bold" if bold else "Helvetica", font_size)
                x_pos = x + (width - text_width) / 2
            else:
                x_pos = x

            c.drawString(x_pos, current_y, line)
            current_y -= leading

        return current_y

    def add_image(self, c, image_path, x, y, width, height):
        """Add image to PDF"""
        try:
            if os.path.exists(image_path):
                img = ImageReader(image_path)
                c.drawImage(img, x, y, width=width, height=height, preserveAspectRatio=True, mask='auto')
                return True
        except Exception as e:
            print(f"Warning: Could not add image {image_path}: {e}")
        return False

    def create_front_cover(self, c, x_start):
        """Panel 1: Front Cover (Outside Right)"""
        panel_x = x_start

        # Background image - Monastery
        monastery_img = os.path.join(self.photos_dir, "monastery-heritage.png")
        if os.path.exists(monastery_img):
            # Full panel background image
            self.add_image(c, monastery_img, panel_x, 0, self.panel_width, self.page_height)

        # Semi-transparent overlay for text readability
        c.setFillColorRGB(0.1, 0.05, 0.05, alpha=0.6)
        c.rect(panel_x, self.page_height - 3*inch, self.panel_width, 2.5*inch, fill=True, stroke=False)

        # Company name (large, centered, white)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 26)
        company_name = "CHÂTEAU ALAVERDI"
        name_width = c.stringWidth(company_name, "Helvetica-Bold", 26)
        c.drawString(panel_x + (self.panel_width - name_width) / 2, self.page_height - 1.5*inch, company_name)

        c.setFont("Helvetica-Bold", 22)
        year = "1782"
        year_width = c.stringWidth(year, "Helvetica-Bold", 22)
        c.drawString(panel_x + (self.panel_width - year_width) / 2, self.page_height - 1.9*inch, year)

        # Tagline
        c.setFont("Helvetica-Oblique", 11)
        tagline = "Where 8,000 years of Georgian"
        tagline2 = "winemaking meets a new"
        tagline3 = "generation of elegance"

        tag_width = c.stringWidth(tagline, "Helvetica-Oblique", 11)
        c.drawString(panel_x + (self.panel_width - tag_width) / 2, self.page_height - 2.3*inch, tagline)
        tag_width2 = c.stringWidth(tagline2, "Helvetica-Oblique", 11)
        c.drawString(panel_x + (self.panel_width - tag_width2) / 2, self.page_height - 2.5*inch, tagline2)
        tag_width3 = c.stringWidth(tagline3, "Helvetica-Oblique", 11)
        c.drawString(panel_x + (self.panel_width - tag_width3) / 2, self.page_height - 2.7*inch, tagline3)

    def create_story_panel(self, c, x_start):
        """Panel 2: Our Story (Inside Left)"""
        panel_x = x_start + self.margin
        current_y = self.page_height - 0.7*inch

        # Header
        c.setFillColor(self.wine_red)
        c.setFont("Helvetica-Bold", 20)
        c.drawString(panel_x, current_y, "Our Story")
        current_y -= 0.4*inch

        # Story text
        story = """For 8,000 years, Georgia has been the cradle of wine.

Château Alaverdi 1782 carries this timeless heritage forward with a modern, château-level approach. Named in honor of the sacred Alaverdi Monastery's restoration in 1782, each bottle captures the terroir, the Georgian sunlight, and eight millennia of winemaking devotion.

At Château Alaverdi 1782, we unite the spiritual depth of Georgia's winemaking tradition with the refinement of European craftsmanship."""

        current_y = self.draw_text_block(c, story, panel_x, current_y,
                                         self.panel_width - self.margin * 2,
                                         font_size=9.5, leading=13)

        current_y -= 0.3*inch

        # Vision box
        c.setFillColor(self.beige)
        box_height = 0.7*inch
        c.rect(panel_x - 0.1*inch, current_y - box_height + 0.1*inch,
               self.panel_width - self.margin*2 + 0.2*inch, box_height, fill=True, stroke=False)

        c.setFillColor(self.wine_red)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(panel_x, current_y - 0.2*inch, "Our Vision")

        c.setFillColor(self.dark_gray)
        c.setFont("Helvetica-Oblique", 9)
        vision = "To bring the soul of Georgian winemaking"
        vision2 = "to the world — one bottle at a time."
        c.drawString(panel_x, current_y - 0.4*inch, vision)
        c.drawString(panel_x, current_y - 0.55*inch, vision2)

        current_y -= 1.0*inch

        # Small vineyard image
        vineyard_img = os.path.join(self.photos_dir, "hero-vineyard.png")
        if os.path.exists(vineyard_img):
            self.add_image(c, vineyard_img, panel_x - 0.1*inch, current_y - 1.8*inch,
                          self.panel_width - self.margin*2 + 0.2*inch, 1.5*inch)

    def create_wines_panel(self, c, x_start):
        """Panel 3: Our Wines (Inside Center)"""
        panel_x = x_start + self.margin
        current_y = self.page_height - 0.7*inch

        # Header
        c.setFillColor(self.wine_red)
        c.setFont("Helvetica-Bold", 20)
        c.drawString(panel_x, current_y, "Our Wines")
        current_y -= 0.5*inch

        # Saperavi
        saperavi_img = os.path.join(self.photos_dir, "bottle-saperavi-new.png")
        if os.path.exists(saperavi_img):
            self.add_image(c, saperavi_img, panel_x + 0.3*inch, current_y - 1.5*inch,
                          1.2*inch, 1.8*inch)

        # Saperavi text
        c.setFillColor(self.wine_red)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(panel_x, current_y, "Alaverdi Saperavi 1782")

        c.setFillColor(self.light_gray)
        c.setFont("Helvetica-Oblique", 10)
        c.drawString(panel_x, current_y - 0.18*inch, "Reserve Red")

        c.setFillColor(self.dark_gray)
        c.setFont("Helvetica", 8)
        c.drawString(panel_x, current_y - 0.35*inch, "Dry Red | 100% Saperavi | ABV: 13.5-14%")

        current_y -= 0.55*inch

        tasting = """Deep ruby-garnet. Aromas of black cherry, plum and graphite. Rich, structured palate with elegant tannin, cedar spice and a long mineral finish. Oak-aged 12-18 months."""

        current_y = self.draw_text_block(c, tasting, panel_x, current_y,
                                         self.panel_width - self.margin * 2,
                                         font_size=8, leading=10)

        c.setFont("Helvetica-Bold", 8)
        c.drawString(panel_x, current_y - 0.15*inch, "Pairing:")
        c.setFont("Helvetica", 8)
        pairing = "Roasted lamb, aged cheeses, dark chocolate"
        c.drawString(panel_x + 0.5*inch, current_y - 0.15*inch, pairing)

        current_y -= 0.5*inch

        # Rkatsiteli
        rkatsiteli_img = os.path.join(self.photos_dir, "bottle-rkatsiteli-new.png")
        if os.path.exists(rkatsiteli_img):
            self.add_image(c, rkatsiteli_img, panel_x + 0.3*inch, current_y - 1.5*inch,
                          1.2*inch, 1.8*inch)

        c.setFillColor(self.wine_red)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(panel_x, current_y, "Alaverdi Rkatsiteli 1782")

        c.setFillColor(self.light_gray)
        c.setFont("Helvetica-Oblique", 10)
        c.drawString(panel_x, current_y - 0.18*inch, "Classic White")

        c.setFillColor(self.dark_gray)
        c.setFont("Helvetica", 8)
        c.drawString(panel_x, current_y - 0.35*inch, "Dry White | 100% Rkatsiteli | ABV: 12.5-13%")

        current_y -= 0.55*inch

        tasting2 = """Golden amber hue. Fragrant notes of pear, quince, and wild honey. Textured, layered, and elegant with a vibrant acidity."""

        current_y = self.draw_text_block(c, tasting2, panel_x, current_y,
                                         self.panel_width - self.margin * 2,
                                         font_size=8, leading=10)

        c.setFont("Helvetica-Bold", 8)
        c.drawString(panel_x, current_y - 0.15*inch, "Pairing:")
        c.setFont("Helvetica", 8)
        pairing2 = "Grilled fish, spiced vegetables, light poultry"
        c.drawString(panel_x + 0.5*inch, current_y - 0.15*inch, pairing2)

    def create_terroir_panel(self, c, x_start):
        """Panel 4: Terroir & Winemaking (Inside Right)"""
        panel_x = x_start + self.margin
        current_y = self.page_height - 0.7*inch

        # Header
        c.setFillColor(self.wine_red)
        c.setFont("Helvetica-Bold", 18)
        c.drawString(panel_x, current_y, "Terroir & Winemaking")
        current_y -= 0.45*inch

        # Region
        c.setFillColor(self.wine_red)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(panel_x, current_y, "Region")

        c.setFillColor(self.dark_gray)
        c.setFont("Helvetica", 9)
        current_y = self.draw_text_block(c, "Kakheti, Eastern Georgia — sunlit valleys, mineral-rich soils, and centuries of winemaking wisdom.",
                                        panel_x, current_y - 0.2*inch,
                                        self.panel_width - self.margin * 2,
                                        font_size=9, leading=12)

        current_y -= 0.3*inch

        # Method
        c.setFillColor(self.wine_red)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(panel_x, current_y, "Method")

        c.setFillColor(self.dark_gray)
        c.setFont("Helvetica", 9)
        current_y = self.draw_text_block(c, "Blending ancient qvevri fermentation with contemporary cellar precision.",
                                        panel_x, current_y - 0.2*inch,
                                        self.panel_width - self.margin * 2,
                                        font_size=9, leading=12)

        current_y -= 0.3*inch

        # Philosophy
        c.setFillColor(self.wine_red)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(panel_x, current_y, "Philosophy")

        c.setFillColor(self.dark_gray)
        c.setFont("Helvetica", 9)
        current_y = self.draw_text_block(c, "Minimal intervention. Maximum expression. True Georgian soul.",
                                        panel_x, current_y - 0.2*inch,
                                        self.panel_width - self.margin * 2,
                                        font_size=9, leading=12)

        current_y -= 0.5*inch

        # Qvevri image
        qvevri_img = os.path.join(self.photos_dir, "qvevri-cellar.png")
        if os.path.exists(qvevri_img):
            self.add_image(c, qvevri_img, panel_x - 0.1*inch, current_y - 2.2*inch,
                          self.panel_width - self.margin*2 + 0.2*inch, 2*inch)

    def create_importers_panel(self, c, x_start):
        """Panel 5: For Importers (Back Center)"""
        panel_x = x_start + self.margin
        current_y = self.page_height - 0.7*inch

        # Header
        c.setFillColor(self.wine_red)
        c.setFont("Helvetica-Bold", 16)
        title = "For Importers &"
        c.drawString(panel_x, current_y, title)
        c.drawString(panel_x, current_y - 0.22*inch, "Distributors")
        current_y -= 0.6*inch

        # Packaging
        c.setFillColor(self.dark_gray)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(panel_x, current_y, "Available Packaging:")
        c.setFont("Helvetica", 9)
        c.drawString(panel_x, current_y - 0.15*inch, "750 ml bottles | Magnum on request")

        current_y -= 0.45*inch

        # MOQ
        c.setFont("Helvetica-Bold", 9)
        c.drawString(panel_x, current_y, "Minimum Order:")
        c.setFont("Helvetica", 9)
        c.drawString(panel_x, current_y - 0.15*inch, "300-600 bottles")
        c.setFont("Helvetica", 8)
        c.drawString(panel_x, current_y - 0.28*inch, "(distributor samples available)")

        current_y -= 0.55*inch

        # Markets
        c.setFont("Helvetica-Bold", 9)
        c.drawString(panel_x, current_y, "Current Markets:")
        c.setFont("Helvetica", 9)
        current_y = self.draw_text_block(c, "Georgia, Armenia, Russia, China, expanding to Central Asia & Middle East",
                                        panel_x, current_y - 0.15*inch,
                                        self.panel_width - self.margin * 2,
                                        font_size=9, leading=12)

        current_y -= 0.35*inch

        # Export support
        c.setFont("Helvetica-Bold", 9)
        c.drawString(panel_x, current_y, "Export Support:")

        support_items = [
            "• Point-of-sale materials",
            "• Tasting training",
            "• Digital assets",
            "• Limited launch events in market"
        ]

        c.setFont("Helvetica", 8)
        for item in support_items:
            current_y -= 0.15*inch
            c.drawString(panel_x + 0.1*inch, current_y, item)

        current_y -= 0.4*inch

        # CTA box
        c.setFillColor(self.wine_red)
        box_height = 0.5*inch
        c.rect(panel_x - 0.15*inch, current_y - box_height + 0.1*inch,
               self.panel_width - self.margin*2 + 0.3*inch, box_height, fill=True, stroke=False)

        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 11)
        cta = "Request samples"
        cta2 = "for your market"
        cta_width = c.stringWidth(cta, "Helvetica-Bold", 11)
        c.drawString(panel_x + (self.panel_width - self.margin*2 - cta_width) / 2, current_y - 0.2*inch, cta)
        cta_width2 = c.stringWidth(cta2, "Helvetica-Bold", 11)
        c.drawString(panel_x + (self.panel_width - self.margin*2 - cta_width2) / 2, current_y - 0.35*inch, cta2)

    def create_contact_panel(self, c, x_start):
        """Panel 6: Contact (Back Left/Cover)"""
        panel_x = x_start + self.margin
        current_y = self.page_height - 0.7*inch

        # Header
        c.setFillColor(self.wine_red)
        c.setFont("Helvetica-Bold", 20)
        c.drawString(panel_x, current_y, "Connect With Us")
        current_y -= 0.6*inch

        # Export inquiries
        c.setFillColor(self.wine_red)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(panel_x, current_y, "Export Inquiries:")

        c.setFillColor(self.dark_gray)
        c.setFont("Helvetica", 10)
        c.drawString(panel_x, current_y - 0.2*inch, "export@chateaualaverdi.ge")

        current_y -= 0.5*inch

        # Commercial contact
        c.setFillColor(self.wine_red)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(panel_x, current_y, "Commercial Contact:")

        c.setFillColor(self.dark_gray)
        c.setFont("Helvetica", 10)
        c.drawString(panel_x, current_y - 0.2*inch, "kristina@chateaualaverdi.ge")

        current_y -= 0.5*inch

        # Website
        c.setFillColor(self.wine_red)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(panel_x, current_y, "Website:")

        c.setFillColor(self.dark_gray)
        c.setFont("Helvetica", 10)
        c.drawString(panel_x, current_y - 0.2*inch, "www.chateaualaverdi.ge")

        current_y -= 0.6*inch

        # QR code placeholder
        c.setFillColor(self.beige)
        qr_size = 1.2 * inch
        c.rect(panel_x + 0.3*inch, current_y - qr_size - 0.1*inch, qr_size, qr_size, fill=True, stroke=True)

        c.setFillColor(self.light_gray)
        c.setFont("Helvetica", 8)
        qr_text = "[QR CODE]"
        qr_width = c.stringWidth(qr_text, "Helvetica", 8)
        c.drawString(panel_x + 0.3*inch + (qr_size - qr_width) / 2,
                    current_y - qr_size/2 - 0.1*inch, qr_text)

        current_y -= qr_size + 0.3*inch

        # Small heritage icon
        icon_img = os.path.join(self.photos_dir, "icon-grapes no bg.svg")
        if not os.path.exists(icon_img):
            icon_img = os.path.join(self.photos_dir, "icon-grapes.svg")

    def generate(self):
        """Generate the complete brochure PDF"""
        print(f"Creating brochure PDF: {self.output_file}")

        c = canvas.Canvas(self.output_file, pagesize=landscape(letter))

        # Add crop marks
        self.add_bleed_marks(c)

        # Create panels (tri-fold layout)
        # When flat: Panel 6 | Panel 5 | Panel 4 || Panel 3 | Panel 2 | Panel 1
        # Panel 1 (front cover) - rightmost
        self.create_front_cover(c, self.panel_width * 2)

        # Panel 2 (story) - center right
        self.create_story_panel(c, 0)

        # Panel 3 (wines) - center
        self.create_wines_panel(c, self.panel_width)

        # Panel 4 (terroir) - center left
        self.create_terroir_panel(c, self.panel_width * 2)

        c.showPage()

        # Back side (when folded over)
        self.add_bleed_marks(c)

        # Panel 5 (importers) - center
        self.create_importers_panel(c, self.panel_width)

        # Panel 6 (contact) - left
        self.create_contact_panel(c, 0)

        # Save PDF
        c.save()
        print(f"✅ Brochure created successfully: {self.output_file}")
        print(f"   Format: 11\" x 8.5\" landscape (tri-fold)")
        print(f"   Ready for printing!")

if __name__ == "__main__":
    brochure = ChateauAlaverdiBrochure("Chateau_Alaverdi_Professional_Brochure.pdf")
    brochure.generate()