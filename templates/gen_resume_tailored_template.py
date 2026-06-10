"""Tailored resume generator (template).

Same layout engine as gen_resume_template.py, but the CONTENT block is meant to
be rewritten per job description by the resume-tailor skill. It adds a richer,
multi-bullet "highlight project" block for showcasing the single most relevant
project in depth.

Tailoring principles (enforced by the resume-tailor skill):
  - Mirror the job description's exact terminology in skills and bullets, but
    ONLY for things the candidate genuinely has. Never invent skills.
  - Reorder skills and bullets so the most relevant items come first.
  - Tune the subtitle and summary toward the target role.
  - Drop the least relevant content to make room and keep one page.

Hard rules: ASCII only (no em dashes / smart quotes), one page (see fit check).
Install deps once: `pip install -r requirements.txt`
"""

import os

from fpdf import FPDF

OUTPUT_PATH = "output/resume_tailored.pdf"
PAGE_HEIGHT = 792
BOTTOM_SAFE_MARGIN = 30


class ResumePDF(FPDF):
    def __init__(self):
        super().__init__("P", "pt", "Letter")
        self.set_auto_page_break(auto=False)
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

    def project_inline(self, name, text):
        """Bold name then inline description on the same flowing block."""
        self.set_text_color(51, 51, 51)
        self.set_font("Helvetica", "B", 8.5)
        self.write(11, f"{name}: ")
        self.set_font("Helvetica", "", 8.5)
        self.write(11, text)
        self.ln(11)

    def project_header(self, title, tech):
        """Bold project title with an italic tech-stack line beneath it."""
        self.set_font("Helvetica", "B", 8.5)
        self.set_text_color(26, 26, 26)
        self.cell(0, 11, title, new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "I", 8.5)
        self.set_text_color(68, 68, 68)
        self.cell(0, 11, tech, new_x="LMARGIN", new_y="NEXT")

    def skill_row(self, items):
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
    # CONTENT - rewrite per job description (resume-tailor skill).
    # =======================================================================

    # --- Header (subtitle tuned to the target role) -----------------------
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(26, 26, 26)
    pdf.cell(0, 20, "FULL NAME", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(68, 68, 68)
    pdf.cell(0, 11, "Role-Aligned Title", new_x="LMARGIN", new_y="NEXT")

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

    # --- Summary (oriented toward the JD) ---------------------------------
    pdf.section_divider("Summary")
    pdf.set_font("Helvetica", "", 8.5)
    pdf.set_text_color(51, 51, 51)
    pdf.multi_cell(
        0,
        11,
        (
            "Positioning statement rewritten to lead with the role's core need and the "
            "candidate's strongest matching evidence. Keep it honest and concrete."
        ),
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.ln(5)

    # --- Skills (reordered; mirror JD terms the candidate truly has) -------
    pdf.section_divider("Skills")
    pdf.skill_row(["Most-relevant skill", "JD keyword skill", "JD keyword skill"])
    pdf.skill_row(["Core language(s)", "JD keyword skill", "JD keyword skill"])
    pdf.skill_row(["Frameworks", "Cloud / infra", "JD keyword skill"])
    pdf.skill_row(["Datastores", "APIs", "Leadership / collaboration"])
    pdf.ln(5)

    # --- Experience -------------------------------------------------------
    pdf.section_divider("Experience")
    pdf.job_header("Job Title", "Company Name", "Mon YYYY - Present")
    pdf.role_description("Context line, framed toward the target role.")
    pdf.bullet("Most JD-relevant accomplishment first, with a measurable outcome.")
    pdf.bullet("Second accomplishment mirroring JD language where genuinely true.")
    pdf.ln(5)

    # --- Highlight project (deep, multi-bullet) ---------------------------
    pdf.section_divider("Projects")
    pdf.project_header(
        "Flagship Project: One-line value proposition",
        "Tech A, Tech B, Tech C, Tech D",
    )
    pdf.bullet("Bullet 1: the architecture / what you built and why it is hard.")
    pdf.bullet("Bullet 2: the part most relevant to this JD, in the JD's terms.")
    pdf.bullet("Bullet 3: measurement / evaluation / reliability angle.")
    pdf.bullet("Bullet 4: outcome, scale, or safeguards.")
    pdf.ln(4)

    # Secondary project(s) as compact one-liners:
    pdf.project_inline(
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
