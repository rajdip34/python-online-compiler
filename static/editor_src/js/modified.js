$(document).ready(function () {
    var southLayout = $('.ui-layout-south').layout({
        south__maskContents: true,
        south__childOptions: {
            center__maskContents: true,
            east__maskContents: true,
            east__minSize: 300,
        },
        east: {
            resizable: true,
            resizeWhileDragging: true,
            slidable: true,
        }
    });
    southLayout.sizePane("east", 699);
    //Collapse/Show all functionality
    var btnCollapse = $('#collapse');
    btnCollapse.click(function () {

        //set button text , do not change button text or this code will not work
        var btnText = $(btnCollapse).text().trim();
        btnText == "Collapse All" ?
            $(btnCollapse).text("Show All") :
            $(btnCollapse).text("Collapse All");

        var shouldCollapse = btnText == "Collapse All";
        // my super awesome hack  :)
        $("div[class^='ui-layout-toggler']").each(function () {
            //get if toggler is open/closed
            var title = $(this).attr('title');
            var opened = title != "Open";
            //don't close north
            if (!$(this).hasClass('ui-layout-toggler-north')) {
                if (shouldCollapse && opened)/*click the toggler */ this.click();
                else if (!shouldCollapse && !opened) this.click();
            }
        });
    });

    $('body').css('border', "6px solid #34c6d9");
    $('body').css('border-top', "none");

    //can change text here , also can make viable for font theme options (Like dropdown with font selection)
/*
    var fontFamily ='Helvetica Neue,Helvetica,Arial,sans-serif;';
    $('h3').each(function(){$(this).css({'font-size':'17px'},{'font-weight':'17px'},{fontFamily});});
    $('p').each(function(){$(this).css({'font-size':'17px'},{'font-weight':'17px'},{fontFamily});});
    $('li').each(function(){$(this).css({'font-size':'17px'},{'font-weight':'17px'},{fontFamily});});
    $('div').each(function(){$(this).css({'font-size':'17px'},{'font-weight':'17px'},{fontFamily});});
    $('textarea').each(function(){$(this).css({'font-size':'17px'},{'font-weight':'17px'},{fontFamily});});
    $('button').each(function(){$(this).css({'font-size':'17px'},{'font-weight':'17px'},{fontFamily});});
    $('span')*/


});
