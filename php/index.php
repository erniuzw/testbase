<!doctype html>
<html>
<head>
	<meta charset="utf-8" />
	<title>测试区</title>
</head>
<body>
	<h1>AJAX</h1>
	<button onclick="loadXML();">Request Data</button>
	<div id="display"></div>
	<?php
	// phpinfo();
	// echo date('H:i, js F')
	?>
	
	<script>
	function loadXML() {
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = function() {
			if (xmlhttp.readyState==4 && xmlhttp.status==200) {
				document.getElementById('display').innerHTML = xmlhttp.responseText;
			}
		}
		xmlhttp.open("GET","ajax_info.txt",true);
		xmlhttp.send();
	}
	</script>	
</body>
</html>
