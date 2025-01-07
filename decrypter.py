import os
import pyaes

# pasta com os arquivos a serem criptografados
folder_name = "/tmp/ransonware"

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

		## chave para descriptografia
		key = b"testeransomwares"
		aes = pyaes.AESModeOfOperationCTR(key)
		decrypt_data = aes.decrypt(file_data)

		## remover o arquivo criptografado
		os.remove(file_name)

		## criar o arquivo descriptografado
		new_file = file_name.split(".ransomwaretroll")[0] #remover a extencao ransonwaretroll
		new_file = open(f'{new_file}', "wb")
		new_file.write(decrypt_data)
		new_file.close()