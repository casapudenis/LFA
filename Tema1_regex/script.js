function checkPattern() {
    var pattern = document.getElementById("pattern").value;
    var text1 = document.getElementById("text1").value;
    var text2 = document.getElementById("text2").value;

    if (!pattern.trim()) {
        document.getElementById("result").textContent = "Pattern is empty!";
        return;
    }
    
    try {
        new RegExp(pattern);
    } catch (error) {
        document.getElementById("result").textContent = "Pattern error!";
        return;
    }

    var result = document.getElementById("result");
    result.textContent = "";

    if (text1.match(new RegExp(pattern))) {
        result.textContent += "Text1 is matching with the pattern!\n";
    } else {
        result.textContent += "Text1 is not matching with the pattern!\n";
    }

    var matches = text2.match(new RegExp(pattern, "g"));
    if (matches) {
        var matchesHeader = document.createElement("p");
        matchesHeader.textContent = "Text2 matches:";
        result.appendChild(matchesHeader);
        var matchesList = document.createElement("ul");
        matches.forEach(function(match) {
            var listItem = document.createElement("li");
            listItem.textContent = match;
            matchesList.appendChild(listItem);
        });
        result.appendChild(matchesList);
    } else {
        var text2Message = document.createElement("p");
        text2Message.textContent = "Matches not found in Text2!";
        result.appendChild(text2Message);
    }
}
