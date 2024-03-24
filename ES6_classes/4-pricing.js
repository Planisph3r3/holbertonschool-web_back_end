// Pricing Class

export default class Pricing {
  constructor(amount, currency) {
    this._amount = Number(amount);
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(amountVal) {
    this._amount = amountVal;
  }

  get currency() {
    return this._currency;
  }

  set currency(currencyVal) {
    this._currency = currencyVal;
  }

  displayFullPrice() {
    return `${this._amount} ${this.currency.displayFullCurrency()}`;
  }

  static convertPrice(amount, conversionRate) {
    return Number(amount) * Number(conversionRate);
  }
}
