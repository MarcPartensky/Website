function clear(text) {
    return text.replace(/…/g, '...')
        .replace(/&#x27;/g, "\'")
        .replace(/—/g, '-')
        .replace(/❝/g, '')
        .replace(/❞/g, '')
        .trim()
}
const vue = new Vue({
    el: "#app",
    delimiters: ["[[", "]]"],
    data: {
        textbox: clear(document.getElementById('textbox').innerHTML),
        textinput: "",
        start: undefined,
        left: Infinity,
        averageWordLetters: 6,
        done: false,
    },
    methods: {
        finish() {
            if (!this.check()) {
                alert("You must correct all of your mistakes.")
            } else if (this.textinput.length !== this.textbox.length) {
                alert("You must finish typing.")
            } else {
                this.done = true;
                clearInterval(this.$interval);
            }
        },
        change() {
            alert()
        },
        getTextInputLength() {
            return unescape(this.textinput).length;
        },
        getTextBoxLength() {
            return unescape(this.textbox).length;
        },
        getRatio() {
            return Math.round(this.getTextInputLength()/this.getTextBoxLength()*100);
        },
        getWPM() {
            if (this.textinput.length>0 && this.start==undefined) {
                this.start = Date.now()
                this.$interval = setInterval(() =>
                {
                    this.left = Math.round(this.getTextBoxLength()-(Date.now()-this.start)/1000);
                },1000)
            }
            if (this.textinput==0) {
                this.start = undefined;
                return 0;
            }
            return Math.round(60*this.textinput.split(' ').length/(Date.now()-this.start)*1000)
        },
        check() {
            return unescape(this.textinput) === unescape(this.textbox).slice(0, unescape(this.textinput).length);
        },
        getTextBox() {
            return unescape(this.textbox);
        },
        getTextInput() {
            return unescape(this.textinput);
        },
    },
})
