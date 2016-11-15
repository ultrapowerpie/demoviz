/**
 * FastPriorityQueue.js : a fast heap-based priority queue  in JavaScript.
 * (c) the authors
 * Licensed under the Apache License, Version 2.0.
 *
 * Speed-optimized heap-based priority queue for modern browsers and JavaScript engines.
 *
 * Usage :
         Installation (in shell, if you use node):
         $ npm install fastpriorityqueue

         Running test program (in JavaScript):
 */
'use strict';

var defaultcomparator = function(a, b) {
    return a < b;
};

// the provided comparator function should take a, b and return *true* when a < b
function FastPriorityQueue(comparator) {
    this.array = [];
    this.size = 0;
    this.compare =  comparator || defaultcomparator;
}


// Add an element the the queue
// runs in O(log n) time
FastPriorityQueue.prototype.add = function(myval) {
    var i = this.size;
    this.array[this.size++] = myval;
    while ( i > 0) {
        var p = (i - 1) >> 1;
        var ap = this.array[p];
        if(!this.compare(myval, ap )) break;
        this.array[i] = ap;
        i = p;
    }
    this.array[i] = myval;
};

// replace the content of the heap by provided array and "heapifies it"
FastPriorityQueue.prototype.heapify = function(arr) {
    this.array = arr;
    this.size = arr.length;
    for (var i = (this.size >> 1); i >= 0; i--) {
        this._percolateDown(i);
    }
};

// for internal use
FastPriorityQueue.prototype._percolateUp = function(i) {
    var myval = this.array[i];
    while ( i > 0) {
        var p = (i - 1) >> 1;
        var ap = this.array[p];
        if(!this.compare(myval, ap )) break;
        this.array[i] = ap;
        i = p;
    }
    this.array[i] = myval;
};


// for internal use
FastPriorityQueue.prototype._percolateDown = function(i) {
    var size = this.size;
    var hsize = this.size >>> 1;
    var ai = this.array[i];
    while (i < hsize) {
        var l = (i << 1) + 1;
        var r = l + 1;
        var bestc = this.array[l];
        if (r < size) {
            if (this.compare(this.array[r], bestc)) {
                l = r;
                bestc = this.array[r];
            }
        }
        if (!this.compare(bestc,ai)) {
          break;
        }
        this.array[i] = bestc;
        i = l;
    }
    this.array[i] = ai;
};

FastPriorityQueue.prototype.peek = function(t) {
    return this.array[0];
};


FastPriorityQueue.prototype.poll = function(i) {
    var ans = this.array[0];
    if(this.size>1) {
        this.array[0] = this.array[--this.size];
        this._percolateDown(0 | 0);
    } else --this.size;
    return ans;
};


// recover unused memory (for long-running priority queues)
FastPriorityQueue.prototype.trim = function() {
    this.array = this.array.slice(0,this.size);
};

// Check whether the heap is empty
FastPriorityQueue.prototype.isEmpty = function(i) {
    return this.size == 0;
};


