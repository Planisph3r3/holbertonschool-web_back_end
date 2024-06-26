// Throwing Error

export default function divideFunction(numerator, denominator) {
  if (denominator !== 0) {
    return numerator / denominator;
  }
  throw Error('cannot divide by 0');
}
