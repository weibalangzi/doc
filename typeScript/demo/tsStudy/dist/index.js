"use strict";
function greeter(person) {
    return 'hello' + person;
}
var Direction;
(function (Direction) {
    Direction[Direction["left"] = 0] = "left";
    Direction[Direction["right"] = 1] = "right";
    Direction[Direction["top"] = 2] = "top";
    Direction[Direction["bottom"] = 3] = "bottom";
})(Direction || (Direction = {}));
var getUser = function (user) {
    return user.name;
};
var userName = getUser({ name: 'hehe', age: 12, gender: 'man' });
var sayhi = function (txt) {
    console.log('txt', txt);
};
sayhi(123);
sayhi('djkfdfkd');
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiaW5kZXguanMiLCJzb3VyY2VSb290IjoiIiwic291cmNlcyI6WyIuLi9zcmMvaW5kZXgudHMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IjtBQUNBLFNBQVMsT0FBTyxDQUFDLE1BQWM7SUFDM0IsT0FBTyxPQUFPLEdBQUcsTUFBTSxDQUFBO0FBQzNCLENBQUM7QUFHRCxJQUFLLFNBS0o7QUFMRCxXQUFLLFNBQVM7SUFDVix5Q0FBSSxDQUFBO0lBQ0osMkNBQUssQ0FBQTtJQUNMLHVDQUFHLENBQUE7SUFDSCw2Q0FBTSxDQUFBO0FBQ1YsQ0FBQyxFQUxJLFNBQVMsS0FBVCxTQUFTLFFBS2I7QUFlRCxJQUFNLE9BQU8sR0FBRyxVQUFDLElBQVU7SUFDdkIsT0FBTyxJQUFJLENBQUMsSUFBSSxDQUFBO0FBQ3BCLENBQUMsQ0FBQTtBQUVELElBQU0sUUFBUSxHQUFXLE9BQU8sQ0FBQyxFQUFDLElBQUksRUFBRSxNQUFNLEVBQUUsR0FBRyxFQUFFLEVBQUUsRUFBRSxNQUFNLEVBQUUsS0FBSyxFQUFDLENBQUMsQ0FBQTtBQUd4RSxJQUFNLEtBQUssR0FBRyxVQUFJLEdBQU07SUFDcEIsT0FBTyxDQUFDLEdBQUcsQ0FBQyxLQUFLLEVBQUUsR0FBRyxDQUFDLENBQUE7QUFDM0IsQ0FBQyxDQUFBO0FBRUQsS0FBSyxDQUFDLEdBQUcsQ0FBQyxDQUFBO0FBQ1YsS0FBSyxDQUFDLFVBQVUsQ0FBQyxDQUFBIn0=