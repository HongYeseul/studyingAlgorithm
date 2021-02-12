function solution(s) {
    var answer = 0;

    // 이 방법 외에도 js에서는 문자열을 숫자로 바꾸려면 s/1만 해주거나 +s 처럼 숫자와 연산만 해 주면 자동으로 숫자 변환이 된다!!!
    return Number(s);
}

console.log(solution("1234"))
console.log(solution("-1234"))