class BasePolygon extends Form {
    constructor(color, lineWidth, fill) {
        super();
        this.color = color;
        this.lineWidth = lineWidth;
        this.fill = fill;
    }
    // get vectors() {
    //     throw "A base polygon must have a points getter."
    // }
    // set vectors() {
    //     throw "A base polygon must have a points getter."
    // }
    get points() {
        throw "A base polygon must have a points getter."
    }
    set points(pts) {
        throw "A base polygon must have a points setter."
    }
    translate(vector) {
        throw "A base polygon must have a translate method."
    }
    move(...vector) {
        this.translate(Vector.from(vector));
    }
    get length() {
        return this.points.length;
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
        const points = this.points;
        ctx.beginPath();
        ctx.moveTo(...points[points.length-1]);
        for (const pt of points) {
            ctx.lineTo(...pt);
        }
        ctx.closePath();
        if (this.fill) {
            ctx.fill();
        } else {
            ctx.stroke();
        }
    }
    get center() {
        return Vector.average(...this.points);
    }
    set center(point) {
        const v = point.sub(this.center)
        this.translate(v);
    }
    get segments() {
        const segments = [];
        const points = this.points;
        let p = points[this.points.length-1];
        for (const pi of points) {
            segments.push(new Segment(p, pi));
            p = pi;
        }
        return segments;
      }
    set segments(segs) {
        // this is naive mapping,
        //because the information is redundant
        this.points = segs.map(s => s.p1);
    }
    showPoints(ctx) {
        for (const point of this.points) {
            point.show(ctx);
        }
    }
    showSegments(ctx) {
        for (const segment of this.segments) {
            segment.show(ctx);
        }
    }
    get area() {
        
    }
    get perimeter() {
        return Math.sum(this.segments.map(s => s.length));
    }
    contains2(point) {
        // make a segment which must cross the polygon.
        // then check if it crosses.
        const s = new Segment(point, point.radd(0, this.perimeter))


    }
    contains(p) {
        const points = this.points;
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
    collide(polygon) {
        for (const p of polygon.points) {
            if (this.contains(p)) {
                return true;
            }
        }
        return false;
    }
}