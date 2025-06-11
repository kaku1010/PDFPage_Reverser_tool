from PyPDF2 import PdfReader, PdfWriter

# 輸入與輸出檔案路徑
input_pdf = "未命名的筆記本.pdf"       # 原始 PDF 檔名
output_pdf = "reversed.pdf"   # 反轉後的檔名

# 讀取原始 PDF
reader = PdfReader(input_pdf)
writer = PdfWriter()

# 反向添加頁面
for page in reversed(reader.pages):
    writer.add_page(page)

# 寫入新的 PDF
with open(output_pdf, "wb") as f:
    writer.write(f)

print("已成功翻轉，並存為reversed.pdf")
