//inheritance with method overriding
//parent class

class Student{
Studentname;
Studentage;
constructor(sname,sage)
{this.Studentname=sname;
 this.Studentage=sage
}
greet(){
    return "parent class welcoming you"
}
//child class
}
class asha extends Student{
    Studentmarks;
    constructor(sname,sage,smarks){ //including super class prprts also here
        super(sname,sage)//calling super class constructor prprties and get back to child
    this.Studentmarks=smarks;
    }
    greet()
    {
        
        return `${super.greet()},child class welcoming you`
    }
}

var std=new asha('ASHA',26,88)
console.log(std.Studentname); //invoking all chld and prnt class attributes
console.log(std.Studentage)
console.log(std.Studentmarks)//invoking
console.log(std.greet())//invoking parent class methd along with child class method(method overloading)

