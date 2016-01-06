function getfilename()
{
file_name = document.getElementById('file_name').value;
if(file_name!="")
	savefile();
else
	$('#file_save').show();
}
function savefile()
	{

		$("#status").html("Status : Saving File..");
		var editor = ace.edit("editor");
		//Make an ajax call with these parameters
		write_code = editor.getSession().getValue(); //Code
		test_case = document.getElementById('input').value; //Input
		file_name = document.getElementById('file_name').value;
		token = document.getElementsByName('csrfmiddlewaretoken')[0].value;	//Token
		if(file_name=="")
		{
			alert("Please enter a file name.");
			return false;
		}
		$.post
		(
			"/ccr/save/",
			{
			csrfmiddlewaretoken:token,
			code:write_code,
			input:test_case,
			file:file_name
			},
			function(data,status)
				{
					$('#status').html(data);
				}
		);
		$('#file_save').hide();
		return false;
	}

function sharecode()
{
	$("#sharing").show();
	$("#sharing").html("Sharing..");
	//Make ajax request
	var editor = ace.edit("editor");
	write_code = editor.getSession().getValue(); //Code
	test_case = document.getElementById('input').value; //Input
	token = document.getElementsByName('csrfmiddlewaretoken')[0].value;	//Token
		
	$.post
		(
			"/ccr/share/",
			{
			csrfmiddlewaretoken:token,
			code:write_code,
			input:test_case,
			},
			function(data,status)
				{
					$('#sharing').html("Link : "+data);
				}
		);
}