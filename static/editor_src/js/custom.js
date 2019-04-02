editorHolder = {};
var myLayout;
function resetZoom() {
  ccc.resetZoom();
}

$(document).ready(function () {

    ccc = new Chart(document.getElementById("line-chart"), {
        type: 'line',
        data: {
            labels: [0],
            datasets: [{
                data: [0],
                label: "Backtest date/price rate",
                borderColor: "#34c6d9",
                fill: true
            }]
        },
        options: {
			legend: {
            labels: {
                fontColor: "#34c6d9",
            }
        },
		 pan: {
      enabled: true,
      mode: "x",
      speed: 10,
      threshold: 10
    },
    zoom: {
      enabled: true,
      drag: false,
      mode: "xy",
      limits: {
        max: 10,
        min: 0.5
      }
    },
		   scales: {
            yAxes: [{
                ticks: {
                    fontColor: "#34c6d9",
                }
            }],
            xAxes: [{
                ticks: {
                    fontColor: "#34c6d9",
                }
            }]
        },
            title: {
                display: false,
                text: 'World population per region (in millions)'
            }
        }
    });

    /****************Code TextEditor**********************/
    CodeMirror.commands.autocomplete = function (cm) {
        cm.showHint({ hint: CodeMirror.hint.anyword });
    }
    var editor = CodeMirror.fromTextArea(document.getElementById("code-ta"), {
        lineNumbers: true,
        autoCloseBrackets: true,
        indentUnit: 4,
		mode:  "python"
        // extraKeys: {"Ctrl-Space": "autocomplete"}
    });

    editor.on("keyup", function (cm, event) {
        if (!cm.state.completionActive && /*Enables keyboard navigation in autocomplete list*/
            event.keyCode != 13) {        /*Enter - do not open autocomplete list just after item has been selected in it*/
            CodeMirror.commands.autocomplete(cm, null, { completeSingle: false });
        }
        doautodebug();
        doautosave();
    });
    /********************Chart******************************/
    var winow_height = $(document).height();

    $('#line-chart').height(winow_height * 0.4);
    $('#log_detail').css("min-height", winow_height * 0.23);
    $('#error').css("min-height", winow_height * 0.23);
    $('#editor').css("min-height", winow_height * 0.58);


    CodeMirror.commands.autocomplete = function (cm) {
        cm.showHint({ hint: CodeMirror.pythonHint });
    };

    editor.setOption("theme", "railscasts");

    $(".CodeMirror").css("height", "100%");
    editorHolder = editor


   

    $("#reset").click(function () {
        var editor = ace.edit("editor");
        var result = editor.setValue();
        //alert(result);
        $("#code_editor_demo_1").html('');
    });


    Chart.defaults.global.elements.line.fill = false;
    

    function toggleLiveResizing() {
        $.each($.layout.config.borderPanes, function (i, pane) {
            var o = myLayout.options[pane];
            o.livePaneResizing = !o.livePaneResizing;
        });
    };

    function toggleStateManagement(skipAlert, mode) {
        if (!$.layout.plugins.stateManagement) return;

        var options = myLayout.options.stateManagement
            , enabled = options.enabled // current setting
            ;
        if ($.type(mode) === "boolean") {
            if (enabled === mode) return; // already correct
            enabled = options.enabled = mode
        }
        else
            enabled = options.enabled = !enabled; // toggle option

        if (!enabled) { // if disabling state management...
            myLayout.deleteCookie(); // ...clear cookie so will NOT be found on next refresh
            if (!skipAlert)
                alert('This layout will reload as the options specify \nwhen the page is refreshed.');
        }
        else if (!skipAlert)
            alert('This layout will save & restore its last state \nwhen the page is refreshed.');

        // update text on button
        var $Btn = $('#btnToggleState');
        text = $Btn.html();
        if (enabled){

            $Btn.html(text.replace(/Enable/i, "Disable"));
        }
        else{
            $Btn.html(text.replace(/Disable/i, "Enable"));
        }
    };

    // set EVERY 'state' here so will undo ALL layout changes
    // used by the 'Reset State' button: myLayout.loadState( stateResetSettings )
    var stateResetSettings = {
        south__size: 100
        , south__initClosed: false
        , south__initHidden: false
        , north__size: "auto"
        , north__initClosed: false
        , north__initHidden: false
        , west__size: 300
        , west__initClosed: false
        , west__initHidden: false
        , east__size: 700
        , east__initClosed: false
        , east__initHidden: false
    };

    myLayout = $('body').layout({
		 center__onresize: function () {
            var height = $('div[class^=ui-layout-center]').css('height');
            var iHeight = height.replace("px", "")
            iHeight = iHeight - 40;//YOU CAN ADJUST HEIGHT HERE
            $('#main').css('height', iHeight + "px");
            $(".CodeMirror").css('height', iHeight + "px");
        },

        //  reference only - these options are NOT required because 'true' is the default
        closable: true  // pane can open & close
        , resizable: true // when open, pane can be resized
        , slidable: true  // when closed, pane can 'slide' open over other panes - closes on mouse-out
        , livePaneResizing: true

        //  some resizing/toggling settings
        , south__slidable: true  // OVERRIDE the pane-default of 'slidable=true'
        , south__togglerLength_closed: '100%' // toggle-button is full-width of resizer-bar
        , south__spacing_closed: 0    // big resizer-bar when open (zero height)
        , north__resizable: true // OVERRIDE the pane-default of 'resizable=true'
        , north__spacing_open: 0    // no resizer-bar when open (zero height)
        , north__spacing_closed: 0  // big resizer-bar when open (zero height)

        //  some pane-size settings
        , west__minSize: 0
        , east__size: 300
        , east__minSize: 0
        , east__maxSize: .9 // 50% of layout width
        , center__minWidth: 100

        //  some pane animation settings
        , west__animatePaneSizing: false
        , west__fxSpeed_size: "fast"  // 'fast' animation when resizing west-pane
        , west__fxSpeed_open: 1000  // 1-second animation when opening west-pane
        , west__fxSettings_open: { easing: "easeOutBounce" } // 'bounce' effect when opening
        , west__fxName_close: "none"  // NO animation when closing west-pane

        //  enable showOverflow on west-pane so CSS popups will overlap south pane
        , west__showOverflowOnHover: true

        //  enable state management
        , stateManagement__enabled: true // automatic cookie load & save enabled by default

        , showDebugMessages: true // log and/or display messages from debugging & testing code
    });

    myLayout.loadState(stateResetSettings);

    // if there is no state-cookie, then DISABLE state management initially
    var cookieExists = !$.isEmptyObject(myLayout.readCookie());
    if (!cookieExists) toggleStateManagement(true, false);

    myLayout
        // add event to the 'Close' button in the East pane dynamically...
        .bindButton('#btnCloseEast', 'close', 'east')

        // add event to the 'Toggle north' buttons in Center AND north panes dynamically...
        .bindButton('.north-toggler', 'toggle', 'north')

        // add MULTIPLE events to the 'Open All Panes' button in the Center pane dynamically...
        .bindButton('#openAllPanes', 'open', 'south')
        .bindButton('#openAllPanes', 'open', 'north')
        .bindButton('#openAllPanes', 'open', 'west')
        .bindButton('#openAllPanes', 'open', 'east')

        // add MULTIPLE events to the 'Close All Panes' button in the Center pane dynamically...
        .bindButton('#closeAllPanes', 'close', 'south')
        .bindButton('#closeAllPanes', 'close', 'north')
        .bindButton('#closeAllPanes', 'close', 'west')
        .bindButton('#closeAllPanes', 'close', 'east')

        // add MULTIPLE events to the 'Toggle All Panes' button in the Center pane dynamically...
        .bindButton('#toggleAllPanes', 'toggle', 'south')
        .bindButton('#toggleAllPanes', 'toggle', 'north')
        .bindButton('#toggleAllPanes', 'toggle', 'west')
        .bindButton('#toggleAllPanes', 'toggle', 'east')
        ;


    /*
     *  DISABLE TEXT-SELECTION WHEN DRAGGING (or even _trying_ to drag!)
     *  this functionality will be included in RC30.80
     */
    $.layout.disableTextSelection = function () {
        var $d = $(document)
            , s = 'textSelectionDisabled'
            , x = 'textSelectionInitialized'
            ;
        if ($.fn.disableSelection) {
            if (!$d.data(x)) // document hasn't been initialized yet
                $d.on('mouseup', $.layout.enableTextSelection).data(x, true);
            if (!$d.data(s))
                $d.disableSelection().data(s, true);
        }
        //console.log('$.layout.disableTextSelection');
    };
    $.layout.enableTextSelection = function () {
        var $d = $(document)
            , s = 'textSelectionDisabled';
        if ($.fn.enableSelection && $d.data(s))
            $d.enableSelection().data(s, false);
        //console.log('$.layout.enableTextSelection');
    };
            
    $(".ui-layout-resizer")
        .disableSelection() // affects only the resizer element
        .on('mousedown', $.layout.disableTextSelection); // affects entire document

});
