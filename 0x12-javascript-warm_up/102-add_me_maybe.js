#!/usr/bin/node
/*
  This script exports a function 'addMeMaybe' that increments a number by one
  and passes the incremented value to another function 'theFunction'.
*/

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
