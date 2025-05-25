const dropArea = document.getElementById("dropArea");
const imageInput = document.getElementById("imageInput");

// Prevent default behaviors
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, e => e.preventDefault());
    dropArea.addEventListener(eventName, e => e.stopPropagation());
});

// Highlight on drag
['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, () => dropArea.classList.add('hover'));
});

// Remove highlight
['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, () => dropArea.classList.remove('hover'));
});

// Handle dropped files
dropArea.addEventListener('drop', e => {
    const files = e.dataTransfer.files;
    if (files.length && files[0].type === 'image/png') {
        imageInput.files = files;
    } else {
        alert("Only PNG files are supported.");
    }
});




// JavaScript Version of Python Image Steganography Encoder (in-browser PNG LSB encoding)
// This version assumes the use of HTML5 canvas and file input elements.
// It encodes 9-bit binary representations of characters into the least significant bits of RGB pixels.

// Define character to 9-bit binary map



const getCharToBinaryMap = {
    "A": "001000001", "B": "001000010", "C": "001000011", "D": "001000100",
    "E": "001000101", "F": "001000110", "G": "001000111", "H": "001001000",
    "I": "001001001", "J": "001001010", "K": "001001011", "L": "001001100",
    "M": "001001101", "N": "001001110", "O": "001001111", "P": "001010000",
    "Q": "001010001", "R": "001010010", "S": "001010011", "T": "001010100",
    "U": "001010101", "V": "001010110", "W": "001010111", "X": "001011000",
    "Y": "001011001", "Z": "001011010", "0": "000110000", "1": "000110001",
    "2": "000110010", "3": "000110011", "4": "000110100", "5": "000110101",
    "6": "000110110", "7": "000110111", "8": "000111000", "9": "000111001",
    " ": "000100000", "~": "001111110", "!": "000100001", "@": "001000000",
    "#": "000100011", "$": "000100100", "%": "000100101", "^": "001011110",
    "&": "000100110", "*": "000101010", "(": "000101000", ")": "000101001",
    "_": "001011111", "+": "000101011", "-": "000101101", "=": "000111101",
    "{": "001111011", "}": "001111101", "[": "001011011", "]": "001011101",
    "|": "001111100", "\\": "001011100", ":": "000111010", ";": "000111011",
    "\"": "000100010", "'": "000100111", "<": "000111100", ">": "000111110",
    "?": "000111111", ",": "000101100", ".": "000101110", "/": "000101111",
    "`": "001100000"
};
let imageData = null; // This will hold the image pixel data
let ctx = null;
document.getElementById('imageInput').addEventListener('change', function (e) {
    const file = e.target.files[0];
    const img = new Image();
    const canvas = document.getElementById('canvas');
    ctx = canvas.getContext('2d');

    img.onload = function () {
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0);

        imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
        const data = imageData.data;

        console.log('First pixel RGBA:', data[0], data[1], data[2], data[3]);
    };

    img.src = URL.createObjectURL(file);
});

function decode() {
    if (!imageData) {
        alert("Please upload an image first!");
        return;
    }

    const binaryToChar = {};
    for (const [char, binary] of Object.entries(getCharToBinaryMap)) {
        binaryToChar[binary] = char;
    }

    const data = imageData.data;
    let binaryString = "";
    let decodedMessage = "";
    const charLength = 9;
    let bir = ""
    for (let i = 0; i < data.length; i++) {
        const colorValue = data[i];
        binaryString += (colorValue % 2).toString();

        if (binaryString.length === charLength) {
            if (binaryString === "111111111") {
                bir += binaryString
                break;
            }

            if (binaryToChar[binaryString]) {
                decodedMessage += binaryToChar[binaryString];
                bir += binaryString
            }
            binaryString = "";

        }

    }
    console.log(bir)

    decodedMessage = decodedMessage.trim().toLowerCase();
    decodedMessage = decodedMessage.charAt(0).toUpperCase() + decodedMessage.slice(1);
    // alert("Decoded message: " + decodedMessage);
    document.getElementById("message").value = decodedMessage
}

