################################################ MAKING SLOT MACHINE #########################################################################
import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {"A":2, "B":4, "C":6, "D":8}
symbol_value = {"A":10, "B":5, "C":2, "D":1}




#################################################### CHECKING IF THE PLAYER WON ################################################################ 
def check_winnings(columns, lines, bet, values):
   winnings = 0
   winning_line = []
   for line in range(lines):
      symbol = columns[0][line]
      for column in columns:
         symbol_to_check = column[line]
         if symbol != symbol_to_check:
            break
      else:
         winnings += values[symbol] * bet
         winning_line.append(line + 1)
   return winnings, winning_line
###############################################################################################################################################




######################################## THIS IS THE ACTUAL WORKING OF THE SLOT MACHINE #######################################################
def get_slot_machine_spin(rows,cols, symbols):
   all_symbols = []
   for symbol, symbol_count in symbols.items():
      for _ in range(symbol_count):
         all_symbols.append(symbol)
   
   columns = []
   for _ in range(cols):
      column = []
      current_symbols = all_symbols[:]

      for _ in range(rows):
         value = random.choice(current_symbols)
         current_symbols.remove(value)
         column.append(value)

      columns.append(column)
   return columns
###############################################################################################################################################



######################################## PRINTING THE SLOT MACHINE ############################################################################
def print_slot_machine(columns):
   for row in range(len(columns[0])):
      for i, column in enumerate(columns):
         if i != len(columns) - 1:
            print(column[row], end=" | ")
         else:
            print(column[row], end="")
      
      print()
###############################################################################################################################################



################################################################# DEPOSITING CASH #############################################################
def deposit():
   while True:
      amount = input("please enter the amount you want to deposit $ ? : ")
      if amount.isdigit():
         amount = int(amount)
         if amount > 0:
            break
         else:
             print("Amount must be greater than $0")
      else:
         print("Please enter a valid numnber")

   return amount
###############################################################################################################################################




######################################## THE NUMBER OF LINES PLAYER WANTS TO BET ON  ##########################################################
def get_number_of_lines():
   while True:
      lines = input("Please enter the number of lines you want to place your bet on from 1 to 3 : ")
      if lines.isdigit():
         lines = int(lines)
         if 1 <= lines <= MAX_LINES:
            break
         else:
            print("Enter a valid number of lines")
      else:
         print(" Please enter a valid number")
   return lines
###############################################################################################################################################



######################################## THE AMOUNT THEY WANT TO PLACE ON EACH LINE ###########################################################
def get_bet():
   while True:
      amount = input(" What amount would you like to bet on each line ? :" )
      if amount.isdigit():
         amount = int(amount)
         
         if MIN_BET <= amount <= MAX_BET:
            break
         else:
            print("Please enter a vallid amount between $10 and $100")
      else:
         print("Please enter a valid amount")
   return amount
###############################################################################################################################################




###############################################################################################################################################
def spin(balance):
   lines = get_number_of_lines()

######################################## CHECK IF THEY HAVE ENOUGH BALANCE FOR THE BET ########################################################

   while True:
      bet = get_bet()
      total_bet = bet * lines

      if total_bet > balance:
         print("You don't have enough balance to bet on that amount. You're current balance is {}".format(balance))
      else:
         break

   print(" You deposited ${}".format(balance))
   print("and you are betting ${} on {} lines. So you're total bet value will be ${}".format(bet, lines, (bet*lines)))


   slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
   print_slot_machine(slots)
   winnings, winning_lines= check_winnings(slots, lines, bet, symbol_value)
   print("You won ${}. CONGRATULATIONS".format(winnings))
   print("You're winning lines  are " , * winning_lines)
   return winnings - total_bet
###############################################################################################################################################


###############################################################################################################################################ef main():
def main():
   balance = deposit()
   while True:
      print("Current balance is ${}".format(balance))
      answer = input("Press enter to play and press Q to quit")
      if answer =="Q":
         break
      balance += spin(balance)
         
print("You are left with ${balance}")



main()
###############################################################################################################################################