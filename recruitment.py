def main():
	skills=["Python","C#","React","Bootstrap","JavaScript","CSS"]
	cv={}
	print("Welcome to the special recruitment program, please answer the following questions:")
	cv["name"]=input("What'your name?")
	cv["age"]=int(input("How old are you?"))
	cv["experience"]=int(input("How many years of experience do you have?"))
	cv["skills"]=[]
	print("Skills:")
	for index, skill in enumerate(skills, start=1):
		print (index,". ",skill)
	cv["skills"]=[int(input("Choose a skill from above by entering its number:"))]
	cv["skills"].extend([int(input("Choose another skill from above by entering its number:"))])
	if(6 in cv["skills"]):
		if(cv["age"]>=25 and cv["age"]<40 and cv["experience"]>5):
			print("You have been accepted")
		else:
			print("You have been rejected")

	else:
		print("You have been rejected")



	#write your code here

if __name__ == '__main__':
	main()
