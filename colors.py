def reset(target):
	str(target)
	reset = '\033[0;0m'
	result = reset + target
	return result

def resetAfter(target):
	str(target)
	reset = '\033[0;0m'
	result = target + reset
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
	else :
		result = ""
		print('\033[1;31m' + "Mode Error!!" + '\033[0;0m')
		
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
	else :
		result = ""
		print('\033[1;31m' + "Mode Error!!" + '\033[0;0m')
		
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
	else :
		result = ""
		print('\033[1;31m' + "Mode Error!!" + '\033[0;0m')
		
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
	else :
		result = ""
		print('\033[1;31m' + "Mode Error!!" + '\033[0;0m')
		
	return result

def backModeAjust(target, color, backMode):
	reset =  '\033[0;0m'
	
	if backMode == 'white':
		result = color + '\033[1;107m' + target + reset
	elif backMode == 'black':
		result = color + '\033[1;40m' + target + reset
	elif backMode == 'red':
		result = color + '\033[1;41m' + target + reset
	elif backMode == 'light-red':
		result = color + '\033[1;101m' + target + reset
	elif backMode == 'green':
		result = color + '\033[1;42m' + target + reset
	elif backMode == 'light-green':
		result = color + '\033[1;102m' + target + reset
	elif backMode == 'yellow':
		result = color + '\033[1;43m' + target + reset
	elif backMode == 'light-yellow':
		result = color + '\033[1;103m' + target + reset
	elif backMode == 'blue':
		result = color + '\033[1;44m' + target + reset
	elif backMode == 'light-blue':
		result = color + '\033[1;104m' + target + reset
	elif backMode == 'pink':
		result = color + '\033[1;45m' + target + reset
	elif backMode == 'light-pink':
		result = color + '\033[1;105m' + target + reset
	elif backMode == 'cyan':
		result = color + '\033[1;46m' + target + reset
	elif backMode == 'light-cyan':
		result = color + '\033[1;106m' + target + reset
	elif backMode == 'gray':
		result = color + '\033[1;100m' + target + reset
	elif backMode == 'light-gray':
		result = color + '\033[1;47m' + target + reset
	else :
		result = ""
		print('\033[1;31m' + "Mode Error!!" + '\033[0;0m')

	return result
	
def fontBack(target, fontMode, backMode):
	str(target)
	
	if fontMode == 'b':
		result = backModeAjust(target, '\033[;1m', backMode)
	elif fontMode == 'white':
		result = backModeAjust(target, '\033[1;97m', backMode)
	elif fontMode == 'black':
		result = backModeAjust(target, '\033[1;30m', backMode)
	elif fontMode == 'red':
		result = backModeAjust(target, '\033[1;31m', backMode)
	elif fontMode == 'light-red':
		result = backModeAjust(target ,'\033[1;91m', backMode)
	elif fontMode == 'green':
		result = backModeAjust(target, '\033[1;32m', backMode)
	elif fontMode == 'light-green':
		result = backModeAjust(target, '\033[1;92m', backMode)
	elif fontMode == 'yellow':
		result = backModeAjust(target, '\033[1;33m', backMode)
	elif fontMode == 'light-yellow':
		result = backModeAjust(target, '\033[1;93m', backMode)
	elif fontMode == 'blue':
		result = backModeAjust(target, '\033[1;34m', backMode)
	elif fontMode == 'blue':
		result = backModeAjust(target, '\033[1;94m', backMode)
	elif fontMode == 'pink':
		result = backModeAjust(target, '\033[1;35m', backMode)
	elif fontMode == 'light-pink':
		result = backModeAjust(target, '\033[1;95m', backMode)
	elif fontMode == 'cyan':
		result = backModeAjust(target, '\033[1;36m', backMode)
	elif fontMode == 'light-cyan':
		result = backModeAjust(target, '\033[1;96m', backMode)
	elif fontMode == 'gray':
		result = backModeAjust(target, '\033[1;90m', backMode)
	elif fontMode == 'light-gray':
		result = backModeAjust(target, '\033[1;37m', backMode)
	else :
		result = ""
		print('\033[1;31m' + "Mode Error!!" + '\033[0;0m')
	
	return result
	
def backModeAllAjust(target, color, backMode):
	if backMode == 'white':
		result = color + '\033[1;107m' + target
	elif backMode == 'black':
		result = color + '\033[1;40m' + target
	elif backMode == 'red':
		result = color + '\033[1;41m' + target
	elif backMode == 'light-red':
		result = color + '\033[1;101m' + target
	elif backMode == 'green':
		result = color + '\033[1;42m' + target
	elif backMode == 'light-green':
		result = color + '\033[1;102m' + target
	elif backMode == 'yellow':
		result = color + '\033[1;43m' + target
	elif backMode == 'light-yellow':
		result = color + '\033[1;103m' + target
	elif backMode == 'blue':
		result = color + '\033[1;44m' + target
	elif backMode == 'light-blue':
		result = color + '\033[1;104m' + target
	elif backMode == 'pink':
		result = color + '\033[1;45m' + target
	elif backMode == 'light-pink':
		result = color + '\033[1;105m' + target
	elif backMode == 'cyan':
		result = color + '\033[1;46m' + target
	elif backMode == 'light-cyan':
		result = color + '\033[1;106m' + target
	elif backMode == 'gray':
		result = color + '\033[1;100m' + target
	elif backMode == 'light-gray':
		result = color + '\033[1;47m' + target
	else :
		result = ""
		print('\033[1;31m' + "Mode Error!!" + '\033[0;0m')

	return result
	
def fontBackAll(target, fontMode, backMode):
	str(target)
	
	if fontMode == 'b':
		result = backModeAllAjust(target, '\033[;1m', backMode)
	elif fontMode == 'white':
		result = backModeAllAjust(target, '\033[1;97m', backMode)
	elif fontMode == 'black':
		result = backModeAllAjust(target, '\033[1;30m', backMode)
	elif fontMode == 'red':
		result = backModeAllAjust(target, '\033[1;31m', backMode)
	elif fontMode == 'light-red':
		result = backModeAllAjust(target ,'\033[1;91m', backMode)
	elif fontMode == 'green':
		result = backModeAllAjust(target, '\033[1;32m', backMode)
	elif fontMode == 'light-green':
		result = backModeAllAjust(target, '\033[1;92m', backMode)
	elif fontMode == 'yellow':
		result = backModeAllAjust(target, '\033[1;33m', backMode)
	elif fontMode == 'light-yellow':
		result = backModeAllAjust(target, '\033[1;93m', backMode)
	elif fontMode == 'blue':
		result = backModeAllAjust(target, '\033[1;34m', backMode)
	elif fontMode == 'blue':
		result = backModeAllAjust(target, '\033[1;94m', backMode)
	elif fontMode == 'pink':
		result = backModeAllAjust(target, '\033[1;35m', backMode)
	elif fontMode == 'light-pink':
		result = backModeAllAjust(target, '\033[1;95m', backMode)
	elif fontMode == 'cyan':
		result = backModeAllAjust(target, '\033[1;36m', backMode)
	elif fontMode == 'light-cyan':
		result = backModeAllAjust(target, '\033[1;96m', backMode)
	elif fontMode == 'gray':
		result = backModeAllAjust(target, '\033[1;90m', backMode)
	elif fontMode == 'light-gray':
		result = backModeAllAjust(target, '\033[1;37m', backMode)
	else :
		result = ""
		print('\033[1;31m' + "Mode Error!!" + '\033[0;0m')
		
	return result
