// Filter method

export default function getStudentsByLocation(students, city) {
  const filteredResult = students.filter((obj) => obj.location === city);
  return filteredResult;
}
