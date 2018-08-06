mx=0
class Tree(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def add_l(self, data):
		self.left = Tree(data)
		return (self.left)

	def add_r(self, data):
		self.right = Tree(data)
		return (self.right)

	def add_2(self, l, r):
		self.left = Tree(l)
		self.right = Tree(r)
		return (self.left, self.right)
	def is_leaf(self):
		return(self.left is None and self.right is None)
	def printer(self):
		if self.is_leaf():
			print ("it's a leaf")
		print (self.data)
		if (self.left):
			print ("left->")
			self.left.printer()
		if (self.right):
			print ("right->")
			self.right.printer()
		print ("level up")
	def h(self):
		if self.is_leaf():
			return(1)
		l=0
		r=0
		if (self.left):
			l = self.left.h()
		if (self.right):
			r = self.right.h()
		return (max(l,r)+1)

	def w(self):
		global mx
		if self.is_leaf():
			return(1)
		l=0
		r=0
		if (self.left):
			l = self.left.w()
		if (self.right):
			r = self.right.w()
		tmp=l+r+1
		if tmp>mx:
			mx=tmp
		return (max(l,r)+1)


root = Tree(1)
root.add_l(2).add_l(3)
root.left.add_r(4).add_l(6)
root.add_r(5).add_2(7,8)

root.printer()

#print root.h()
root.w()
print mx
