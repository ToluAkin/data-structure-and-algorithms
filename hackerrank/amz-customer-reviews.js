(function searchSuggestions(repository, customerQuery) {
    let queryLength = customerQuery.length
    let answer = []

    for (let i = 2; i <= queryLength; i++) {
        let resultArray = []
        let currentQuery = customerQuery.toLowerCase().slice(0, i)

        repository.sort().map(word => {
            if (word.toLowerCase().startsWith(currentQuery) && resultArray.length <= 2) {
                resultArray.push(word.toLowerCase())
            }
        })
        answer.push(resultArray)
    }

    console.log(answer);
})(['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'], 'mouse')