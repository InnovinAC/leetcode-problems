class Solution {

    function fizzBuzz($n) {
        $new_list = [];
      for($x =1; $x < $n+1; $x++) {
        
        if($x%3 == 0 && $x%5 == 0) {
          array_push($new_list, 'FizzBuzz');
          }
        elseif($x%3 == 0) {
          array_push($new_list, 'Fizz');
          }
        elseif($x%5 == 0) {
          array_push($new_list, 'Buzz');
          }
        else{
          array_push($new_list, strval($x));
          }
      
      }
      return $new_list;
    
    }
}
