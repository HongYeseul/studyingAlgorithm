import java.util.*;

class Solution {
    fun solution(numbers: IntArray): String {
        var answer = ""
        var list = LinkedList<String>()
        
        // 1. 모든 수를 string으로 치환 후 정렬
        for (n in numbers) {
            list.add(n.toString())
        }
        var l = list.sortedWith {
            // x + y 와 y + x 자리 변경해서 비교 후 큰 값을 앞으로 정렬
            x, y -> (y + x).toInt() - (x + y).toInt()
        }
        // 만약 0만 존재한다면 0 return
        if (l[0] == "0") {
            return l[0]
        }
        return l.joinToString("")
    }
    
}
