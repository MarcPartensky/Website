class GameMap {
    static fromSize(n,m) {
        const x=-n/2, y=-n/2, w=n, h=n;
        const r  = new Rectangle(new Vector(x, y), new Vector(w, h))
        return new this(r);
    }
    constructor(rectangle) {
        this.rectangle = rectangle;
    }
    
    get r() {
        return this.rectangle;
    }
    set r(value) {
        this.rectangle = value;
    }


    
    compute(position) {
        let x,y
        if (Math.abs(position.x) > this.r.w / 2) {
            let delta = position.x % this.r.w / 2;
            delta = 0;
            x = -(position.x/Math.abs(position.x)) * (this.r.w / 2) + delta;
        } else {
            x = position.x;
        }

        if (Math.abs(position.y) > this.r.h / 2) {
            let delta = position.y % this.r.h / 2;
            delta = 0;
            y = -(position.y/Math.abs(position.y)) * (this.r.h / 2) + delta;
        } else {
            y = position.y;
        }
        return new Vector(x, y);
    }
    
    compute2(position) {
        const t = this.r.size.rdiv(2);
        // console.log(position)
        // console.log(t)
        // position.iradd(t);
        position.x += this.r.w/2;
        position.y += this.r.h/2;
        position.x = position.x % this.r.w;
        position.y = position.y % this.r.h;
        position.x -= this.r.w/2;
        position.y -= this.r.h/2;
        // position.irsub(t);
        return position;
    }

    
    
    limit(entities) {
        for (const entity of entities) {
            entity.position = this.compute(entity.position);
        }
    }
    
    show(ctx) {
        this.rectangle.show(ctx)
    }

    
    update(dt) {

        }
}