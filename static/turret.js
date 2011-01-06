TURRET_SERVER = 'http://itd-armel/';

function feedback(s) {
    $('#feedback').text(s);
}

$(document).ready(function() {
	$('#panleft').mousedown(function() {
		$.get(TURRET_SERVER,
		      {'item': 4,
			      'duration': 0,
			      'newState': 1});
		})
	    .mouseup(function() {
		    $.get(TURRET_SERVER,
			  {'item': 4,
				  'duration': 0,
				  'newState': 0});
		});

	$('#panright').mousedown(function() {
		$.get(TURRET_SERVER,
		      {'item': 4,
			      'duration': 0,
			      'newState': 2});
		})
	    .mouseup(function() {
		    $.get(TURRET_SERVER,
			  {'item': 4,
				  'duration': 0,
				  'newState': 0});
		});

	$('#tiltangle').change(function() {
		$.get(TURRET_SERVER,
		      {'item': 1,
			      'duration': 0,
			      'newState': $('#tiltangle').val()});
	    });

	$('#fireonce').click(function() {
		$.get(TURRET_SERVER,
		      {'item': 2,
			      'duration': '0.3',
			      'newState': 1,
			      'defState': 0});
	    });

	$('#fireburst').click(function() {
		$.get(TURRET_SERVER,
		      {'item': 2,
			      'duration': '0.8',
			      'newState': 1,
			      'defState': 0});
	    });

	$('#blinklight').click(function() {
		$.get(TURRET_SERVER,
		      {'item': '3',
			      'duration': $('#blinkduration').val(),
			      'newState': '1',
			      'defState': '0'},
		      function() {
			  feedback('command sent');
		      });
	    });
	$('#pan').click(function() {
		$.get(TURRET_SERVER,
		      {'item': '4',
			      'duration': $('#panduration').val(),
			      'newState': $('#pandirection').val(),
			      'defState': 0},
		      function() {
			  feedback('panning...');
		      });
	    });
	$('#tilt').click(function() {
		$.get(TURRET_SERVER,
		      {'item': 1,
			      'duration': 0,
			      'newState': $('#servoangle').val()},
		      function() {
			  feedback('tilting...');
		      });
	    });
	$('#fire').click(function() {
		$.get(TURRET_SERVER,
		      {'item': 2,
			      'duration': $('#fireduration').val(),
			      'newState': 1,
			      'defState': 0},
		      function() {
			  feedback('firing...');
		      });
	    });
	/*
	$('#sendraw').click(function() {
		$.get(TURRET_SERVER,
		      {'item': $('#rawitem').val(),
			      'duration': $('#rawduration').val(),
			      'newState': $('#rawnewstate').val(),
			      'defState': $('#rawdefstate').val()},
		      function() {
			  feedback('command sent');
		      });
	    });
	*/

	
    });
