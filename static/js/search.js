/******************************************************************************/
/*  jQuery for returning input data                                           */
/******************************************************************************/
function isSearched(d) { return d.name === $("#search").getSelectedItemData().name }

/******************************************************************************/
/*  draw the search bar                                                       */
/******************************************************************************/
function drawSearch() {

  var options = {

    url: graphURL,

    placeholder: "Search",

    getValue: function(d) { return d.name.substring(d.name.lastIndexOf(".")+1)+" : "+String(d.search).split(",").join(" ,"); },

    list: { 

      showAnimation: {
        type: "slide",
        time: 150,
      },

      hideAnimation: {
        type: "slide",
        time: 150,
      },

      onSelectItemEvent: function() { node.filter(isSearched).each(function(d) { mouseovered(d); }); },
      onChooseEvent: function() { node.filter(isSearched).each(function(d) { mouseclick(d); }); },
      
      maxNumberOfElements: 10,
      match: {
        enabled: true
      },
      sort: {
        enabled: true
      }
    },

    theme: "round"
  };

  $("#search").easyAutocomplete(options);
}