fread = open("P/aula01/teste.txt", "r") ## Abre e prepara-se para ler o ficheiro
content = fread.read()
print("O ficheiro contêm:",content)
fread.close()

fwrite = open("P/aula01/teste.txt", "w") ## Cria e prepara-se para escrever no ficheiro
write = input("O que quer escrever no ficheiro?")
print(write,file=fwrite)
fwrite.close()  ##Para fechar o ficheiro no computador