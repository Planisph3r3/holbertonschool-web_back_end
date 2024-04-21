// Clean Set

export default function cleanSet(set, string) {
  let newString = '';
  if (string === '' || !string || typeof string !== 'string') {
    return '';
  }
  for (const element of set) {
    if (element.startsWith(string)) {
      newString += `${element.slice(string.length)}-`;
    }
  }
  if (newString.endsWith('-')) {
    newString = newString.slice(0, -1);
  }
  return newString;
}
