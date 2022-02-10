(function foo(codeList, shoppingCart) {
    const mergedCodeList = [].concat.apply([], codeList)
    let currentIndex = 0
    const any = 'anything'

    for (let index = 0; index < shoppingCart.length; index++) {
        if (currentIndex >= mergedCodeList.length) continue

        if (shoppingCart[index] == mergedCodeList[currentIndex] || mergedCodeList[currentIndex] == any) {
            currentIndex++
        }
    }

    currentIndex >= mergedCodeList.length ? console.log(1) : console.log(0);
    // console.log(mergedCodeList);
})(
    [['apple', 'apple'], ['banana', 'anything', 'banana']],
    ['orange', 'apple', 'apple', 'banana', 'orange', 'banana', 'orange', 'orange', 'banana', 'apple', 'banana', 'banana'])