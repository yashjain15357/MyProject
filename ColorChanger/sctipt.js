const button = document.querySelectorAll('.button');
console.log(button);

    const body = document.querySelector('body');
    button.forEach(element => {
        // console.log(element);
        element.addEventListener('click', (e) => {
            console.log(e);
            console.log(e.target);
            if (e.target.id == "black") {
                // document.querySelector('body').style.background=e.target.id
                body.style.background = e.target.id
                
                document.querySelector('h1').style.color = "white"
                document.querySelector("h1").style.border = "5px solid white";
                let index = 0;
                const borders = ["5px solid red", "5px solid blue", "5px solid green", "5px solid purple","5px solid white"];

                setInterval(() => {
                    document.querySelector("h1").style.border = borders[index];
                    index++;
                    if (index === borders.length) {
                        index = 0;
                    }
                }, 200); // Change the border every second (1000 milliseconds)


            }
            else if (e.target.id == "white") {
                // document.querySelector('body').style.background=e.target.id
                body.style.background = e.target.id

            }
            else if (e.target.id == "green") {
                // document.querySelector('body').style.background=e.target.id
                body.style.background = e.target.id

            }
            else if (e.target.id == "pink") {
                // document.querySelector('body').style.background=e.target.id
                body.style.background = e.target.id

            }
            else if (e.target.id == "red") {
                // document.querySelector('body').style.background=e.target.id
                body.style.background = e.target.id

            }

        })

    });

