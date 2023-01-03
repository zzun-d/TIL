const numbers = [1, 2, 3, 4, 5]

class Student {
    constructor(name, koreanLanguage, english, mathematis) {
        this.name = name
        this.koreanLanguage = koreanLanguage
        this.english = english
        this.mathematis = mathematis
    }
}

const student1 = new Student("홍길동", 95, 87, 75)
const student2 = new Student("김길동", 67, 80, 100)
const student3 = new Student("고길동", 89, 75, 80)
const student4 = new Student("최길동", 48, 52, 98)

const students = [student1, student2, student3, student4]

const result = numbers.map((number) => number*2)
console.log(result)
console.log(
    "학생 이름",
    students.map((student) => student.name)
)