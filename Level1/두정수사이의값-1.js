function solution(a, b) {
    var answer = 0;

    // Math.min()을 생각을 쓰다니..! 사람들은 정말 대단한 것 같다 :>
    for(let i=Math.min(a,b); i<=Math.max(a, b); i++)
        answer+=i;
    return answer;
}

console.log(solution(3, 5))