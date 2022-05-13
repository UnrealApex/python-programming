class Stack(list):
  def __init__(self):
    super().__init__()
    self.stack = []


  def getStack(self):
    """Prompts the user to enter five strings and stores them in a stack."""
    for i in range(5):
      self.stack.append(input(f"Enter string {i + 1} out of 5: "))

  def reverseStack(self):
    """Reverses the order of the stack and displays it."""
    for i in range(1, 6):
      print(self.stack[-i])

x = Stack()
x.getStack()
x.reverseStack()
