# Creating an excel workbook with one worksheet
import xlsxwriter

workbook = xlsxwriter.Workbook('ScoreConversions.xlsx')
worksheet = workbook.add_worksheet('ExecutiveFunction')

#Create Domain labels with room to fill in or calculate data

worksheet.write(0, 0, "Domain:")
worksheet.write(0, 5, "Domain Average:")
worksheet.write(0, 6, "Standard Score:")
worksheet.write(0, 8, "Scaled Score:")
worksheet.write(0, 10, "T-score:")
worksheet.write(0, 12, "z-score:")

#Create  Divider

worksheet.write(1, 0, "Individual Tests:")

# Labels to add to the worksheet with 999 for temporary filler
labels = (
    ["Test Name", 999],
    ["Score Type", 999],
    ["Patient Raw Score", 999],
    ["Standardized Score", 999],
    ["Conversions:", 999],
    )

# Start in next row
row = 2
column = 0

#Fill in labels
for title, filler in (labels):
    worksheet.write(row, column, title)
    worksheet.write(row, column+1, filler)
    row += 1

workbook.close()
