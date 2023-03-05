const fs = require("fs")
const { range } = require("lodash")
let input = fs
  .readFileSync(
    "C:/Users/multicampus/ssafy08/TIL/Algorithm/Baekjoon/22_11_week_2/test.txt"
  )
  .toString()
  .trim()
  .split("\n")
const N = Number(input[0])
let cnt = 0
for (let i = 1; i < N + 1; i++) {
  // console.log(input, i)
  const word = input[i].replace(/\r/g, "").split("")
  const stack = []
  for (let j in range(word.length)) {
    console.log(stack, j, word)

    if (word && word[j - 1] === "A") {
      if (stack[j] == "A") {
        stack.pop()
      } else {
        stack.push(word[j])
      }
    } else {
      if (word && stack[j - 1] == "B") {
        stack.pop()
      } else {
        stack.push(word[j])
      }
    }
  }
  // console.log(stack)
  if (!stack) {
    cnt++
  }
}
console.log(cnt)
