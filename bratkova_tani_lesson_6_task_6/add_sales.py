# Примеры запуска скрипта:
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7

# add_sale.py
import sys

price = sys.argv[1]

with open('bakery.txt', 'a', encoding='utf-8') as f:
    f.write(price + '\n')
