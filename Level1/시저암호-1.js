// 아래의 코드들은 다른 사람들의 코드를 구경하던 중, 알면 좋을 것 같은 코드들을 가지고 와봤다.

// ascii 코드 값을 사용하지 않고 그냥 문자열의 length만 가지고 깔끔하게 풀어낸 예시
function solution1(s, n) {
    var upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    var lower = "abcdefghijklmnopqrstuvwxyz";
    var answer= '';

    for(var i =0; i <s.length; i++){
        var text = s[i];
        if(text == ' ') {
            answer += ' '; 
            continue;
        }
        var textArr = upper.includes(text) ? upper : lower;
        var index = textArr.indexOf(text)+n;
        if(index >= textArr.length) index -= textArr.length;
        answer += textArr[index];
    }
    return answer;
}


// 제일 간편하고 용량도 적게 쓰는 코드인것 같다. 이해도 쉽게 된다.
function solution2(s, n) {
    var chars = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXY                          "
    return s.split('').map(e => chars[chars.indexOf(e)+n]).join('');
}