function loadeditor(language)
	{
		if(language=="python")
			$('#editor').html("#Write your code here\n");
		else
			$('#editor').html("//Write your code here\n");
		var editor = ace.edit("editor");
		var mode="ace/mode/"+language;
		editor.getSession().setMode(mode);
		$('#editor').focus();   
	}

function doCompile()
	{
		$('#status').html("Compiling..");
		var editor = ace.edit("editor");
		
		//Make an ajax call with these parameters
		write_code = editor.getSession().getValue(); //Code
		test_case = document.getElementById('input').value; //Input
		token = document.getElementsByName('csrfmiddlewaretoken')[0].value;	//Token
		
		$.post
		(
			"/ccr/compile/",
			{
			csrfmiddlewaretoken:token,
			code:write_code,
			input:test_case
			},
			function(data,status)
				{
					$('#response').html(data);
				}
		);
	}

function doRun()
	{
		$('#status').html("Executing..");
		var editor = ace.edit("editor");
		write_code = editor.getSession().getValue();
		token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
		test_case = document.getElementById('input').value;
		$.post
		(
			"/ccr/run/",
			{
			csrfmiddlewaretoken : token,
			code:write_code,
			input:test_case
			},
			function(data,status)
			{
				$('#response').html(data);
				//$('#status').html("Execution Completed..");
			}
		);

	}