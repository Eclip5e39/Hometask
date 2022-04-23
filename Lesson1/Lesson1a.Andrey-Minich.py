# 1) Создать 3 переменных с одинаковыми данными с одинаковыми идентификаторами.
QA = ('Junior', 'Middle', 'Senior')
print(QA)
print(id(QA))
QA1 = QA
print(QA1)
print(id(QA1))
QA2 = QA
print(QA2)
print(id(QA2))
# 2) Создать 2 перменных с одинаковыми данными с разными идентификаторами.
QA3 = ['Junior', 'Middle', 'Senior']
print(QA3)
print(id(QA3))
QA4 = ['Junior', 'Middle', 'Senior']
print(QA4)
print(id(QA4))

# 3) Поменять их типы так, чтобы у 1х трех были разные идентификаторы,а у 2х последних были одинаковые.
# a)
print(QA)
print(id(QA))
QA1 = list(QA1)
print(QA1)
print(id(QA1))
QA2 = set(QA2)
print(QA2)
print(id(QA2))
# b)
QA3 = tuple(QA3)
print(QA3)
print(id(QA3))
QA4 = tuple(QA3)
print(QA4)
print(id(QA4))
