window.onload = init;

function init() {
	var button = document.getElementById("addButton");
	button.onclick = handleButtonClick;
}

function handleButtonClick() {
	var textInput = document.getElementById("songTextInput");
	var songName = textInput.value;

	var fileInput = document.getElementById("songFileInput");
	var filePath = fileInput.src;
	if (songName == "") {
		alert("还未输入音乐名！");
	} else {
		var li = document.createElement("li");
		li.innerHTML = filePath;
		var ul = document.getElementById("playlist");
		ul.appendChild(li);
	}
}

