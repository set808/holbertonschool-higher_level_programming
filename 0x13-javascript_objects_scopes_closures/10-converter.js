#!/usr/bin/node


exports.converter = function (base) {
    return function (n) {
        n.toString(base);
    };
};