def reset(target):
	str(target)
	reset = '\033[0;0m'
	result = reset + target
	return result

def invert(target):
	str(target)
	reset = '\033[0;0m'
	result = '\033[;7m' + target + reset
	return result

def invertAll(target):
	str(target)
	result = '\033[;7m' + target
	return result

def font(target, mode):
	str(target)
	reset = '\033[0;0m'
	
	if mode == 'b':
		result = '\033[;1m' + target + reset
	elif mode == 'white':
		result = '\033[1;97m' + target + reset
	elif mode == 'black':
		result = '\033[1;30m' + target + reset
	elif mode == 'red':
		result = '\033[1;31m' + target + reset
	elif mode == 'light-red':
		result = '\033[1;91m' + target + reset
	elif mode == 'green':
		result = '\033[1;32m' + target + reset
	elif mode == 'light-green':
		result = '\033[1;92m' + target + reset
	elif mode == 'yellow':
		result = '\033[1;33m' + target + reset
	elif mode == 'light-yellow':
		result = '\033[1;93m' + target + reset
	elif mode == 'blue':
		result = '\033[1;34m' + target + reset
	elif mode == 'light-blue':
		result = '\033[1;94m' + target + reset
	elif mode == 'pink':
		result = '\033[1;35m' + target + reset
	elif mode == 'light-pink':
		result = '\033[1;95m' + target + reset
	elif mode == 'cyan':
		result = '\033[1;36m' + target + reset
	elif mode == 'light-cyan':
		result = '\033[1;96m' + target + reset
	elif mode == 'gray':
		result = '\033[1;90m' + target + reset
	elif mode == 'light-gray':
		result = '\033[1;37m' + target + reset
		
	return result
	
def allFont(target, mode):
	str(target)
	
	if mode == 'b':
		result = '\033[;1m' + target
	elif mode == 'white':
		result = '\033[1;97m' + target
	elif mode == 'black':
		result = '\033[1;30m' + target
	elif mode == 'red':
		result = '\033[1;31m' + target
	elif mode == 'light-red':
		result = '\033[1;91m' + target
	elif mode == 'green':
		result = '\033[1;32m' + target
	elif mode == 'light-green':
		result = '\033[1;92m' + target
	elif mode == 'yellow':
		result = '\033[1;33m' + target
	elif mode == 'light-yellow':
		result = '\033[1;93m' + target
	elif mode == 'blue':
		result = '\033[1;34m' + target
	elif mode == 'light-blue':
		result = '\033[1;94m' + target
	elif mode == 'pink':
		result = '\033[1;35m' + target
	elif mode == 'light-pink':
		result = '\033[1;95m' + target
	elif mode == 'cyan':
		result = '\033[1;36m' + target
	elif mode == 'light-cyan':
		result = '\033[1;96m' + target
	elif mode == 'gray':
		result = '\033[1;90m' + target
	elif mode == 'light-gray':
		result = '\033[1;37m' + target
		
	return result
	
def background(target, mode):
	str(target)
	reset = '\033[0;0m'
	
	if mode == 'white':
		result = '\033[1;107m' + target + reset
	elif mode == 'black':
		result = '\033[1;40m' + target + reset
	elif mode == 'red':
		result = '\033[1;41m' + target + reset
	elif mode == 'light-red':
		result = '\033[1;101m' + target + reset
	elif mode == 'green':
		result = '\033[1;42m' + target + reset
	elif mode == 'light-green':
		result = '\033[1;102m' + target + reset
	elif mode == 'yellow':
		result = '\033[1;43m' + target + reset
	elif mode == 'light-yellow':
		result = '\033[1;103m' + target + reset
	elif mode == 'blue':
		result = '\033[1;44m' + target + reset
	elif mode == 'light-blue':
		result = '\033[1;104m' + target + reset
	elif mode == 'pink':
		result = '\033[1;45m' + target + reset
	elif mode == 'light-pink':
		result = '\033[1;105m' + target + reset
	elif mode == 'cyan':
		result = '\033[1;46m' + target + reset
	elif mode == 'light-cyan':
		result = '\033[1;106m' + target + reset
	elif mode == 'gray':
		result = '\033[1;100m' + target + reset
	elif mode == 'light-gray':
		result = '\033[1;47m' + target + reset
	
	return result
	
def allBackground(target, mode):
	str(target)
	
	if mode == 'white':
		result = '\033[1;107m' + target
	elif mode == 'black':
		result = '\033[1;40m' + target
	elif mode == 'red':
		result = '\033[1;41m' + target
	elif mode == 'light-red':
		result = '\033[1;101m' + target
	elif mode == 'green':
		result = '\033[1;42m' + target
	elif mode == 'light-green':
		result = '\033[1;102m' + target
	elif mode == 'yellow':
		result = '\033[1;43m' + target
	elif mode == 'light-yellow':
		result = '\033[1;103m' + target
	elif mode == 'blue':
		result = '\033[1;44m' + target
	elif mode == 'light-blue':
		result = '\033[1;104m' + target
	elif mode == 'pink':
		result = '\033[1;45m' + target
	elif mode == 'light-pink':
		result = '\033[1;105m' + target
	elif mode == 'cyan':
		result = '\033[1;46m' + target
	elif mode == 'light-cyan':
		result = '\033[1;106m' + target
	elif mode == 'gray':
		result = '\033[1;100m' + target
	elif mode == 'light-gray':
		result = '\033[1;47m' + target
	
	return result
