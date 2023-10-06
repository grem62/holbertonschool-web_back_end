export default function getListStudents() {
  const array1 = [];
  const array2 = [];
  const array3 = [];
  array1.push({ id: 1, firstName: 'Guillaume', location: 'San Francisco' });
  array2.push({ id: 2, firstName: 'James', location: 'Columbia' });
  array3.push({ id: 5, firstName: 'Serena', location: 'San Francisco' });

  const arraytotal = array1.concat(array2, array3);

  return arraytotal;
}
