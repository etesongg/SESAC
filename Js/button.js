function number_inc() {
    result = document.getElementById('result')
    let current = result.innerText;
    current++;
    result.innerText = current;
}
function number_dec() {
    result = document.getElementById('result')
    let current = result.innerText;
    current--;
    result.innerText = current;
}   