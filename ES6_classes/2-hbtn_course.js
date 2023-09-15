export default class HolbertonCourse {
    constructor(name, length, students) {
      // Vérification du type des attributs
      if (typeof name !== 'string') {
        throw new TypeError('Name must be a string');
      }
      if (typeof length !== 'number') {
        throw new TypeError('Length must be a number');
      }
      if (!Array.isArray(students) || !students.every((student) => typeof student === 'string')) {
        throw new TypeError('Students must be an array of strings');
      }
  
      this._name = name;
      this._length = length;
      this._students = students;
    }
  
    // Getter pour l'attribut 'name'
    get name() {
      return this._name;
    }
  
    // Setter pour l'attribut 'name'
    set name(newName) {
      if (typeof newName === 'string') {
        this._name = newName;
      } else {
        throw new TypeError('Name must be a string');
      }
    }
  
    // Getter pour l'attribut 'length'
    get length() {
      return this._length;
    }
  
    // Setter pour l'attribut 'length'
    set length(newLength) {
      if (typeof newLength === 'number') {
        this._length = newLength;
      } else {
        throw new TypeError('Length must be a number');
      }
    }
  
    // Getter pour l'attribut 'students'
    get students() {
      return this._students;
    }
  
    // Setter pour l'attribut 'student'
    set students(newStudents) {
      if (Array.isArray(newStudents) && newStudents.every((student) => typeof student === 'string')) {
        this._students = newStudents;
      } else {
        throw new TypeError('Students must be an array of strings');
      }
    }
  }
  