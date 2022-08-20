class MeteorGroup extends Grouper(Meteor) {
    static meteorShower(n) {
        let wtf = [];
        for (let pas = 0; pas < n; pas++) {
            wtf.push(["meteor:"+pas, Meteor.random()]);
        }
        return new this(wtf);
    }
}
