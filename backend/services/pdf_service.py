import os
from typing import Dict, Any


class PDFService:
    def __init__(self):
        self.templates_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
        self.static_dir = os.path.join(os.path.dirname(__file__), '..', 'static')

    def generate_pdf(self, resume_data: Dict[str, Any]) -> bytes:
        from io import BytesIO
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas

        buffer = BytesIO()
        data = resume_data

        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        margin = 50
        y = height - margin

        # ---------------- HELPER FUNCTIONS ----------------

        def draw_line():
            nonlocal y
            c.line(margin, y, width - margin, y)
            y -= 20

        def add_text(text, size=10, indent=0):
            nonlocal y
            c.setFont("Helvetica", size)
            c.drawString(margin + indent, y, text)
            y -= size + 5

        # ---------------- HEADER ----------------

        c.setFont("Helvetica-Bold", 16)
        name = data.get("header", {}).get("name", "")
        c.drawString(margin, y, name)
        y -= 25

        # ---------------- CONTACT ----------------

        contact = data.get("header", {}).get("contact", {})

        add_text(f"Phone: {contact.get('phone', '')}")
        add_text(f"Email: {contact.get('email', '')}")
        add_text(f"LinkedIn: {contact.get('linkedin', '')}")

        draw_line()

        # ---------------- SUMMARY ----------------

        add_text("Summary", 12)
        add_text(data.get("summary", ""))

        draw_line()

        # ---------------- EDUCATION ----------------

        add_text("Education", 12)

        for edu in data.get("education", []):
            add_text(f"{edu.get('degree', '')} - {edu.get('university', '')}")
            add_text(f"GPA: {edu.get('gpa', '')}")

        draw_line()

        # ---------------- SKILLS ----------------

        add_text("Skills", 12)

        skills = data.get("skills", [])

        if isinstance(skills, list):
            add_text(", ".join(skills))
        elif isinstance(skills, dict):
            for category, skill_list in skills.items():
                add_text(f"{category}: {', '.join(skill_list)}")

        draw_line()

        # ---------------- EXPERIENCE ----------------

        add_text("Experience", 12)

        for exp in data.get("experience", []):
            add_text(f"{exp.get('title', '')} - {exp.get('company', '')}")
            add_text(exp.get('duration', ''))

            for resp in exp.get("responsibilities", []):
                add_text(f"- {resp}", indent=10)

        draw_line()

        # ---------------- PROJECTS ----------------

        add_text("Projects", 12)

        for proj in data.get("projects", []):
            add_text(proj.get("name", ""))
            add_text(proj.get("description", ""), indent=10)

        # ---------------- FINAL ----------------

        c.save()
        buffer.seek(0)

        return buffer.read()
