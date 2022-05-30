class Tree extends Map {
    paths(path=[]) {
        const ps = [];
        for (const [k, v] of this) {
            if (v instanceof Tree) {
                ps.push(...v.paths(path+[k]));
            } else {
                ps.push(path+[k]);
            }
        }
        return ps;
    }
    iforEach(f) {
        for (const [k,v] of this) {
            f(this[k]);
        }
    }
    imap(f) {
        for (const [k, v] of this) {
            this[k] = f(v);
        }
    }
    irmap(f) {
        for (const [k, v] of this) {
            if (v instanceof Tree) {
                v.irmap(f);
            } else {
                this[k] = f(v);
            }
        }
    }

    traverse() {

    }
    filter(condition) {
        const l = [];
        for (const [k,v] of this) {
            if (condition(k, v)) {
                l.push(v);
            }
            if (v instanceof Tree) {
                l.push(...v.filter(key));
            }
        }
        return l;
    }
    findOne(key) {
        for (const [k,v] of this) {
            if (k==key) {
                return v;
            }
            if (v instanceof Tree) {
                return v.findOne(k);
            }
        }
    }
    findAll(key) {
        const l = [];
        for (const [k,v] of this) {
            if (k==key) {
                l.push(v);
            }
            if (v instanceof Tree) {
                l.push(...v.findAll(key));
            }
        }
        return l;
    }
    rget(path, v) {
        const k = path[0];
        path = path.slice(1);
        if (path.length==0) {
            return this.get(k);
        } 
        return this.get(k).rget(path);
    }
    rset(path, v) {
        const k = path[0];
        path = path.slice(1);
        if (path.length==0) {
            return this.set(k, v);
        }
        return this.get(k).rset(path);
    }
}

t = new Tree([[1,2],[3,new Tree([[1,2]])]]);