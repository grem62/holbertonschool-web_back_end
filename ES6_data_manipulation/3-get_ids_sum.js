export default function getStudentIdsSum(idarray) {
  const valuestart = 0;
  const sumid = idarray.reduce((accumu, currentValue) => accumu + currentValue.id, valuestart);
  return sumid;
}
