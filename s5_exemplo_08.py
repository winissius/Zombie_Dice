print('Exemplo de aplicação 8: Elabore um programa que exemplifique a remoção de itens de um '
      'dicionário usando o método pop().')

agenda = {"Maria": "(41) 98765-4321", "João": "(11) 12345-6789"}
print(agenda.pop("Maria", "Contato com nome Maria localizado"))
print(agenda.pop("José", "Contato com nome José não localizado"))
print(agenda)