
import docx

def is_question(paragraph):
    # Customize this function to identify questions based on specific criteria.
    return paragraph.text.endswith('?')

def change_questions_format(input_file, output_file, font_family, font_size):
    doc = docx.Document(input_file)

    for paragraph in doc.paragraphs:
        if is_question(paragraph):
            for run in paragraph.runs:
                run.bold = True
                run.font.name = font_family
                run.font.size = docx.shared.Pt(font_size)

    doc.save(output_file)

# Replace 'input.docx' with the path of your input Word document,
# and 'output.docx' with the desired name of the modified output document.
input_file = 'C:\Dhanush\Documents\Datavalley\Python\Imports\Edureka Basic Python Interview Questions for Freshers.docx'
output_file = 'C:\Dhanush\Documents\Datavalley\Python\Imports\Python Q&A FORMATTED.docx'
font_family = 'Libre Baskerville'  # Customize the font family as desired
font_size = 12        # Customize the font size as desired

change_questions_format(input_file, output_file, font_family, font_size)

