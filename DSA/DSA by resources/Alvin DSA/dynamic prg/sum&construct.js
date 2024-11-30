a
const canSum1 = (sum,pos,moi={}) =>{
    if(sum == 0) return true;
    if(sum < 0) return false;
    if(sum in moi) return moi[sum];

    for(i of pos){
        if(canSum1(sum-i,pos,moi) == true) return true;
    }
    return moi[sum] = false;
}

const canSum2 = (sum,pos) =>{
    tab = Array(sum+1).fill(false);
    tab[0] = true;
    for (let i=0;i<sum;++i){
        if(tab[i] == true){
            for(j of pos){    
                tab[i+j] = true;
            }
        }
    }
    return tab[sum];
}



/*

console.log(canSum1(7,[2,3]))     //=> true
console.log(canSum1(7,[5,3,4,7])) //=> true
console.log(canSum1(7,[2,4]))     //=> false
console.log(canSum1(8,[2,3,5]))   //=> true
console.log(canSum1(300,[7,14]))  //=> false 

console.log();

console.log(canSum2(7,[2,3]))     //=> true
console.log(canSum2(7,[5,3,4,7])) //=> true
console.log(canSum2(7,[2,4]))     //=> false
console.log(canSum2(8,[2,3,5]))   //=> true
console.log(canSum2(300,[7,14]))  //=> false 

*/


const howSum1 = (sum,pos,moi={0:[]}) =>{
    if(sum == 0) return [];
    if(sum < 0) return null;
    if(sum in moi) return moi[sum];
    for(i of pos){
        combi = howSum1(sum-i,pos,moi);
        if( combi != null){
            moi[sum] = [...combi,i];
        }
    }
    return (moi[sum] = null);
}

const howSum2 = (sum,pos) =>{
    tab = Array(sum+1).fill(null);
    tab[0] = [];
    for(let i=0;i<sum;i++){
        if(tab[i] != null){
            for(j of pos){
                tab[i+j] = [j,...tab[i]];
            }            
        }
    }
    return tab[sum];
}




console.log(howSum1(7,[2,3]))     //=> [3,2,2]
console.log(howSum1(7,[5,3,4,7])) //=> [4,3]
console.log(howSum1(7,[2,4]))     //=> null
console.log(howSum1(8,[2,3,5]))   //=> [2,2,2,2]
console.log(howSum1(300,[7,14]))  //=> null 

console.log()

/*

console.log(howSum2(7,[2,3]))     //=> [3,2,2]
console.log(howSum2(7,[5,3,4,7])) //=> [4,3]
console.log(howSum2(7,[2,4]))     //=> null
console.log(howSum2(8,[2,3,5]))   //=> [2,2,2,2]
console.log(howSum2(300,[7,14]))  //=> null 

*/


/*

const bestSum1 = (sum,pos,moi={}) =>{

    if(sum == 0) return [[]];
    if(sum < 0) return null;
    if( sum in moi) return moi[sum];

    for(i of pos){
        combi = bestSum1(sum-i,pos,moi);
        if(combi != null && moi[sum] == undefined){
            moi[sum] = combi;
        }
        if( combi != null  && combi.length < moi[sum] ){
            moi[sum] = [...combi,i];
        }
    }
    return moi[sum];
}

const bestSum2 = (sum,pos) =>{
    tab = Array(sum+1).fill([]);
    tab[0] = [];


}




console.log(bestSum1(7,[2,3]))     //=> [2,2,3]
console.log(bestSum1(7,[5,3,4,7])) //=> [7]
console.log(bestSum1(7,[2,4]))     //=> null
console.log(bestSum1(8,[2,3,5]))   //=> [3,5]
console.log(bestSum1(8,[3,5,2]))   //=> [3,5]
console.log(bestSum1(8,[1,4,5]))   //=> [4,4]
console.log(bestSum1(300,[7,14]))  //=> null 
console.log(bestSum1(100,[1,2,5,25]))//=> [ 25, 25, 25, 25 ]

*/



// CONSTRUCT

/*

const canConstruct1 = () =>{
    
};

const canConstruct2 = () => {

};

console.log(canConstruct("abcdef",['ab','abc','cd','def','abcd']));     //=> true           
console.log(canConstruct("skateboard",['bo','rd','ate','t','ska','sk','boar']));//=> false
console.log(canConstruct("enterapotentpot",['a','p','ent','enter','ot','o','t']));//=> true
console.log(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee',
    'eeeeeeee',
]))   //=> false  

*/


