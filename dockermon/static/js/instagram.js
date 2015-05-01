 var userFeed = new Instafeed({
        get: 'user',
        userId: 199117602,
        accessToken: '199117602.467ede5.ae85c621804d4cfa893f4243b7fc39b6',
        target:'insta'

    });
    userFeed.run();

function function_name (query) {
    
    $("#insta").html(" ");
	var feed = new Instafeed({
        get: 'tagged',
        tagName: query,
        clientId: 'e0ae0e1d75f742d38b3fbce19fde5712',
        target:'insta'
    });
    feed.run();

$.ajax({
        url : "search_tweet/", // the endpoint
        type : "GET", // http method
        data : { q : query }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#post-text').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
             $('#latest_tweet').html(json);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });   




    $.ajax({
        url : "http://www.reddit.com/search.json", // the endpoint
        type : "GET", // http method
        data : { q : query }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#post-text').val(''); // remove the value from the input
            console.log(json.data.children[0].data.selftext_html); // log the returned json to the console
            console.log("success"); // another sanity check
            for(var loop_i = 0 ;loop_i< json.data.children.length; loop_i++ ){
            $('#redit').append("<hr>");
             $('#redit').append("<pre>"+json.data.children[loop_i].data.selftext+"</pre>");
            $('#redit').append("<hr>");
            }
            alert("You Searched for "+ query);

        },  

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });       
}
  