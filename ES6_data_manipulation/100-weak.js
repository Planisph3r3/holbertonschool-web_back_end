// Weak link data structure

export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  if (!(weakMap.has(endpoint))) {
    weakMap.set(endpoint, 1);
  } else {
    const addCount = weakMap.get(endpoint) + 1;
    weakMap.set(endpoint, addCount);
    if (addCount >= 5) {
      throw new Error('Endpoint load is high');
    }
  }
}
