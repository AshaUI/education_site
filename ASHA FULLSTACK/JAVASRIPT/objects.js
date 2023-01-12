var std=
{
  sno:102,
  sname:'sasi',
  sage:23,
  smarks:[60,70,80,90],
  sstatus:true,
  saddress:
  {
    drno:123,
    street:"kphb",
    city:'hyd',
    pin:500072
  }


};
//console.log(std.sno);//it gives only single value,to access multiple values we use loops
//for in loop
for(j in std)
{
    console.log(`${j}  is  ${std[j]}`);
}
//for addrss
//for(j in std.saddress)
//{
    console.log(`${j} is ${std.saddress[j]}`)
//}