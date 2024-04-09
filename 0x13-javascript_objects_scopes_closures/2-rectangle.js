#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

// Export the class a module
module.exports = Rectangle;
