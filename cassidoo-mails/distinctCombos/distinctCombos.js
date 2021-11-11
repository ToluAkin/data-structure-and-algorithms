function distinctCombos(arr, r){
    let result = []
    arr = [...new Set(arr)]

    for (let i = 0; i < arr.length; i++) {
        for (let j = i; j < arr.length; j++) {
            result.push([arr[i], arr[j]])
        }
    }
    
    console.log(result)
}

function combination(arr) {
    let result = [];
    let seen = new Set();

    for (let i = 0; i < arr.length; i++) {
        for (let j = i; j < arr.length; j++) {
            if (j > i && arr[i] === arr[j]) continue;
            if (!seen.has(arr[i]))  result.push([arr[i], arr[j]]);
        }
        seen.add(arr[i])
    }

    return result;
}
distinctCombos([1, 1, 2], 2)