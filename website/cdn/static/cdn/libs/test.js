export function test(f, args=[], iterations=10**6) {
    const start = performance.now();
    for(let i=0; i<iterations; i++ ){
        f(...args);
    };
    return performance.now() - start;
}


export function compare(f1, f2, args=[], n=10**6, comparison=(x,y)=>x/y) {
    const t1 = test(f1, args, n);
    const t2 = test(f2, args, n);
    return comparison(t1,t2);
}

export function analyse(fs=[], args=[], iterations=10**6) {
    const results = [];
    for(let i=0; i<fs.length; i++ ){
        results.push(test(fs[i],args,iterations));
    };
    const m = Math.max(...results);
    for(let i=0; i<fs.length; i++ ){
        results[i]/=m;
    };

    return results;
}