
$(document).ready(function(){
    $(".dropdown-toggle").dropdown("toggle");
});


$(function(){
    var x =$("#firstQuestion,#secondQuestion,#thirdQuestion,#fourthQuestion,#fifthQuestion,#sixthQuestion,#seventhQuestion,#eighthQuestion,#ninethQuestion,#10Question")
    x.hide()
    $("#first_button").click(function(){
        var x =$("#firstQuestion")
        x.toggle()       
    })
    $("#second_button").click(function(){
        var y =$("#secondQuestion")
        y.toggle()       
    })
    $("#third_button").click(function(){
        var y =$("#thirdQuestion")
        y.toggle()       
    })
    $("#fourth_button").click(function(){
        var y =$("#fourthQuestion")
        y.toggle()       
    })
    $("#fifth_button").click(function(){
        var y =$("#fifthQuestion")
        y.toggle()       
    })
    $("#sixth_button").click(function(){
        var y =$("#sixthQuestion")
        y.toggle()       
    })
    $("#seventh_button").click(function(){
        var y =$("#seventhQuestion")
        y.toggle()       
    })
    $("#eighth_button").click(function(){
        var y =$("#eighthQuestion")
        y.toggle()       
    })
    $("#nineth_button").click(function(){
        var y =$("#ninethQuestion")
        y.toggle()       
    })

    $("#10_button").click(function(){
        var y =$("#10Question")
        y.toggle()       
    })
    $("#11_button").click(function(){
        var y =$("#11Question")
        y.toggle()       
    })
    $("#12_button").click(function(){
        var y =$("#12Question")
        y.toggle()       
    })
})