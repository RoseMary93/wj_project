# 轉換pdf表格成df再儲存到csv。
import pdfplumber
import pandas as pd

pdf_file_path = 'file.pdf'
pdf = pdfplumber.open(pdf_file_path)

merged_df = pd.DataFrame() 

# 抓出每一頁的表格，合併到全部的df(merged_df)
for page in pdf.pages:
    table = page.extract_table()
    if table:
        df = pd.DataFrame(table[0:])
        # df.columns = ["column1", "column2"]  # 依據column數量
        merged_df = merged_df.append(df, ignore_index=True)

merged_df.to_csv('merged_table.csv', index=False, encoding='utf-8-sig')

pdf.close()