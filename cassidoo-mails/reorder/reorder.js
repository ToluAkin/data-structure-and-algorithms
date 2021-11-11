function reorder(a, b) {
    let orderSet = new Map();

    for (let i = 0; i < a.length; i++) {
        orderSet.set(b[i], a[i])
    }

    for (let i = 0; i < a.length; i++) {
        if (a[i] === orderSet.get(i)) {
            continue
        } else {
            a[i] = orderSet.get(i)
        }
    }
    // console.log(orderSet);
    console.log(a)
}
reorder(["C", "D", "E", "F", "G", "H"], [3, 0, 4, 1, 2, 5])