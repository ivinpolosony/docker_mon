 google.load("search", "1");
 //google.load("search", "1", {"nocss" : true});

      // Call this function when the page has been loaded
      function initialize() {
        var searchControl = new google.search.SearchControl();
//searchControl.setOnKeepCallback(this, MyKeepHandler);
        var options = new google.search.SearcherOptions();
        options.setExpandMode(google.search.SearchControl.EXPAND_MODE_OPEN);
          options.setRoot(document.getElementById("tes"));


        searchControl.addSearcher(new google.search.WebSearch(),options);
   //     searchControl.addSearcher(new google.search.NewsSearch());
        searchControl.draw(document.getElementById("searchcontrol"));



/*
App.prototype.OnSearchComplete = function(sc, searcher) {

  // if we have local search results, put them on the map
  if ( searcher.results && searcher.results.length > 0) {
    for (var i = 0; i < searcher.results.length; i++) {
      var result = searcher.results[i];

      // if this is a local search result, then proceed...
      if (result.GsearchResultClass == GlocalSearch.RESULT_CLASS ) {
       

App.prototype.OnSearchStarting = function(sc, searcher, query) {
  alert("The Query is: " + query);*/


      }

      
      google.setOnLoadCallback(initialize);





