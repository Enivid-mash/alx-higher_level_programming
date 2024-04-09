#!/usr/bin/node
const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  charPrint (c) {
    this.side = c;
    if (this.side === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i += 1) {
        console.log(this.side.repeat(this.height));
      }
    }
  }
};
