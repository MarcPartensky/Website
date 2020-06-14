class Polygon extends Figure {
    static color = "#ffffff";
    static width=null;
    static fill=false;
    static w=3; // number of points (triangle)
    static h=2; // number of components (2d)
    static s=10; // size factor
    static random(
        w=Polygon.w,
        h=Polygon.h,
        s=Polygon.s,
        color=Polygon.color,
        width=Polygon.width,
        fill=Polygon.fill
    ) {
        let m = new Matrix(w);
        let v = Vector.random(w, 0, 1);
        v.irdiv(v.sum);
        let a = 0;
        for (let i=0; i<w; i++) {
            a += v[i];
            m[i] = Vector.polar(s * Math.random(), 2*Math.PI*a);
        }
        return new this(m, color, width, fill);
    }
    constructor(
        matrix,
        color=Polygon.color,
        width=Polygon.width,
        fill=Polygon.fill,
    ) {
        super();
        this.matrix = Matrix.from(matrix);
        this.color = color;
        this.width = width;
        this.fill = fill;
    }
    get points() {
        return Array.from(this.matrix);
    }
    set points(points) {
        this.matrix.set(points);
    }
    get length() {return this.matrix.length;}
    move(x, y) {

    }
    get segments() {
        const segments = [];
        const p = this.matrix[0];
        for (const pi of this.matrix) {
            segments.push(new Segment(p, pi));
        }
        return segments;
      }
    get center() {
        return Point.average(...this.matrix);
    }
    set center(point) {
        const v = point.sub(this.center)
        this.translate(v);
    }

    get angle(){
        //Retourne l'angle du polygone, lors de la création du polygone, celui-ci vaut 0
        const c = this.center;
        const p = this.points[0];
        return p.sub(c).angle;
    }

    set angle(r) {
        this.rotate(r-this.angle);
    }



    translate(vector) {
        this.matrix.map(v => v.translate(vector));
    }
    rotate(angle, point=Point.zero) {
        this.matrix.map(v => v.rotate(angle, point));
    }
    show(ctx) {
        if (this.fill) {
            ctx.fillStyle = this.color;
        } else {
            ctx.strokeStyle = this.color;
        }
        if (this.lineWidth) {
            ctx.lineWidth = this.lineWidth;
        }
        ctx.beginPath();
        ctx.moveTo(...this.matrix[this.matrix.length-1]);
        for (const pt of this.matrix) {
            ctx.lineTo(...pt);
        }
        ctx.closePath();
        if (this.fill) {
            ctx.fill();
        } else {
            ctx.stroke();
        }
    }
    get length() {
        return this.segments.reduce((s1, s2) => s1.length+s2.length);
    }
    get area() {

    }
    /**
     * Determine if the polygon contains a point
     * @param {*} point 
     */
    contains(point) {
        const s = new Segment(point, point.radd(0, ))


    }
}
