/**
 * Wikipedia:
 * In vector calculus and physics, a vector field is an
 * assignment of a vector to each point in a subset of space.
 */
class TensorField {
    constructor(f) {
        this.f = f;
    }
    call(vector) {
        return this.f(vector);
    }
    add(vf) {
        return new VectorField(
            function add(f1, f2, x) {
                return f1(x).add(f2(x));
            }.bind(null, this.f, vf.f));
    }
    sub(vf) {
        return new VectorField(function sub(f1, f2, x) {
            return f1(x).sub(f2(x));
        }.bind(null, this.f, vf.f));
    }
    mul(vf) {
        return new VectorField(function mul(f1, f2, x) {
            return f1(x).mul(f2(x));
        }.bind(null, this.f, vf.f));
    }
    neg() {
        return new VectorField(function neg(f, x) {
            return f(x).neg();
        }.bind(null, this.f));
    }
    vadd(v) {
        return new VectorField(function vadd(f1, v, x) {
            return f1(x).add(v);
        }.bind(null, this.f, v));
    }
    vsub(v) {
        return new VectorField(function vsub(f1, v, x) {
            return f1(x).sub(v);
        }.bind(null, this.f, v));
    }
    vmul(v) {
        return new VectorField(function vmul(f1, v, x) {
            return f1(x).mul(v);
        }.bind(null, this.f, v));
    }
}

class VectorField extends {

}

function vadd2(v) {return v.radd(2)}
function vsub1(v) {return v.rsub(1)}

var vf1 = new VectorField(vadd2);
var vf2 = new VectorField(vsub1);
var vf3 = vf2.add(vf1)

var v = Vector.of(1, 0);

console.log(vf1.call(v));
console.log(vf2.call(v));
console.log(vf3.call(v));

/**
.load tensor.js
.load vector.js
.load VectorField.js
*/