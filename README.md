# Entendendo um Ransomware na Prática com Python

## Estrutura do Projeto

* Será composto de dois arquivos python:
	* encrypter.py: Irá criptografar os arquivos
	* decrypter.py: Irá descriptografas os arquivos

## Instalando os pacotes necessários

* Abra o terminal do linux:
	* Execute o comando: ``` python -m pip install pyaes ```

## Criando os arquivos

* Em sua máquina crie ou copie os dois arquivos:
	* encrypter.py
	* decrypter.py

## Bonus

* Foi adicionado no codigo a criação de uma pasta no diretorio "/tmp/ransonware" caso deseje basta alterar o caminho para um de sua preferência;
* Criação de 10 arquivos para serem criptografados dentro da pasta criada;
* Uma função para percorrer todos os arquivos da pasta e criptografa-los;
* Realizado o mesmo processo para o script decrypter.py onde ele vai descriptografar todos os arquivos da pasta definida;