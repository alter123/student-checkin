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

someJSONdata = [
    {
       name: 'John Doe',
       email: 'john@doe.com',
       phone: '111-111-1111'
    },
    {
       name: 'Barry Allen',
       email: 'barry@flash.com',
       phone: '222-222-2222'
    },
    {
       name: 'Cool Dude',
       email: 'cool@dude.com',
       phone: '333-333-3333'
    }
 ]

function reserve(pk){
    $.ajax({
        url: '/reserve/',
        data: {
            'pk': pk
        },
        dataType: 'json',
        success: function (data) {
            var printContents = '<p>Sagar Shingade</p>';
            var originalContents = document.body.innerHTML;
            document.body.innerHTML = printContents;
            window.print();
            document.body.innerHTML = originalContents;
            location.reload();
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
            alert("LIST HAS BEEN UPADATED!")
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
            alert("ALL DATA HAS BEEN DELETED!")
        }
     })
});


function confirm_alert(node) {
    return confirm("Confirm checking out all attendees");
}

function confirm_delete(node) {
    return confirm("Confirm deleteing all attendees");
}

