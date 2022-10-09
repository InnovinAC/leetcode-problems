// 1. Simple method - Absolutely fast(4ms)
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function smallestEvenMultiple($n) {
      if($n%2 == 0 ) {
        return $n;
      }
      return $n*2;
        
    }
}




// 2. Using tenary operator(fast  but slower than solution above)
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function smallestEvenMultiple($n) {
      $n%2 == 0 ? $a = $n: $a = $n*2;
        return $a;
    }
}
