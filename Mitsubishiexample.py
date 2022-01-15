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
        solution_mitsubishi, rowmarked, columnmarked= matrixmark(currentmatrix)
        zero_num = len(rowmarked) + len(columnmarked)
        if zero_num < dimension:
            currentmatrix = matrixadjust(currentmatrix, rowmarked, columnmarked)
    return solution_mitsubishi

def calculation(matrix,mitsubishi):
    total = 0
    solutionofmatrix = np.zeros((matrix.shape[0], matrix.shape[1]))
    for s in range(len(mitsubishi)):
        total += matrix[mitsubishi[s][0], mitsubishi[s][1]]
        matrix[mitsubishi[s][0], mitsubishi[s][1]] = matrix[mitsubishi[s][0], mitsubishi[s][1]]
    return total,solutionofmatrix

def MitsubishiExample():
    mitsubishi_productioncost_matrix = np.array([[61,33 , 18, 6, 13],
                                                [36, 81, 66, 10, 30],
                                                [8, 60, 80, 1, 3],
                                                [11, 18, 31, 6, 8],
                                                [6, 8, 16, 10, 81]])
    solution_mitsubishi = hungarian_method(mitsubishi_productioncost_matrix.copy())
    solution, solutionofmatrix = calculation(mitsubishi_productioncost_matrix, solution_mitsubishi)

    mitsubishi_profitmatrix = np.array([[2, 3, 12, 2, 3],
                                       [2, 5, 2, 3, 1],
                                       [2, 1, 1, 2, 3],
                                       [7, 12, 2, 4, 2],
                                       [2, 2, 0, 1, 2]])
    maximumvalue = np.max(mitsubishi_profitmatrix)
    mitsubishi_productioncost_matrix = maximumvalue - (mitsubishi_profitmatrix)
    solution_mitsubishi = hungarian_method(mitsubishi_productioncost_matrix.copy())
    solution, solutionofmatrix = calculation(mitsubishi_profitmatrix, solution_mitsubishi)
    print(maximumvalue-mitsubishi_profitmatrix)
    print(mitsubishi_profitmatrix)
    print(f"Mitsubishi Air Conditioner assignment problem solution is: {solution:}")

MitsubishiExample()
