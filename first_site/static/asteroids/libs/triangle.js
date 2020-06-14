class Triangle extends Polygon {
  constructor(matrix, ...args) {
    super(matrix, ...args)
  }
  get area() {
    const a,b,c = this.segments.map(s => s.length());
    return 1/4*Math.sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c));
  }
}
