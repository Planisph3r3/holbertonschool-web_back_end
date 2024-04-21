// Clean Set

export default function cleanSet(set, string) {
  let newString = '';
  if (string === '' || !string) {
    return '';
  }
  let counter = 1;
  for (const element of set) {
    counter += 1;
    if (element.startsWith(string)) {
      newString += element.slice(string.length);
      if (counter !== set.size) {
        newString += '-';
      }
    }
  }

  return newString;
}
