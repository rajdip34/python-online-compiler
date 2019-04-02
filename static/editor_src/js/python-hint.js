objectProperties = [];

function searchSimilar(arr,q) {
    fetch = [];
    for (var i = arr.length - 1; i >= 0; i--)
        if (arr[i].startsWith(q)) fetch.push(arr[i])
  
    return fetch
}

(function () {
  function forEach(arr, f) {
    for (var i = 0, e = arr.length; i < e; ++i) f(arr[i]);
  }

  function arrayContains(arr, item) {
    if (!Array.prototype.indexOf) {
      var i = arr.length;
      while (i--) {
        if (arr[i] === item) {
          return true;
        }
      }
      return false;
    }
    return arr.indexOf( item) != -1;
  }

  async function scriptHint(editor, _keywords, getToken) {
    // Find the token at the cursor
    var cur = editor.getCursor(), token = getToken(editor, cur), tprop = token;
    editorHolder = editor;

    // If it's not a 'word-style' token, ignore the token.

    if (!/^[\w$_]*$/.test(token.string)) {
        token = tprop = {start: cur.ch, end: cur.ch, string: "", state: token.state,
                         className: token.string == ":" ? "python-type" : null};
    }


    if (!context) var context = [];
    context.push(tprop);


    var completionList = await getCompletions(token, context);
    completionList = completionList.sort();
    //prevent autocomplete for last word, instead show dropdown with one word
    if(completionList.length == 1) {
      completionList.push(" ");
    }

    return {list: completionList,
            from: CodeMirror.Pos(cur.line, token.start),
            to: CodeMirror.Pos(cur.line, token.end)};
  }

  CodeMirror.pythonHint = function(editor) {
    editorHolder = editor;
    return scriptHint(editor, pythonKeywordsU, function (e, cur) {return e.getTokenAt(cur);});
  };

  var pythonKeywords = "and import from del not while as elif global or with assert else if pass yield"
+ "break except print class exec in raise continue finally is return def for lambda try";
  var pythonKeywordsL = pythonKeywords.split(" ");
  var pythonKeywordsU = pythonKeywords.toUpperCase().split(" ");

  var pythonBuiltins = "abs divmod input open staticmethod all enumerate int ord str "
+ "any eval isinstance pow sum basestring execfile issubclass print super"
+ "bin file iter property tuple bool filter len range type"
+ "bytearray float list raw_input unichr callable format locals reduce unicode"
+ "chr frozenset long reload vars classmethod getattr map repr xrange"
+ "cmp globals max reversed zip compile hasattr memoryview round __import__"
+ "complex hash min set apply delattr help next setattr buffer"
+ "dict hex object slice coerce dir id oct sorted intern ";
  var pythonBuiltinsL = pythonBuiltins.split(" ").join("() ").split(" ");
  var pythonBuiltinsU = pythonBuiltins.toUpperCase().split(" ").join("() ").split(" ");
  
  
  async function getCompletions(token, context) {
    var found = [], start = token.string, locals=[];
    function maybeAdd(str) {
      if (str.indexOf(start) == 0 && !arrayContains(found, str)) found.push(str);
      // console.log(str)
    }


    function checkForLibs() {
        cur = editorHolder.getCursor();
        line = editorHolder.doc.getLine(cur.line)
        cond1 = line.startsWith("from ");
        cond2 = line.indexOf("import ")==-1;
        cond3 = line.startsWith("import ");
        cond4 = line.substr(line.length-2,2)==' i' || line.substr(line.length-3,3)==' im' || line.substr(line.length-4,4)==' imp' || line.substr(line.length-5,5)==' impo' || line.substr(line.length-6,6)==' impor';
        cond5 = line=="from "

        // console.log(cond1,cond2,cond3,cond4,cond5)
        // console.log(cond1,cond2,cond3,cond4)
        if((cond3 || (cond1 && cond2)) && !cond4){
            if(cond3){
                line = line.replace('import ','')
                parts = line.split('.');
                prev = parts.length==1 ? "" : parts.slice(0,parts.length-1).join(".")
                fetch = searchSimilar(libs,line);
                
            }else if (cond1 && cond2){
                line = line.replace('from ','')
                parts = line.split('.');
                prev = parts.length==1 ? "" : parts.slice(0,parts.length-1).join(".")
                fetch = searchSimilar(libs,line);
            
            }else
                return;

            for (var i = fetch.length - 1; i >= 0; i--) {
                fetch[i] = parts.length==1 ? fetch[i] : fetch[i].replace(prev+".","")
                fetch[i] = fetch[i].split(".")[0]
            }
        }else if (cond1 && !cond2){
            fetch = searchSimilar(methods, line)
            for (var i = fetch.length - 1; i >= 0; i--)
                fetch[i] = fetch[i].substr(fetch[i].indexOf("import ")).replace('import ','')
        }else if (cond4 && cond1 && !cond5)
            fetch = ["import"];
        else 
            return;
        
        found = Array.from(new Set(fetch))
      
    }

    async function checkForAutocompleteObjects() {
        cur = editorHolder.getCursor();
        line = editorHolder.doc.getLine(cur.line);

        importfroms = ["from","import","fro","fr","im","imp","impor"]
        for (var i = importfroms.length - 1; i >= 0; i--) {
            if(line.startsWith(importfroms[i])) 
                return;
        }

        if (line.substring(cur.ch-1)!="." && objectProperties!=[]){
            if(objectProperties==[])
                return;

            
            
            q2 = "";
            for (var i = line.length - 1; i >= 0; i--) {
                q = line.substring(i,line.length);
                if (["."," ","]","[",")","(",":"].indexOf(q.substring(0,1))==-1)
                    q2 = q;
                else
                    break;
            }
            
            found = [];
            for (var i = objectProperties.length - 1; i >= 0; i--) {
                if (objectProperties[i].startsWith(q2))
                    found.push(objectProperties[i]);
            }
        }else if(line.substring(cur.ch-1)!=".")
            return;


        code = "";
        len = editorHolder.doc.lineCount();
        done = false;
        for (var i = 0; i < len ; i++) {
            line_text = editorHolder.doc.getLine(i);
            if (i==cur.line){
                line_text = line_text.substring(0,cur.ch) + "{blinker}" + line_text.substring(cur.ch)
                done = true;
            }
            code += line_text + "\n"
            if (done)
                break;
        }
        
        d = await $.post('commander',{
            'type':         "autocomplete_objs",
            "code":         code,
        }).promise();

        if(d.indexOf("_X_end_X_")==-1)
            return;

        d = d.substring(d.indexOf("_X_start_X_"),d.indexOf("_X_end_X_")).replace("_X_start_X_","")
        found = JSON.parse(d.replace(/'/g,'"'))
		found = found.filter(function(e) {
			return e.trim() !== 'sys' && e.trim() !== "";
		})
        objectProperties = found;
      
    }

    async function checkForAutocompleteVars() {
        cur = editorHolder.getCursor();
        if (editorHolder.doc.getLine(cur.line).substring(cur.ch-1)==".")
            return;

        code = "";
        len = editorHolder.doc.lineCount();
        for (var i = 0; i < len ; i++) {
            line_text = editorHolder.getLine(i);
            if (i==cur.line)
                break;
            
            code += line_text + "\n"
        }
        
        d = await $.post('commander',{
            'type':         "autocomplete_vars",
            "code":         code,
        }).promise();

        if(d.indexOf("_X_start_X_")==-1)
            return;
        
        d = d.substring(d.indexOf("_X_start_X_"),d.indexOf("_X_end_X_")).replace("_X_start_X_","")
        locals = JSON.parse(d.replace(/'/g,'"'))
      
    }

    function gatherCompletions(_obj) {
        cur = editorHolder.getCursor();
        if (editorHolder.doc.getLine(cur.line).substring(0,4)=="from" || editorHolder.doc.getLine(cur.line).substring(0,6)=="import")
            return;

        forEach(pythonBuiltinsL, maybeAdd);
        forEach(pythonBuiltinsU, maybeAdd);
        forEach(pythonKeywordsL, maybeAdd);
        forEach(pythonKeywordsU, maybeAdd);

        

        forEach(locals, maybeAdd)
    }

    if (context) {
        
        await checkForAutocompleteVars();

        var obj = context.pop(), base;

        if (obj.type == "variable")
            base = obj.string; 
        else if(obj.type == "variable-3")
            base = ":" + obj.string;

        while (base != null && context.length)
            base = base[context.pop().string];
        if (base != null)
            gatherCompletions(base);


        await checkForAutocompleteObjects();

        checkForLibs();

      
      
    }

    return found;
  }
})();
 