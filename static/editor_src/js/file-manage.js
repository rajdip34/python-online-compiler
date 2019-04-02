autoSaveDelayInMilisec=10*(10**3);
updateChartDelayInMilisec=100;


var autoSaveTimer=null;
var updateChartDelayTimer=null;
chartlastid=0;
chartdb={};
currentPath = "";
widgets=[];
currentBreak=-1;
debuggerState=false;
initialFileSavingState=true;

$.fn.afterPaste = function (options) {
	var settings = {
		delay: 300,
		callback: function () {} };

	options = $.extend(settings, options);
	return this.each(function () {
		var $element = $(this);
		$element.on('paste', function () {
			setTimeout(options.callback, options.delay);
		});

	});
};


$(document).ready(function () {
	currentPath = $(".add-folder-root").attr('data-path')+"/newfile-"+makeid()+".py";
	new $.bonsai($('.bonsai'));
	$("#filess").change(function() {
  		file = this.files[0];
  		if (file) {
		    var reader = new FileReader();
		    reader.readAsText(file, "UTF-8");
		    reader.onload = function (evt) {
		    	$.post('commander',{'type':'uploadfile','name':file.name,'text':evt.target.result},function (d) {
		    		out = $(d);
		        	set_events(out);
		        	$(".bonsai>.section").append(out);
		    		updateLibsAndMethods();
		    	});
		    }
		    reader.onerror = function (evt) {
		        alert("Error on uploading file named "+file.name)
		    }
		}
	});

	$("#run_full").click(function(e) {
		e.stopImmediatePropagation();
		if(debuggerState){
			alert("Please stop debug feature, first.")
			return;
		}
		chartdb={};
		clearTimeout(updateChartDelayTimer);
		chartlastid=0;
		ccc.data['datasets'][0]['data']=[0];
		ccc.data['labels']=[0];
		text = '';

		len = editorHolder.doc.lineCount();
		for (var i = 0 ; i < len; i++)
			text += editorHolder.doc.getLine(i) + "\n";

		const regex = /dbconf(\s)*=(\s)*{(\s)*"user"(\s)*:(\s)*"([a-zA-Z0-9_]*)"(\s)*,(\s)*"pass"(\s)*:(\s)*"(.*)"(\s)*,(\s)*"name"(\s)*:(\s)*"([a-zA-Z0-9_]*)"(\s)*,(\s)*"host"(\s)*:(\s)*"([a-zA-Z0-9_.]*)",?(\s)*}/gm;

		let m;
 
		while ((m = regex.exec(text)) !== null) {
		    if (m.index === regex.lastIndex)
		        regex.lastIndex++;
		    
		    m.forEach((match, groupIndex) => {
		        if (groupIndex==6)
		        	chartdb['user'] = `${match}`;
		        if (groupIndex==11)
		        	chartdb['pass'] = `${match}`;
		       	if (groupIndex==16)
		        	chartdb['name'] = `${match}`;
		        if (groupIndex==21)
		        	chartdb['host'] = `${match}`;
		    });
		}

		if(JSON.stringify(chartdb) === JSON.stringify({})) {
			$.post('commander', {'type':'backtest','code':text}, function (data) {
				data = JSON.parse(data)
				values = data.values;
				labels = data.labels;
				// console.log(data)
				for (var i = 0; i < values.length ; i++) {
					ccc.data['labels'].push(values[i]['date'])
					ccc.data['datasets'][0]['data'].push(values[i]['price']);
				}	

				$("#line .status > *").remove()
				for (var i = 0; i < labels.length ; i++) {
					$("<div />").append("<p>"+labels[i].title+"&nbsp;&nbsp;</p><p>"+labels[i].value+"</p>").appendTo("#line .status");				
				}	
				ccc.update();
			});
		}else{
			$.post('commander',{'type':'backtest','code':text},function (d) {
				$("#log_detail pre").html(d)
			})
			updateChart();
		}
		

	});


	$("#run").click(function(e) {
		e.stopImmediatePropagation();
		if(debuggerState){
			alert("Please stop debug feature, first.")
			return;
		}
		text = '';
		len = editorHolder.doc.lineCount();
		for (var i = 0 ; i < len; i++)
			text += editorHolder.doc.getLine(i) + "\n";

		$.post('commander',{'type':'run','code':text},function (d) {
			$("#log_detail pre").html(d)
		});
		e.preventDefault();
		return false;
	});

	$("#save_btn").click(function (e) {
		text = '';
		len = editorHolder.doc.lineCount();
		for (var i = 0 ; i < len; i++)
			text += editorHolder.doc.getLine(i) + "\n";
		$.post('commander',{'type':'savefile','path':currentPath,'text':text},function(d){
			if($(".bonsai").html().indexOf(currentPath)==-1){
				out = $(d);
				out.addClass('hsel');
		    	set_events(out);
	    		$(".bonsai>.section").append(out);
	    	}
			updateLibsAndMethods();
			doautosave();
		});
		e.stopImmediatePropagation()
	})

	$("#folderrss").change(function() {
		for (var i = this.files.length-1; i >= 0; i--) {
			var reader = new FileReader();
		    reader.readAsText(this.files[i], "UTF-8");
		    reader.onloadend = (function(file) {
		      return function(evt) {
		        $.post('commander',{'type':'uploadfolder','name':file.webkitRelativePath,'text':evt.target.result},function (d) {
		        	// updateLibsAndMethods();
		        	out = $(d.replace('\n',''));
		        	out.find(".file, .folder").each(function () {
		        		set_events($(this));
		        	});
		        	$(".bonsai>.section").append(out);
		        });
		      };
		    })(this.files[i]);
		    reader.onerror = function (evt) {
		        alert("Error on uploading file named "+file.name)
		    }
		    if(i==0){
		    	l = this.files[i].webkitRelativePath.split("/")[0];
		    	LoadNavFolder(l)
		    }
		}
	});

	$(".file, .folder").each(function () {
		set_events($(this))
	});
	$(".add-folder-root").click(function (e) {
		path = $(this).attr('data-path');
		$.post('commander',{'type':'newfolder','path':path},function (d) {
			out = $(d);
			set_events(out)
			$('.bonsai>.section').append(out);
			// el.addClass('open');
			// el.find('.cus-dd').removeClass('open')

			updateLibsAndMethods();
		});
		e.stopImmediatePropagation();
	})
	$(".add-file-root").click(function (e) {
		path = $(this).attr('data-path');
		initialFileSavingState = false;
		$.post('commander',{'type':'newfile','path':path}, function (d) {
			out = $(d);
			set_events(out);
			$(".bonsai>.section").append(out);
			out.find(">a").click();
			updateLibsAndMethods();
		});
		e.stopImmediatePropagation();
	});

	
	$('#editor').afterPaste({delay: 200,callback: function () {
		doautosave();
		doautodebug();
	}});

	$("#debug").click(function (e) {
		if(debuggerState){
			alert("Please stop the debugger first.")
			return;
		}
		debuggerState=true;
		currentBreak = 0;
		editorHolder.setOption("readOnly",true)
		$("#debug_detail").addClass("show");
		updateGutterRed();
		doautodebug();
		e.stopImmediatePropagation();
	})
	$("#back").click(function (e) {
		if(!debuggerState) return false;
		if (currentBreak>0)
			currentBreak--;
		else
			currentBreak=editorHolder.doc.lineCount()-1;
		updateGutterRed();
		doautodebug();
		e.stopImmediatePropagation();
	})
	$("#step").click(function (e) {
		if(!debuggerState) return false;
		if (currentBreak<editorHolder.doc.lineCount()-1)
			currentBreak++;
		else
			currentBreak = 0;
		updateGutterRed();
		doautodebug();
		e.stopImmediatePropagation();
	})
	$("#stop").click(function (e) {
		autoDebugMutex = false;
		debuggerState = false;
		currentBreak = -1;
		$("#debug_detail").removeClass("show");
		$("#log_detail pre").html('')
		editorHolder.setOption("readOnly",false)
		updateGutterRed();
		e.stopImmediatePropagation();
		doautosave();
	})
	

});

