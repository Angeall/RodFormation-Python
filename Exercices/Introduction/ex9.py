def belongs_to_dictionary():
	word = input("Entrez un mot : ")
	while not word_in_file(word):
		word = input("Entrez un mot : ")
	return word

def word_in_file(word):
	f = open("dico.txt", 'r')
	for line in f:
		if line.strip() == word:
			return True
	return False

def uncover(s1, s2, x):
	new_word = ""
	for i in range(len(s1)):
		if s1[i] == x:
			new_word+=s1[i]
		else:
			new_word+=s2[i]
	return new_word

def is_one_letter(chaine):
	if type(chaine) == str and len(chaine) == 1 and chaine.isalpha():
		return True
	else: 
		return False






















def pendu():
	trialsLeft = 10

	lettersTried = ""

	chosenWord = belongs_to_dictionary()

	hiddenWord = '*' * len(chosenWord)

	inputLetter = ""

	while not(trialsLeft == 0 or hiddenWord == chosenWord):
		print("Mot : " + hiddenWord + "\nEssais restants : " + \
			str(trialsLeft) + "\nLettres essayees : " + lettersTried + "\n")
		
		while inputLetter in lettersTried or not(is_one_letter(inputLetter)):
			inputLetter = input("Entrez une lettre : ")
		lettersTried += inputLetter
		if not inputLetter in chosenWord:
			trialsLeft -= 1
		else:
			hiddenWord = uncover(chosenWord,hiddenWord,inputLetter)

	if hiddenWord == chosenWord:
		print("Vous avez gagne")
	else:
		print("Vous avez perdu")

if __name__ == "__main__": 
	pendu()
