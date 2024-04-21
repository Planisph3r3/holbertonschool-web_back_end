// Typed Int

export default function createInt8TypedArray(length, position, value) {
  const intArray = new ArrayBuffer(length);
  const view = new DataView(intArray, 0);
  view.setInt8(position, value);
  return view;
}
