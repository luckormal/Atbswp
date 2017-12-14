tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
'''
apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
'''
import copy

def printTable(table):
    coldWidths = [0] * len(table)
    tmp_table = []
    for i in range(len(table[0])):
        tmp_table.append([])
    
    for i in range(len(table)):
        for j in range(len(table[i])):
            tmp_table[j].insert(i, table[i][j])
            if coldWidths[i] < len(table[i][j]):
                coldWidths[i] = len(table[i][j])
    for i in range(len(tmp_table)):
        for j in range(len(tmp_table[i])):
                print(table[j][i].rjust(coldWidths[j]+1), end='')
        print()
        
printTable(tableData)



