function getfilename()
	{
		file_name = document.getElementById('file_name').value;
		if(file_name!="")
		{
			savefile();
			if(file_name=="template")
				{
					$('#status').html("Status : Ready");
					document.getElementById('file_name').value = "";
					$('#file_save').show();
				}
		}
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
		name = "File : saved/" + file_name + ".cpp";
		$('#file_name_label').html(name)
		return false;
	}

function loadeditor(language)
	{
		$("#file_save").hide();
		$("#sharing").hide();
		if(language=="python")
			$('#editor').html("#Write your code here\n");
		else
			$('#editor').html("//Write your code here\n");
		var editor = ace.edit("editor");
		var mode="ace/mode/"+language;
		editor.getSession().setMode(mode);
		token = document.getElementsByName('csrfmiddlewaretoken')[0].value;	//Token
		$('#editor').focus();   
		$.post
		(
			"/ccr/template/",
			{
				csrfmiddlewaretoken:token,
			},
			function(data,status)
			{
				if(data!="")
					editor.setValue(data);
			}
		)
		$('#editor').focus();
	}

function doCompile()
	{
		$('#status').html("Status : Compiling..");
		var editor = ace.edit("editor");
		
		//Make an ajax call with these parameters
		write_code = editor.getSession().getValue(); //Code
		test_case = document.getElementById('input').value; //Input
		token = document.getElementsByName('csrfmiddlewaretoken')[0].value;	//Token
		utoken = document.getElementById('uniquetoken').value;	//To distinguish different tabs
		
		$.post
		(
			"/ccr/compile/",
			{
			csrfmiddlewaretoken:token,
			uniquetoken:utoken,
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
		$('#status').html("Status : Executing..");
		var editor = ace.edit("editor");

		//Make an ajax call with these parameters
		write_code = editor.getSession().getValue();
		test_case = document.getElementById('input').value;
		token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
		utoken = document.getElementById('uniquetoken').value;

		$.post
		(
			"/ccr/run/",
			{
			csrfmiddlewaretoken : token,
			uniquetoken:utoken,
			code:write_code,
			input:test_case
			},
			function(data,status)
				{
					$('#response').html(data);
				}
		);
	}