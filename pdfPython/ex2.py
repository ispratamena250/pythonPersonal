#Exercício 2 - extrair texto
from pypdf import PdfReader

reader = PdfReader("/home/isaac/Documents/Livros/Matematica/ComplexVariablesAndapplications_6thEdition--Brown-Churchill.pdf")

page = reader.pages[0]
text = page.extract_text()

print(text)

if text and text.strip():
    print("PDF tem texto extratível")
else:
    print("PDF talvez seja escaneado")
