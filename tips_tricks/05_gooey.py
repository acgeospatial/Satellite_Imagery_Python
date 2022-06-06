import argparse
from gooey import Gooey

@Gooey
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-n", "--name", help="What is your name", action="store", required=True)
	args = parser.parse_args()

	print("you entered: ", args.name)
	

if __name__ == '__main__':
    main()