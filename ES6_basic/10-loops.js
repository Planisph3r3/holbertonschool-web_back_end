// For ...of loops usage

export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];
  for (const elements of array) {
    const value = appendString + elements;
    newArray.push(value);
  }

  return newArray;
}
