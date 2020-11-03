import Vector from './vector.js';

/*
* Color namespace.
*/
var Color = {
  /*
  * Return a random color.
  */
  random: function() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i=0; i<6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  },
  /*
  * Create a vector using a color.
  */
  toVector: function(color) {
    const letters = '0123456789ABCDEF';
    let v = new Vector();
    for (let i=0; i<3; i++) {
      let a = letters.indexOf(color[2*i+1].toUpperCase());
      let b = letters.indexOf(color[2*i+2].toUpperCase());
      v.push(a*16+b);
    }
    return v;
  },
  /*
  * Create a color using a vector.
  */
  fromVector: function(vector) {
    const letters = '0123456789ABCDEF';
    let v = vector.floor();
    let color = "#";
    for (let i=0; i<3; i++) {
      let b = v[i]%16;
      let a = (v[i]-b)/16;
      color += letters[a];
      color += letters[b];
    }
    return color;
  },

  /*
  * Mix the given colors together.
  */
  mix: function(...colors) {
    let vectors = colors.map(Color.toVector);
    let vector = Vector.average(...vectors);
    return Color.fromVector(vector);
  },
  /*
  * Ligthen a given color using some k factor which must be between 0 and 1.
  */
  lighten: function(color, k=0.5) {
    let v = Color.toVector(color);
    let m = new Vector(255, 255, 255);
    let d = m.sub(v);
    d.irmul(k);
    v.iadd(d);
    return Color.fromVector(v);
  },
  /*
  * Ligthen a given color using some k factor which must be between 0 and 1.
  */
  darken: function(color, k=0.5) {
    let v = Color.toVector(color);
    let d = Vector.copy(v);
    d.irmul(k);
    v.isub(d);
    return Color.fromVector(v);
  },
  /*
  * Interpolate a color between a list of couples (color,value) using a t parameter between 0 and 1.
  */
  interpolate: function(couples, t) {
    let i = 0;
    while (t>couples[i][1]) {
      i+=1;
    }
    let v1 = Color.toVector(couples[i-1][0]);
    let v2 = Color.toVector(couples[i][0]);
    t = Color.linear(t, couples[i-1][1], couples[i][1], 0, 1);
    return Color.fromVector(v1.rmul(1-t).add(v2.rmul(t)));
  },
  linear: function(x, e1, e2, s1, s2) {
    return (x-e1)/(e2-e1)*(s2-s1)+s1;
  },
}
