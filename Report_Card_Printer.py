from fpdf import FPDF

# -------------------- STUDENT PROFILE --------------------

STUDENT_NAME = "Alice"
STUDENT_CLASS = "7th A"
ROLL_NO = 12

# -------------------- SUBJECT MARKS --------------------

Maths = 85
Science = 78
English = 76
Social_Science = 45
Hindi = 34


# -------------------- DISPLAY REPORT CARD --------------------

def display_report():
    print("--------------------")
    print("   STUDENT REPORT CARD")
    print("--------------------")
    print(f"Student Name      : {STUDENT_NAME}")
    print(f"Class             : {STUDENT_CLASS}")
    print(f"Roll No           : {ROLL_NO}\n")

    print("Subject           Marks")
    print("------------------------")
    print("Maths             ", Maths)
    print("Science           ", Science)
    print("English           ", English)
    print("Social Science    ", Social_Science)
    print("Hindi             ", Hindi)
    print()


def calculate_result():
    total = Maths + Science + English + Social_Science + Hindi
    percentage = total / 500 * 100

    if percentage >= 90:
        grade = "A Pass"
        remark = "Keep it up"
    elif percentage >= 70:
        grade = "B Pass"
        remark = "Improvement in progress"
    elif percentage >= 40:
        grade = "C Pass"
        remark = "Work on yourself"
    else:
        grade = "Fail"
        remark = "Bring your parents to staffroom"

    print("Total             ", total)
    print(f"Percentage        {percentage:.2f}%")
    print("Grade             ", grade)
    print("Teacher Remark    ", remark)

    return total, percentage, grade, remark


# -------------------- PDF GENERATION --------------------

def download_pdf():
    total, percentage, grade, remark = calculate_result()

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "STUDENT REPORT CARD", ln=True, align="C")
    pdf.ln(5)

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 8, f"Student Name : {STUDENT_NAME}", ln=True)
    pdf.cell(0, 8, f"Class        : {STUDENT_CLASS}", ln=True)
    pdf.cell(0, 8, f"Roll No      : {ROLL_NO}", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(100, 8, "Subject", border=1)
    pdf.cell(40, 8, "Marks", border=1, ln=True)

    pdf.set_font("Arial", size=12)
    subjects = {
        "Maths": Maths,
        "Science": Science,
        "English": English,
        "Social Science": Social_Science,
        "Hindi": Hindi
    }

    for subject, mark in subjects.items():
        pdf.cell(100, 8, subject, border=1)
        pdf.cell(40, 8, str(mark), border=1, ln=True)

    pdf.ln(5)
    pdf.cell(0, 8, f"Total      : {total}", ln=True)
    pdf.cell(0, 8, f"Percentage : {percentage:.2f}%", ln=True)
    pdf.cell(0, 8, f"Grade      : {grade}", ln=True)
    pdf.ln(5)
    pdf.multi_cell(0, 8, f"Teacher Remark:\n{remark}")

    pdf.output("Alice_ReportCard.pdf")
    print("\n✅ PDF downloaded successfully!")


# -------------------- MAIN MENU --------------------


print("\n1. View Report Card")
print("2. Download Report Card as PDF")

choice = int(input("Enter your choice: "))

if choice == 1:
    display_report()
    calculate_result()
if choice == 2:
    download_pdf()
