// Reduce method

export default function getStudentIdsSum(students) {
  const arrayStore = [];
  students.forEach((element) => {
    arrayStore.push(element.id);
  });
  return arrayStore.reduce((accumulator, firstVal) => accumulator + firstVal, 0);
}
