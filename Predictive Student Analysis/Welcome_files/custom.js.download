$(document).ready(function(){
    $("th").css("text-align","center");
    setTimeout(function(){
        $(".preloading-screen").fadeOut(500);
    },700);
    $('.dropdown-button').dropdown({
            inDuration: 300,
            outDuration: 225,
            constrainWidth: false, // Does not change width of dropdown to that of the activator
            hover: false, // Activate on hover
            gutter: 2, // Spacing from edge
            belowOrigin: true, // Displays dropdown below the button
            alignment: 'left', // Displays dropdown with edge aligned to the left of button
            stopPropagation: false // Stops event propagation
        }
    );
    $(".open-seasame").click(function(){
        var $right = $("aside.right-aside").css("right");
        if($right == "-200px"){
            $(this).find("i").removeClass("fa-arrow-up").addClass("fa-arrow-down");
            $("aside.right-aside").animate({
                right : 0
            },300);
        }
        else{
            $(this).find("i").removeClass("fa-arrow-down").addClass("fa-arrow-up");
            $("aside.right-aside").animate({
                right : "-200px"
            },300);
        }
    });
    $(".open-alohomora").click(function(){
        var $left = $("aside.left-aside").css("left");
        if($left == "-200px"){
            $(this).find("i").removeClass("fa-arrow-up").addClass("fa-arrow-down");
            $("aside.left-aside").animate({
                left : 0
            },300);
        }
        else{
            $(this).find("i").removeClass("fa-arrow-down").addClass("fa-arrow-up");
            $("aside.left-aside").animate({
                left : "-200px"
            },300);
        }
    });
    $("aside.side-navigation ul li").hide();
    $(".oh-here-is-a-back-button").hide();
    var $showing=false;
    $("aside.side-navigation ul a").click(function(){
        if($showing == true) {
            $(this).parent("ul").siblings("ul").show();
            $(this).siblings("li").hide();
            $showing=false;
            $(this).removeClass("green darken-2")
            $(this).find(".oh-here-is-a-back-button").toggle();
        }
        else if($showing==false){
            $(this).parent("ul").siblings("ul").hide();
            $(this).siblings("li").show();
            $(this).addClass("green darken-2");
            $showing=true;
            $(this).find(".oh-here-is-a-back-button").toggle();
        }
    });
    $("aside.side-navigation ul li a.backwards").click(function(){
        $(this).closest("ul").siblings("ul").show();
        $(this).parent("li").siblings("li").hide();
        $(this).parent("li").hide();
        $(".oh-here-is-a-back-button").hide();
        $(this).addClass("green darken-2");
    });

});

$(".g").addClass("tooltipped");
$(".g").attr("data-tooltip","What is GreenBoard?");
$(".g").attr("data-delay","100");

$(".h").addClass("tooltipped");
$(".h").attr("data-tooltip","Back to Home?");
$(".h").attr("data-delay","100");
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#profile').attr('src', e.target.result);
        };
        $("#profile").show();
        $("#icon").hide();

        reader.readAsDataURL(input.files[0]);
    }
}