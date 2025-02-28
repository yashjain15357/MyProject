let randomNumber = parseInt(Math.random() * 100 + 1);
let pg = [];
let rg = 9;
let tn = 1;
let start = true;
const para = document.querySelectorAll('p');
const div = document.querySelector('#print');
const userInput = document.querySelector('#input');
const button = document.querySelector('#button');
const res = document.querySelector('#restart');

// Add event listener for the restart button at the beginning
res.addEventListener("click", function () {
    // Reset all variables
    randomNumber = parseInt(Math.random() * 100 + 1);
    pg = [];
    rg = 9;
    tn = 1;
    start = true;

    // Clear all messages and input
    para[0].innerHTML = "Start guessing!";
    para[1].innerHTML = "Previous guesses: ";
    para[2].innerHTML = "Turn Number: ";
    para[3].innerHTML = "Remaining guesses: ";
    div.innerHTML = ""; // Clear the congratulations message
    userInput.value = "";
    button.disabled = false; // Enable the guess button
    console.log("Game restarted!");
});

// Main game logic
if (start) {
    button.addEventListener("click", function (e) {
        e.preventDefault();
        const int = parseInt(userInput.value);
// console.log(e.preventDefault())
        function validNumber(int) {
            if (isNaN(int)) {
                alert('Enter a valid number');
                para[0].innerHTML = "Enter a valid number";
            } else if (int > 100) {
                para[0].innerHTML = "Number is greater than 100: " + int;
                alert("Enter a valid number");
            } else if (int < 1) {
                para[0].innerHTML = "Number is smaller than 1: " + int;
                alert("Enter a valid number");
            } else {
                pg.push(int);
                para[1].innerHTML = "Previous guesses: " + pg.join(", ");
                para[2].innerHTML = "Turn Number: " + tn++;
                para[3].innerHTML = "Remaining guesses: " + rg--;
                para[1].style.backgroundColor = "#212121";
                userInput.value = "";
            }
        }

        function cong(int) {
            if (int === randomNumber) {
                para[0].innerHTML = "Your guess is correct!";
                const newElement = document.createElement("h1");
                newElement.textContent = "🎉 Congratulations! 🎉";
                newElement.style.color = "rgb(28, 182, 14)";
                newElement.style.textShadow = "0 0 10px rgba(28, 182, 14, 0.8)";
                div.appendChild(newElement);
                button.disabled = true; // Disable the guess button
                correctSound.play(); // Play correct sound

                // Change background color
                document.body.style.backgroundColor = "rgb(28, 182, 14)";
            } else if (int < randomNumber) {
                para[0].innerHTML = "Your guess is too low!";
                // wrongSound.play(); // Play wrong sound
            } else if (int > randomNumber) {
                para[0].innerHTML = "Your guess is too high!";
                // wrongSound.play(); // Play wrong sound
            }
        }

        function end(tn) {
            if (tn === 11 || rg < 0 || int === randomNumber) {
                para[0].innerHTML = `<h2>Game over! The correct number was: ${randomNumber}</h2>`;
                button.disabled = true; // Disable the guess button
                start = false; // End the game
            }
        }

        if (start) {
            validNumber(int);
            cong(int);
            end(tn);
        }
    });
}
