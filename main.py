'''
Program Version: 1.0.2
Developer: Brad Thompson
Program: CLI-Based Black Jack
'''
import random # Import random for random handouts
import sys # Import sys for program exiting
try:
	import hashlib # Import hashlib for hashing passwords for security
except ModuleNotFoundError:
	print("Module 'hashlib' is not installed!")

def BlackJack(): # Creating the BlackJack function
	while True: # Starting infinite loop
		print("-=-=-=-=-=-=-=-") # Fancy detail for separation of games
		print("Dealer is dealing cards") # Announcing the dealing of cards

		# Randomizing 2 cards to start with for the dealer
		dealer_first_card = random.randint(1, 13)
		dealer_second_card = random.randint(1, 13)

		total = dealer_first_card + dealer_second_card # Assigning the sum of the first & second card to "total"
		if total == 21: # If the total is 21
			print("Dealer has won") # Announce of automatic instant win via dealer
			print("Dealer was given a {} and a {}".format(dealer_first_card, dealer_second_card)) # Display what cards the dealer was given to equal 21
		elif total > 21: #  If the total is over 21
			print("Dealer was dealt over 21! You win!") # Announce of automatic instant win via player
		elif total < 21: # If the total is less than 21
			# Randomizing 2 cards to give the player
			player_first_card = random.randint(1, 13)
			player_second_card = random.randint(1, 13)

			total_player = player_first_card + player_second_card # Assigning the sum of the first and second player cards to "total_player"
			if total_player == 21: # If the total is 21
				print("You win!") # Announce of automatic instant win via player
				print("You were given a {} and a {}".format(player_first_card, player_second_card)) # Display what cards the player was given to equal 21
			elif total_player > 21: # If the total is over 21
				print("You were dealt over 21! Dealer wins!") # Announce of automatic instant win via dealer
			elif total_player < 21: # If the total is less than 21
				print("You were dealt a total of: {}".format(total_player)) # Display player card total
				while total_player < 21: # While the total is less than 21
					another = input("Do you want another card?[Y/n] ") # Ask player if they want another card
					if another == "Y" or another == "y": # If the player would like another card
						total_player += random.randint(1, 13) # Add a random number between 1 to 13 to the players total

						if total_player == 21: # If the players total is equal to 21
							print("You win!") # Announce of automatic instant win via player
							replay = input("Would you like to play again?[Y/n] ") # Ask if the player would like to play again
							if replay == "Y" or replay == "y": # If the player would like to play again
								break # Break out of loop (causing reinitiation of it)
							elif replay == "N" or replay == "n": # If the player would not like to play again
								print("Ok, bye!") # Say goodbye
								sys.exit(1) # Exit program via exit code 1
						elif total_player > 21: # If the players total is over 21
							print("You dealt over 21! You lose!") # Announce of loss
							replay = input("Would you like to play again?[Y/n] ") # Ask if the playewr would like to play again
							if replay == "Y" or replay == "y": # If the player would like to play again
								break # Break out of loop (causing reinitiation of it)
							elif replay == "N" or replay == "n": # If the plater would not like to play again
								print("Ok, bye!") # Say goodbye
								sys.exit(1) # Exit program via exit code 1
						elif total_player < 21: # If the players total is less than 21
							print("You now have: {}".format(total_player)) # Announce the players total
					elif another == "N" or another == "n": # If the player would not like another card
						print("Ok! Dealer if flipping over his cards!") # Announce the dealer flipping over his cards

						print("Dealer has: {}".format(total)) # Accounce dealers amount
						if total < 17: # If the total is less than 17
							while total < 17: # While loop for if the Dealer has less then 17
								print("Dealer needs to stand on 17!")
								total += random.randint(1, 13) # Add a random number from 1 to 13 to the total

								if total == 21: # If the total now equals 21
									print("Dealer wins! He was given 21!") # Announce the Dealer has automatically won
									replay = input("Would you like to play again?[Y/n] ") # Ask if the player would like to play again
									if replay == "Y" or replay == "y": # If the user would like to play again
										break # Break out of loop (causing reinitiation of it)
									elif replay == "N" or replay == "n": # If the user would not like to play again
										print("Ok, bye!") # Say goodbye
										sys.exit(1) # Exit program via exit code 1
								elif total > 21: # If the total is greater than 21
									print("Dealer has over 21! You win!") # Announce the player has automatically won
									print("Dealer was given: {}".format(total)) # Display how much the dealer was dealt total
									replay = input("Would you like to play again?[Y/n] ") # Ask if the player would like to play again
									if replay == "Y" or replay == "y": # If the user would like to play again
										break # Break out of loop
										break # Break out of loop (causing reinitiation of it)
									elif replay == "N" or replay == "n": # If the user would not like to play again
										print("Ok, bye!") # Say goodbye
										sys.exit(1) # Exit program via exit code 1
								elif total >= 17: # If the total is greater than 17
									print("Dealer now has: {}".format(total)) # Display the dealers total
									if total == 21: # If the total is 21
										print("Dealer has won!") # Announce automatic win of the dealer
									elif total > 21: # If the total is greater than 21
										print("Dealer went over! You win!") # Announce automatic win of the player
									elif total > 17 and total < 21 and total > total_player: # If the total is greater than 17, less than 21, and greater than the players total
										print("Dealer has won!") # Announce the dealer has won
										replay = input("Would you like to play again?[Y/n] ") # Ask if the player would like to play again
										if replay == "Y" or replay == "y": # If the user would like to play again
											break # Break out of loop (causing reinitiation of it)
 										elif replay == "N" or replay == "n": # If the user would not like to play again
											print("Ok, bye!") # Say goodbye
											sys.exit(1) # Exit program via exit code 1
									elif total > 17 and total < 21 and total < total_player: # If the total is greater than 17, less than 21, and less than the players total
										print("You win!") # Announce the player has won
										replay = input("Would you like to play again?[Y/n] ") # Ask if the player would like to play again
										if replay == "Y" or replay == "y": # If the user would like to play again
											break # Break out of loop (causing reinitiation of it)
										elif replay == "N" or replay == "n": # If the user would not like to play again
											print("Ok, bye!") # Say goodbye
											sys.exit(1) # Exit program via exit code 1
							break # Break out of loop

