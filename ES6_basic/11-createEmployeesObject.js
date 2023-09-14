export default function createEmployeesObject(departmentName, employees) {
  return `{ ${departmentName}: ${JSON.stringify(employees)} }`;
}
