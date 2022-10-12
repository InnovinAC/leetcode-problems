class Solution {

    /**
     * @param Integer $num
     * @return Boolean
     */
    function isPerfectSquare($num) {
      $a = 0;
      $b = 1;
      while($a < $num) {
        $a += $b;
        $b += 2;
        }
      return $a==$num;
    }
}
