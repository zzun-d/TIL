const fs = require('fs')
let input = fs.readFileSync('./test.txt').toString().trim().split('\n')
const N = input[0].split(' ').map(Number)
const alpha = 'abcdefghijklmnopqrstuvwxyz'
console.log(input)
for (let i = 1; i < N[0]+1; i++) {
    const alpha_nums = [0]*26
    const S = input[i].replace(/\r/g, '').split('')
    // for (s of S) {
    //     alpha_nums[]
    // }

}
