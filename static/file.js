function load_data(file){
    console.log(file)
    var start_line = $('#start_line').val()
    var end_line = $('#end_line').val()
    url = "?file_name="+file+".txt&start_line="+start_line+"&end_line="+end_line
    $.ajax({
        url: url,
        type: 'GET',
        success: function(response){
            var result = $(response).find('#data');
            console.log(response);
            $('#data').replaceWith($('#data').html(response));
            $('#start_line').val(start_line)
            $('#end_line').val(end_line)
        },
        error: function(error){
            console.log(error);
        }
    });
}