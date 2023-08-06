import docx

def is_question(paragraph):
    # Customize this function to identify questions based on specific criteria.
    return paragraph.text.endswith('?')

def change_questions_format(input_file, output_file, font_family, font_size):
    doc = docx.Document(input_file)

    # Convert the first line to title size
    if doc.paragraphs:
        first_paragraph = doc.paragraphs[0]
        for run in first_paragraph.runs:
            run.font.size = docx.shared.Pt(font_size * 2)
            run.bold = True
            run.font.color.rgb = docx.shared.RGBColor(*font_color)

    
    for paragraph in doc.paragraphs:
        if is_question(paragraph):
            for run in paragraph.runs:
                run.bold = True
                run.font.name = font_family
                run.font.size = docx.shared.Pt(font_size)

    doc.save(output_file)

# Replace 'input.docx' with the path of your input Word document,
# and 'output.docx' with the desired name of the modified output document.
input_file = 'C:\Dhanush\Documents\Datavalley\Python\Imports\(40)Python Interview Questions & Answers.docx'
output_file = 'C:\Dhanush\Documents\Datavalley\Python\Exports\(40)Python Interview Questions & Answers.docx'
font_family = 'Libre Baskerville'  # Customize the font family as desired
font_size = 12        # Customize the font size as desired
font_color = (65, 105, 225)

change_questions_format(input_file, output_file, font_family, font_size)
