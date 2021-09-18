# INF1407-2021.2
PUC-Rio - INF1407 - Programação para a Web - 2021.2
---
## Trabalho 1 - Servidor HTTP em Python3
## Membro do grupo: Felipe Holanda Bezerra - 1810238
### Como Configurar o protótipo

1. Em dirname, manter a variável __file__ (entre _underscores_), para que o Python3 encontre o diretório corrente do arquivo e evite cair em erro FileNotFound.

2. Em defaultport, digitar o número desejado para a porta que o servidor escutará, por default: 8080.

3. Prover uma string entre aspas duplas, começando e terminando com barras simples ("/[string]/"), com o nome (ou caminho) do arquivo desejado, nas seguintes variáveis:

- gifsdir
- htmldir
- imagesdir
- jsdir

4. Prover uma string entre aspas duplas ("[string]"), com o nome (ou caminho) do arquivo desejado, nas seguintes variáveis:

- default404
- index

5. Em defaultindex e defaulterror, manter as varíaveis como estão.

### O que Funcionou

1. "Implemente o método GET" - OK
2. "Permita a conexão de mais de um cliente simultaneamente. Como sugestão, inclua dentro do servidor 
um delay para testar conexões simultâneas (eu vou fazer isso para testar o seu trabalho)." - OK, mas não foi adicionado o delay nos testes
3. "O seu servidor deverá servir arquivos HTML, JS, JPEG (JPG), PNG e GIF." - OK
10 . "No caso de recurso inexistente (página não encontrada), exibir código de erro 404." - OK
4. "A porta que o seu servidor irá escutar. Uma sugestão para você realizar testes é usar a porta 80 ou 8080." - OK
5. "O diretório físico (local) que será utilizado para armazenar os arquivos publicados na Web." - OK
6. "Em caso de erro, qual página será exibida (normalmente quem configurar o seu trabalho irá exibir uma página com mensagem 404 – crie uma como exemplo)." - OK

### O que Não Funcionou

1. "Emita mensagens de erro ao tentar executar o seu trabalho e houver alguma inconsistência no arquivo de configuração (ver descrição de arquivo de configuração abaixo)." - _Não_ OK
2. "Uma lista de arquivos default, ou seja, se o pedido chegar sem nome de arquivo, o seu programa deverá procurar por arquivos nessa lista, na ordem, antes de enviar erro 404." - _Não_ OK. Funciona com apenas um arquivo, sem ser uma lista, no caso, o index.html