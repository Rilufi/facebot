# facebot
## Instalações necessárias
### Instale o Python

Para instalar o Python 3:

No Linux, digite em um terminal:
$ sudo apt-get install python3

Em outros OS:
https://realpython.com/installing-python/

### Instale o pip

Para instalar o gerenciador de pacotes pip:

No Linux,  digite em um terminal:
$ sudo apt-get install python3-pip

Windows:
https://www.liquidweb.com/kb/install-pip-windows/

No Mac, ditie em um terminal:
$ sudo easy_install pip
$ sudo pip install --upgrade pip

### Instale o Selenium

Digite em um terminal
$ pip install selenium

### Edições

Com o facebot.py e o chromedriver.exe na mesma pasta, faça o seguinte:
  
1º Clique com o botão direito do mouse no chromedriver e em propriedades para checar sua localização (ou seja, a pasta onde você salvou)

2º Clique para editar o arquivo faceot.py, pode ser em qualquer bloco de notas ou editor de scripts que você preferir

3º Vá em "chrome_path" e no meio das aspas, apague o endereço caminho\até\chromedriver.exe e cole o endereço que copiou no 1º passo, ele irá ficar assim:
Exemplo: chrome_path = r"C:\Users\usuario\Desktop\pasta\chromedriver.exe"

4º Vá em "login" e "senha" e troque seu@email.com pelo seu email e sua_senha pela senha para efetuar o login no site

5º mude o https://www.facebook.com/post_que_quer_comentar pelo endereço do post onde vc quer que o bot comente, ele está pré-programado pra comentar os números de 1 até onde vc deixar ele rodar

### Executando

Após isso, é só salvar a edição e executar o faceot.py na sua linha de comando com 

$ python facebot.py 

;)

### Outras edições

Dentro da função comentar, vc vai ver um:
driver.find_element_by_xpath("""/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div/div/form/div/div/div[2]/div/div/div/div""").send_keys(comment_cont, Keys.RETURN)

Tudo que tem dentro de send_keys é o que ele vai comentar, você pode alterar isso, ele está automaticamente configurado para comentar números de 1 até onde você deixar e dar ENTER, você pode colocar o que quiser aí


Além disso, pra mudar onde você quer que ele clique e comente, é só encontrar outros xpaths pelo código html do site

## Solução de problemas
### Chromedriver

Caso o chromedriver dê erro, pode ser por conta da permissão da pasta onde ele está, uma solução possível é colocar o chromedriver.exe no PATH ou em alguma pasta onde o PATH já abra normalmente e apagar a variável chrome_path
Outra opção pode ser com a versão do chromedriver que não é compatível com sua versão do Chrome ou do PC, para isso baixe outra versão no site: https://chromedriver.chromium.org/downloads

### Selenium

Instalar o Selenium pode ser treta às vezes, então vou incluir a documentação original, caso o método que citei acima não funcione: https://www.selenium.dev/documentation/en/selenium_installation/installing_selenium_libraries/

### Sistema operacional

É pra funcionar em todos os OS, Windows e MAC podem dar alguns problemas de instalação, como na hora de instalar o pip pra instalar o Selenium, mas daí é só pesquisar "como instalar pip no Windows".

### Problemas a resolver

Se demora muito pra ter resposta do site, o bot fica bravo e fecha

### Agradecimentos

Bot inspirado no bot de @he4rt e @r3br34k
