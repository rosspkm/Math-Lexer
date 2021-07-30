from dataclasses import dataclass

# holds different value types that the interpreter is able to produce
# being a number
@dataclass
class Number:
	value: any
	
	def __repr__(self):
		return f"{self.value}"
