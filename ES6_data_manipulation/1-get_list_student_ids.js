export default function getListStudentIds(idarray) {
  if (!Array.isArray(idarray)) {
    return [];
  }
  const idmap = idarray.map((item) => item.id);
  return idmap;
}
