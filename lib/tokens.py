from enum import Enum
from dataclasses import dataclass

# different token types in the simple calculator
class TokenType(Enum):
	UNKNOWN 	= 99
	DIGIT    	= 1
	ADD_OP      = 21
	SUB_OP     	= 22
	MULT_OP  	= 23
	DIV_OP    	= 24
	LEFT_PAREN  = 25
	RIGHT_PAREN = 26

# define what a token actually is
@dataclass
class Token:
	type: TokenType
	value: any = None # default value if it doesnt have a value

	def __repr__(self):
		return self.type.name + (f":{self.value}" if self.value != None else "")
