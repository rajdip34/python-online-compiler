"use strict";

$("#mySidenav").css("display", "block");


$(".mob-tabs .mob-tabs-link").click(function(){
	var getId = $(this).attr("name");
	$(".mob-tabs-link").removeClass("active");
//	alert(getId);
	$("#mySidenav, #main, #mobChart").css("display","none");
	  $(getId).css("display","block");
	$(this).addClass("active");
});
'use strict';

// polyfill
function polyfill() {
  // aliases
  var w = window;
  var d = document;

  // return if scroll behavior is supported and polyfill is not forced
  if (
    'scrollBehavior' in d.documentElement.style &&
    w.__forceSmoothScrollPolyfill__ !== true
  ) {
    return;
  }

  // globals
  var Element = w.HTMLElement || w.Element;
  var SCROLL_TIME = 468;

  // object gathering original scroll methods
  var original = {
    scroll: w.scroll || w.scrollTo,
    scrollBy: w.scrollBy,
    elementScroll: Element.prototype.scroll || scrollElement,
    scrollIntoView: Element.prototype.scrollIntoView
  };

  // define timing method
  var now =
    w.performance && w.performance.now
      ? w.performance.now.bind(w.performance)
      : Date.now;

  /**
   * indicates if a the current browser is made by Microsoft
   * @method isMicrosoftBrowser
   * @param {String} userAgent
   * @returns {Boolean}
   */
  function isMicrosoftBrowser(userAgent) {
    var userAgentPatterns = ['MSIE ', 'Trident/', 'Edge/'];

    return new RegExp(userAgentPatterns.join('|')).test(userAgent);
  }

  /*
   * IE has rounding bug rounding down clientHeight and clientWidth and
   * rounding up scrollHeight and scrollWidth causing false positives
   * on hasScrollableSpace
   */
  var ROUNDING_TOLERANCE = isMicrosoftBrowser(w.navigator.userAgent) ? 1 : 0;

  /**
   * changes scroll position inside an element
   * @method scrollElement
   * @param {Number} x
   * @param {Number} y
   * @returns {undefined}
   */
  function scrollElement(x, y) {
    this.scrollLeft = x;
    this.scrollTop = y;
  }

  /**
   * returns result of applying ease math function to a number
   * @method ease
   * @param {Number} k
   * @returns {Number}
   */
  function ease(k) {
    return 0.5 * (1 - Math.cos(Math.PI * k));
  }

  /**
   * indicates if a smooth behavior should be applied
   * @method shouldBailOut
   * @param {Number|Object} firstArg
   * @returns {Boolean}
   */
  function shouldBailOut(firstArg) {
    if (
      firstArg === null ||
      typeof firstArg !== 'object' ||
      firstArg.behavior === undefined ||
      firstArg.behavior === 'auto' ||
      firstArg.behavior === 'instant'
    ) {
      // first argument is not an object/null
      // or behavior is auto, instant or undefined
      return true;
    }

    if (typeof firstArg === 'object' && firstArg.behavior === 'smooth') {
      // first argument is an object and behavior is smooth
      return false;
    }

    // throw error when behavior is not supported
    throw new TypeError(
      'behavior member of ScrollOptions ' +
        firstArg.behavior +
        ' is not a valid value for enumeration ScrollBehavior.'
    );
  }

  /**
   * indicates if an element has scrollable space in the provided axis
   * @method hasScrollableSpace
   * @param {Node} el
   * @param {String} axis
   * @returns {Boolean}
   */
  function hasScrollableSpace(el, axis) {
    if (axis === 'Y') {
      return el.clientHeight + ROUNDING_TOLERANCE < el.scrollHeight;
    }

    if (axis === 'X') {
      return el.clientWidth + ROUNDING_TOLERANCE < el.scrollWidth;
    }
  }

  /**
   * indicates if an element has a scrollable overflow property in the axis
   * @method canOverflow
   * @param {Node} el
   * @param {String} axis
   * @returns {Boolean}
   */
  function canOverflow(el, axis) {
    var overflowValue = w.getComputedStyle(el, null)['overflow' + axis];

    return overflowValue === 'auto' || overflowValue === 'scroll';
  }

  /**
   * indicates if an element can be scrolled in either axis
   * @method isScrollable
   * @param {Node} el
   * @param {String} axis
   * @returns {Boolean}
   */
  function isScrollable(el) {
    var isScrollableY = hasScrollableSpace(el, 'Y') && canOverflow(el, 'Y');
    var isScrollableX = hasScrollableSpace(el, 'X') && canOverflow(el, 'X');

    return isScrollableY || isScrollableX;
  }

  /**
   * finds scrollable parent of an element
   * @method findScrollableParent
   * @param {Node} el
   * @returns {Node} el
   */
  function findScrollableParent(el) {
    while (el !== d.body && isScrollable(el) === false) {
      el = el.parentNode;
    }

    return el;
  }

  /**
   * self invoked function that, given a context, steps through scrolling
   * @method step
   * @param {Object} context
   * @returns {undefined}
   */
  function step(context) {
    var time = now();
    var value;
    var currentX;
    var currentY;
    var elapsed = (time - context.startTime) / SCROLL_TIME;

    // avoid elapsed times higher than one
    elapsed = elapsed > 1 ? 1 : elapsed;

    // apply easing to elapsed time
    value = ease(elapsed);

    currentX = context.startX + (context.x - context.startX) * value;
    currentY = context.startY + (context.y - context.startY) * value;

    context.method.call(context.scrollable, currentX, currentY);

    // scroll more if we have not reached our destination
    if (currentX !== context.x || currentY !== context.y) {
      w.requestAnimationFrame(step.bind(w, context));
    }
  }

  /**
   * scrolls window or element with a smooth behavior
   * @method smoothScroll
   * @param {Object|Node} el
   * @param {Number} x
   * @param {Number} y
   * @returns {undefined}
   */
  function smoothScroll(el, x, y) {
    var scrollable;
    var startX;
    var startY;
    var method;
    var startTime = now();

    // define scroll context
    if (el === d.body) {
      scrollable = w;
      startX = w.scrollX || w.pageXOffset;
      startY = w.scrollY || w.pageYOffset;
      method = original.scroll;
    } else {
      scrollable = el;
      startX = el.scrollLeft;
      startY = el.scrollTop;
      method = scrollElement;
    }

    // scroll looping over a frame
    step({
      scrollable: scrollable,
      method: method,
      startTime: startTime,
      startX: startX,
      startY: startY,
      x: x,
      y: y
    });
  }

  // ORIGINAL METHODS OVERRIDES
  // w.scroll and w.scrollTo
  w.scroll = w.scrollTo = function() {
    // avoid action when no arguments are passed
    if (arguments[0] === undefined) {
      return;
    }

    // avoid smooth behavior if not required
    if (shouldBailOut(arguments[0]) === true) {
      original.scroll.call(
        w,
        arguments[0].left !== undefined
          ? arguments[0].left
          : typeof arguments[0] !== 'object'
            ? arguments[0]
            : w.scrollX || w.pageXOffset,
        // use top prop, second argument if present or fallback to scrollY
        arguments[0].top !== undefined
          ? arguments[0].top
          : arguments[1] !== undefined
            ? arguments[1]
            : w.scrollY || w.pageYOffset
      );

      return;
    }

    // LET THE SMOOTHNESS BEGIN!
    smoothScroll.call(
      w,
      d.body,
      arguments[0].left !== undefined
        ? ~~arguments[0].left
        : w.scrollX || w.pageXOffset,
      arguments[0].top !== undefined
        ? ~~arguments[0].top
        : w.scrollY || w.pageYOffset
    );
  };

  // w.scrollBy
  w.scrollBy = function() {
    // avoid action when no arguments are passed
    if (arguments[0] === undefined) {
      return;
    }

    // avoid smooth behavior if not required
    if (shouldBailOut(arguments[0])) {
      original.scrollBy.call(
        w,
        arguments[0].left !== undefined
          ? arguments[0].left
          : typeof arguments[0] !== 'object' ? arguments[0] : 0,
        arguments[0].top !== undefined
          ? arguments[0].top
          : arguments[1] !== undefined ? arguments[1] : 0
      );

      return;
    }

    // LET THE SMOOTHNESS BEGIN!
    smoothScroll.call(
      w,
      d.body,
      ~~arguments[0].left + (w.scrollX || w.pageXOffset),
      ~~arguments[0].top + (w.scrollY || w.pageYOffset)
    );
  };

  // Element.prototype.scroll and Element.prototype.scrollTo
  Element.prototype.scroll = Element.prototype.scrollTo = function() {
    // avoid action when no arguments are passed
    if (arguments[0] === undefined) {
      return;
    }

    // avoid smooth behavior if not required
    if (shouldBailOut(arguments[0]) === true) {
      // if one number is passed, throw error to match Firefox implementation
      if (typeof arguments[0] === 'number' && arguments[1] === undefined) {
        throw new SyntaxError('Value could not be converted');
      }

      original.elementScroll.call(
        this,
        // use left prop, first number argument or fallback to scrollLeft
        arguments[0].left !== undefined
          ? ~~arguments[0].left
          : typeof arguments[0] !== 'object' ? ~~arguments[0] : this.scrollLeft,
        // use top prop, second argument or fallback to scrollTop
        arguments[0].top !== undefined
          ? ~~arguments[0].top
          : arguments[1] !== undefined ? ~~arguments[1] : this.scrollTop
      );

      return;
    }

    var left = arguments[0].left;
    var top = arguments[0].top;

    // LET THE SMOOTHNESS BEGIN!
    smoothScroll.call(
      this,
      this,
      typeof left === 'undefined' ? this.scrollLeft : ~~left,
      typeof top === 'undefined' ? this.scrollTop : ~~top
    );
  };

  // Element.prototype.scrollBy
  Element.prototype.scrollBy = function() {
    // avoid action when no arguments are passed
    if (arguments[0] === undefined) {
      return;
    }

    // avoid smooth behavior if not required
    if (shouldBailOut(arguments[0]) === true) {
      original.elementScroll.call(
        this,
        arguments[0].left !== undefined
          ? ~~arguments[0].left + this.scrollLeft
          : ~~arguments[0] + this.scrollLeft,
        arguments[0].top !== undefined
          ? ~~arguments[0].top + this.scrollTop
          : ~~arguments[1] + this.scrollTop
      );

      return;
    }

    this.scroll({
      left: ~~arguments[0].left + this.scrollLeft,
      top: ~~arguments[0].top + this.scrollTop,
      behavior: arguments[0].behavior
    });
  };

  // Element.prototype.scrollIntoView
  Element.prototype.scrollIntoView = function() {
    // avoid smooth behavior if not required
    if (shouldBailOut(arguments[0]) === true) {
      original.scrollIntoView.call(
        this,
        arguments[0] === undefined ? true : arguments[0]
      );

      return;
    }

    // LET THE SMOOTHNESS BEGIN!
    var scrollableParent = findScrollableParent(this);
    var parentRects = scrollableParent.getBoundingClientRect();
    var clientRects = this.getBoundingClientRect();

    if (scrollableParent !== d.body) {
      // reveal element inside parent
      smoothScroll.call(
        this,
        scrollableParent,
        scrollableParent.scrollLeft + clientRects.left - parentRects.left,
        scrollableParent.scrollTop + clientRects.top - parentRects.top
      );

      // reveal parent in viewport unless is fixed
      if (w.getComputedStyle(scrollableParent).position !== 'fixed') {
        w.scrollBy({
          left: parentRects.left,
          top: parentRects.top,
          behavior: 'smooth'
        });
      }
    } else {
      // reveal element in viewport
      w.scrollBy({
        left: clientRects.left,
        top: clientRects.top,
        behavior: 'smooth'
      });
    }
  };
}

