// Array

export default function getListStudentIds(param) {
  if (!Array.isArray(param)) {
    return [];
  }
  const arrayStore = [];
  param.forEach((element) => {
    arrayStore.push(element.id);
  });
  return arrayStore;
}
