import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
import os

class PDFReverserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF 頁數反轉工具")
        self.root.geometry("400x250")
        self.files = []
        self.output_folder = os.getcwd()

        # 標題
        tk.Label(root, text="📄 拖曳或選擇 PDF 檔案", font=("Arial", 14)).pack(pady=10)

        # 選擇檔案按鈕
        tk.Button(root, text="選擇 PDF 檔案", command=self.select_files).pack(pady=5)

        # 選擇輸出資料夾
        tk.Button(root, text="選擇輸出資料夾", command=self.select_output_folder).pack(pady=5)

        # 執行按鈕
        tk.Button(root, text="開始反轉", command=self.reverse_all_pdfs, bg="#4CAF50", fg="white").pack(pady=15)

        # 顯示輸出資料夾路徑
        self.output_label = tk.Label(root, text=f"輸出位置：{self.output_folder}", wraplength=350)
        self.output_label.pack(pady=5)

    def select_files(self):
        self.files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        if self.files:
            messagebox.showinfo("已選取檔案", f"共選取 {len(self.files)} 個 PDF 檔案")

    def select_output_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder = folder
            self.output_label.config(text=f"輸出位置：{self.output_folder}")

    def reverse_all_pdfs(self):
        if not self.files:
            messagebox.showwarning("警告", "請先選擇 PDF 檔案")
            return

        for file_path in self.files:
            try:
                reader = PdfReader(file_path)
                writer = PdfWriter()
                for page in reversed(reader.pages):
                    writer.add_page(page)

                filename = os.path.splitext(os.path.basename(file_path))[0] + "_reversed.pdf"
                output_path = os.path.join(self.output_folder, filename)

                with open(output_path, "wb") as f:
                    writer.write(f)

            except Exception as e:
                messagebox.showerror("錯誤", f"{file_path} 處理失敗：\n{str(e)}")
                return

        messagebox.showinfo("完成", f"成功反轉 {len(self.files)} 個 PDF 檔案！")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFReverserApp(root)
    root.mainloop()