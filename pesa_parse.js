function parseSingleMessage() {
    var message = document.getElementById("singleMessage").value;
    document.getElementById("singleMessageResult").innerHTML = "<p>Parsed single message: " + message + "</p>";
}

function parseMultipleMessages() {
    var file = document.getElementById("multiMessages").files[0];

    if (file) {
        var reader = new FileReader();
        reader.onload = function (e) {
            var content = e.target.result;
            var messages = content.split("\n");
            var result = "<h3>Parsed Messages:</h3>";
            messages.forEach(function (message) {
                result += "<p>" + message + "</p>";
            });
            document.getElementById("multiMessagesResult").innerHTML = result;
        };
        reader.readAsText(file);
    }
}

