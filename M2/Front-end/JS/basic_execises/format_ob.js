function student_summary(student) {
  const average =
    student.grades.reduce((average, g) => {
      return (average += g.grade);
    }, 0) / student.grades.length;

  const highest = student.grades.reduce(
    (max, g) => (g.grade > max.grade ? g : max),
    student.grades[0]
  );
  const lowest = student.grades.reduce(
    (min, g) => (g.grade < min.grade ? g : min),
    student.grades[0]
  );

  return {
    name: student.name,
    gradeAvg: average,
    highesGrade: highest.name,
    lowestGrade: lowest.name,
  };
}



// Entrada
const student = {
  name: "John Doe",
  grades: [
    { name: "math", grade: 80 },
    { name: "science", grade: 100 },
    { name: "history", grade: 60 },
    { name: "PE", grade: 90 },
    { name: "music", grade: 98 },
  ],
};

result = student_resume(student);
console.log(result);
