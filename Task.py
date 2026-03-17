import pandas as pd
from fpdf import FPDF

# Read data
data = pd.read_csv("student.csv")

# Analysis
average_marks = data['Marks'].mean()
highest = data['Marks'].max()
lowest = data['Marks'].min()

# Create PDF
pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=14)

# Title
pdf.cell(200, 10, txt="Student Marks Report", ln=True, align='C')

pdf.ln(10)

# Table Data
for index, row in data.iterrows():
    line = f"{row['Name']} : {row['Marks']}"
    pdf.cell(200, 10, txt=line, ln=True)

pdf.ln(10)

# Analysis Results
pdf.cell(200, 10, txt=f"Average Marks: {average_marks:.2f}", ln=True)
pdf.cell(200, 10, txt=f"Highest Marks: {highest}", ln=True)
pdf.cell(200, 10, txt=f"Lowest Marks: {lowest}", ln=True)

# Save PDF
pdf.output("report.pdf")

print("PDF Report Generated!")
