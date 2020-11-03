/**
 * More responsible array.
 * Inspired from python.
 */
export default class List extends Array {
    removeOne(item, n=undefined) {
        let i = 0;
        while (i < this.length) {
            if (this[i] === item) {
            this.splice(i, n);
            } else {
                ++i;
            }
        }
    }
    removeMany(items, n=undefined) {
        for (const item in items) {
            this.removeOne(item, n);
        }
    }
    remove(...items) {
        this.removeMany(items);
    }
    deleteOne(index, n=undefined) {
        this.splice(index, n);
    }
    deleteMany(indices, n=undefined) {
        for (const index of indices) {
            this.splice(index, n);
        }
    }
    delete(...indices) {
        this.deleteMany(indices);
    }
    contains(item) {
        for (const item_ of this) {
            if (item==item_) {
                return true;
            }
        }
        return false;
    }
    str() {
        return String(this);
    }
    append = this.push;
    extend = this.concat;
    len = this.length;
}