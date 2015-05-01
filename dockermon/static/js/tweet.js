
$.getJSON( "/latest_tweet/", function( data ) {
  var items = [];
  console.log(data[0].text);
 	for(var twt_i = 0 ; twt_i < data.length; twt_i++ ){
 		
 		items.push( "<img src=" + data[twt_i].user.profile_image_url_https + "/>&nbsp&nbsp&nbsp<b>"+data[0].text +"</b><hr><br>");
 		
    
    	
 	}
 
  	$("#latest_tweet").html(items);  
 
 
  
});

 
 var f = $(".gsc-search-button");
//alert(f);

console.log("dfghjk"); 