def login_bet(): # Creating the account creation function !INCOMPLETE!
	existing_acc_check = input("Do you have an existing account[Y/n]? ") # If the user has an existing account

	if existing_acc_check == "N" or existing_acc_check == "n": # If they do not have an existing account
		username = input("Choose a username: ") # Tell the user to choose a username
		password = input("Choose a password: ") # Tell the user to choose a password
		password_confirm = input("Confirm password: ") # Tell the user to confirm their password

		if str(password) == str(password_confirm): # If the passwords to match
			chips = 1000 # Give the user 1000 chips

			password.encode('utf-8') # encode the password in utf-8

			passwd = hashlib.md5(password.encode('utf-8')) # Hash the password using md5
			passwd_hashed = passwd.hexdigest() # Digest the hex (complete the hash)

			creation = open("Accounts.txt", "w") # Open Accounts.txt in write mode
			creation.write("Username: {} | Password: {} | Chips: {}".format(username, passwd_hashed, chips)) # Write the username, hashed password, and chip value
			creation.close() # Close the file

			print("Account Created Successfully!") # Announce successfull account creation

		elif str(password) != str(password_confirm): # If the passwords do NOT match
			print("Passwords do not match!") # Announce the passwords do NOT match

	elif existing_acc_check == "Y" or existing_acc_check == "y": # If the user has an existing account
		username_login = input("Username: ") # Ask for their username
		password_login = input("Password: ") # Ask for their username

		password_login.encode('utf-8')

		passwd_login = hashlib.md5(password_login.encode('utf-8'))
		passwd_login_hash = passwd_login.hexdigest()

		creation = open("Accounts.txt", "r") # Open Accounts.txt in read mode
		creation.read() # Read the file

		if username_login == creation: # If the username is in the file
			if checking_password == creation: # If the password is in the file
				print("Login successful") # Announce successful login
				BlackJack() # Call the BlackJack function
			elif password_login != creation: # If the password is not in the file
				print("Incorrect password!") # Announce the password is incorrect

		elif username_login != creation: # If the username is not in the file
			print("That username was not found") # Announce that the username entered was not found in the file

login_bet() # Call the login_bet function
