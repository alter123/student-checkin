var DEBUG = false;


// SEARCH FORM

$('#searchform').keyup(function(e) {
    var query = $("#searchform").val();
    if( query.length > 3 )
    $.ajax({
        url: '/checkin/',
        data: {
            'query': query
        },
        dataType: 'json',
        success: function (data) {
            append_list(data)
        }
    });
});


function reserve(pk){
    $.ajax({
        url: '/reserve/',
        data: {
            'pk': pk
        },
        dataType: 'json',
        success: function (data) {
            originalContents = document.body.innerHTML;
            document.body.innerHTML = printContents( 
                data.branch.toUpperCase(),
                data.name.toUpperCase(),
                data.seat.toString().toUpperCase(),
            )
            window.print()
            document.body.innerHTML = originalContents
            location.reload()
        }
    });
}


function append_list(data){
    // Generates Search Results Html

    student_list = data.list

    results = ""
    for( val in student_list ){

        results+= "<button type='button' class='list-group-item list-group-item-action' "+
        "onclick='reserve("+ student_list[val].pk + ")' > <div class='row'> <div class='col-md-5'>" +
            student_list[val].name
        + "</div> <div class='col-md-4'>" +
            student_list[val].rollno
        + "</div> <div class='col-md-1'>" +
            student_list[val].branch
        + "</div> </div>"
        + "</button>"
    }
    $('#results').html(results);
}


// UPLOAD FORM

$('.populate-button').click(function(){
    var docid = $(this).attr("id");
    $.ajax({
        type: 'GET',
        url: '/populate/'+docid,
        data: { pk: docid },
        success: function( data ){
        }
     })
});


$('.delete-button').click(function(){
    var docid = $(this).attr("id");
    $.ajax({
        type: 'GET',
        url: '/delete/'+docid,
        data: { pk: docid },
        success: function( data ){
            if(data.success == true){ 
                setTimeout(function(){
                     location.reload();
                }, 2000);
             }
        }
     })
});


$('#checkout-button').click(function(){
    $.ajax({
        url: '/manage/',
        data: { 
            'type': 'checkout'
         },
        success: function( data ){
            alert("LIST HAS BEEN UPADATED!")
        }
     })
});


$('#delete-button').click(function(){
    $.ajax({
        url: '/manage/',
        data: { 
            'type': 'delete'
         },
        success: function( data ){
        }
     })
});


function printContents( branch, name, seat ){
    return "<style scoped>table { padding-top: 50px; padding-right: 50px; padding-left: 50px; text-align: center; border-collapse: collapse; border-spacing: 0;width: 100%;border: none; } </style><br/><br/><br/><br/><br/><br/><br/><table cellspacing='0' cellpadding='0'><tbody><tr><td><h5>BRANCH</h5></td><td><h5>STUDENT</h5></td><td><h5>SEAT</h5></td></tr><tr><td><h2>"+ branch + "</h2></td><td><h2>"+ name +"</h2></td><td><h2>"+ seat +"</h2></td></tr></tbody></table>";
}