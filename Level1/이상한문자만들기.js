function solution(s) {
    // var answer = '';

    // map()은 Function이 준 값으로 이루어진 배열을 'return' 하기 때문에 {}를 사용하려면 return 값이 필수!!
    // answer = s.split(' ').map((word, i)=>{
    //     return word.split('').map((c, i)=>{
    //         if(i%2 == 0) return c.toUpperCase()
    //         else return c.toLowerCase()
    //     }).join('')
    // }).join(' ')

    // 아래는 참고한 코드
    let answer = s.split(' ').map((a,i)=>
        a.split('').map((e,i)=>
            i%2==0 
            ? e.toUpperCase() 
            : e.toLowerCase()
        ).join('')
    ).join(' ');

    return answer;
}

console.log(solution('TRY HELLO WORLD'));