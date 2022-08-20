import Tensor from './tensor.js';

let t1 = new Tensor1([1,2], [3,4]);
let t2 = new Tensor1([3,4], [5,6]);

let ta = t1.add(t2);
console.log("addition:", ta);

let tn = t1.neg();
console.log("negation:", tn);


let ts = t1.sub(t2);
console.log("substraction:", ts);

let format = [1,2,3];
console.log(Tensor1.zero(format));

// iadd
// isub
// imul
