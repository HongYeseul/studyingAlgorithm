function solution(s) {
    
    if(s.length != 4 && s.length != 6) return false;

    for(let i=0; i<s.length; i++){
        console.log(s[i])
        if(!(s[i] <= '9' && s[i] >= '0')) return false 
    }

    return true;
}

function solution2(s){
    // 처음에 제출 했었던 코드. 11번을 계속 틀려서 결국 다른 방법으로 제출했는데, 아니나다를까 다른사람들의 풀이중 이것과 비슷한 방법이 있었다. 예전에는 가능했었던것같다.
    return (s.length == 4 || s.length == 6) && !isNaN(s);
}
// 그런데 이 코드에서 메소드만 조금 바꿔주면 가능해진다. 문제 풀 때는 왜 parseInt를 생각하지 못했을까.
function solution3(s){
    return (s.length == 4 || s.length == 6) && (parseInt(s) == s)
}
// 여기서 문제는 아래의 console을 실행했을 때 문제 답으로는 false가 나와야하는데 true가 나와버리는 이슈가 발생한다.
// -> parseInt나 isNaN()은 쓰면 안될 것 같다.. 
console.log(solution3('123 '));