//arrays is collection of multiple variables with same type is is also called 
//ex:array has 4 elmnts strtng inx 0 and length is 4
var x=[100,200,300,400]
//we can create arrya in 3 ways
//1.array literal 
var x=[100,200,300,400]
//fr printing all elmnts we use for loop
for(i=0;i<x.length;i++){
   console.log(x[i])
}
//  2.array directly 
var stds=new Array();
stds[0]='Raj'
stds[2]='Sam'
stds[3]='Ram'
stds[4]='Raji'
//fr printing all elemnts we are using while loop
j=0;   //initialisation
while(j<stds.length){  //condition check
   console.log(stds[j])
   j++        //increment
}

// 3.array constructor (literal+directly)
var emp=new Array(100,200,300)

//Array.of()-array construction
console.log(Array.of(2, false, 'test', {'name': 'Alex'}));
//o/p: 0: 2 1: false 2: "test" 3: {name: 'Alex'}length:4
//--------------ARRAY METHODS------------------------------

//push(): adding elements/element to an array at end
var alpha=new Array('a','b','c','d','e'); 
alpha.push('f','g'); 
console.log("after push:",alpha);  //o/p:['a','b','c','d','e','f','g']


//unshift(): adding elements/element to an array at begining
var alpha=new Array('a','b','c','d','e');
alpha.unshift('f','g'); 
console.log("after unshift:",alpha);  //o/p:['f','g','a','b','c','d','e']


//pop(): removing elements/element from an array at end var alpha=new Array('a','b','c','d','e'); 
var alpha=new Array('a','b','c','d','e'); 
alpha.pop();
console.log(alpha)  //o/p:['a','b','c','d','e']]


//shift(): removing elements/element from an array at beginning
var alpha=new Array('a','b','c','d','e'); 
alpha.shift(); 
console.log("after shift",alpha)  //o/p:['b','c','d','e']

//splice(): insertion and removal in between array elements. syntax:array.splice(start index,delete count,elements );
var alpha=new Array('a','b','c','d','e'); 
alpha.splice(2,2,'x','y'); 
console.log(alpha);  //o/p:['a', 'b', 'x', 'y', 'e']   //o/p:a,b,c,d,e


//join(): joins all the elements of the array using a separator and returns a string
var alpha=['a','b','c','d','e'] 
var joined=alpha.join(); 
console.log(joined);   //o/p:a,b,c,d,e

//fill():The fill() method fills an array with a static value,
var colors=['red','blue','black'];
colors.fill('pink');   //o/p:['pink', 'pink', 'pink']
console.log(colors);//fill() //method changes the original array//includes():checking presence on an element in an array,if finds returns ' true' otrws 'false'
var names = ['tom', 'alex', 'bob', 'john'];
names.includes('tom');  //o/p: true

//indexOf() returnd index position of elemnt
var names = ['tom', 'alex', 'bob', 'john']; 
console.log(names.indexOf('john')); //o/p: 1 
console.log( names.indexOf('sam')); //o/p:-1  bcs ther is no 'sam'

//reverse():reverses the array
var names = ['tom', 'alex', 'bob', 'john'];
names.reverse()
console.log(names);  //o/p: ['john', 'bob', 'alex', 'tom']

//sort() --ascending order accrd alphabts and numbrs
var names = ['tom', 'alex', 'bob', 'john']; 
names.sort()
console.log(names); // o/p:['alex', 'bob', 'john', 'tom']; 

var num=[12,23,34,4,5,67,68,79]; 
num.sort()
console.log(num); //o/p:[4,5,12,23,34,67,68,79]

var num=[12,23,34,4,5,67,68,79];
num.sort(); 
console.log(num)

  //static array methods
 
var alpha=['a','b','c','d','e'];
for (i=0;i<alpha.length;i++);
{
console.log(alpha[i]);
}

let students = [
    {
       'id': 001,
       'f_name': 'Alex',
       'l_name': 'B',
       'gender': 'M',
       'married': false,
       'age': 22,
       'paid': 250,  
       'courses': ['JavaScript', 'React']
    },
    {
       'id': 002,
       'f_name': 'Ibrahim',
       'l_name': 'M',
       'gender': 'M',
       'married': true,
       'age': 32,
       'paid': 150,  
       'courses': ['JavaScript', 'PWA']
    },
    {
       'id': 003,
       'f_name': 'Rubi',
       'l_name': 'S',
       'gender': 'F',
       'married': false,
       'age': 27,
       'paid': 350,  
       'courses': ['Blogging', 'React', 'UX']
    },
   
 ];
 //filter()----------------

const femaleStudents = students.filter((element, index) => {
    return element.gender === 'F';})
    console.log(femaleStudents);

    const fullNames = students.map((element, index) => {
        return {'fullName': element['f_name'] + ' ' + element['l_name']}
      });
      
      console.log(fullNames);
//reduce()-------------
      const total = students.reduce(
        (accumulator, student, currentIndex, array) => {
           accumulator = accumulator + student.paid;
           return (accumulator);
        }, 
     0);
     
     console.log(total); // 1000
//some()---------------
     let hasStudentBelow30 = students.some((element, index) => {
        return element.age < 30;
      });
      
      console.log(hasStudentBelow30); // true
//find()------------
      const student = students.find((element, index) => {
        return element.age < 30;
      });
//every()-------------
      console.log(student);
      const atLeastTwoCourses = students.every((elements, index) => {
        return elements.courses.length >= 2;
      });
      
      console.log(atLeastTwoCourses); // true
//at()--------------------
      const Alpha = ['a','b','c','d','e','f','g','h'];
      console.log(Alpha.at(0)); // a
      console.log(Alpha.at(3)); // d
      console.log(Alpha.at(-1)); // h
      console.log(Alpha.at(-5)); // d
      console.log(Alpha.at(-8)); // a
      console.log(Alpha.at(10)); // undefined
      

      

     