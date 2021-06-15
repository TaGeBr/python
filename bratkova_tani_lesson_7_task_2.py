import os
# # https://pythobyte.com/reading-and-writing-yaml-to-a-file-in-python-16071/
import yaml

print('по второму заданию я взяла пример из интернета, только вот смогла записать yaml файл, '
      'дальше не разбиралась, не хватило времени')

dict_file = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
{'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

with open('yaml_example.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)
