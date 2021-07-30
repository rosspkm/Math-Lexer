from lib.tokens import TokenType
from src.nodes import *

# reason this is called parser_ is cause there is a built in parser opperator and didnt want to interfere

# transforms tokens into nodes 

class Parser:
    # takes in tokens we are parsing
	def __init__(self, tokens):
		self.tokens = iter(tokens)
		self.advance()

	# exception for invalid error
	def raise_error(self):
		raise Exception("Invalid syntax")
	
	# advances through characters
	def advance(self):
		try:
			self.current_token = next(self.tokens)
		except StopIteration:
			self.current_token = None

	# entry into parser
	def parse(self):
		if self.current_token == None:
			return None

		result = self.expr()

		if self.current_token != None:
			self.raise_error()

		return result

	# define expressions add and subtract
	def expr(self):
		result = self.term()

		while self.current_token != None and self.current_token.type in (TokenType.ADD_OP, TokenType.SUB_OP):
			if self.current_token.type == TokenType.ADD_OP:
				self.advance()
				result = AddNode(result, self.term())
			elif self.current_token.type == TokenType.SUB_OP:
				self.advance()
				result = SubtractNode(result, self.term())

		return result

	# define expressions multiply and divide
	def term(self):
		result = self.factor()

		while self.current_token != None and self.current_token.type in (TokenType.MULT_OP, TokenType.DIV_OP):
			if self.current_token.type == TokenType.MULT_OP:
				self.advance()
				result = MultiplyNode(result, self.factor())
			elif self.current_token.type == TokenType.DIV_OP:
				self.advance()
				result = DivideNode(result, self.factor())
				
		return result

	def factor(self):
		token = self.current_token

		# adds acceptance for left paranthesis and is evaluated first
		if token.type == TokenType.LEFT_PAREN:
			self.advance()
			result = self.expr()

			# checks for right parenthesis after left
			if self.current_token.type != TokenType.RIGHT_PAREN:
				self.raise_error()
			
			self.advance()
			return result

		# allows numbers
		elif token.type == TokenType.DIGIT:
			self.advance()
			return NumberNode(token.value)

		# allows a + node in front of a value
		elif token.type == TokenType.ADD_OP:
			self.advance()
			return PlusNode(self.factor())
		
		# allows negative numbers
		elif token.type == TokenType.SUB_OP:
			self.advance()
			return MinusNode(self.factor())
		
		self.raise_error()
