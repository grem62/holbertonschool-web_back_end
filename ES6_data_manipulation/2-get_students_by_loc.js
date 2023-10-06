export default function getStudentsByLocation(filterarray, city) {
  const filter = filterarray.filter((item) => item.location === city);
  return filter;
}
