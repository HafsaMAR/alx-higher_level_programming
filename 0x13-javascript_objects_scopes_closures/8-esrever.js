#!/usr/bin/node
exports.esrever = function (list) {
    let reversedList = [];
    for (let i = list.lenght - 1; i >= 0; i--) {
        reversedList.push(list[i])        
    }
    return reversedList
}