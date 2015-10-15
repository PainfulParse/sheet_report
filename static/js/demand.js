$(function() {
    paintButton = $('#display_paint')
    non_paintButton = $('#display_non_paint')

    paintButton.click(function() {
        var date = $('#paint_date').val();
        var report = 'Paint'
        console.log('Paint Button Clicked')

        //Disabled generate button so user can't keep submitting
        paintButton.attr('disabled', 'disabled');

        $.ajax({
            url: '/reports/paint/',
            data: {date, report},
            type: 'POST',
            success: function(response) {
                console.log('Response is : ' + response)
                $('#paintDiv').html('<p>' + response + '</p>')
                paintButton.removeAttr('disabled')
            },
            error: function(error) {
                console.log('Error--------------')
                console.log(error)
                paintButton.removeAttr('disabled')
            }
        });
    });

    non_paintButton.click(function() {
        var date = $('#non_paint_date').val();
        var report = 'Non Paint'
        console.log('Non Paint Button Clicked')

        //Disabled generate button so user can't keep submitting
        paintButton.attr('disabled', 'disabled');

        $.ajax({
            url: '/reports/non_paint/',
            data: {date, report},
            type: 'POST',
            success: function(response) {
                console.log('Response is : ' + response)
                $('#nonPaintDiv').html('<p>' + response + '</p>')
                paintButton.removeAttr('disabled')
            },
            error: function(error) {
                console.log('Error--------------')
                console.log(error)
                paintButton.removeAttr('disabled')
            }
        });
    });
});