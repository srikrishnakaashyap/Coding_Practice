const fs = require("fs");

fs.readFile("file1.txt", "utf8", function (err, data) {
  if (err) throw err;
  console.log("The text in the file:\n\n", data, "\n");

  var lines = data.split("\n");

  //console.log("total lines---", lines.length);

  // readLines(0, lines);

  // console.log("Total Lines---", Totallines);

  readWords(0, lines);

  var words = 0;

  var characters = 0;

  lines.map((lines1) => (words = words + lines1.split(" ").length));

  for (let i = 0; i < lines.length; i++) {
    var splitLines = lines[i].split(" ");

    splitLines.map((word) => (characters = characters + word.length));
  }

  console.log("total lines--using map-", lines.length);

  console.log("total words--using map-", words);

  console.log("total characters--using map-", characters);

  let result = {
    "Total lines using Recursion": lines.length,
    "Total words using Recursion": Totalwords,
    "Total characters using Recursion": Totalcharacters,
  };
  console.table(result);
});
