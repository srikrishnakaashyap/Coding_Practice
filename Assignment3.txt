const fs = require("fs");

var Totallines = 0;

var Totalwords = 0;

var Totalcharacters = 0;

function readWords(currentIndex, lines) {
  if (currentIndex == lines.length) return;

  var currentLine = lines[currentIndex].split(" ");

  Totalwords = Totalwords + currentLine.length;

  readCharacters(currentLine, 0);

  readWords(currentIndex + 1, lines);
}

function readCharacters(word, currentIndex) {
  if (currentIndex == word.length) return;

  Totalcharacters = Totalcharacters + word[currentIndex].length;

  readCharacters(word, currentIndex + 1);
}

fs.readFile("file3.txt", "utf8", function (err, data) {
  if (err) throw err;
  console.log("File Contents:\n\n", data, "\n");

  var lines = data.split("\n");

  readWords(0, lines);

  var words = 0;

  var characters = 0;

  lines.map((lines1) => (words = words + lines1.split(" ").length));

  for (let i = 0; i < lines.length; i++) {
    var splitLines = lines[i].split(" ");

    splitLines.map((word) => (characters = characters + word.length));
  }

  console.log("Number of Lines--using map-", lines.length);

  console.log("Number of Words--using map-", words);

  console.log("Number of Characters--using map-", characters);

  let result = {
    "Total lines using Recursion": lines.length,
    "Total words using Recursion": Totalwords,
    "Total characters using Recursion": Totalcharacters,
  };
  console.table(result);
});
