(function() {
	var ghostPositions = [
		[200, 30],
		[190, 120],
		[210, 240],
		[200, 350],
		[195, 490]
	];
	var stage = document.getElementById('stage');
	var ghostList = stage.getElementsByTagName('span');
	for (var i = 0; i < ghostList.length; i += 1) {
		ghostList[i].style.top = ghostPositions[i][0] + 'px';
		ghostList[i].style.left = ghostPositions[i][1] + 'px';
	}
})();










