import time
import random

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
						elif total_player > 21:
							print("You dealt over 21! You lose!")
							replay = input("Would you like to play again?[Y/n] ")
							if replay == "Y" or replay == "y":
								break
							elif replay == "N" or replay == "n":
								print("Ok, bye!")
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
								elif total > 21:
									print("Dealer has over 21! You win!")
									print("Dealer was given: {}".format(total))
									replay = input("Would you like to play again?[Y/n] ")
									if replay == "Y" or replay == "y":
										break
										break
									elif replay == "N" or replay == "n":
										print("Ok, bye!")
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
											break
									elif total > 17 and total < 21 and total < total_player:
										print("You win!")
										replay = input("Would you like to play again?[Y/n] ")
										if replay == "Y" or replay == "y":
											continue
										elif replay == "N" or replay == "n":
											print("Ok, bye!")
											break
BlackJack()