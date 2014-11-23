document.addEventListener("DOMContentLoaded", function() {
  cardColors =  [{ top: '#68B78F', bottom: '#4CAF7C' }, 
              { top: '#9BC0CD', bottom: '#79B1C4' }, 
              { top: '#CDCA00', bottom: '#E7B700' },
              { top: '#C3322B', bottom: '#AF2B26' }];

  var cards = document.getElementsByClassName('card');
  var color = cardColors.shuffle();
  for (var i = 0; i < cards.length; i++) {
    current_color = color.pop()
    /*if(current_color) {
      $(cards[i]).find("div").css('background-color', current_color.top);      
      $(cards[i]).find("p:nth-child(4)").css('background-color', current_color.bottom);  
    }*/
  };
});  

$(document).ready(function() {

  Array.prototype.shuffle = function() {
    var input = this;
    for (var i = input.length-1; i >=0; i--) {
      var randomIndex = Math.floor(Math.random()*(i+1)); 
      var itemAtIndex = input[randomIndex];    
      input[randomIndex] = input[i]; 
      input[i] = itemAtIndex;
    }
    return input;
  };

  function docViewerHeader() {
    var tableInfo = getTableInformation($(this));
    var header = $('#docviewer-view div:first-child');
    header.addClass('docviewer-header');
    header.find('span:first-child').addClass('docviewer-title').text(tableInfo.title);
    header.find('span:nth-child(3)').addClass('docviewer-author').text(tableInfo.author);
  };

  function getTableInformation(row) {
    var title = row.find("td:first-child").text();
    var author = row.find("td:nth-child(2)").text();
    return {title: title, author: author};
  };

  function selectRow() {
    if($(this).hasClass('selected')) {
      $(this).removeClass('selected');
    } else {
      $(this).addClass('selected');
      $(this).siblings().removeClass('selected');
    };
  };

$('#results-view .cards .card').on("click", docViewerHeader);
$('#results-view tr').on("click", selectRow);

});