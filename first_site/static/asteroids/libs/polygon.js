class Polygon extends BasePolygon {
    static color = "#ffffff";
    static width=null;
    static fill=false;
    static w=3; // number of points (triangle)
    static h=2; // number of components (2d)
    static s=1; // size factor
    static random(
        w=Polygon.w,
        h=Polygon.h,
        s=Polygon.s,
        color=Polygon.color,
        width=Polygon.width,
        fill=Polygon.fill
    ) {
        let m = new Matrix(w);
        let v = Vector.random(w, 0, s);
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
        super(color, width, fill);
        this.matrix = Matrix.from(matrix);
    }
    get points() {
        return Array.from(this.matrix);
    }
    set points(points) {
        this.matrix.set(points);
    }
    move(x, y) {

    }
    get segments() {
        const segments = [];
        let p = this.matrix[this.matrix.length-1];
        for (const pi of this.matrix) {
            segments.push(new Segment(p, pi));
            p = pi;
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
    /**
     * Determine if the polygon contains a point
     * @param {*} point 
     */
    contains(p) {
        const points = this.matrix;
        var isInside = false;
        var minX = points[0].x, maxX = points[0].x;
        var minY = points[0].y, maxY = points[0].y;
        for (let n = 1; n < points.length; n++) {
            let q = points[n];
            minX = Math.min(q.x, minX);
            maxX = Math.max(q.x, maxX);
            minY = Math.min(q.y, minY);
            maxY = Math.max(q.y, maxY);
        }
        if (p.x < minX || p.x > maxX || p.y < minY || p.y > maxY) {
            return false;
        }
        let i = 0, j = points.length - 1;
        for (i, j; i < points.length; j = i++) {
            if ( (points[i].y > p.y) != (points[j].y > p.y) &&
                    p.x < (points[j].x - points[i].x) * (p.y - points[i].y) / (points[j].y - points[i].y) + points[i].x ) {
                isInside = !isInside;
            }
        }
        return isInside;
    }
}
