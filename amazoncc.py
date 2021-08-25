carrinho = []
execucao = 'sim'
carrinhovalor = []
cpfs = list()
opcao = 'sim'
chega = ''
limite = 1000
usuarios = list()
produtos = ['Controle naointendo', 'Xaina Bluemi note 10', 'Refrigerante de cola', 'Chocolate branco', 'Chocolate preto', 'Xícara espelhada', 'Fita led', 'Televisão LB - life is bad', 'Mouse heyzer', 'Travesseiro microfibra', 'Régua 30cm', 'Escova de dente', 'Cobertor', 'Geladeira frost free', 'Despertador', 'Arroz 1kg', 'Bolacha salgada', 'Feijão 1kg', 'Açucar 1kg', 'Achocolatado 500g']
preco = [199.00, 899.00, 2.99, 2.99, 1.99, 15.50, 20, 1200, 300, 15.99, 5.90, 13.90, 89.90, 859.90, 49.90, 5.50, 2.99, 4.99, 12.99, 6.50]
def cadastro():
    cpflist = []
    emailinvalido = 0
    email = input('Crie um email para o usuário \n')
    senha = input('Crie uma senha para o usuário com exatamente 6 digitos\n')
    nome = input('Informe o seu nome\n')
    cpf = input('Informe o seu cpf, somente números.\n')
    #Verificação de validação das entradas
    for letra in email:
        if letra == '@':
            pass
        else:
            emailinvalido+=1 #Variável utilizada como contador de caracteres que não são um @.
        if emailinvalido == len(email): #caso a variável tenha a mesma quantidade de digitos que a variável email, significa que o email não possui @
            return print('Email incorreto, é necessário que tenha um @.')
    if len(senha) != 6:
        return print('Senha inválida. Deve ser constituída de 6 digitos.')
    if nome.isalpha() == False: #A função isalpha() retorna true caso toda a string seja uma letra, caso contrário retorna falso.
        return print('Nome inválido. Apenas caracteres alfabéticos são permitidos')
    for numero in cpf:
        cpflist.append(int(numero))
    if len(cpf) < 11: #Verificação do CPF
        return print('CPF inválido, exatamente 11 números.')
    #Verificação se o primeiro dígito verificador está corretos, utiliziando o seguinte algoritmo de verificação http://www.macoratti.net/alg_cpf.htm
    digito1 = cpflist[0] * 10 + cpflist[1] * 9 + cpflist[2] * 8 + cpflist[3] * 7 + cpflist[4] * 6 + cpflist[5] * 5 + cpflist[6] * 4 + cpflist[7] * 3 + cpflist[8] * 2
    digito1 = digito1 % 11
    if digito1 < 2:
        if cpflist[9] == 0:
            pass
        else:
            return print('Dígito verificador está incorreto.')
    else:
        resto = 11 - digito1
        if cpflist[9] == resto:
            pass
        else:
            return print('Dígito verificador está incorreto')
    #Verificação do segundo dígito verificador.
    digito2 = cpflist[0] * 11 + cpflist[1] * 10 + cpflist[2] * 9 + cpflist[3] * 8 + cpflist[4] * 7 + cpflist[5] * 6 + cpflist[6] * 5 + cpflist[7] * 4 + cpflist[8] * 3 + cpflist[9] * 2
    digito2 = digito2 % 11
    if digito2 < 2:
        if cpflist[10] == 0:
            pass
        else:
            return print('Dígito verificador está incorreto.')
    elif digito2 >= 2:
        resto = 11 - digito2
        if cpflist[10] == resto:
            pass
        else:
            return print('Dígito verificador está incorreto')
    #Verificando se os dados já estão cadastrados.
    if cpf in cpfs:
        return print('CPF ja está cadastrado')
    elif nome in usuarios:
        return print('Usuário ja está cadastrado')
    else:
        cpfs.append(cpf)
        usuarios.append(nome)
        print('Usuário cadastrado com sucesso')
        usuarioComSucesso = True
        limite = 1000
    return email, cpf, usuarioComSucesso, limite
