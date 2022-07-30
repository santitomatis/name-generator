import random
import pandas as pd

def file_to_list(file):
    rtn: object = []
    file_object: object = open(file, "r", encoding="utf8", errors='ignore')
    rtn: object = file_object.read().splitlines()
    file_object.close()
    return list(filter(None, pd.unique(rtn).tolist())) # Remove Empty/Duplicates Values

def print_lists():
    names_male: object = file_to_list('namesMaleMX.txt') 	
    names_us: object = file_to_list('namesUS.txt') 	
    nouns_mx: object = file_to_list('nounsMX.txt')
    surnames_mx: object = file_to_list('surnamesMX.txt') 
    for i in range(len(names_male)):
        print(names_male[i])
    
    print("---------------------------------------------------------------")

    for i in range(15):
        print(names_us[i])
    
    print("---------------------------------------------------------------")

    for i in range(15):
        print(nouns_mx[i])


    # for i in range(1):
    #     print(random.choice(names_male))
    #     print(random.choice(names_us))
    #     print(random.choice(nouns_mx))
    #     print(random.choice(surnames_mx))	 	

def run():
	print_lists()
	
if __name__ == "__main__":
	run()