#!/usr/bin/node
/* Define a Rectangle class with a constructor that accepts width and height parameters */
class Rectangle {
  constructor (w, h) {
    // Check if both width and height are positive
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
