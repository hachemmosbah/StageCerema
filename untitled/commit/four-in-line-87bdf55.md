# four in line@87bdf55

|  |  | @@ -0,0 +1,205 @@ |
| :--- | :--- | :--- |
|  |  |  { |
|  |  |  "cells": \[ |
|  |  |  { |
|  |  |  "cell\_type": "code", |
|  |  |  "execution\_count": 1, |
|  |  |  "id": "sunset-salmon", |
|  |  |  "metadata": {}, |
|  |  |  "outputs": \[\], |
|  |  |  "source": \[ |
|  |  |  "import numpy as np \n", |
|  |  |  "import random" |
|  |  |  \] |
|  |  |  }, |
|  |  |  { |
|  |  |  "cell\_type": "code", |
|  |  |  "execution\_count": 63, |
|  |  |  "id": "verified-birthday", |
|  |  |  "metadata": { |
|  |  |  "scrolled": false |
|  |  |  }, |
|  |  |  "outputs": \[ |
|  |  |  { |
|  |  |  "ename": "KeyboardInterrupt", |
|  |  |  "evalue": "Interrupted by user", |
|  |  |  "output\_type": "error", |
|  |  |  "traceback": \[ |
|  |  |  "\u001b\[0;31m---------------------------------------------------------------------------\u001b\[0m", |
|  |  |  "\u001b\[0;31mKeyboardInterrupt\u001b\[0m Traceback \(most recent call last\)", |
|  |  |  "\u001b\[0;32m\u001b\[0m in \u001b\[0;36m\u001b\[0;34m\u001b\[0m\n\u001b\[1;32m 140\u001b\[0m \u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[1;32m 141\u001b\[0m \u001b\[0mconnect\u001b\[0m \u001b\[0;34m=\u001b\[0m \u001b\[0mConnect4\u001b\[0m\u001b\[0;34m\(\u001b\[0m\u001b\[0;34m\)\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[0;32m--&gt; 142\u001b\[0;31m \u001b\[0mconnect\u001b\[0m\u001b\[0;34m.\u001b\[0m\u001b\[0mgameOver\u001b\[0m\u001b\[0;34m\(\u001b\[0m\u001b\[0;34m\)\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[0m", |
|  |  |  "\u001b\[0;32m\u001b\[0m in \u001b\[0;36mgameOver\u001b\[0;34m\(self\)\u001b\[0m\n\u001b\[1;32m 53\u001b\[0m \u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[1;32m 54\u001b\[0m \u001b\[0;32mdef\u001b\[0m \u001b\[0mgameOver\u001b\[0m\u001b\[0;34m\(\u001b\[0m\u001b\[0mself\u001b\[0m\u001b\[0;34m\)\u001b\[0m\u001b\[0;34m:\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[0;32m---&gt; 55\u001b\[0;31m \u001b\[0mchoice\u001b\[0m \u001b\[0;34m=\u001b\[0m \u001b\[0mself\u001b\[0m\u001b\[0;34m.\u001b\[0m\u001b\[0mchoicePlay\u001b\[0m\u001b\[0;34m\(\u001b\[0m\u001b\[0;34m\)\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[0m\u001b\[1;32m 56\u001b\[0m \u001b\[0;32mif\u001b\[0m \u001b\[0mchoice\u001b\[0m \u001b\[0;34m==\u001b\[0m \u001b\[0;36m1\u001b\[0m\u001b\[0;34m:\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[1;32m 57\u001b\[0m \u001b\[0mturn\u001b\[0m \u001b\[0;34m=\u001b\[0m \u001b\[0;36m0\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n", |
|  |  |  "\u001b\[0;32m\u001b\[0m in \u001b\[0;36mchoicePlay\u001b\[0;34m\(self\)\u001b\[0m\n\u001b\[1;32m 49\u001b\[0m \u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[1;32m 50\u001b\[0m \u001b\[0;32mdef\u001b\[0m \u001b\[0mchoicePlay\u001b\[0m\u001b\[0;34m\(\u001b\[0m\u001b\[0mself\u001b\[0m\u001b\[0;34m\)\u001b\[0m\u001b\[0;34m:\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[0;32m---&gt; 51\u001b\[0;31m \u001b\[0mchoice\u001b\[0m \u001b\[0;34m=\u001b\[0m \u001b\[0mint\u001b\[0m\u001b\[0;34m\(\u001b\[0m\u001b\[0minput\u001b\[0m\u001b\[0;34m\(\u001b\[0m\u001b\[0;34m'Choice your game: \\n 1: Player1 Vs Player2 \\n 2: Player1 VS Bot \\n 3: Bot VS Bot \\n'\u001b\[0m\u001b\[0;34m\)\u001b\[0m\u001b\[0;34m\)\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[0m\u001b\[1;32m 52\u001b\[0m \u001b\[0;32mreturn\u001b\[0m \u001b\[0mchoice\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[1;32m 53\u001b\[0m \u001b\[0;34m\u001b\[0m\u001b\[0m\n", |
|  |  |  "\u001b\[0;32m/opt/anaconda3/envs/machinelearning/lib/python3.8/site-packages/ipykernel/kernelbase.py\u001b\[0m in \u001b\[0;36mraw\_input\u001b\[0;34m\(self, prompt\)\u001b\[0m\n\u001b\[1;32m 858\u001b\[0m \u001b\[0;34m\"raw\_input was called, but this frontend does not support input requests.\"\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[1;32m 859\u001b\[0m \)\n\u001b\[0;32m--&gt; 860\u001b\[0;31m return self.\_input\_request\(str\(prompt\),\n\u001b\[0m\u001b\[1;32m 861\u001b\[0m \u001b\[0mself\u001b\[0m\u001b\[0;34m.\u001b\[0m\u001b\[0m\_parent\_ident\u001b\[0m\u001b\[0;34m,\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[1;32m 862\u001b\[0m \u001b\[0mself\u001b\[0m\u001b\[0;34m.\u001b\[0m\u001b\[0m\_parent\_header\u001b\[0m\u001b\[0;34m,\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n", |
|  |  |  "\u001b\[0;32m/opt/anaconda3/envs/machinelearning/lib/python3.8/site-packages/ipykernel/kernelbase.py\u001b\[0m in \u001b\[0;36m\_input\_request\u001b\[0;34m\(self, prompt, ident, parent, password\)\u001b\[0m\n\u001b\[1;32m 902\u001b\[0m \u001b\[0;32mexcept\u001b\[0m \u001b\[0mKeyboardInterrupt\u001b\[0m\u001b\[0;34m:\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[1;32m 903\u001b\[0m \u001b\[0;31m\# re-raise KeyboardInterrupt, to truncate traceback\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[0;32m--&gt; 904\u001b\[0;31m \u001b\[0;32mraise\u001b\[0m \u001b\[0mKeyboardInterrupt\u001b\[0m\u001b\[0;34m\(\u001b\[0m\u001b\[0;34m\"Interrupted by user\"\u001b\[0m\u001b\[0;34m\)\u001b\[0m \u001b\[0;32mfrom\u001b\[0m \u001b\[0;32mNone\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[0m\u001b\[1;32m 905\u001b\[0m \u001b\[0;32mexcept\u001b\[0m \u001b\[0mException\u001b\[0m \u001b\[0;32mas\u001b\[0m \u001b\[0me\u001b\[0m\u001b\[0;34m:\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n\u001b\[1;32m 906\u001b\[0m \u001b\[0mself\u001b\[0m\u001b\[0;34m.\u001b\[0m\u001b\[0mlog\u001b\[0m\u001b\[0;34m.\u001b\[0m\u001b\[0mwarning\u001b\[0m\u001b\[0;34m\(\u001b\[0m\u001b\[0;34m\"Invalid Message:\"\u001b\[0m\u001b\[0;34m,\u001b\[0m \u001b\[0mexc\_info\u001b\[0m\u001b\[0;34m=\u001b\[0m\u001b\[0;32mTrue\u001b\[0m\u001b\[0;34m\)\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0;34m\u001b\[0m\u001b\[0m\n", |
|  |  |  "\u001b\[0;31mKeyboardInterrupt\u001b\[0m: Interrupted by user" |
|  |  |  \] |
|  |  |  } |
|  |  |  \], |
|  |  |  "source": \[ |
|  |  |  "class Connect4\(\):\n", |
|  |  |  "\n", |
|  |  |  " def \_\_init\_\_\(self\):\n", |
|  |  |  " self.rowCount = 6\n", |
|  |  |  " self.columnCount = 7\n", |
|  |  |  " self.board = np.zeros\(\(self.rowCount, self.columnCount\)\)\n", |
|  |  |  " self.win = None\n", |
|  |  |  " self.game\_over = False\n", |
|  |  |  " \n", |
|  |  |  " def isValidLocation\(self, col\):\n", |
|  |  |  " return self.board\[self.rowCount-1\]\[col\] == 0 \n", |
|  |  |  " \n", |
|  |  |  " def getNextOpenRow\(self, col\):\n", |
|  |  |  " for r in range\(self.rowCount\):\n", |
|  |  |  " if self.board\[r\]\[col\] == 0:\n", |
|  |  |  " return r\n", |
|  |  |  " def printBoard\(self\):\n", |
|  |  |  " \# print board\n", |
|  |  |  " print\(np.flip\(self.board, 0\)\)\n", |
|  |  |  " \n", |
|  |  |  " def dropPiece\(self, row, col, piece\):\n", |
|  |  |  " self.board\[row\]\[col\] = piece\n", |
|  |  |  " \n", |
|  |  |  " def winningMove\(self, piece\):\n", |
|  |  |  " \n", |
|  |  |  " \# check horizontal\n", |
|  |  |  " for c in range\(self.columnCount-3\):\n", |
|  |  |  " for r in range\(self.rowCount\):\n", |
|  |  |  " if self.board\[r\]\[c\] == piece and self.board\[r\]\[c+1\] == piece and self.board\[r\]\[c+2\] == piece and self.board\[r\]\[c+3\] == piece:\n", |
|  |  |  " return True\n", |
|  |  |  " \n", |
|  |  |  " \# check verticale\n", |
|  |  |  " for c in range\(self.columnCount\):\n", |
|  |  |  " for r in range\(self.rowCount-3\):\n", |
|  |  |  " if self.board\[r\]\[c\] == piece and self.board\[r+1\]\[c\] == piece and self.board\[r+2\]\[c\] == piece and self.board\[r+3\]\[c\] == piece:\n", |
|  |  |  " return True \n", |
|  |  |  " \n", |
|  |  |  " \# check positivly diagnols\n", |
|  |  |  " for c in range\(self.columnCount-3\):\n", |
|  |  |  " for r in range\(self.rowCount-3\):\n", |
|  |  |  " if self.board\[r\]\[c\] == piece and self.board\[r+1\]\[c+1\] == piece and self.board\[r+2\]\[c+2\] == piece and self.board\[r+3\]\[c+3\] == piece:\n", |
|  |  |  " return True \n", |
|  |  |  " \n", |
|  |  |  " \# check negativly diaghnols\n", |
|  |  |  " for c in range\(self.columnCount-3\):\n", |
|  |  |  " for r in range\(3, self.rowCount\):\n", |
|  |  |  " if self.board\[r\]\[c\] == piece and self.board\[r-1\]\[c+1\] == piece and self.board\[r-2\]\[c+2\] == piece and self.board\[r-3\]\[c+3\] == piece:\n", |
|  |  |  " return True\n", |
|  |  |  " \n", |
|  |  |  " def choicePlay\(self\):\n", |
|  |  |  " choice = int\(input\('Choice your game: \\n 1: Player1 Vs Player2 \\n 2: Player1 VS Bot \\n 3: Bot VS Bot \\n'\)\)\n", |
|  |  |  " return choice\n", |
|  |  |  "\n", |
|  |  |  " def gameOver\(self\):\n", |
|  |  |  " choice = self.choicePlay\(\)\n", |
|  |  |  " if choice == 1: \n", |
|  |  |  " turn = 0\n", |
|  |  |  " while not self.game\_over:\n", |
|  |  |  " \n", |
|  |  |  " if turn == 0:\n", |
|  |  |  " col = int\(input\('Player 1 make your selection \(0-6\):'\)\) \n", |
|  |  |  " if self.isValidLocation\(col\): \n", |
|  |  |  " row = self.getNextOpenRow\(col\)\n", |
|  |  |  " self.dropPiece\(row, col, 1\)\n", |
|  |  |  " \n", |
|  |  |  " if self.winningMove\(1\):\n", |
|  |  |  " print\('Player 1 wins !!!!'\)\n", |
|  |  |  " self.game\_over = True\n", |
|  |  |  " \n", |
|  |  |  " else: \n", |
|  |  |  " col = int\(input\('Player 2 make your selection \(0-6\):'\)\)\n", |
|  |  |  " \n", |
|  |  |  " if self.isValidLocation\(col\):\n", |
|  |  |  " \n", |
|  |  |  " row = self.getNextOpenRow\(col\)\n", |
|  |  |  " self.dropPiece\(row, col, -1\)\n", |
|  |  |  " \n", |
|  |  |  " if self.winningMove\(-1\):\n", |
|  |  |  " print\('Player 2 wins !!!!'\)\n", |
|  |  |  " self.game\_over = True\n", |
|  |  |  " \n", |
|  |  |  " self.printBoard\(\)\n", |
|  |  |  " \n", |
|  |  |  " turn += 1\n", |
|  |  |  " turn = turn % 2\n", |
|  |  |  " elif choice == 2: \n", |
|  |  |  " turn = 0\n", |
|  |  |  " while not self.game\_over:\n", |
|  |  |  " if turn == 0:\n", |
|  |  |  " col = int\(input\('Player 1 make your selection \(0-6\):'\)\)\n", |
|  |  |  " if self.isValidLocation\(col\):\n", |
|  |  |  " row = self.getNextOpenRow\(col\)\n", |
|  |  |  " self.dropPiece\(row, col, 1\)\n", |
|  |  |  " \n", |
|  |  |  " if self.winningMove\(1\):\n", |
|  |  |  " print\('Player 1 wins !!!!'\)\n", |
|  |  |  " self.game\_over = True\n", |
|  |  |  " \n", |
|  |  |  " else: \n", |
|  |  |  " col = random.randint\(0, 6\)\n", |
|  |  |  " if self.isValidLocation\(col\):\n", |
|  |  |  " row = self.getNextOpenRow\(col\)\n", |
|  |  |  " self.dropPiece\(row, col, -1\)\n", |
|  |  |  " \n", |
|  |  |  " if self.winningMove\(-1\):\n", |
|  |  |  " print\(' Bot wins !!!!'\)\n", |
|  |  |  " self.game\_over = True\n", |
|  |  |  " \n", |
|  |  |  " self.printBoard\(\)\n", |
|  |  |  " \n", |
|  |  |  " turn += 1\n", |
|  |  |  " turn = turn % 2\n", |
|  |  |  " else: \n", |
|  |  |  " turn = 0\n", |
|  |  |  " while not self.game\_over:\n", |
|  |  |  " if turn == 0:\n", |
|  |  |  " col = random.randint\(0, 6\)\n", |
|  |  |  " if self.isValidLocation\(col\):\n", |
|  |  |  " row = self.getNextOpenRow\(col\)\n", |
|  |  |  " self.dropPiece\(row, col, 1\)\n", |
|  |  |  " \n", |
|  |  |  " if self.winningMove\(1\):\n", |
|  |  |  " print\('Bot 1 wins !!!!'\)\n", |
|  |  |  " self.game\_over = True\n", |
|  |  |  " else: \n", |
|  |  |  " col = random.randint\(0, 6\)\n", |
|  |  |  " if self.isValidLocation\(col\):\n", |
|  |  |  " row = self.getNextOpenRow\(col\)\n", |
|  |  |  " self.dropPiece\(row, col, -1\)\n", |
|  |  |  " \n", |
|  |  |  " if self.winningMove\(-1\):\n", |
|  |  |  " print\('Bot 2 wins !!!!'\)\n", |
|  |  |  " self.game\_over = True\n", |
|  |  |  " \n", |
|  |  |  " self.printBoard\(\)\n", |
|  |  |  " \n", |
|  |  |  " turn += 1\n", |
|  |  |  " turn = turn % 2 \n", |
|  |  |  " \n", |
|  |  |  " \n", |
|  |  |  "connect = Connect4\(\)\n", |
|  |  |  "connect.gameOver\(\)" |
|  |  |  \] |
|  |  |  } |
|  |  |  \], |
|  |  |  "metadata": { |
|  |  |  "kernelspec": { |
|  |  |  "display\_name": "Python 3", |
|  |  |  "language": "python", |
|  |  |  "name": "python3" |
|  |  |  }, |
|  |  |  "language\_info": { |
|  |  |  "codemirror\_mode": { |
|  |  |  "name": "ipython", |
|  |  |  "version": 3 |
|  |  |  }, |
|  |  |  "file\_extension": ".py", |
|  |  |  "mimetype": "text/x-python", |
|  |  |  "name": "python", |
|  |  |  "nbconvert\_exporter": "python", |
|  |  |  "pygments\_lexer": "ipython3", |
|  |  |  "version": "3.8.5" |
|  |  |  } |
|  |  |  }, |
|  |  |  "nbformat": 4, |
|  |  |  "nbformat\_minor": 5 |
|  |  |  } |

