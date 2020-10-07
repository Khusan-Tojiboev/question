# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
# ikta sana orasidagi kunlarni sonini chiqarish kerak
# uning uchun ikta datani olishimiz kerak. datani olmimiz, uning o'rniga o'zimiz beramiz ekan
# keyin ayirib qo'yish kerak.
# bundan o'rgangan narsam
# datetime bilan data ni bilish

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2017, 8, 11)
delta = l_date - f_date
print(delta.days)

# yangi yil
# from datetime import date
import datetime
today = datetime.date.today()
someday = datetime.date(2020, 12, 31)
diff = someday - today
print(diff.days)


from datetime import date
today = date.today()
someday = date(2020, 12, 31)
diff = someday - today
print(diff.days)
