class Solution {

    /**
     * @param String $s
     * @param String $letter
     * @return Integer
     */
    function percentageLetter($s, $letter) {
        return intval(substr_count($s, $letter)/strlen($s) * 100);
    }
}
