let person = {
    name: 'John',
    age: 25,
    greet: function() {
      console.log('Hello, ' + this.name + '!');
    }
  };
  
  console.log(person.name);
  console.log(person.age);
  person.greet();