def compras(limite):
    comprandoboolean = False
    limiteover = False
    print('Olá, atualmente temos os seguintes produtos em estoque.')
    for prod in range(len(produtos)): #For para mostrar todos os produtos na tela.
        print(f'{prod}.{produtos[prod]}-R$ {preco[prod]}') 
    print('Para adicionar ao carrinho basta apenas digitar o número do item.')
    print('Caso queira para de comprar digite 0')
    while limite > 0:
        print(f'Você possui um limite de crédito de {limite}')
        comprando = int(input())
        if comprando == 0:
            break
        comprando = comprando - 1 #diminuindo 1 da escolha do usuário para que se encaixe no range da lista.
        try: #Caso o produto exista.
            produtos[comprando]
        except: #Se o produto não existir.
            print('Produto não existe')
            break
        if limite > preco[comprando]:
            limite = limite - preco[comprando]
            print(f'{produtos[comprando]} adicionado ao carrinho')
            carrinho.append(produtos[comprando])
            carrinhovalor.append(preco[comprando])
        else:
            print('Limite indisponivel.')
    for valoritem in carrinhovalor:
        gasto = valoritem
    return carrinho, carrinhovalor, gasto
def mostrarCarrinho(carrinho, carrinhovalor, gasto):
    print(f'O valor total do seu carrinho é {gasto}')
    escolha = input('Deseja ver os itens que estão no seu carrinho?')
    escolha.lower()#Para que não haja erro na comparação, caso o usuário digite letras maiusculas.
    if escolha == 'sim':
        for item in carrinho:
            print({item})
    return gasto
def pagamento(gasto, email, cpf):
    if gasto != 0:
        print(f'O valor do seu carrinho é {gasto}')
        pagar = input('Deseja realizar o pagamento agora?')
        pagar.lower() #Para que não haja erro na comparação, caso o usuário digite letras maiusculas.
    else:
        return print('Você não possui produtos em seu carrinho.')
    if pagar == 'sim':
        print(f'Um boleto no valor de {gasto} foi gerado no CPF {cpf} e enviado para o email {email} e seu limite foi liberado')

# !-=-=-=-=-=-=-=-=-=-=-=- Programa principal =-=-=-=-=-=-=-=-=-=-=-=-!

while execucao == 'sim':
    print('Seja muito bem vindo à minha loja HorizonCC, meu nome é Murilo e estou aqui para te ajudar.')
    print('1-Fazer o cadastro de um novo cliente.')
    print('2-Comprar nossos produtos')
    print('3-Ver o seu carrinho')
    print('4-Realizar o pagamento do seu carrinho')
    menu = input('Digite o numero correspondente a ação que deseja realizar.')
    if menu == '1':
        retornocadastro = cadastro() #execução da função e armazenamento do retorno.
    elif menu == '2':
         #Se o usuário possuir cadastro ativo ele chamará a função compras, caso contrário irá dar um aviso que não possui cadastro.
        retornocompras = compras(retornocadastro[3]) #execução da função e armazenamento do retorno.
    elif menu == '3':
        try: retornomostrarCarrinho = mostrarCarrinho(retornocompras[0], retornocompras[1], retornocompras[2]) #execução da função e armazenamento do retorno.
        #Se o usuário possuir carrinho ativo ele chamará a função mostrarCarrinho, caso contrário irá dar um aviso que não possui carrinho.
        except: 
            print('Você não possui um carrinho.')
    elif menu == '4':
            pagamento(retornocompras[2], retornocadastro[0], retornocadastro[1]) #Se o usuário possuir carrinho ativo ele chamará a função pagamento, caso contrário irá dar um aviso que não possui carrinho.

    execucao = input('Deseja realizar outra ação?')