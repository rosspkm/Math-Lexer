from src.nodes import *
from lib.values import Number

class Interpreter:
	def __init__(self):
		pass
	
	# takes in a root node of a tree and it will process tree and return a number 
	def visit(self, node):
		method_name = f'visit_{type(node).__name__}' # makes the method name from the node to call
		method = getattr(self, method_name)
		return method(node) # calls method
	
	# translate the node to the number
	def visit_NumberNode(self, node):
		return Number(node.value)

	# translate the nodes to numbers and adds them together
	def visit_AddNode(self, node):
		return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

	# translate the nodes to numbers and subtracts them
	def visit_SubtractNode(self, node):
		return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

	# translate the nodes to numbers and multiplys them
	def visit_MultiplyNode(self, node):
		return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

	# translate the nodes to numbers and divides them
	def visit_DivideNode(self, node):
		try:
			return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
		except:
			# catch if illegal math rule
			raise Exception("Runtime math error")

	# translates a plus in front of a node to a positive
	def visit_PlusNode(self, node):
    		return self.visit(node.node)
	
	# translates a - infront of a node to a negative
	def visit_MinusNode(self, node):
    		return self.visit(node.node)
