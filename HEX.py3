def game_status(board_size, board):
  # TODO: implement this method to determine the status of the game board
  if (board_size==1):
    if(board[0][0]=='.'):
      return "Nobody wins"
    elif(board[0][0]=='B'):
      return "Blue wins"
    else:
      return "Red wins"
  else:
    blueWin=0
    redWin=0
    tempBlue=0
    tempRed=0
    print(board)
    for i in board:
      for j in i:
        if (j=="B"):
          tempBlue+=1
      if (tempBlue==board_size):
        blueWin+=1
        tempBlue=0


    print(blueWin)
    print(redWin)

    if (blueWin>1 or redWin>1):
      return "Impossible"
    elif (blueWin==1):
      return "Blue wins"
    elif(redWin==1):
      return "Red wins"
    else:
      return "Nobody wins"

  return ""

def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1, 1):
    board_size = int(input())
    board = []
    for _ in range(board_size):
      board.append(list(input().strip()))

    ans = game_status(board_size, board)

    print("Case #{}: {}".format(test_case, ans))

if __name__ == "__main__":
  main()
