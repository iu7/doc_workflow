/**
 * Created by zdvitas on 27.04.15.
 */

if (typeof jQuery === 'undefined') {
    throw new Error('Bootstrap\'s JavaScript requires jQuery')
}

$(".popup").offset({top: 0, left: 0});

$(".list-for").click(
    function(){

        var id = "pop" + this.id;
        var obj = $("#"+id);
        $(".black_overlay").show();

        //
        obj.offset($(this).position());
        obj.html("<img src='load.gif' width='40px' height='40px'>").fadeIn(500).delay(3000);
        //obj.html("teest").delay(5000).fadeOut(1000);



    }
);

$(".black_overlay").click(
    function()
    {
        $(".popup").offset({top: 0, left: 0});
        $(".popup").hide();

        $(this).hide();
    }
);