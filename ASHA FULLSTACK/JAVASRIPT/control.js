//control statements  are 2 types
//1. conditions  2. looping statements
//------conditional statements are 4 types  simple if,if else,else if, neste
var marks;
var marks=99;


switch(true)
{
    case  marks>=90: grade ="A grade";
    break;
    case marks>=70 && marks<90:  grade ="B grade";
    break;
    case marks>=65 && marks<70: grade ="C grade";
    break;
    case marks>=35 && marks<65: grade ="D grade";
    break;
    case marks<35 :grade="FAIL"
    break;
    default:grade="invalid grade"
}
console.log(grade)
//---------------------------------------------------------------
var marks;
var marks=99;
switch(marks)
{
    case  33: grade ="A grade";
    break;
    case 44:  grade ="B grade";
    break;
    case 88: grade ="C grade";
    break;
    case 99: grade ="D grade";
    break;
    case 77 :grade="FAIL"
    break;
    default:grade="invalid grade"
}
console.log(grade)