import random # Import random for random handouts
import sys # Import sys for program exiting
import hashlib # Import hashlib for hashing passwords for security

def BlackJack():
	while True:
		print("-=-=-=-=-=-=-=-")
		print("Dealer is dealing cards")

		dealer_first_card = random.randint(1, 13)
		dealer_second_card = random.randint(1, 13)

		total = dealer_first_card + dealer_second_card
		if total == 21:
			print("Dealer has won")
			print("Dealer was given a {} and a {}".format(dealer_first_card, dealer_second_card))
		elif total > 21:
			print("Dealer was dealt over 21! You win!")
		elif total < 21:
			player_first_card = random.randint(1, 13)
			player_second_card = random.randint(1, 13)

			total_player = player_first_card + player_second_card
			if total_player == 21:
				print("You win!")
			elif total_player > 21:
				print("You were dealt over 21! You lose!")
			elif total_player < 21:
				print("You were dealt a total of: {}".format(total_player))
				while total_player < 21:
					another = input("Do you want another card?[Y/n] ")
					if another == "Y" or another == "y":
						total_player += random.randint(1, 13)

						if total_player == 21:
							print("You win!")
							replay = input("Would you like to play again?[Y/n] ")
							if replay == "Y" or replay == "y":
								break
							elif replay == "N" or replay == "n":
								print("Ok, bye!")
								sys.exit(1)
						elif total_player > 21:
							print("You dealt over 21! You lose!")
							replay = input("Would you like to play again?[Y/n] ")
							if replay == "Y" or replay == "y":
								break
							elif replay == "N" or replay == "n":
								print("Ok, bye!")
								sys.exit(1)
						elif total_player < 21:
							print("You now have: {}".format(total_player))
					elif another == "N" or another == "n":
						print("Ok! Dealer if flipping over his cards!")

						print("Dealer has: {}".format(total))
						if total < 17:
							while total < 17:
								total += random.randint(1, 13)

								if total == 21:
									print("Dealer wins! He was given 21!")
									replay = input("Would you like to play again?[Y/n] ")
									if replay == "Y" or replay == "y":
										break
									elif replay == "N" or replay == "n":
										print("Ok, bye!")
										sys.exit(1)
								elif total > 21:
									print("Dealer has over 21! You win!")
									print("Dealer was given: {}".format(total))
									replay = input("Would you like to play again?[Y/n] ")
									if replay == "Y" or replay == "y":
										break
										break
									elif replay == "N" or replay == "n":
										print("Ok, bye!")
										sys.exit(1)
								elif total > 17:
									print("Dealer needs to stand on 17!")
									print("Dealer now has: {}".format(total))
									if total == 21:
										print("Dealer has won!")
									elif total > 21:
										print("Dealer went over! You win!")
									elif total > 17 and total < 21 and total > total_player:
										print("Dealer has won!")
										replay = input("Would you like to play again?[Y/n] ")
										if replay == "Y" or replay == "y":
											continue
										elif replay == "N" or replay == "n":
											print("Ok, bye!")
											sys.exit(1)
									elif total > 17 and total < 21 and total < total_player:
										print("You win!")
										replay = input("Would you like to play again?[Y/n] ")
										if replay == "Y" or replay == "y":
											continue
										elif replay == "N" or replay == "n":
											print("Ok, bye!")
											sys.exit(1)
							break

def login_bet():
	existing_acc_check = input("Do you have an existing account[Y/n]? ")

	if existing_acc_check == "N" or existing_acc_check == "n":
		username = input("Choose a username: ")
		password = input("Choose a password: ")
		password_confirm = input("Confirm password: ")

		if str(password) == str(password_confirm):
			chips = 1000

			password.encode('utf-8')

			passwd = hashlib.md5(password.encode('utf-8'))
			passwd_hashed = passwd.hexdigest()

			creation = open("Accounts.txt", "w")
			creation.write("Username: {} | Password: {} | Chips: {}".format(username, passwd_hashed, chips))
			creation.close()

			print("Account Created Successfully!")

		elif str(password) != str(password_confirm):
			print("Passwords do not match!")

	elif existing_acc_check == "Y" or existing_acc_check == "y":
		username_login = input("Username: ")
		password_login = input("Password: ")

		checking_password = hashlib.md5()
		checking_password.update(password_login)

		creation = open("Accounts.txt", "r")
		creation.read()

		if username_login == creation:
			if checking_password == creation:
				print("Login successful")
				BlackJack()
			elif password_login != creation:
				print("Incorrect password!")

		elif username_login != creation:
			print("Incorrect username!")

login_bet()