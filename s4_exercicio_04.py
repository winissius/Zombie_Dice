print('Exemplo de aplicação 4: Dada a lista de dados nums = [17, 33, 23, 11, 8, 15, 9], '
      'corra a lista e identifique o maior e o menor número.')

maior = 0
menor = 0
nums = [17, 33, 23, 11, 8, 15, 9]
for n in range(len(nums)):
    if n == 0:
        maior = menor = nums[n]
    else:
        if nums[n] > maior:
            maior = nums [n]
        if nums [n] < menor:
            menor = nums [n]
print(f'O maior é {maior} e o menor é {menor}')

print(''
      'outra solução'
      '')
maior = nums[0]
menor = nums[0]
for n in nums:
    if n > maior:
        maior = n
    if n < menor:
        menor = menor
print(f'O maior é {maior} e o menor é {menor}')
