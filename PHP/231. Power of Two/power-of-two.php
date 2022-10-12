class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function isPowerOfTwo($n) {
        $squares = array();
        for($i=0; $i < 32; $i++) {
          array_push($squares, 2**$i);
        }
      return in_array($n, $squares);
          
        
    }
}
