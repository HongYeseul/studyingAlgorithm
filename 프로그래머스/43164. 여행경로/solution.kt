class Solution {
    fun solution(tickets: Array<Array<String>>): Array<String> {
        var answer = mutableListOf<String>()
        val visited = BooleanArray(tickets.size)
        
        fun dfs(node: Int) {
            // return 조건
            if (visited[node]) {
                return
            }
            
            // 방문 기록 (현재 도착지)
            visited[node] = true
            answer.add(tickets[node][1])
            
            // 다음 노드
            val nextSites = mutableListOf<Pair<Int, String>>()
            for (next in 0 until tickets.size) {
                
                // 방문 가능 노드 (현재 티켓 도착지 == 다음 티켓 출발지)
                if (tickets[node][1] == tickets[next][0]) {
                    // 방문 가능한 노드의 도착지
                    nextSites.add(Pair(next, tickets[next][1]))
                }
                
            }
            nextSites.sortedBy{it.second}
                .forEach {it -> dfs(it.first)}
            
            // 모든 곳 방문 완료시 return
            if (visited.all{it}) {
                return
            }
            
            // 만약 더이상 갈 수 있는 곳이 없다면 해당 길로는 진행 불가
            visited[node] = false
            answer.removeLast()
        }
        
        
        // todo: 아래 내용 dfs 메서드와 동일해서 dfs로 넣어서 메서드 수정
        val nextSites = mutableListOf<Pair<Int, String>>()
        for (next in 0 until tickets.size) {
            if (tickets[next][0] == "ICN") {
                nextSites.add(Pair(next, tickets[next][1]))
            }
        }
        nextSites.sortedBy{
            it.second
        }
            .forEach {it -> 
                answer.clear()
                answer.add("ICN")
                
                dfs(it.first)
                // 모든 곳 방문 완료시 return
                if (visited.all{it}) {
                    return answer.toTypedArray()
                }
            
            }

        return answer.toTypedArray()
    }
}
