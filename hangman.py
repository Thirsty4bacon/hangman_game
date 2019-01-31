from random import choice
#function created for replacing dashes with good letters
def good_letter(str):
	for i in str:
		if i == ' ':
			puzzle.append(i)
		elif i == guess:
			puzzle.append(guess) 
		elif i in good_guess:
			puzzle.append(i)
		elif i in punctuation:
			puzzle.append(i)
		else:
			puzzle.append('_')
puzzle1 = []#dashes that hold the places for the letters in the puzzle
misses = []# tracks how many wrong guesses with an "x"
wrong = 0
guessed =[]# holds all letters alrady guessed
good_guess = []# holds letters guessed that are in the puzzle
punctuation = ['!','.','?',"'",',']
print "\nLet's play HANGMAN!"
print "\nIf at any time you want to try and solve the puzzle,"
print 'type "solve".'
print '\nIf you want to exit the game type "done".'
print '\nHave Fun!!!'
green = True
while green:
	lets_play = raw_input('\nWould you like to play? y/n : ')
	if lets_play == 'n':
		green = False
		print "\n I didn't want to play with you anyway!" 
	elif lets_play == 'y':
		go = True
		while go:
			print "\nHere is your puzzle:\n" 
			phrases =['look at all those chickens!',
						'to infinity and beyond!',
						'we are the nights who say ne!',
						'free shaw vacadoos!',
						"i can't believe this program works!",
						'holy crap, a talking muffin!']
			solution = choice(phrases)
			phrases.remove(solution)
			for i in solution:
				if i == ' ':
					puzzle1.append(i)
				else:
					puzzle1.append('_')
			print ' '.join(puzzle1)
			while wrong < 7:
				if wrong == 5:
					print '\n YOU LOSE!'
					go= False
					break
				else:
					puzzle = []	 
					print '\n'+' '.join(misses)
					guess = raw_input('Guess a letter: ')
					if guess == 'done':
						green = False
						go = False
						break
					elif guess == 'solve':
						solve = raw_input('\nGo ahead and solve it! : ')
						if solve == solution:
							print '\n YOU WIN!\n'
							play_again = raw_input('Would you like to play again? :')
							if play_again == 'n':
								green = False 
								go = False
								break
							elif play_again == 'y':
								wrong = 8
								go = False
						else:
							misses.append('X')
							wrong+=1
							print "\n\nNope!"		
					elif len(guess) > 1 and guess != 'done' and guess != 'solve':
						print 'Please guess one letter at a time.' 
					elif guess in guessed:
						wrong += 1
						print 'You already guessssed that, stupid!'
					elif guess in solution:
						guessed.append(guess)
						good_guess.append(guess)
						print '\n'+ 'Got one!'
						good_letter(solution)# from the fuction at the top of the page
						print '\n'+' '.join(puzzle)
						if '_' not in puzzle:
							print '\n YOU WIN!\n'
							play_again = raw_input('Would you like to play again? :')
							if play_again == 'n':
								green = False
								go = False
								break
							else:
								go = False
								break
					else:
						misses.append('X')
						wrong+=1 
						print '\n Nope! Try again!'
						for i in solution:
							if i == ' ':
								puzzle.append(i)
							elif i in good_guess:
								puzzle.append(i)
							elif i in punctuation:
								puzzle.append(i)
							else:
								puzzle.append('_')
						print '\n'+' '.join(puzzle)
						if guess not in guessed:
							guessed.append(guess)
				print '\n'
				print 'Already Guessed:'
				print ",".join(guessed)

	else:
		print '\nenter "y" or "n" stupid!'
							

				


