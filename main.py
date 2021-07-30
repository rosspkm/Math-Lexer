from src.lexer import Lexer
from src.parser_ import Parser
from src.interpreter import Interpreter
import os


# read from front.in file
with open("./input/front.txt", "r") as file:
# if file is empty accept console output
	if os.stat("./input/front.txt").st_size == 0:
		while True:
			try:
				text = input("calc > ")
				lexer = Lexer(text)
				tokens = lexer.generate_tokens()
				parser = Parser(tokens)
				tree = parser.parse()
		
				if not tree: 
					continue
				interpreter = Interpreter()
				value = interpreter.visit(tree)
				print(f"Answer is {value}")
			except Exception as e:
				print(e)

	else:
		# loop through file line by line
		for line in file:
			text = line
			try:
				lexer = Lexer(text)
				tokens = lexer.generate_tokens()
				parser = Parser(tokens)
				tree = parser.parse()
				if not tree: 
					continue
				
				interpreter = Interpreter()
				value = interpreter.visit(tree)
				print(f"Answer is {value}")	
			except Exception as e:
				print(e)
