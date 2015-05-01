/*jQuery(document).ready(function($) {
	
	$('#search_bar').keydown(function(event){    
    if(event.keyCode==13){
    	alert("sdfsdf");
    	  event.preventDefault();
       $('#search_button').trigger('click');
    }
	});
	jQuery("#search_button").click(function(event) {
		/* Act on the event */
		/*json = $('#search_bar').val()
		search_tweet();*/
//	$('#results').html(json);
	


       
    

});*/


function search_tweet (argument) {
	$.ajax({
        url : "search_tweet/", // the endpoint
        type : "GET", // http method
        data : { q : $('#search_bar').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#post-text').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
             $('#results').html(json);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });			
}

function search_redit (argument) {
	$.ajax({
        url : "http://www.reddit.com/search.json", // the endpoint
        type : "GET", // http method
        data : { q : $('#search_bar').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#post-text').val(''); // remove the value from the input
            console.log(json.data.children[0].data.selftext_html); // log the returned json to the console
            console.log("success"); // another sanity check
            $('#results').append("<pre>");
             $('#results').html("<pre>"+json.data.children[0].data.selftext);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });	
}