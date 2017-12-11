tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose44']]
'''
apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
'''

def printTable(table):
    coldWidths = [0] * len(table)
    for i in range(len(table)):
        for j in range(len(table[i])):
            if coldWidths[i] < len(table[i][j]):
                coldWidths[i] = len(table[i][j])
    for i in range(len(table)):
        for j in range(len(table[i])):
            if j <= len(table[i]):
                print(table[j][i].rjust(coldWidths[j]+1), end='')
        print()
        
printTable(tableData)



