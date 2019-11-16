def eraseTable(tab):
    '''
   (list) -> None
   This function prepares the game table (array) 
   by putting '-' in all the elements.
   It does not create a new array
   Preconditions: tab is a reference to an nxn array matrice n x n that contains '-', 'X' or 'O'
   '''

    # to complete
    row = 0
    while row < len(tab):

        col = 0
        while col < len(tab[row]):

            tab[row][col] = '-'
            col += 1
        row += 1
    # returns nothing


def verifyWin(tab):
    '''(list) ->  bool
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    * Verify if there is a winner.
    * Look for 3 X's and O's in a row, column, and diagonal.
    * If we find one, we display the winner (the message "Player X has won" 
    * or "Player O has won!") and returns True.
    * If there is a draw (verify it with the function testdraw),
    * display "It is a draw" and returns True.
    * If the game is not over, returns False.
    * The function call the functions testrows, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Those functions returns the winner 'X' or 'O', or '-' if there is no winner.
    '''
    result = [testRows(tab), testCols(tab), testDiags(tab)]
    for v in result:
        if v == 'X':
            print('Player X has won ')
            return True
        elif v == 'O':
            print('Player O has won ')
            return True
        else:
            if testDraw(tab):
                print("It is a draw")
                return True

    return False


def testRows(tab):
    """ (list) ->  str
   * verify if there is a winning row.
   * Look for three 'X' or three 'O' in a row.
   * If they are found, the character 'X' or 'O' is returned, otherwise '-' is returned.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   """

    for row in tab:
        if all(v == 'X' for v in row):
            return 'X'
        elif all(v == 'O' for v in row):
            return 'O'

    return '-'

    #  to complete  # to be modified so that it returns the winner, or '-' if there is no winner


def testCols(tab):
    """ (list) ->  str
      * verify a winning column.
      * look for three 'X' or three 'O' in a column.
      * If it is the case the character 'X' or 'O' is returned, otherwise '-' is returned.
      * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
      """
    col = 0
    while col < len(tab):
        if all(row[col] == 'X' for row in tab):
            return 'X'
        elif all(row[col] == 'O' for row in tab):
            return 'O'
        col = col + 1
    return '-'
    # to be modified so that it returns the winner, or '-' if there is no winner


def testDiags(tab):
    ''' (list) ->  str
   * Look for three 'X' or three 'O' in a diagonal.
   * If it is the case, the character 'X' or 'O' is returned
   * otherwise '-' is returned.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
    diag = [tab[i][i] for i in range(len(tab))]
    diagopp = [tab[i][~i] for i in range(len(tab))]
    if all((i == 'X' for i in diag)) or all((j == 'X' for j in diagopp)):
        return 'X'
    elif all((i == 'O' for i in diag)) or all((j == 'O' for j in diagopp)):
        return 'O'

    return '-'  # #to be modified so that it returns the winner, or '-' if there is no winner


def testDraw(tab):
    ''' (list) ->  bool
   * verify if there is a draw
   * check if all the array elements have X or O, not '-'.  
   * If we do not find find any '-' in the array, return True. 
   * If there is any '-', return false.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''

    # to complete
    for row in tab:
        for col in row:
            if col == '-':
                return False

    return True
