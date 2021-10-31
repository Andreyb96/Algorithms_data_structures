FIND = 'find'
DEL = 'del'
ADD =  'add'

phoneBook = {}

n = int(input())
for i in range(n):
	s = input().split()
	operation = s[0]
	number = s[1]
	if len(s) > 2:
		name = s[2]

	if operation == ADD:
		phoneBook[number] = name
	elif operation == DEL:
		if phoneBook.get(number):
			phoneBook.pop(number)
	elif operation == FIND and phoneBook.get(number):
		print(phoneBook[number])
	else:
		print('not found')