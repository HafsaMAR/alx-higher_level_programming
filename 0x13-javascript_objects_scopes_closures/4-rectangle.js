#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.Width = w;
      this.height = h;
    }
  }

  print () {
    if (this.Width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.Width));
      }
    }
  }

  rotate () {
    if (this.Width && this.height) {
      [this.Width, this.height] = [this.height, this.Width];
    }
  }

  double () {
    if (this.Width && this.height) {
      [this.Width, this.height] = [this.Width * 2, this.height * 2];
    }
  }
}
module.exports = Rectangle;
