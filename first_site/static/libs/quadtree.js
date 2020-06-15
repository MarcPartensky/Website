class Quadtree {
    /*
    format :
        recursive case:
            tree = [tree1, tree2, tree3, tree4]
        base case:
            tree = [point1, point2, ...]
        
        point = [x, y]
        2|3
        0|1
    */
    constructor(tree=new Map(), chart=new Map(), nodes=3) {
        this.tree = tree;
        this.chart = chart;
        this.nodes = nodes;
    }
    create(points) {
        this.borders = this.getBorders(points);
        this.size = this.getSize(this.borders);
        this.tree = this.divide(points, ...this.size);
    }
    divide(points, sx, sy, hx=0, hy=0, n=0) {
        if (points.length<this.nodes) {return points}
        if (n>10) {return points}
        n += 1;
        sx /= 2;
        sy /= 2;
        const xmin = this.borders[0];
        const ymin = this.borders[1];
        const tree = new Map([
            [0, []], [1, []], [2, []], [3, []]
        ]);
        for (const [x, y] of points) {
            if (y<hy+sx+ymin) {
                if (x<hx+sy+xmin) {
                    tree.get(0).push([x, y]);
                } else {
                    tree.get(1).push([x, y]);
                }
            } else {
                if (x<hx+xmin) {
                    tree.get(2).push([x, y]);
                } else {
                    tree.get(3).push([x, y]);
                }
            }
        }
        // console.log(points.length, n, sx, hx);
        let x, y;
        for (let i=0; i<4; i++) {
            if (tree.get(i).length==0) {
                tree.delete(i);
            } else {
                x = i%2;
                y = Math.floor(i/2);
                console.log(i, x, y);
                tree.set(i, 
                    this.divide(
                        tree.get(i), sx, sy, hx+sx*x, hy+sx*y, n
                    )
                );
            }
        }
        return tree;
    }
    access(path) {
        let tree = this.tree;
        while (path.lenth!=0) {
            tree = tree.get(path.pop());
        }
        return tree;
    }
    getBorders(points) {
        let xmin = Infinity;
        let ymin = Infinity;
        let xmax = -Infinity;
        let ymax = -Infinity;
        for (const [x, y] of points) {
            xmin = Math.min(xmin, x);
            ymin = Math.min(ymin, y);
            xmax = Math.max(xmax, x);
            ymax = Math.max(ymax, y);
        }
        return [xmin, ymin, xmax, ymax];
    }
    getSize(borders) {
        return [borders[2]-borders[0], borders[3]-borders[1]];
    }
    getPoints(tree) {
        const points = [];
        return points;
    }
    contains(x, y, r) {

    }

    
}


function test(n=1000) {
    let pts = [];
    for (let i=0; i<n; i++) {
        pts.push([Math.random(), Math.random()]);
    }

    let q = new Quadtree();
    q.create(pts);
    return q;
}

