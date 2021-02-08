function solution(arr)
{
    var answer = [];
    let index = 0;

    for(let i=0; i<arr.length; i++){
        if(answer.length ==0 ){ answer.push(arr[i]); index++}
        else{
            if(answer[index-1] == arr[i]) continue;
            answer.push(arr[i]);
            index++
        }
    }
    
    return answer;
}

console.log(solution([1, 1, 3, 3, 0, 1, 1]));