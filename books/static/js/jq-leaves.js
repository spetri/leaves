$(document).ready(function() {
  
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

$('#results-view tr').on("click", docViewerHeader);
$('#results-view tr').on("click", selectRow);

});