"""Main resume generator (template).

Single-page, ATS-friendly PDF resume built with fpdf2 (Helvetica core font).

How the resume-generate skill uses this file:
  1. Copy this template to output/<name>_resume.py
  2. Replace the CONTENT block (and OUTPUT_PATH) with data pulled from
     user-knowledge/ plus anything new the user provided.
  3. Run it: `python3 output/<name>_resume.py`
  4. Read the "Final Y" line it prints and trim/adjust until it reports FITS.

Hard rules:
  - ASCII only. No em dashes (use commas, colons, or rephrase), no smart quotes.
    The Helvetica core font cannot encode them and the review skill flags them as
    AI tells. Use " - " or ": " as separators.
  - Keep it to ONE page. The footer prints whether content fits.

Install deps once: `pip install -r requirements.txt`
"""

import os

from fpdf import FPDF

# ---------------------------------------------------------------------------
# Output location
# ---------------------------------------------------------------------------
OUTPUT_PATH = "output/resume.pdf"
PAGE_HEIGHT = 792  # Letter, in points
BOTTOM_SAFE_MARGIN = 30  # content should end before PAGE_HEIGHT - this


class ResumePDF(FPDF):
    def __init__(self):
        super().__init__("P", "pt", "Letter")
        self.set_auto_page_break(auto=False)
        # (left, top, right). Nudge top margin to vertically balance the page.
        self.set_margins(40, 36, 40)

    def section_divider(self, title):
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(17, 17, 17)
        self.cell(0, 13, title.upper(), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(170, 170, 170)
        self.line(
            self.l_margin,
            self.get_y() - 1.5,
            self.w - self.r_margin,
            self.get_y() - 1.5,
        )

    def job_header(self, title, company, date):
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(26, 26, 26)
        tw = self.get_string_width(title)
        self.cell(tw + 2, 11, title)
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(68, 68, 68)
        sep_w = self.get_string_width(" | ")
        self.cell(sep_w, 11, " | ")
        self.set_font("Helvetica", "I", 8.5)
        cw = self.get_string_width(company)
        self.cell(cw + 2, 11, company)
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(85, 85, 85)
        self.cell(0, 11, date, align="R", new_x="LMARGIN", new_y="NEXT")

    def role_description(self, text):
        self.set_font("Helvetica", "I", 8.5)
        self.set_text_color(51, 51, 51)
        self.multi_cell(0, 11, text, new_x="LMARGIN", new_y="NEXT")

    def client_label(self, text):
        self.set_font("Helvetica", "BI", 8)
        self.set_text_color(51, 51, 51)
        self.cell(0, 11, text, new_x="LMARGIN", new_y="NEXT")

    def bullet(self, text):
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(51, 51, 51)
        x = self.get_x()
        self.cell(8, 11, "-")
        self.set_x(x + 8)
        self.multi_cell(0, 11, text, new_x="LMARGIN", new_y="NEXT")

    def project_bullet(self, name, text):
        """Bold project name followed by an inline wrapped description."""
        self.set_text_color(51, 51, 51)
        x = self.get_x()
        self.set_font("Helvetica", "", 8.5)
        self.cell(8, 11, "-")
        self.set_x(x + 8)
        saved_margin = self.l_margin
        self.l_margin = x + 8
        self.set_font("Helvetica", "B", 8.5)
        self.write(11, f"{name}: ")
        self.set_font("Helvetica", "", 8.5)
        self.write(11, text)
        self.l_margin = saved_margin
        self.ln(11)

    def skill_row(self, items):
        """Render N skills as evenly spaced columns on one row."""
        col_w = (self.w - self.l_margin - self.r_margin) / len(items)
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(51, 51, 51)
        y = self.get_y()
        for i, item in enumerate(items):
            self.set_xy(self.l_margin + i * col_w, y)
            self.cell(col_w, 11, item)
        self.set_y(y + 11)


def build():
    pdf = ResumePDF()
    pdf.add_page()

    # =======================================================================
    # CONTENT - replace everything below with data from user-knowledge/.
    # Keep ASCII only. Keep to one page (see footer fit check).
    # =======================================================================

    # --- Header -----------------------------------------------------------
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(26, 26, 26)
    pdf.cell(0, 20, "FULL NAME", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(68, 68, 68)
    pdf.cell(0, 11, "Professional Title", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "", 7.5)
    pdf.set_text_color(85, 85, 85)
    pdf.cell(
        0,
        9,
        "(000) 000-0000 | email@example.com | linkedin.com/in/handle | site.com",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.ln(5)

    # --- Summary ----------------------------------------------------------
    pdf.section_divider("Summary")
    pdf.set_font("Helvetica", "", 8.5)
    pdf.set_text_color(51, 51, 51)
    pdf.multi_cell(
        0,
        11,
        (
            "Two to four sentence positioning statement. Lead with role identity and "
            "domain, then differentiators and proof of impact. Avoid filler adjectives "
            "and AI tells."
        ),
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.ln(5)

    # --- Skills (3 columns x N rows) --------------------------------------
    pdf.section_divider("Skills")
    pdf.skill_row(["Languages: A / B / C", "Domain skill / area", "Domain skill / area"])
    pdf.skill_row(["Frameworks: A / B / C", "Cloud: AWS / Azure / GCP", "Domain skill / area"])
    pdf.skill_row(["Datastores: A / B / C", "APIs: REST / GraphQL", "Practice / methodology"])
    pdf.skill_row(["Infra: Docker / K8s / CI-CD", "Domain skill / area", "Leadership / collaboration"])
    pdf.ln(5)

    # --- Experience -------------------------------------------------------
    pdf.section_divider("Experience")

    pdf.job_header("Job Title", "Company Name", "Mon YYYY - Present")
    pdf.role_description(
        "One or two italic lines of role context: scope, team, and headline scale."
    )
    pdf.bullet(
        "Accomplishment with action verb, what you did, and a measurable outcome."
    )
    pdf.bullet(
        "Second accomplishment. Prefer numbers (latency, revenue, scale, time saved)."
    )

    # Optional sub-engagements under one employer (e.g., consulting clients):
    # pdf.client_label("Client: Name (Mon YYYY - Mon YYYY)")
    # pdf.role_description("...")
    # pdf.bullet("...")

    pdf.job_header("Earlier Title", "Earlier Company", "Mon YYYY - Mon YYYY")
    pdf.role_description("Context line.")
    pdf.bullet("Accomplishment with measurable outcome.")
    pdf.ln(5)

    # --- Projects ---------------------------------------------------------
    pdf.section_divider("Projects")
    pdf.project_bullet(
        "Project Name",
        "What it does and the standout technical detail, then the stack. Tech A, Tech B.",
    )
    pdf.project_bullet(
        "Second Project",
        "One-line value plus differentiator. Tech A, Tech B.",
    )
    pdf.ln(5)

    # --- Education --------------------------------------------------------
    pdf.section_divider("Education")
    pdf.job_header("Degree", "Institution", "Mon YYYY - Mon YYYY")
    pdf.ln(5)

    # --- Certifications ---------------------------------------------------
    pdf.section_divider("Certifications")
    pdf.job_header("Certification Name", "Issuer", "Mon YYYY")

    # =======================================================================
    # END CONTENT
    # =======================================================================

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
