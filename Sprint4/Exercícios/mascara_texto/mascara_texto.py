import hashlib

texto = input("Entre com texto a mascarar (tecle 0 para sair): ")

while len(texto) > 0:
    texto_mascarado = hashlib.sha1(texto.encode("utf-8"))
    print(texto_mascarado.hexdigest())
    texto = input("Entre com texto a mascarar ([ENTER] para sair): ")


