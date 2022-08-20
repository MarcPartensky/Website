class List extends Array {
    constructor(...items) {
        super(...items);
    }
    remove(items) {
    }
    delete(index) {

    }
    contains(item) {

    }
    str() {
        return String(this);
    }
    append = this.push;
    extend = this.concat;
    len = this.length;
}