
def chai_flavour(flavor="masala"):
  """Return the flavor of chai,"""
  return flavor


print(chai_flavour.__doc__)
print(chai_flavour.__name__)


def generate_bill(chai=0, samosa=0):
  """
  Calculate the total bill for chai and samosa
  
  :param chai: Number of chai cups (10 rupees each)
  :param samosa: Number of samosa (15 rupees each)
  :return: (total amount, thank you message as string)
  """
  total = chai*10 + samosa*15
  return total, "Thank you for visiting chaicode.com"


