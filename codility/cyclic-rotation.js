(function CyclicRotation(arr, round) {
    const length = arr.length
    let completed = Array(length).fill(0)

    if (round == length) {
        return arr
    }

    for (let i = 0; i < length; i++) {
        completed[(i + round) % length] = arr[i]
    }
    
    console.log(completed)
    return completed
})([3, 8, 9, 7, 6], 3)