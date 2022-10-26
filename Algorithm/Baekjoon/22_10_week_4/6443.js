const fs = require('fs')
let input = fs.readFileSync('./test').toString().trim().split('\n')
const N = input[0].split(' ').map(number)
const alpha = 'abcdefghijklmnopqrstuvwxyz'
for (let i = 1; i < N[0]+1; i++) {
    const alpha_nums = [0]*26
    const S = input[1]
    console.log(S)
}