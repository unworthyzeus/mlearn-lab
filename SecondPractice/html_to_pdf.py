import pdfkit
options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}
pdfkit.from_file('SecondPracticeV2.html', 'SecondPracticeV2.pdf', options=options)
