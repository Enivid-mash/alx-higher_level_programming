#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return 'Rectangle {}';
    } else {
      this.width = w;
      this.height = h;
    }
  }
  print() {
		let result = '';
		for (let i = 0; i < this.width; i++) {
			result += 'X';
		}
		for (let j = 0; j < this.height; j++) {
			console.log(result);
		}
	}
}

// Export the class a module
module.exports = Rectangle;
