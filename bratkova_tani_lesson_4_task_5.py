# запускаем из консоли с параметрами
# python bratkova_tani_lesson_4_task_5.py usd eur
from bratkova_tani_lesson_4_task_3 import currency_rates
import sys

for idx in sys.argv[1:]:
    currency_rates(idx)
