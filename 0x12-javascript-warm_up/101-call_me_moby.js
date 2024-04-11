#!/usr/bin/node
/*
  This script exports a function 'callMeMoby' that invokes another function 'theFunction' 'x' times.
*/

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
