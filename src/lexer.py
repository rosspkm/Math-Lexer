from lib.tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '0123456789'

class Lexer:
	# takes in text that it is processing
	def __init__(self, text):
		self.text = iter(text)
		self.advance()

	# keeps track of current character/where it is in the text
	def advance(self):
		try:
			self.current_char = next(self.text)
		except StopIteration: # detects end of input
			self.current_char = None

	# generates tokens from input text
	def generate_tokens(self):
		while self.current_char != None:
			if self.current_char in WHITESPACE:
				self.advance()
			elif self.current_char == '.' or self.current_char in DIGITS:
				yield self.generate_number()

			# generate tokens for symbols
			elif self.current_char == '+':
				print(f"Next token is: {TokenType.ADD_OP.value}, Next lexeme is {self.current_char}")
				self.advance()
				yield Token(TokenType.ADD_OP)
			elif self.current_char == '-':
				print(f"Next token is: {TokenType.SUB_OP.value}, Next lexeme is {self.current_char}")
				self.advance()
				yield Token(TokenType.SUB_OP)
			elif self.current_char == '*':
				print(f"Next token is: {TokenType.MULT_OP.value}, Next lexeme is {self.current_char}")
				self.advance()
				yield Token(TokenType.MULT_OP)
			elif self.current_char == '/':
				print(f"Next token is: {TokenType.DIV_OP.value}, Next lexeme is {self.current_char}")
				self.advance()
				yield Token(TokenType.DIV_OP)
			elif self.current_char == '(':
				print(f"Next token is: {TokenType.LEFT_PAREN.value}, Next lexeme is {self.current_char}")
				self.advance()
				yield Token(TokenType.LEFT_PAREN)
			elif self.current_char == ')':
				print(f"Next token is: {TokenType.RIGHT_PAREN.value}, Next lexeme is {self.current_char}")
				self.advance()
				yield Token(TokenType.RIGHT_PAREN)

				# if we come across a token we dont understand
			else:
				print(f"Next token is: {TokenType.UNKNOWN.value}, Illegal character '{self.current_char}'")
				self.advance()

	# builds the character into a digit    
	def generate_number(self):
		decimal_point_count = 0
		number_str = self.current_char
		self.advance()

		# this loops though to make sure that the value is accepted
		while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
			if self.current_char == '.':
				decimal_point_count += 1

				# if more then 1 decimal break out of loop and thats the end of the token
				if decimal_point_count > 1:
					break
			
			number_str += self.current_char
			self.advance()

		# add a 0 if its missing it before or after the decimal point
		if number_str.startswith('.'):
			number_str = '0' + number_str
		if number_str.endswith('.'):
			number_str += '0'
		
		# checks if number_str has a decimal if yes, float if no, int
		print(f"Next token is: {TokenType.DIGIT.value}, Next lexeme is {number_str}")
		if '.' in number_str:
			return Token(TokenType.DIGIT, float(number_str)) #return token as a float
		else:
			return Token(TokenType.DIGIT, int(number_str)) #return token as a float
