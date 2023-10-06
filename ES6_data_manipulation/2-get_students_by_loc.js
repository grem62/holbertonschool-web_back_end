export default function getStudentsByLocation(filterarray) {
  const filter = filterarray.filter((item) => item.location === 'San Francisco');
  return filter;
}
