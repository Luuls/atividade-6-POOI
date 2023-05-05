# https://www.beecrowd.com.br/judge/pt/problems/view/1514

def noneSolvedAll(competitionResults) -> bool:
    for competitor in competitionResults:
        if sum(competitor) == m:
            return False

    return True

def allSolvedByAtLeastOne(competitionsResults) -> bool:
    for j in range(m):
        sumQuestions = 0
        for i in range(n):
            sumQuestions += competitionResults[i][j]

        if sumQuestions == 0:
            return False
        
    return True

while True:
    n, m = map(int, input().split())
    if n == 0:
        break

    competitionResults = [[int(x) for x in input().split()] for _ in range(n)]

    print(allSolvedByAtLeastOne(competitionResults))