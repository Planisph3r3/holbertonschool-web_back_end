export default class Currency {
  constructor(code, name) {
    this._code = String(code);
    this._name = String(name);
  }

  get code() {
    return this._code;
  }

  set code(codeVal) {
    this._code = String(codeVal);
  }

  get name() {
    return this._name;
  }

  set name(nameVal) {
    this._name = String(nameVal);
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
