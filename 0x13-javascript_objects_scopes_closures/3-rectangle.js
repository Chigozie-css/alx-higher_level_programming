#!/usr/bin/node
/* Define a Rectangle class with a constructor that accepts width and height parameters */
class Rectangle {
  constructor (w, h) {
    /* Check if both width and height are positive */
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  /* Define a method to print a rectangle of X characters with dimensions width and height */
  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;
