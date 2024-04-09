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

  print () {
    let result = '';
    for (let i = 0; i < this.width; i++) {
      result += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(result);
    }
  }

  double () {
    this.width += this.width;
    this.height += this.height;
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
// Export the class as module
module.exports = Rectangle;
module.exports = Square;
