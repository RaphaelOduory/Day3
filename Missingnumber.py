def find_missing(lista,listb):
  #initializes a place holder for the missing variable
	absent = 0
	#returns missing number if list a is shorter than list b in terms of lenght
	if len(lista) < len(listb):
		miss = (set(listb) - set(lista))
		absent = miss.pop()
		return absent
	#returns missing number if list b is shorter than list a in terms of lenght
	if len(listb) < len(lista):
		miss = (set(lista) - set(listb))
		absent = miss.pop()
		return absent
	#default statement
	else:
	  return 0