class Vector {
  constructor(components) {
    this.components = components;
  }
  show(canvas){

  }
  neg() {
    const components = [];
    this.components.forEach(component => {
      components.push(-component);
    });
    return new Vector(components);
  }
  add(vector) {
    length = Math.max(this.components.length, vector.components.length);
    const components = [];
    for (let i=0; i<length; i++) {
      components.push(this.components[i]+vector.components[i]);
    }
    return new Vector(components);
  }
  sub(vector) {
    return this.add(vector.neg())
  }
  rmul(scalar) {
    const components = [];
    this.components.forEach(component => {
      components.push(scalar * component);
    });
    return new Vector(components);
  }
}

// export default Vector;

//
// a = new Vector([1,2,3]);
// b = new Vector([3,2,1]);
// v1 = b.sub(a);
// v2 = a.rmul(5);
//
// // console.log(v.components);
//
// alert(v2.components);