if (typeof exports === 'object' && typeof module !== 'undefined') {
  // commonjs
  module.exports = { polyfill: polyfill };
} else {
  // global
  polyfill();
}

document.querySelectorAll('.dropdown-toggle.ddt').forEach(function(e) {
 e.addEventListener('click', function(event) {
   window.setTimeout(function() {
     var rect = e.nextElementSibling.getBoundingClientRect();
	 var parent = document.querySelector('#mySidenav');
     var parentRect = parent.getBoundingClientRect()
     console.log(rect.top - parentRect.top + rect.height);
     console.log(parentRect.height)
     if (rect.top - rect.height < 0)
		 e.nextElementSibling.scrollIntoView();
	else if(rect.top - parentRect.top + rect.height > parentRect.height)
    //    e.nextElementSibling.setAttribute('style', 'top:' + (rect.top - parentRect.top  - parentRect.height - 40) + 'px') 
		parent.scrollBy({ top: rect.top - parentRect.top  - parentRect.height + rect.height, left: 0, behavior: 'instant' });
   
   }, 50);
 });
});

function searchRecursive(container, phrase, resetOnly, depth) {
  if(depth <= 0)
    return 0;
  depth -= 1;
  
  container.removeAttribute('search-found')
  container.removeAttribute('search-highlight')
  container.removeAttribute('search-open')
  if (resetOnly)
    return 0;
  
  let matchCount = 0;
  var text = $(container).find('> a')[0];
  if (text && text.textContent.toLowerCase().indexOf(phrase) !== -1) {
     matchCount = 1;
  }
   const isFolder = container.hasAttribute('class') && (container.getAttribute('class').indexOf('folder') !== -1 || container.getAttribute('class').indexOf('bonsai') !== -1);
   let childMatchCount = 0;
    if (isFolder) {
		
      childMatchCount += Array.prototype.slice.call($(container).find('> ul.section > li')).reduce((matches, element) => {
        return matches + searchRecursive(element, phrase, false, depth);
      
      }, 0);
   }
  matchCount += childMatchCount; 
  
  if(matchCount > 0) {
	  if (isFolder && childMatchCount)
		  container.setAttribute('search-open', "true");
      container.setAttribute('search-found', "true")
  }
  else {
    container.setAttribute('search-found', "false")
  }
    
  return matchCount;
}
var bonasai = document.querySelector('.bonsai');
bonasai.querySelectorAll('ul.section li').forEach(e => {
	if (e.classList.contains('file'))
		e = e.querySelector('a');
	
	e.addEventListener('click', function(event) {
		console.log('asdasd');
		bonasai.classList.remove('highlight-on');
	});
});

