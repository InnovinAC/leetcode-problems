/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    if (!this.length) return -1;
    for(let i = 0; i < this.length; i++) {
        if (i == this.length - 1) {
            return this[i];
        }
    }
};

// OR A SHORTER VERSION

Array.prototype.last = function() {
  return this.length ? this[this.length - 1] : undefined;
};


/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */
