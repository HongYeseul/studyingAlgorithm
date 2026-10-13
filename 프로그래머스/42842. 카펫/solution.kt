class Solution {
    fun solution(brown: Int, yellow: Int): IntArray {
        var answer = intArrayOf()
        var size = brown + yellow
        
        if (yellow == 1) {
            return intArrayOf(3, 3)
        }
        
        // yellow 의 가로, 세로를 구한다
        for (x in 1 until yellow) {
            
            if (yellow % x == 0) {
                var y = yellow / x
                
                // yellow 기준 (가로/세로) 각각의 +2 값에 대해 넓이 구하기
                val xy = (x + 2) * (y + 2)
                // println("x $x, y $y, size $size, xy $xy")
                
                // brown + yellow == 넓이라면 return
                // 가로 > 세로 (내림차순)
                if (size == xy) {
                    return intArrayOf(y + 2, x + 2)
                }
                
            }
        }
        
        return answer
    }
}
