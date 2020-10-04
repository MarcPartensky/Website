function map2str(map) {
    let str = "{";
    for (const [key, value] of map) {
        str += key;
        str += ":"
        str += String(value);
        str += ","
    }
    return str.slice(0, str.length-1)+"}";
}

function str2map(str) {
    str = str.replace("{","").replace("}","");
    let m = new Map();
    let key, value;
    for (const parameters of str.split(",")) {
        [key, value] = parameters.split(":")
        m.set(key, eval(value));
    }
    return m;
}

function tree2str(tree) {
    str = "{";
    for (const [key, value] of tree) {
        str += key;
        str += ":"
        if (value instanceof Map) {
            str += tree2str(String(value))
        } else {
            str += value;
        }
        str += ","
    }
    return str.slice(0, str.length-1)+"}";
}



function prod(...values) {
    if (values.length>1) {
        return values[0] * prod(...values.slice(1, values.length));
    } else {
        return values[0];
    }
}

function round(r, n) {
    return Math.round(r*10**n)/10**n;
}

let sigmoid = (x) => 1/(1+Math.exp(-x));

function hash(s){
    return s.split("").reduce(function(a,b){a=((a<<5)-a)+b.charCodeAt(0);return a&a},0);              
}