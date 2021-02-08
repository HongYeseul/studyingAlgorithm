function solution(arr)
{
    return arr.filter( (n, index) => n != arr[index+1] );
}

console.log(solution([1, 1, 3, 3, 0, 1, 1]))