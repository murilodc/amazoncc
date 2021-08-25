carrinho = []
carrinhovalor = []
cpfs = list()
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
        return print('Usuário cadastrado com sucesso')
def compras():
    print('Olá, atualmente temos os seguintes produtos em estoque.')
    for prod in range(len(produtos)): #For para mostrar todos os produtos na tela.
        print(f'{prod}.{produtos[prod]}-R$ {preco[prod]}') 
    print('Para adicionar ao carrinho basta apenas digitar o número do item.')
    limite = 1000
    while limite != 0:
        print(f'Você possui um limite de crédito de {limite}')
        opcao = input('Deseja continuar comprando?')
        opcao.lower() #Para que não haja erro na comparação, caso o usuário digite letras maiusculas.
        if opcao == 'sim':
            pass
        else:
            break
        comprando = int(input())
        comprando = comprando - 1 #diminuindo 1 da escolha do usuário para que se encaixe no range da lista.
        for i in range(len(produtos)):
            if comprando == i:
                limite = limite - preco[i]
                print(f'{produtos[i]} adicionado ao carrinho')
                carrinho.append(produtos[i])
                carrinhovalor.append(preco[i])
        
#PAREI NA PARTE DE COMECAR A FUNCAO DE MOSTRAR CARINHO

n = 0
while n != 5:
    cadastro()
    compras()
    n = int(input())