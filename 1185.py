# https://www.beecrowd.com.br/judge/pt/problems/view/1185

matrix = [[None for _ in range(13)] for _ in range(12)]

o = input()

for i in range(12):
    for j in range(12):
        matrix[i][j] = float(input())

sumNumbers = 0
for i in range(11):
    for j in range(11 - i):
        sumNumbers += matrix[i][j]

if o == 'S':
    print(round(sumNumbers, 1))

else:
    numbersQuantity = (11 * 12) / 2
    average = sumNumbers / numbersQuantity
    print(round(average, 1))