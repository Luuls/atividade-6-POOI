# https://www.beecrowd.com.br/judge/pt/problems/view/1187

o = input()

matrix = [[None for _ in range(12)] for _ in range(12)]

for i in range(12):
    for j in range(12):
        matrix[i][j] = float(input())

sumNumbers = 0
for j in range(1, 12 // 2):
    for i in range(j):
        sumNumbers += matrix[i][j]
        sumNumbers += matrix[i][-j - 1]

if o == 'S':
    print(round(sumNumbers, 1))

else:
    numbersQuantity = 2 * ((1 + 5) * 5) / 2
    average = sumNumbers / numbersQuantity
    print(round(average, 1))