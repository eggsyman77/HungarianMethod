import numpy as np

def row_minimization(zeromatrix, zeromark):
    rowofminimum =[63180010,0]
    for number_of_row in range(zeromatrix.shape[0]):
        if np.sum(zeromatrix[number_of_row] == True) > 0 and rowofminimum[0] > np.sum(zeromatrix[number_of_row] == True):
            rowofminimum = [np.sum(zeromatrix[number_of_row] == True),number_of_row]
    zeroindex = np.where(zeromatrix[rowofminimum[1]] == True)[0][0]
    zeromark.append((rowofminimum[1], zeroindex))
    zeromatrix[rowofminimum [1], :] = False
    zeromatrix[:, zeroindex] = False

def matrixmark (matrix):
    currentmatrix = matrix
    zeroboolean_matrix = (currentmatrix == 0)
    zeroboolean_matrix_copy = zeroboolean_matrix.copy()
    zeromarked = []
    while (True in zeroboolean_matrix_copy):
        row_minimization(zeroboolean_matrix_copy, zeromarked)
    row_zeromarked = []
    column_zeromarked = []
    for s in range(len(zeromarked)):
        row_zeromarked.append(zeromarked[s][0])
        column_zeromarked.append(zeromarked[s][1])
        unmarked_row = list(set(range(currentmatrix.shape[0])) - set(row_zeromarked))
    columnmarked = []
    change = True
    while change:
        change = False
        for s in range(len(unmarked_row)):
            row_array = zeroboolean_matrix[unmarked_row[s],:]
            for m in range(row_array.shape[0]):
                if row_array[m] == True and m not in columnmarked:
                    columnmarked.append(m)
                    change = True
        for numberofrow, numberofcolumn in zeromarked:
            if numberofrow not in unmarked_row and numberofcolumn in columnmarked:
                unmarked_row.append(numberofrow)
                change = True
    rowmarked = list(set(range(matrix.shape[0])) - set(unmarked_row))
    return (zeromarked, rowmarked, columnmarked)

def matrixadjust(matrix, rowscover,columnscover ):
    currentmatrix = matrix
    zeroelement_none = []
    for row in range(len(currentmatrix)):
        if row not in rowscover:
            for s in range(len(currentmatrix[row])):
                if s not in columnscover:
                    zeroelement_none.append(currentmatrix[row][s])
    minimumnumber = min(zeroelement_none)
    for row in range(len(currentmatrix)):
        if row not in rowscover:
            for s in range(len(currentmatrix[row])):
                if s not in columnscover:
                    currentmatrix[row, s] = currentmatrix[row, s] - (minimumnumber)
    for row in range(len(rowscover)):
        for column in range(len(columnscover)):
           currentmatrix[rowscover[row], columnscover[column]] = currentmatrix[rowscover[row], columnscover[column]] + (minimumnumber)
    return currentmatrix

def hungarian_method(matrix):
    dimension = matrix.shape[0]
    currentmatrix = matrix
    for numberofrow in range(matrix.shape[0]):
        currentmatrix[numberofrow] = currentmatrix[numberofrow] - np.min(currentmatrix[numberofrow])
    for numberofcolumn in range(matrix.shape[1]):
        currentmatrix[:, numberofcolumn] = currentmatrix[:, numberofcolumn] - np.min(currentmatrix[:, numberofcolumn])
    zero_num = 0
    while zero_num < dimension:
        solution_kumtel, rowmarked, columnmarked= matrixmark(currentmatrix)
        zero_num = len(rowmarked) + len(columnmarked)
        if zero_num < dimension:
            currentmatrix = matrixadjust(currentmatrix, rowmarked, columnmarked)
    return solution_kumtel

def calculation(matrix,kumtel):
    total = 0
    solutionofmatrix = np.zeros((matrix.shape[0], matrix.shape[1]))
    for s in range(len(kumtel)):
        total += matrix[kumtel[s][0], kumtel[s][1]]
        matrix[kumtel[s][0], kumtel[s][1]] = matrix[kumtel[s][0], kumtel[s][1]]
    return total,solutionofmatrix

def KumtelExample():
    kumtel_productioncost_matrix = np.array([[16, 10, 66, 30, 86],
                                            [8, 60, 80, 13, 31],
                                            [6, 81, 36, 8, 10],
                                            [33, 30, 68, 13, 80],
                                            [10, 36, 83, 60, 66]])
    solution_kumtel = hungarian_method(kumtel_productioncost_matrix.copy())
    solution, solutionofmatrix = calculation(kumtel_productioncost_matrix,solution_kumtel)

    kumtel_profitmatrix = np.array([[2, 1, 2, 3, 2],
                                   [2, 3, 1, 3, 5],
                                   [4, 7, 0, 3, 8],
                                   [3, 3, 12, 3, 1],
                                   [6, 2, 3, 3, 2]])
    maximumvalue = np.max(kumtel_profitmatrix)
    kumtel_productioncost_matrix = maximumvalue - (kumtel_profitmatrix)
    solution_kumtel = hungarian_method(kumtel_productioncost_matrix.copy())
    solution, solutionofmatrix = calculation(kumtel_profitmatrix, solution_kumtel)
    print(maximumvalue-kumtel_profitmatrix)
    print(kumtel_profitmatrix)
    print(f"Kumtel Infrared Heaters assignment problem solution is: {solution:}")


KumtelExample()
