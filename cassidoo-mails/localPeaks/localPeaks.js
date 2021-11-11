(function localPeaks(arr) {
    let peaks = []
    arr.map((item, i) => {
        if (i !== 0 && i !== arr.length + 1) {
            if (item > arr[i-1] && item > arr[i+1]) {
                peaks.push(i)
            }
        }
        return peaks
    })
    console.log(peaks);
})([1,2,3,1])
