$(function() {
            genButton = $('#genButton')

            genButton.click(function() {
                var begin      = $('#begRange').val();
                var end        = $('#endRange').val();
                var chartType  = $('#select_chart_type').val();
                var begMonth   = $('#select_beg_month').val();
                var endMonth   = $('#select_end_month').val();
                var v1Checked  = $('#v1').prop('checked');
                var v2Checked  = $('#v2').prop('checked');
                var v3Checked  = $('#v3').prop('checked');
                var v5Checked  = $('#v5').prop('checked');
                var l1Checked  = $('#l1').prop('checked');
                var p1Checked  = $('#p1').prop('checked');
                var t1Checked  = $('#t1').prop('checked');
                var t2Checked  = $('#t2').prop('checked');
                var sg1Checked = $('#sg1').prop('checked');
                var sg2Checked = $('#sg2').prop('checked');
                var sg3Checked = $('#sg3').prop('checked');
                var sg4Checked = $('#sg4').prop('checked');
                var sg5Checked = $('#sg5').prop('checked');
                var mach       = [];

                //Disabled generate button so user can't keep submitting
                genButton.attr('disabled', 'disabled');

                //Determind which checkboxes are selcted
                if (v1Checked) {
                    mach.push('v1')
                } 
                if (v2Checked) {
                    mach.push('v2')
                }
                if (v3Checked) {
                    mach.push('v3')
                }
                if (v5Checked) {
                    mach.push('v5')
                } 
                if (l1Checked) {
                    mach.push('l1')
                }
                if (p1Checked) {
                    mach.push('p1')
                }
                if (t1Checked) {
                    mach.push('t1')
                } 
                if (t2Checked) {
                    mach.push('t2')
                }
                if (sg1Checked) {
                    mach.push('sg1')
                }
                if (sg2Checked) {
                    mach.push('sg2')
                } 
                if (sg3Checked) {
                    mach.push('sg3')
                }
                if (sg4Checked) {
                    mach.push('sg4')
                }
                if (sg5Checked) {
                    mach.push('sg5')
                }

                //Convert array to JSON string to be passed to python script main.py
                mach = JSON.stringify(mach);

                //Check if all fields have been filled in correctly
                if (chartType == 'none'){
                    $('#chart').html('<p>Select Chart Type</p>')
                    genButton.removeAttr('disabled')
                } else if (new Date(end) < new Date(begin)) {
                    $('#chart').html('<p>End Date must be after Start Date</p>')
                    genButton.removeAttr('disabled')
                } else if (begin == '' || end == '') {
                    $('#chart').html('<p>You must select a valid date</p>')
                    genButton.removeAttr('disabled')
                } else {
                    $('#chart').html('<p>Generating Chart....</p>')
                        //Ajax call to send data (begin date, end date, 
                        //chart type, and mach array) to main.py
                        $.ajax({
                        url: '/build/',
                        data: {begin,end,chartType,mach},
                        type: 'POST',
                        success: function(response) {
                            $('#chart').html(response)
                            console.log('Response is : ' + response)
                            genButton.removeAttr('disabled')
                        },
                        error: function(error) {
                            $('#chart').html('<p>Unable to generate chart</p>')
                            console.log(error)
                            genButton.removeAttr('disabled')
                        }
                    });
                }
            });
        });