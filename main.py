def exportTxtProducts(products):
    with open("CADTXT.txt", "w") as file:
        for product in products:
            product_line = f"{product['code']:06d}{product['type']}{product['description'][:22].ljust(22)}{product['price']:07}000"
            file.write(product_line + '\n')


def main():
    products = []

    while True:
        codigo = int(input('Digite o codigo do produto:'))
        tipo = input('Digite o tipo do produto, sendo ele apenas P(preço) e U (unidade):')

        if tipo not in ['P', 'U']:
            print('O Tipo de Produto inserido é invalido.')
            break

        descricao = input('Digite a descrição do produto:')
        preco = float(input('Digite o preço do produto:'))

        product = {
            'code': codigo,
            'type': tipo,
            'description': descricao,
            'price': int(preco * 100)
        }

        products.append(product)

        proceed = input("Você deseja continuar adicionando produtos? S or N: ").upper()
        if proceed != 'S':
            break
    exportTxtProducts(products)

    print('Seus produtos foram adicionados e exportados. E foi criado um arquivo CADTXT.txt com eles.')


main()