function updateGutterRed() {
	$(".CodeMirror-linenumber").removeClass("breakpoint")

	if (currentBreak==-1)
		return;

	$(".CodeMirror-linenumber").each(function(){
		if ($(this).html()==currentBreak+1) $(this).addClass('breakpoint');
	})
}

chartLockMutex=false;
function updateChart() {
	if (chartLockMutex) return;
	chartLockMutex = true;
	updateChartDelayTimer = null;
	$.post('chartdata',{
		'last': 		chartlastid,
		"start_date": 	$("#start").val(),
		"end_date": 	$("#end").val(),
		"money": 		$("#money").val(),
		"user": 		chartdb["user"],
		"pass": 		chartdb["pass"],
		"name": 		chartdb["name"],
		"host": 		chartdb["host"]
	},function (d) {
		chartlastid = d.last;
		data = d.data;
		for (var i = 0; i < data.length ; i++) {
			ccc.data['labels'].push(data[i]['date'])
			ccc.data['datasets'][0]['data'].push(data[i]['price']);
		}	
		ccc.update();
		updateChartDelayTimer=setTimeout(updateChart,updateChartDelayInMilisec);
		chartLockMutex=false;
	});
}

function LoadNavFolder(l) {
	setTimeout(function () {
		$.post("nav_folder?"+(new Date()).getTime(),{"folder":l},function (d) {
			out = $(d)
			out.find(".file").each(function () {
        		set_events($(this));
        	});
        	set_events(out);
        	out.find('>a').click(function () {
        		$(this).parent().toggleClass('open')
        	});
        	out.find(".folder").each(function () {
        		set_events($(this));
        		$(this).find('>a').click(function () {
        			$(this).parent().toggleClass('open')
        		})
        	});
			$(".bonsai>.section").append(out);
		});
		updateLibsAndMethods();
	},1000);
}

