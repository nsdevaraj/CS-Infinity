
// FIBONNOCI

// fib(0) = 0

const  fib1 = (n) => {
    if(n<3) return 1;
    return fib1(n-1)+fib1(n-2);
} 

const  fib2 = (n,moi={1:1,2:1}) => {
    if(n in moi) return moi[n];
    return (moi[n] = fib2(n-1,moi)+fib2(n-2,moi));
}


const  fib3 = (n) =>{
    tab = Array(n+1).fill(0);
    tab[1] = 1;
    for(let i=2;i<=n;++i){
        tab[i] = tab[i-1]+tab[i-2];
    }
    return tab[n];

};

const  fib4 = (n) => {
    if(n<3) return 1;
    bck2 = 1 , bck1 = 1;
    for(let i=3;i<=n;++i){
        [bck1, bck2] = [bck2,bck2+bck1];
    }
    return bck2;
};

/*
console.log(fib1(2)) //=> 1
console.log(fib1(6)) //=> 8
console.log(fib1(7)) //=> 13
console.log(fib1(8)) //=> 21
//console.log(fib(50)) //=> 12586269025

console.log(fib2(2)) //=> 1
console.log(fib2(6)) //=> 8
console.log(fib2(7)) //=> 13
console.log(fib2(8)) //=> 21
console.log(fib2(50)) //=> 12586269025 

console.log(fib3(2)) //=> 1
console.log(fib3(6)) //=> 8
console.log(fib3(7)) //=> 13
console.log(fib3(8)) //=> 21
console.log(fib3(50)) //=> 12586269025 

console.log(fib4(1)) //=> 1
console.log(fib4(6)) //=> 8
console.log(fib4(7)) //=> 13
console.log(fib4(8)) //=> 21
console.log(fib4(50)) //=> 12586269025 
*/



// GRID TRAVELLER

const grid1 = (n,m,moi={'1,1':1}) =>{
    if(n==0 || m==0) return 0;
    
    key = n+','+m
    rkey = m+','+n;

    if(key in moi) return moi[key];
    if (rkey in moi) return moi[rkey];

    return grid1(n-1,m)+grid1(n,m-1);

}

/*
const grid2 = (m,n) =>{
    const tabl = Array(m+1).fill().map(()=>Array(n+1).fill(0));
    tabl[1][1] = 1;
    for(let i=1;i<=m;i++){
        for(let j=1;j<=n;j++){
            tabl[i,j] += tabl[i-1,j]+tabl[i,j-1];
        }
    }
    return tabl;
}
*/


/*
console.log(grid1(1,1)); //=> 1
console.log(grid1(2,3)); //=> 3
console.log(grid1(3,2)); //=> 3
console.log(grid1(3,3)); //=> 6
*/

/*
console.log(grid2(1,1)); //=> 1
console.log(grid2(2,3)); //=> 3
console.log(grid2(3,2)); //=> 3
console.log(grid2(3,3)); //=> 6
*/

//+ tab grid traveler updated

const gridTraveler = (m,n) => {
    const table = Array(m+1)
        .fill()
         .map(
            () => Array(n+1).fill(0)
        );
    
    table[1][1] = 1;
 
    for(let i=1;i<= m;i++){
        for(let j=1;j<= n;j++){
            table[i][j] +=  table[i-1][j] + table[i][j-1];
        }
    }
    
    return table[m][n];        
 }
 
 console.log(gridTraveler(1,1)); //=> 1
 console.log(gridTraveler(2,3)); //=> 3
 console.log(gridTraveler(3,2)); //=> 3
 console.log(gridTraveler(3,3)); //=> 6


 
// grid2 which i wrote test is not working , see it out ..
