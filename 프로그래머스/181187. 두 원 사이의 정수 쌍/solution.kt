import kotlin.math.ceil
import kotlin.math.sqrt

class Solution {
    // 해설 참고 .. 이해 못함
    
    fun solution(r1: Int, r2: Int): Long {
        // 곱셈 전에 Long으로 변환해 Int 범위 초과를 방지한다.
        val innerSquared = r1.toLong() * r1
        val outerSquared = r2.toLong() * r2
        var count = 0L

        // 양의 x축은 포함하고 y축은 제외해, 4배 할 때 축의 중복을 피한다.
        for (x in 1..r2) {
            val xSquared = x.toLong() * x

            // 큰 원의 경계를 넘지 않는 최대 정수 y
            val maxY = sqrt((outerSquared - xSquared).toDouble()).toLong()

            // 작은 원의 경계는 포함하고, 그 안쪽의 점만 제외한다.
            val minY = if (x >= r1) {
                0L
            } else {
                ceil(sqrt((innerSquared - xSquared).toDouble())).toLong()
            }

            count += maxY - minY + 1
        }

        return count * 4
    }
}
