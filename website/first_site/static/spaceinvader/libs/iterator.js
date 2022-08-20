function permutation(array) {
    const l = array.length,
        used = Array(l),
        data = Array(l);
    return function* backtracking(pos) {
        if(pos == l) yield data.slice();
        else for(let i=0; i<l; i+=1) if(!used[i]) {
            used[i] = true;
            data[pos] = array[i];
            yield* backtracking(pos+1);
            used[i] = false;
        }
    }(0);
}
function permuted(array) {
    return [...permutation(array)];
}


function* range(...args) {
    let end;
    let start = 0;
    let step = 1;
    if (args.length == 1) {
        [end] = args;
    } else if (args.length == 2) {
        [start, end] = args;
    } else if (args.length == 3) {
        [start, end, step] = args;
    } else {
        throw new RangeError("Invalid number of arguments.");
    }
    for (let i = start; i < end; i+=1) {
        yield i;
    }
}

function ranged(...args) {
    return [...range(...args)];
}

function *enumerate(array) {
    for (let i = 0; i < array.length; i+=1) {
       yield [i, array[i]];
    }
 }

 function enumerated(array) {
     return [...enumerate(array)];
 }


 function *zip (...iterables){
    let iterators = iterables.map(i => i[Symbol.iterator]() )
    while (true) {
        let results = iterators.map(iter => iter.next() )
        if (results.some(res => res.done) ) return
        else yield results.map(res => res.value )
    }
}

function zipped(...iterables) {
    return [...zip(...iterables)]
}

function last(array) { return array[array.length - 1]; }

function* numericCombinations(n, r, loc = []) {
    const idx = loc.length;
    if (idx === r) {
        yield loc;
        return;
    }
    for (let next of range(idx ? last(loc) + 1 : 0, n - r + 1 + idx)) { yield* numericCombinations(n, r, loc.concat(next)); }
}

function numericCombinated(n, r) {
    return [...numericCombinations(n, r)];
}

function* combinations(array, r) {
  for (let idxs of numericCombinations(array.length, r)) { yield idxs.map(i => array[i]); }
}


function combinated(array, r) {
    return [...combinations(array, r)];
}

function count() {
    let index = 0;
    return {
        next: function(){
            return {value: index++, done: false};
        }
    }
}

function repeat(value, n=Infinity) {
    let i = 0;
    return {
        next: function(){
            i+=1;
            return {value: value, done: i>=n};
        }
    }
}

function cycle(array) {
    let index = 0;
    return {
        next: function(){
            return {value: array[(index++)%array.length], done: false};
        }
    }
}
