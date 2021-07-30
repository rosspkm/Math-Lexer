from dataclasses import dataclass

# stores values of the number
@dataclass
class NumberNode:
	value: any

	def __repr__(self):
		return f"{self.value}"

# adding 2 nodes together
@dataclass
class AddNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}+{self.node_b})"

# subtracting 2 nodes together
@dataclass
class SubtractNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}-{self.node_b})"

# multiplying 2 nodes together
@dataclass
class MultiplyNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}*{self.node_b})"

# dividing 2 nodes
@dataclass
class DivideNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}/{self.node_b})"


# for positive numbers have to have it
@dataclass
class PlusNode:
	node: any

	def __repr__(self):
		return f"(+{self.node})"

# for a negative value
@dataclass
class MinusNode:
	node: any

	def __repr__(self):
		return f"(-{self.node})"
