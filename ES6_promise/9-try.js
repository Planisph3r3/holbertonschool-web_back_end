// Try / Catch

export default function guardrail(mathFunction) {
  const queue = [];

  try {
    const safeValue = mathFunction();
    queue.push(safeValue);
  } catch (error) {
    const nonSafeValue = `Error: ${error.message}`;
    queue.push(nonSafeValue);
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
