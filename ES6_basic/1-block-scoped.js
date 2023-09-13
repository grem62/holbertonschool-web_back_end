export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    //Block Scope
    const task = true; // Utilisation de 'let' pour éviter la réaffectation
    const task2 = false; // Utilisation de 'let' pour éviter la réaffectation
  }

  return [task, task2];
}