function updateLibsAndMethods() {
	$.getScript("python_libs_js?"+(new Date()).getTime());
}

function set_events(elm) {
	// console.log(el)
	elm.find(".rename").click(function (e) {
		el = $(this).closest('[data-path]')
		path = el.attr('data-path');

		if(path==currentPath){
			if(debuggerState){
				alert("Please stop debug feature, first.")
				return;
			}
			clearTimeout(autoSaveTimer);
		}

		arr = path.split("/")
		name = arr[arr.length-1];
		$("#rename_name").val(name);

		$("#rename_modal").modal('show');
		$("#rename_btn").click(function (e) {
			$.post('commander',{'type':'rename','current':path,'name':$("#rename_name").val()},function (d) {
				s = d.split(",");
				el.attr('data-path',s[1]);
				an = el.find('>a span');
				an.html(s[0]);
				// console.log(newname,an,path,el)
				$("#rename_modal").modal('hide');
				if(path==currentPath){
					currentPath = s[1];
					$(".fil-nam-dis span").html("&nbsp;&nbsp;"+s[0]);
					doautosave();
				}
				
		
			});
			e.stopImmediatePropagation();	
			updateLibsAndMethods();
		});
		$("#rename_modal").on('keyup', function (e) {
		    if (e.keyCode == 13) {
		        $("#rename_btn").click();
		    }
		});
		e.stopImmediatePropagation();
	});
	elm.find(".del").click(function (e) {
		el = $(this).closest('[data-path]')
		path = el.attr('data-path');

		if(path==currentPath){
			if(debuggerState){
				alert("Please stop debug feature, first.")
				return;
			}
			clearTimeout(autoSaveTimer);
		}

		arr = path.split("/")
		name = arr[arr.length-1];

		$("#delete_filename").html(name);
		$("#delete_modal").modal('show');

		$("#delete_btn").click(function (e) {
			$.post('commander',{'type':'delete','path':path},function (d) {
				el.remove();
				if(path==currentPath){
					editorHolder.doc.setValue("");
					editorHolder.doc.clearHistory();
					$(".add-file-root").click();

				}
			});
			$("#delete_modal").modal('hide');
			e.stopImmediatePropagation();	
			updateLibsAndMethods();
		});
		$("#delete_modal").on('keyup', function (e) {
		    if (e.keyCode == 13) {
		        $("#delete_btn").click();
		    }
		});
		e.stopImmediatePropagation();
	});

	elm.find(".add-file").click(function (e) {
		el = $(this).closest('[data-path]')
		path = el.attr('data-path');
		initialFileSavingState = false;
		$.post('commander',{'type':'newfile','path':path}, function (d) {
			out = $(d);
			set_events(out);
			el.append(out);
			el.find(">a").click();

			el.find('.cus-dd').removeClass('open')
		});
		e.stopImmediatePropagation();
		updateLibsAndMethods();
	})

	elm.find(".add-folder").click(function (e) {
		el = $(this).closest('[data-path]')
		path = el.attr('data-path');
		$.post('commander',{'type':'newfolder','path':path},function (d) {
			out = $(d);
			set_events(out)
			el.find('>.section').append(out);
			el.addClass('open');
			el.find('.cus-dd').removeClass('open')
		});
		e.stopImmediatePropagation();
		updateLibsAndMethods();
	})


	if(elm.hasClass('file'))
		elm.find(">a").click(function (e) {
			if(debuggerState){
				alert("Please stop debug feature, first.")
				return;
			}
			el = $(this).closest("[data-path]");
			$(".bonsai li").removeClass('hsel');
			path = el.attr('data-path');
			el.addClass('hsel')
			currentPath = path;
			initialFileSavingState = false;
			$.post('commander',{'type':'load','path':path},function (d) {
				// console.log(d)
				editorHolder.doc.setValue(d);
				arr = path.split("/")
				name = arr[arr.length-1];
				$(".fil-nam-dis span").html(name);
				clearTimeout(autoSaveTimer);
				autoSaveTimer=setTimeout(doautosave,autoSaveDelayInMilisec);
				doautodebug();
			});
			e.stopImmediatePropagation();
			updateLibsAndMethods();
		});


}

