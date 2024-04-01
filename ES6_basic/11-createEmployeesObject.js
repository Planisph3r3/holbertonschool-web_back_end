// Creation of a object

export default function createEmployeesObject(departmentName, employees) {
  const createdEmployeesObject = {
    [departmentName]: employees,
  };

  return createdEmployeesObject;
}
