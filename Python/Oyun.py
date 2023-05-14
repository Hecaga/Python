name = input("Adınızı daxil edin: ")
print("Salam " + name + " Oyun vaxtıdır!")

secret_word = "Salam"

guess_string = ""

lives = 10

while lives > 0:

	character_left = 0

	for character in secret_word:

		if character in guess_string:

			print(character)
		else:
			print("-")
			character_left += 1

	if character_left == 0:
		print("Siz qalibsiniz!!!")	
		break


	guess = input("Bir hərf yazın: ")
	guess_string += guess

	if guess not in secret_word:
		lives -= 1
		print("Yanlış!")
		print(f"Sizin {lives} canınız qaldı")

		if lives == 0:
			print("Siz məğlub oldunuz!")

