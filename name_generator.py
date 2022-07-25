import random
import pandas as pd

def file_to_list(file):
    rtn: object = []
    file_object: object = open(file, "r")
    rtn: object = file_object.read().splitlines()
    file_object.close()
    return list(filter(None, pd.unique(rtn).tolist())) # Remove Empty/Duplicates Values

def name_generator(nouns, amount_words, spaces, case):
	password = []
	CHARS = ('*', '+', '-', '/', '_', '!', ',', ';', '.', '>', '<', '~', '&')
	CASES = ("uc", "lc", "c")
	char = " "

	if spaces == "y":
		char = random.choice(CHARS)
	
	if case == "r":
		case = random.choice(CASES)

	for i in range(amount_words):
		word = random.choice(nouns)
		password.append(word)
		if i != amount_words - 1:
			password.append(char)
		
	for i in range(len(password)):
		if case == "uc":
			password[i] = password[i].upper()
		
		elif case == "lc":
			password[i] = password[i].lower()

		elif case == "c":
			password[i] = password[i].capitalize()

	password = "".join(map(str, password))
	return password
			

def run():
	nouns: object = file_to_list('nouns.txt') 
	names_male_mx: object = file_to_list('namesMaleMX.txt')
	names_female_mx: object = file_to_list('namesFemaleMX.txt')
	names_us: object = file_to_list('namesUS.txt')
	surnames_mx: object = file_to_list('surnamesMX.txt')
	surnames_us: object = file_to_list('surnamesMX.txt')
	print("Welcome to Bot Name Generator Project") 
	advanced_config = str(input("Do you want to do some advanced configuration? Just type y/n (yes or no) "))
	if advanced_config == "y":
		language = str(input("From which country do you want your name to be? (type mx for Mexico or us for United States)"))
		ammount = int(input("How many bot names do you want to generate? (just type an int number (eg: 5))"))


	elif advanced_config == "n":
		language = "r" #random
		ammount = 1
	
	if ammount == 1:
		print("Your bot name is:")
		bot_name = name_generator(language)
	else:
		print("Your bots names are:")
		for i in range(ammount):
			name = name_generator(language)
			print(name)

if __name__ == "__main__":
	run()