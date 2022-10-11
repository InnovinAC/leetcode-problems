class Solution:
    def decodeMessage(self, key, message):
      alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
      checker = []
      
      [checker.append(x) for x in list(key) if x not in checker and x != ' ']
      new_dict = {}
      for x in range(len(checker)):
        new_dict[checker[x]] = alpha[x]
      new_dict[' '] = ' '
      my_str = ''
      for x in message:
          my_str += new_dict[x]
      return my_str
