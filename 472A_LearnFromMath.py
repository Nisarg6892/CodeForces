# n = int(raw_input())

# def Check_Composite(number) :

# 	Found_Composite = 0

# 	for x in range(2,number/2+1) :

# 		if number % x == 0 :

# 			Found_Composite = 1
# 			break

# 	return Found_Composite

# def Calculation(a, b) :

# 	c = 0

# 	if a % 2 != 0 :

# 		c = Check_Composite(a)

# 	else :

# 		c = Check_Composite(b)

# 	return c


# def Print_Answer(a, b) :

# 	print str(a)+' '+str(b)

# a = n/2
# b = n - a

# while True :

# 	if n % 2 == 0 :

# 		if Check_Composite(a) == 1 :
		
# 			Print_Answer(a, b)
# 			break

# 		else :

# 			c = Calculation(a, b)

# 			if c != 1 :

# 				a = a + 1
# 				b = b - 1

# 			else :

# 				Print_Answer(a,b)
# 				break

# 	else :

# 		c = Calculation(a, b)

# 		if c != 1 :

# 			a = a + 1
# 			b = b - 1

# 		else :

# 			Print_Answer(a,b)
# 			break

n = input()

if n % 2 == 0 :

	a = 4

else :

	a = 9

print a, n-a