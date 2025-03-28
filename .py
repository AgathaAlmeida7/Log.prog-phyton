while True:
    try:
        # Entrada dos valores para a multiplicação
        valor01 = int(input('Digite o primeiro valor:\n'))
        valor02 = int(input('Digite o segundo valor:\n'))

        # Realizando a multiplicação
        multiplicacao = valor01 * valor02

        # Exibindo o resultado da multiplicação
        print(f'O resultado da multiplicação do primeiro valor: {valor01}, com o segundo valor: {valor02}, resultou em: {valor01} X {valor02} = {multiplicacao}')

        # Perguntar ao usuário se deseja continuar
        while True:
            opção = input('Você deseja continuar a saber outros resultados de multiplicação? [s/n]:\n').strip().lower()
            
            # Verificando a resposta do usuário
            if opção == 'sim' or opção == 's':
                print('Você só tem direito a saber mais um resultado:\n')
                # Solicitar novos números para a multiplicação
                try:
                    valor01nv = int(input('Digite um novo inteiro:\n'))
                    valor02nv = int(input('Digite mais outro número:\n'))

                    # Realizando a multiplicação do novo par de números
                    multiplicacao_nv = valor01nv * valor02nv
                    print(f'O resultado da multiplicação do primeiro valor: {valor01nv}, com o segundo valor: {valor02nv}, resultou em: {valor01nv} X {valor02nv} = {multiplicacao_nv}')
                    
                    break  # Após o cálculo extra, sai do loop de continuar
                except ValueError:
                    print('Os números inseridos devem ser do tipo inteiro. Por favor, tente novamente.')

            elif opção == 'não' or opção == 'nao' or opção == 'n':
                print('O programa será encerrado. Obrigado!')
                break  # Sai do loop principal e encerra o programa

            else:
                # Caso o usuário tenha digitado algo inesperado
                print('Resposta inválida. Por favor, responda com "sim" ou "não".')

        if opção == 'não' or opção == 'nao' or opção == 'n':
            break  # Encerra o loop principal se a resposta for "não"

    except ValueError:
        print('O número deve ser inteiro para você poder obter a resposta, por favor digite novamente.\n')