document.querySelector('[name="searchBox"]').addEventListener('input', event => {
  
  
  if (event.target.value.trim() == "")
    bonasai.classList.remove('search-on');
  else {
    bonasai.classList.add('search-on');
	bonasai.classList.add('highlight-on');
    searchRecursive(bonasai, event.target.value.trim().toLowerCase(), false, 10);
  }
})



var separator = 20;
	
	function showTable(tabValue, modal) {
		
		var tableWrapper = $(modal.find('#data-table')[0])
			
		var dataTable = $('<table/>').attr('class', 'table table-bordered table-hover').attr('style', 'width: 100%')
		tableWrapper.empty().append(dataTable);
		dataTable.DataTable(
			{
				'columns': tabValue.columns,
				'data': tabValue.values,
				"paging": false
			}
		);
	}
	
	function handleDataTabChange(tabValue, modal) {
		return function(event) {
			$(event.target).tab('show');
			showTable(tabValue, modal);
		}
	}
	
	function initializeDataModal(modal, tabValues) {
		
		$(modal.find('.nav.nav-tabs')[0]).empty().append(
		
			tabValues.map(function(tab, index) {
				var tabA = $('<a/>').attr('class', 'nav-link').append(tab.name).click(handleDataTabChange(tab, modal));
				
				if (index == 0) {
					showTable(tab, modal);
				}
					
				
				return $('<li/>').attr('class', 'nav-item' + ((index == 0) ? " active" : "")).append(tabA);
			})
		);
		
		var width = document.documentElement.clientWidth - 2 * separator;
		var height = document.documentElement.clientHeight - 2 * separator;
		var margin = width / 2;
		var top = separator;
		
		var css = `top: ${top}px; min-width: ${width}px; margin-left: -${margin}px; min-height: ${height}px; scrollbar-color: #34c6d9 #555;`;
		modal.attr('style', css);
		
		if (tabValues.length == 0)
			$(modal.find('#data-table')[0]).empty()
	}
	
	$('#dataset').click(function(event) {
		event.stopImmediatePropagation();
		if(debuggerState){
			alert("Please stop debug feature, first.")
			return;
		}
		text = '';
		len = editorHolder.doc.lineCount();
		for (var i = 0 ; i < len; i++)
			text += editorHolder.doc.getLine(i) + "\n";

		$.post('commander',{'type':'run','code':text}, function (output) {
		
				var modal = $("#dataset_modal");
			
		
				try {
					var datasets = JSON.parse(output);
					var view = $(modal.find(".dataset-view")[0])
				
					if (Array.isArray(datasets) == false)
						datasets = [datasets];
			
					var tabValues = datasets.map(function(dataset, index) {
					var name = dataset.name == undefined ? "dataset-" + (index + 1) : dataset.name;
				
					if (dataset.values.length > 0) {
						var columns = Object.keys(dataset.values[0]).map(function(name) {
							return {
								'name': name,
								'title': name
							}
						});
					
						var dataValues = dataset.values.map(function(data) {
							return Object.values(data);
						});
					
						return {
							'name': name,
							'columns': columns,
							'values': dataValues,
						}
					}
					else {
						return {
							'name': name,
							'columns': [],
							'values': [],
						}
					}
				});
				modal.modal('toggle');
				initializeDataModal(modal, tabValues);
			
			}
			catch(e) {
				var width = document.documentElement.clientWidth - 2 * separator;
				var height = document.documentElement.clientHeight - 2 * separator;
				var margin = width / 2;
				var top = separator;
		
				var css = `top: ${top}px; min-width: ${width}px; margin-left: -${margin}px; min-height: ${height}px; scrollbar-color: #34c6d9 #555;`;
				modal.attr('style', css);
				modal.modal('toggle');
				var view = $(modal.find("#data-table")[0])
				$(modal.find('.nav.nav-tabs')[0]).empty()
				view.empty().append("No datasets found in current output");
			}
		});
		
	
		
		event.preventDefault();
		return false;
	});