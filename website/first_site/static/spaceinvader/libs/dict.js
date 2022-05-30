/**
 * Python like dictionary in javascript
 * - btw:
 * The keys in Map are ordered. Thus, when iterating over it,
 * a Map object returns keys in order of insertion. And so
 * it is for this dictionary class.
 * - also:	
 * Performs better in scenarios involving frequent additions
 * and removals of key-value pairs.
 */
class Dict extends Map {
    static fromIterables(iterable) {



    }
    get items() {
        return this.entries();
    }
    /**
     * Same as dict.setdefault in python.
     * @param {Any} key 
     * @param {Any} value 
     */
    setDefault(key, value) {
        if (!this.has(key)) {
            this.set(key, value);
        }
        
    }
    /**
     * Same as dict.update in python
     * @param {IterableCouples, ArrayOfCouples, Map, Dict} entries 
     */
    update(entries) {
        for (const [k,v] in entries) {
            if (!this.has(k)) {
                this.set(k, v);
            }
        }
    }
    /**
     * Same as update but it is syntactic sugar.
     * @param  {...Couple} entries 
     */
    setDefaults(...entries) {
        this.update(entries);
    }
    imap(f) {
        for (const [k,v] in this) {
            this.set(k, f(v));
        }
    }
    map(f) {
        const dict = new this();
        for (const [k,v] in this) {
            dict.set(k, f(v));
        }
        return dict;
    }
}
