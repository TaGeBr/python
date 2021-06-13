with open('nginx_logs.txt', 'r') as f:
    list_out = []
    for line in f:
        result = line.split()
        list_out.append((result[0], result[5].replace('"',''), result[6]))
print(list_out)
#print(*list_out, sep=',\n')

print(f'\nЗдесь я вывела только первые три элемента списка, т.к. список огромный и в консоли не видно начала:\n'
      f'{list_out[0:3]}', type(list_out))
