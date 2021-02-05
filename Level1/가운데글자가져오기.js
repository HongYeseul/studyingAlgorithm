function solution(s) {
    var answer = '';

    let n = s.length;
    console.log(n)

    if(n % 2 == 0){
        console.log((n/2)-1, n/2);
        answer = s.substr((n/2)-1, 2)
    }else{
        answer = s.charAt(n/2);
    }

    return answer;
}

console.log(solution("abcdefghij"));