def invert(target):
	str(target)
	reset = '\033[0;0m'
	result = '\033[;7m' + target + reset
	return result

def font(target, colorId):
	str(target)
	reset = '\033[0;0m'
	
	if colorId == 'b':
		result = '\033[;1m' + target + reset
	elif colorId == 'white':
		result = '\033[1;97m' + target + reset
	elif colorId == 'black':
		result = '\033[1;30m' + target + reset
	elif colorId == 'red':
		result = '\033[1;31m' + target + reset
	elif colorId == 'light-red':
		result = '\033[1;91m' + target + reset
	elif colorId == 'green':
		result = '\033[1;32m' + target + reset
	elif colorId == 'light-green':
		result = '\033[1;92m' + target + reset
	elif colorId == 'yellow':
		result = '\033[1;33m' + target + reset
	elif colorId == 'light-yellow':
		result = '\033[1;93m' + target + reset
	elif colorId == 'blue':
		result = '\033[1;34m' + target + reset
	elif colorId == 'light-blue':
		result = '\033[1;94m' + target + reset
	elif colorId == 'pink':
		result = '\033[1;35m' + target + reset
	elif colorId == 'light-pink':
		result = '\033[1;95m' + target + reset
	elif colorId == 'cyan':
		result = '\033[1;36m' + target + reset
	elif colorId == 'light-cyan':
		result = '\033[1;96m' + target + reset
	elif colorId == 'gray':
		result = '\033[1;90m' + target + reset
	elif colorId == 'light-gray':
		result = '\033[1;37m' + target + reset
		
	return result
	
def background(target, colorId):
	str(target)
	reset = '\033[0;0m'
	
	if colorId == 'white':
		result = '\033[1;107m' + target + reset
	elif colorId == 'black':
		result = '\033[1;40m' + target + reset
	elif colorId == 'red':
		result = '\033[1;41m' + target + reset
	elif colorId == 'light-red':
		result = '\033[1;101m' + target + reset
	elif colorId == 'green':
		result = '\033[1;42m' + target + reset
	elif colorId == 'light-green':
		result = '\033[1;102m' + target + reset
	elif colorId == 'yellow':
		result = '\033[1;43m' + target + reset
	elif colorId == 'light-yellow':
		result = '\033[1;103m' + target + reset
	elif colorId == 'blue':
		result = '\033[1;44m' + target + reset
	elif colorId == 'light-blue':
		result = '\033[1;104m' + target + reset
	elif colorId == 'pink':
		result = '\033[1;45m' + target + reset
	elif colorId == 'light-pink':
		result = '\033[1;105m' + target + reset
	elif colorId == 'cyan':
		result = '\033[1;46m' + target + reset
	elif colorId == 'light-cyan':
		result = '\033[1;106m' + target + reset
	elif colorId == 'gray':
		result = '\033[1;100m' + target + reset
	elif colorId == 'light-gray':
		result = '\033[1;47m' + target + reset
	
	return result