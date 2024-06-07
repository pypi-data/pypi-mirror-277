import img2pdf
import os
import subprocess
import markdown2


def image_to_pdf(image_path, pdf_path):
    with open(image_path, 'rb') as img_file:
        pdf_bytes = img2pdf.convert(img_file)
        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(pdf_bytes)
    print(f"Converted {image_path} to PDF: {pdf_path}")


def pdf_to_markdown(pdf_path, output_dir, batch_multiplier=2, max_pages=10, languages='English,Arabic'):
    try:
        subprocess.run([
            'marker_single',
            pdf_path,
            output_dir,
            '--batch_multiplier', str(batch_multiplier),
            '--max_pages', str(max_pages),
            '--langs', languages,
        ], check=True)
        print(f"Converted {pdf_path} to Markdown")
    except subprocess.CalledProcessError as e:
        print(f"Error during Marker conversion: {e}")


def markdown_to_text(markdown_path, text_path):
    try:
        with open(markdown_path, 'r', encoding='utf-8') as md_file:
            markdown_content = md_file.read()
        text_content = markdown2.markdown(markdown_content)
        with open(text_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text_content)
        print(f"Converted {markdown_path} to Text: {text_path}")
    except Exception as e:
        print(f"Error converting markdown to text: {e}")


def convert_image_to_text(image_path, output_dir):
    pdf_path = os.path.join(output_dir, 'output.pdf')
    markdown_path = os.path.join(output_dir, 'output/output.md')
    text_path = os.path.join(output_dir, 'output.txt')

    image_to_pdf(image_path, pdf_path)
    pdf_to_markdown(pdf_path, output_dir)
    markdown_to_text(markdown_path, text_path)

    print("Process completed.")
