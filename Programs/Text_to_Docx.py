import docx

def text_to_docx(input_file, output_file):
    doc = docx.Document()
    
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            doc.add_paragraph(line.strip())

    doc.save(output_file)

# Replace 'input.txt' with the path of your input text file,
# and 'output.docx' with the desired name of the converted Word document.
input_file = 'C:\Dhanush\Documents\Datavalley\Python\Imports\Python Interview Questions & Answers(40).txt'
output_file = 'C:\Dhanush\Documents\Datavalley\Python\Exports\(40)Python Interview Questions & Answers.docx'

text_to_docx(input_file, output_file)
