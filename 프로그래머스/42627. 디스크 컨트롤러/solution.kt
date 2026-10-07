import java.util.*

class Solution {
    fun solution(jobs: Array<IntArray>): Int {
        var answer = 0
        val pq = PriorityQueue<IntArray>(compareBy( {it[1]}, {it[0]} ))
        val done = BooleanArray(jobs.size)
        
        // 시작 시간 기준 sorting
        jobs.sortWith( compareBy{ it[0] } )
        // jobs.forEach { println(it.contentToString()) }
        
        var time = 0
        var count = 0 // 처리 끝낸 job 수
        
        // 현재 시간 기준으로 가능한 job들 큐에 넣음
        while (count < jobs.size) {
            for (i in jobs.indices) {
                if (!done[i] && time >= jobs[i][0]) {
                    pq.add(jobs[i])
                    done[i] = true
                }
            }
            
            // 큐에서 하나를 꺼내서 처리
            if (pq.isNotEmpty()) {
                val new = pq.poll()
                time += new[1]
                answer += (time - new[0]) // 반환 시간 = 끝난 시각 - 요청 시각
                // println("new[0]: ${new[0]}, new[1]: ${new[1]}, answer: $answer, time: $time")
                count++
            } else {
                // 대기 중인 job이 없으면 시간 흐르게
                time++
            }
        }
        return (answer) / jobs.size
    }
}
