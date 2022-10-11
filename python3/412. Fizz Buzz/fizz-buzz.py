class Solution:
    def fizzBuzz(self, n):
      new_list = []
      for x in range(1, n+1):
        if x%3 == 0 == x%5:
          new_list.append("FizzBuzz")
        elif x%3 == 0:
          new_list.append("Fizz")
        elif x%5 == 0:
          new_list.append("Buzz")
        else:
          new_list.append(str(x))
      return new_list
        
