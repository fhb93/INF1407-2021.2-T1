from os import path


# manter a variável __file__, para que o Python3 encontre o diretório corrente do arquivo e evite cair em erro FileNotFound.
dirname = path.dirname(__file__)

#  digitar o número desejado para a porta que o servidor escutará, por default: 8080
defaultport = 8080 

# Prover uma string entre aspas duplas, começando e terminando com barras simples ("/<string>/"), com o nome (ou caminho) do arquivo desejado
gifsdir = "/gif/"

# Prover uma string entre aspas duplas, começando e terminando com barras simples ("/<string>/"), com o nome (ou caminho) do arquivo desejado
htmldir = "/html/"

# Prover uma string entre aspas duplas, começando e terminando com barras simples ("/<string>/"), com o nome (ou caminho) do arquivo desejado
imagesdir = "/img/"

# Prover uma string entre aspas duplas, começando e terminando com barras simples ("/<string>/"), com o nome (ou caminho) do arquivo desejado
jsdir = "/js/"

# Prover uma string entre aspas duplas ("<string>"), com o nome (ou caminho) do arquivo desejado
default404 = "404.html"

# Prover uma string entre aspas duplas ("<string>"), com o nome (ou caminho) do arquivo desejado
index = "index.html"

# Manter como está
defaultindex = htmldir + index

# Manter como está
defaulterror = htmldir + default404