function solution(s){
    var answer = true;
    let pValue = 0;
    let yValue = 0;

    s = s.toUpperCase();
    console.log(s);

    if(s.indexOf('P') == -1 && s.indexOf('Y') == -1)
        return true;

    for(let i=0; i<s.length; i++){
        if(s[i] == 'P'){
            pValue++;
        }else if(s[i] == 'Y'){
            yValue++;
        }
    }

    if(pValue == yValue) answer = true;
    else answer = false;

    return answer;
}

console.log(solution("Pyy"));