autoDebugMutex=false;
function doautodebug() {
	if(autoDebugMutex) return;
	autoDebugMutex=true;

	text = '';
	len = editorHolder.doc.lineCount();
	for (var i = 0 ; i < len; i++)
		text += editorHolder.doc.getLine(i) + "\n";

	$.post('commander',{'type':'debugger','code':text, "break":currentBreak, "debugger":(debuggerState)?1:0}).done(function (d) {

		parts = d.split("@+_!___!#")
		nparts = [];
		for (var i = 0; i <parts.length; i++) {
			w = $.trim(parts[i]);
			if(w!="")
				nparts.push(w);
		}
		parts = nparts;

		newWidgets = [];
		for (var i = widgets.length - 1; i >= 0; i--) {
			if (widgets[i][0]=="error")
				widgets[i][1].clear();
			else
				newWidgets.push(widgets[i]);
		}
		widgets = newWidgets;

		if (parts.length<=1){
			autoDebugMutex = false;
			return;
		} 
		q = d
		hln = parts[0];
		d = parts[1];
		

		vars_start = d.indexOf("_X_start_vars_X_");
		if(vars_start!=-1){
			vars_end = d.indexOf("_X_end_vars_X_");
			vars = d.substring(vars_start, vars_end).replace("_X_start_vars_X_","");
			d = d.substring(0, vars_start) + d.substring(vars_end+"_X_end_vars_X_".length);
			vars = vars.replace(/</g,'&lt;').replace(/>/g,'&gt;')
			vars = JSON.parse(vars);
		}else{
			vars = {};
		}


		trace_start = d.indexOf("_X_start_trace_X_");
		if(trace_start!=-1){

			trace_end = d.indexOf("_X_end_trace_X_");
			trace = d.substring(trace_start, trace_end).replace("_X_start_trace_X_","");
			d = d.substring(0, trace_start) + d.substring(trace_end+"_X_end_trace_X_".length);
			trace = trace.replace(/</g,'&lt;').replace(/>/g,'&gt;')
			
			trace = JSON.parse(trace);
		}else{
			trace = [];
		}

		if (d.indexOf("File")!=-1){
			arr = d.split("\n");
			lines = [];
			for (var i = 0; i < arr.length; i++) {
				if(arr[i]!="" && arr[i].indexOf("Traceback")==-1)
					lines.push(arr[i]);
			}

			lni = 0;
			for (var i = 0; i < lines.length; i++) {
				if(lines[i].indexOf("line")!=-1){
					lni = i;
					break;
				}	
			}


			ln = $.trim(lines[lni].substring(lines[lni].indexOf("line"),lines[lni].length).replace(/line/,""));

			end = ln.indexOf(",") > -1 ? ln.indexOf(",") : ln.indexOf(" ");
			ln = $.trim(ln.substring(0, end)) - hln - 5;
			var msg = document.createElement("div");
		    msg.appendChild(document.createTextNode(lines[lines.length-1]));
		    msg.className = "CodeMirror-lint-message-error";
		    widgets.push(["error",editorHolder.doc.addLineWidget(ln, msg, {coverGutter: false, noHScroll: true})]);
    	}
		output = d
		if(debuggerState){
			$("#log_detail pre").html(output);
			$("#local-vars").html('');
			$("#call-stack tbody").html('');
		
			debuggerState = false;
			autoDebugMutex = false;
			doautodebug();
			setTimeout(function () {
				debuggerState = true;
			},500);
			$.each(vars, function (k, v) {
				$("#local-vars").append('<li><span class="q">"</span>'+k+'<span class="q">"</span>:&nbsp;<span class="num">'+v+'</span>,</li>')
			});

			currnet_file = "";
			j = 0;
			for (var i = trace.length - 1; i >= 0; i--) {
				arr = trace[i].split(",")
				file = arr[0].replace("File","").replace(/"/g,'');
				line = arr[1].replace("line","");
				line = line - hln;
				where = arr[2].substring(0, arr[2].indexOf("\n")).replace("in ","");
				if(i==trace.length-1)
					currnet_file = file;

				if(currnet_file==file){
					arr = currentPath.split("/")
					file = arr[arr.length-1];
				}

				$("#call-stack tbody").append('<tr data-file="'+file+'" data-line="'+line+'" data-frame-num="0" onclick="ide.set_frame('+j+')"><td>'+j+'</td><td>'+where+'</td><td>'+file+':'+line+'</td></tr>')
					// console.log("Trace", file, line, where);
				j++;
				
			}
		}
		autoDebugMutex=false;
	}).fail(function () {
		autoDebugMutex = false;
		doautodebug();
	});
}

function savefile() {
	$(".fil-nam-dis span").html("Saving...");

	text = '';

	len = editorHolder.doc.lineCount();
		for (var i = 0 ; i < len; i++)
			text += editorHolder.doc.getLine(i) + "\n";

	$.post('commander',{'type':'savefile','path':currentPath,'text':text},function (d) {
		autoSaveMutex = false;
		arr = currentPath.split("/")
		name = arr[arr.length-1];
		$(".fil-nam-dis span").html(name);

		if(initialFileSavingState){
			out = $(d);
			out.addClass('hsel');
			$(".bonsai>.section").append(out);
			initialFileSavingState = false;
		}
	})
}

function makeid() {
  var text = "";
  var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

  for (var i = 0; i < 5; i++)
    text += possible.charAt(Math.floor(Math.random() * possible.length));

  return text;
}

autoSaveMutex=false;
function doautosave() {
	clearTimeout(autoSaveTimer);

	if(debuggerState)
		return;

	if(!autoSaveMutex)
		savefile();
	
	setTimeout(function(){ 
		document.getElementById("save_btn").value = "Saved";
		
	}, 1000);
	
}