"""Cover letter generator (template).

Single-page PDF cover letter styled to match the resume generators (Helvetica core
font, same letterhead treatment).

How the cover-letter skill uses this file:
  1. Copy this template to output/<name>_cover_letter.py
  2. Replace the CONTENT block (NAME, CONTACT, ROLE, COMPANY, GREETING,
     PARAGRAPHS, CLOSING) and OUTPUT_PATH from user-knowledge/ + the job.
  3. Run it: `python3 output/<name>_cover_letter.py`
  4. Confirm it prints FITS (one page).

For a plain-text cover letter (e.g. pasting into a textarea), the skill can skip
this generator entirely and just write the prose. This file is the PDF path.

Hard rules: ASCII only (no em dashes / smart quotes), one page.
Install deps once: `pip install -r requirements.txt`
"""

import os
from datetime import date

from fpdf import FPDF

# ---------------------------------------------------------------------------
# CONTENT - replace per role.
# ---------------------------------------------------------------------------
NAME = "Full Name"
CONTACT = "(000) 000-0000 | email@example.com | linkedin.com/in/handle | site.com"

ROLE = "Target Role Title"
COMPANY = "Company Name"
GREETING = "Dear Company Hiring Team,"

PARAGRAPHS = [
    (
        "Opening hook tied to the team's mission or charter, and why this specific "
        "role caught your attention. Keep it concrete, not generic."
    ),
    (
        "Strongest proof paragraph: the experience or project that maps most directly "
        "to the role, with a measurable outcome."
    ),
    (
        "Second proof or differentiator. Mirror the job's language only where it is "
        "genuinely true. Be candid about any honest framing of fit."
    ),
    (
        "Close: how you work, why this company specifically, and a brief thank-you "
        "with an invitation to talk."
    ),
]

CLOSING = "Best regards,"

OUTPUT_PATH = "output/cover_letter.pdf"
PAGE_HEIGHT = 792
BOTTOM_SAFE_MARGIN = 30


class CoverLetterPDF(FPDF):
    def __init__(self):
        super().__init__("P", "pt", "Letter")
        self.set_auto_page_break(auto=False)
        self.set_margins(40, 36, 40)

    def header_block(self):
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(26, 26, 26)
        self.cell(0, 20, NAME, new_x="LMARGIN", new_y="NEXT")

        self.set_font("Helvetica", "", 7.5)
        self.set_text_color(85, 85, 85)
        self.cell(0, 9, CONTACT, new_x="LMARGIN", new_y="NEXT")

        self.ln(6)
        self.set_draw_color(170, 170, 170)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(12)

    def meta_block(self):
        today = date.today()
        date_str = f"{today:%B} {today.day}, {today.year}"
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(51, 51, 51)
        self.cell(0, 14, date_str, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

        self.set_font("Helvetica", "B", 9.5)
        self.set_text_color(26, 26, 26)
        self.cell(0, 14, f"Re: {ROLE} at {COMPANY}", new_x="LMARGIN", new_y="NEXT")
        self.ln(8)

    def body_block(self):
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(51, 51, 51)
        self.cell(0, 14, GREETING, new_x="LMARGIN", new_y="NEXT")
        self.ln(8)

        for para in PARAGRAPHS:
            self.multi_cell(0, 13.5, para, new_x="LMARGIN", new_y="NEXT", align="J")
            self.ln(8)

    def closing_block(self):
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(51, 51, 51)
        self.cell(0, 14, CLOSING, new_x="LMARGIN", new_y="NEXT")
        self.ln(4)
        self.set_font("Helvetica", "B", 9.5)
        self.set_text_color(26, 26, 26)
        self.cell(0, 14, NAME, new_x="LMARGIN", new_y="NEXT")


def build():
    pdf = CoverLetterPDF()
    pdf.add_page()
    pdf.header_block()
    pdf.meta_block()
    pdf.body_block()
    pdf.closing_block()

    y_final = pdf.get_y()
    fits = "FITS" if y_final < PAGE_HEIGHT - BOTTOM_SAFE_MARGIN else "OVERFLOW"
    print(f"Final Y: {y_final:.0f} / {PAGE_HEIGHT} ({fits})")
    print(f"Pages: {pdf.page_no()}")
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    pdf.output(OUTPUT_PATH)
    print(f"PDF generated: {OUTPUT_PATH}")


if __name__ == "__main__":
    build()
