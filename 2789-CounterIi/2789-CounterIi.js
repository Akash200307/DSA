// Last updated: 2/3/2026, 9:36:23 PM
/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let defa=init
    return{
        increment:()=>++init,
        decrement:()=>--init,
        reset:()=>init=defa

    }

};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */