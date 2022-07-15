from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Tamanho da folha A4 - 210mm x 297mm

# A unidade de medida padrão é 'pontos' e não milímetros. Por isso é criada a função abaixo para realizar a conversão para mm

def mm2p (milimetros):
    return milimetros / 0.352777

# Criar um arquivo em pdf e salvar ele
cnv = canvas.Canvas('meu_pdf.pdf', pagesize=A4)

# Inserir um texto
cnv.drawString(mm2p(195), mm2p(280), 'Teste')

# Desenhar uma linha
cnv.line(mm2p(1), mm2p(100), mm2p(100), mm2p(100))

# Desenhar um retângulo
cnv.rect(mm2p(50), mm2p(90), mm2p(100), mm2p(150))

# Inserir imagem
cnv.drawImage('imagem.jpg', 200, 250, width=50, height=50)


cnv.save()