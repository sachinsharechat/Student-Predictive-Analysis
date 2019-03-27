/**
 * Created by Ritik on 07-08-2017.
 */
$(document).ready(function(){
    setTimeout(function(){
        Materialize.toast("This is your Home Screen!", 4000, "rounded green");
    },1500);
    $("article").find(".batman").hide();
    $(".view-some-shit").click(function(){
        $(this).closest("article").siblings("article").hide();
        $(this).closest("article").addClass("s12").removeClass("s4");
        $(this).closest("article").find(".robin").hide();
        $(this).closest("article").find(".batman").fadeIn();
    });
    $(".joker-backwards").click(function(){
        $(this).closest("article").siblings("article").show();
        $(this).closest("article").addClass("s4").removeClass("s12");
        $(this).closest("article").find(".batman").hide();
        $(this).closest("article").find(".robin").fadeIn();
        Materialize.toast("We are Home!", 3000, "rounded green");
    });
});
$("html").keypress(function(e){
    if(e.keyCode == 37 || e.keyCode == 8 )
    {
        alert();
        $(".joker-backwards").click();
    }
});