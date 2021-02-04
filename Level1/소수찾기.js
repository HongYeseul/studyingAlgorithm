function solution(n){
    var answer = 0;
    let flag = 0;

    for(let i=n; i>1; i--){
        for(let j=2; j<Math.sqrt(i+1); j++){
            if(i%j == 0){
                flag = 1;
                break;
            }
        }
        if(flag == 0)
            answer++
        flag = 0;
    }

    return answer;
}

console.log(solution(5))

