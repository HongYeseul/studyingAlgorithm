function solution(s, n) {
    var answer = '';
    
    for(let i=0; i<s.length; i++){
        if(s[i] == ' '){
            answer+=" ";
            continue;
        }
        
        if(s[i] >= 'a' && s[i] <= 'z'){
            let a = ((s.charCodeAt(i)-97)+n)%26;
            console.log(a)
            answer+=String.fromCharCode(a+97)
        }
        else if(s[i] >= 'A' && s[i] <= 'Z'){
            let a = ((s.charCodeAt(i)-65)+n)%26;
            answer+=String.fromCharCode(a+65)
        }
        
    }
    
    return answer;
}

console.log(solution('AB', 1))

// System.out.println(cc.solution(AB, 1));
// System.out.println(cc.solution(z, 1));
// System.out.println(cc.solution(Z, 10));
// System.out.println(cc.solution(a B z, 4));
// System.out.println(cc.solution(aBZ, 20));
// System.out.println(cc.solution(y X Z, 4));
// System.out.println(cc.solution(. h z, 20));