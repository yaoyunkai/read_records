let name = 'Nicholas';
let age = 36;

if (typeof name === 'undefined') {
    let name;
}

name = 'Matt';

try {
    console.log(age);
} catch (error) {
    let age;
}

age = 26;
