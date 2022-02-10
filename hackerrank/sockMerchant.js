(function sockMerchant (n, arr) {
    let newMap = new Map()
    let counter = 0

    arr.map(value => {
        if (newMap.has(value)) {
            newMap.set(value, newMap.get(value) + 1)
        } else {
            newMap.set(value, 1)
        }
    })

    newMap.forEach(function (value, key) {
        if (value > 1) {
            counter += Math.floor(value / 2)
        }
    })

    console.log(counter);
    // return newArray
})(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])