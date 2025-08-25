def module():
	print("Je suis un module")

def module2():
	print("Je ne suis pas un module")

if __name__ == "__module__":
	print("Mon script est exécuté directement")
else:
	print("Mon script est importé par un autre module")
