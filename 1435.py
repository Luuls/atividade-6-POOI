# https://www.beecrowd.com.br/judge/pt/problems/view/1435

while (n := int(input())) != 0:
    if n == 1:
        print('  1\n')
        continue

    matrix = [[None for _ in range(n)] for _ in range(n)]
    for layer in range(n // 2 + 1):
        for i in range(layer, layer + n - 2 * layer):
            matrix[layer][i] = layer + 1
            matrix[-layer - 1][i] = layer + 1

            matrix[i][layer] = layer + 1
            matrix[i][-layer - 1] = layer + 1

    for i in range(n):
        print('  ', end='')
        for j in range(n - 1):
            print(f'{matrix[i][j]:<4}', end='')

        print(matrix[i][-1])

    print()