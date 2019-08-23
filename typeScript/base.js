var Product = /** @class */ (function () {
    function Product() {
    }
    Product.prototype.sayHi = function () {
        console.log('sayhi');
    };
    Product.prototype.sayHello = function () {
        console.log('sayHello');
    };
    Product.productName = 'hehe';
    return Product;
}());
var baozi = new Product();
console.log(Product.productName);
baozi.sayHi();
baozi.sayHello();
