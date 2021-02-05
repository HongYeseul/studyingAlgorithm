let str = '';

function make3(n){
    if(n<3){
        str = str+String(n);
        return;
    }
    else{
        // console.log(n%3)
        str = str + String(n%3)
        make3(parseInt(n/3));
    }
}

function make10(str){
    let num = 0;
    for(let i=(str.length-1); i>=0; i--){
        let p = str.length-i-1;
        if(p == 0) num += Number(str[i])
        else{
            console.log(str.length-i-1)
            let n = Math.pow(3, str.length-i-1)
            console.log("pow Value "+n*str[i])
            num += Number(n* str[i])
    
            // console.log(num);
        }
    }
    return num;
}

function solution(n) {
    // var answer = 0;

    make3(n);
    console.log(str)

    var answer = make10(str);

    return answer;
}

// solution(125)

console.log(solution(125));