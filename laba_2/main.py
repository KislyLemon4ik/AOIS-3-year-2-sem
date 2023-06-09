from SDNF import *
from SKNF import *
from subscript import *

# !((!x2+!x3)*!(!x1*!x3))


form = input('-->')

print('форм-ла: {}'.format(form))

print('сднф --> ', SDNF(form))

print('сднф в бинорном виде -->', SDNF_form_number(form)[0])

print('сднф в числовой форме -->', SDNF_form_number(form)[1])

print('скнф --> ', SKNF(form))

print('скнф в бинорном виде -->', SKNF_form_number(form)[0])

print('скнф в числовой форме -->', SKNF_form_number(form)[1])

print('индекс = ', subscript(form))

print('таблица :\n', create_logic_table(form)[0])