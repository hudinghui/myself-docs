from PyPDF4 import PdfReader, PdfWriter
 
def encrypt_pdf(input_pdf_path, output_pdf_path, user_password, owner_password):
    # 打开PDF文件
    with open(input_pdf_path, 'rb') as file:
        reader = PyPDF4.PdfReader(file)
        writer = PyPDF4.PdfWriter()
        writer._set_outlines(reader.outlines)  # 复制书签（如果需要）
        writer._set_page_layout(reader.page_layout)  # 设置页面布局（如果需要）
        writer._set_page_mode(reader.page_mode)  # 设置页面模式（如果需要）
        writer._set_transition(reader.transition)  # 设置过渡效果（如果需要）
        writer._set_doc_info(reader.docinfo)  # 复制文档信息（如果需要）
        writer._set_encryption(userPassword=user_password, ownerPassword=owner_password, encryption=PyPDF4.utils.encryption.Encryption.ENC_AES_)
        
        # 复制原始PDF的所有页面并加密它们
        for page in reader.pages:
            writer.add_page(page)
        
        # 写入加密后的PDF到新文件
        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)
 
# 使用示例与上面相同，只需替换库的导入和函数调用即可。
 
encrypt_pdf("/Users/edy/Downloads/个人参保证明.pdf", "/Users/edy/Downloads/个人参保证明1.pdf", "user_pass", "owner_pass")