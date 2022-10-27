class Solution:
    def dayOfYear(self, date):
      date = date.split('-')
      date = list(map(int, date))
      
      a,b, c = date[0], date[1], date[2]
      year = {1:31, 2:28, 3:31, 4:30, 5: 31, 6: 30, 7:31, 8: 31, 9:30, 10:31, 11:30, 12:31}
      if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0 :
        year[2] = 29
        
      new_list = [v for k,v in year.items() if k < b]
      return sum(new_list) + c
