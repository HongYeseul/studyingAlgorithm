let PrimeArray = [];

function Eratos(n){
    if(n<=1) return;

    for(let i=2; i<=n; i++){
        PrimeArray[i] = true
    }

    for(let i=2; i*i <=n; i++){
        if(PrimeArray[i])
            for(let j=i*i; j<=n; j+=i)
                PrimeArray[j] = false;
    }
}

function solution(n) {
    var answer = 0;
    Eratos(n)
    for(let i=2; i<=n+1; i++){
        if(PrimeArray[i] == true){
            answer++
        }
    }
    
    return answer;
}

console.log(solution(5))

