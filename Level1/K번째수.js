function solution(array, commands) {
    var answer = [];
    console.log(array)
    

    // console.log(array.slice(2,6))
    for(let i=0; i<commands.length; i++){
        let newArr = array.slice(commands[i][0]-1, commands[i][1]).sort((a,b)=> a-b);
        answer.push( newArr[commands[i][2]-1] )
    }
    
    return answer;
}

console.log(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))