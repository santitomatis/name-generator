import random
import pandas as pd

def file_to_list(file):
	"""Converts every line of a .txt file to an item of an array

    Args:
        file (.txt): the file you want to convert

    Returns:
        array: an array with each line of the .txt
    """
	rtn: object = []
	file_object: object = open(file, "r")
	# file_object: object = open(file, "r", encoding='utf-8')
	# file_object: object = open(file, encoding='utf-8')
	rtn: object = file_object.read().splitlines()
	file_object.close()
	return list(filter(None, pd.unique(rtn).tolist())) # Remove Empty/Duplicates Values

def name_generator(language, legitimacy):
	"""Creates a random name

	Args:
		language (str): Determines wether the name generated is taken from the list of most common names of Mexico or USA
		legitimacy (str): Allows you to generate names more credible or names more likely to be available for registration(e.g: the availabilty option adds numbers at the end)

	Returns:
		str: a name
	"""
	bot_name = []
	first_name = []
	surname = []
	CASES = ("uc", "lc", "c") 
	START = ("Xx", "xX", "the", "The")
	FINISH = ("xX", "Xx", "pro", "Pro", "gamer", "Gamer", "123", "1234", )
	# Indexes 0 and 1 are paired, e.g: if a name starts with START[0] it has to end with FINISH[0]
	NUMS = ("0", "1", "3", "4", "5", "6", "7", "8", "9")
	case = random.choice(CASES) # Makes the casing of the name random
	# Start (sometimes adds a prefix)
	r = random.randint(1, 5)
	if legitimacy == "av": 
		r = 1

	if r == 1 or 2 or 3:
		start = random.choice(START)
		finish_index = START.index(start)
	# Concatenates the name itself
	if language == "mx":
		names_male_mx: object = file_to_list('namesMaleMX.txt')
		names_female_mx: object = file_to_list('namesFemaleMX.txt')
		surnames_mx: object = file_to_list('surnamesMX.txt')
		nouns_mx: object = file_to_list('nounsMX.txt')
		r2 = random.randint(1, 2) # Chooses from the female or Male MX common nammes
		r2b = random.randint(1, 4) # Sometimes chooses a "surname" from a noun list rather than a surname list
		if legitimacy == "cr": # If the user chooses the credibility option it will always pick a surname form the surname list, not the nouns one
			r2b = 1
		if r2 == 1:
			first_name = random.choice(names_male_mx)

		elif r2 == 2:
			first_name = random.choice(names_female_mx)

		if r2b == 1 or 2 or 3:
			surname = random.choice(surnames_mx)
		
		elif r2b == 4:
			surname = random.choice(nouns_mx)

	
	elif language == "en":
		names_us: object = file_to_list('namesUS.txt')
		surnames_us: object = file_to_list('surnamesMX.txt')
		nouns: object = file_to_list('nouns.txt') 
		first_name = random.choice(names_us)
		r6 = random.randint(1, 4) # Sometimes chooses a "surname" from a noun list rather than a surname list
		if legitimacy == "cr": # If the user chooses the credibility option it will always pick a surname form the surname list, not the nouns one
			r6 = 1

		if r6 == 1 or 2 or 3: 
			surname = random.choice(surnames_us)

		if r6 == 4:
			surname = random.choice(nouns)

	# Cases the name and surname
	for i in range(len(first_name)):
		first_name[i] = first_name[i].strip()
		if case == "uc":
			first_name[i] = first_name[i].upper()
		
		elif case == "lc":
			first_name[i] = first_name[i].lower()

		elif case == "c":
			first_name[i] = first_name[i].capitalize()

	i = 0	
	for i in range(len(surname)):
		surname[i] = surname[i].strip()
		if case == "uc":
			surname[i] = surname[i].upper()
			
		elif case == "lc":
			surname[i] =surname[i].lower()

		elif case == "c":
			surname[i] = surname[i].capitalize()

	r3 = random.randint(1, 2) # Determines which is going first (name or surname)
	r4 = random.randint(1, 4) # Determines if a suffix is added
	if legitimacy == "av": # If te user chooses the "availability" option it always add numbers in the end (in a wider length that if the user chooses "credibility" and the number option is choosen randomly)
		r4 = 3

	if r3 == 1:
		bot_name.append(surname)
		bot_name.append(first_name)
	elif r3 == 2:
		bot_name.append(surname)
		bot_name.append(first_name)
	# Finish (sometimes adds a suffix)
	if r == 1 and finish_index > 1: # Adds the other pair of the start choice
		finish = FINISH[finish_index]
		bot_name.append(finish)
	
	elif r4 == 1 or 2: # Adds a common suffix (also biases the random generator to make this option more frequent)
		finishIndex = random.randint(2, 7)
		finish = FINISH[finish_index]
		bot_name.append(finish)
	
	elif r4 == 3: # Adds a random combination of numbers to the name
		finish = ""
		if legitimacy == "av": # If the user chooses the "availability" option it will make the number of the suffix >= 4 digits long
			length = random.randint(4, 7)
		
		elif legitimacy == "cr": # If the user chooses the "credibility" option it will make the number of the suffix <= 4
			length = random.randint(1, 4)

		for i in range(length):
			finish.append(random.choice(NUMS))

		bot_name.append(finish)

	bot_name = "".join(map(str, bot_name))
	return bot_name
			

def run():
	print("Welcome to Bot Name Generator Project") 
	advanced_config = str(input("Do you want to do some advanced configuration? Just type y/n (yes or no) "))
	if advanced_config == "y":
		language = str(input("From which country do you want your name to be? (type mx for Mexico or us for United States)"))
		ammount = int(input("How many bot names do you want to generate? (just type an int number (eg: 5))"))
		legitimacy = str(input("Do you want your name to be more credible or more likely to be available (for registration in 3rd party apps)? | (type cr for credible and av for available)"))


	elif advanced_config == "n":
		language = "r" #random, using "r" as a template to declare random variables from now on
		ammount = 1
		legitimacy = "cr"
	
	if ammount == 1:
		print("Your bot name is:")
		bot_name = name_generator(language, legitimacy)
	else:
		print("Your bots names are:")
		for i in range(ammount):
			name = name_generator(language, legitimacy)
			print(name)

if __name__ == "__main__":
	run()