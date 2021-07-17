var subtype = (document.getElementById('id_use_sub_type').value);
var type = (document.getElementById('id_use_type').value);

$(document).ready(function(){
    function dropdowns(){
        var url = $("#serviceAreaCalculatorForm").attr("sub_types_url");
        console.log(subtype);
        if (type == '1' || subtype == ''){
            success = function (data) {
                $('#id_use_sub_type').html(data);
                };
        } else {
            success = function (data) {
            $('#id_use_sub_type').html(data);
            $('#id_use_sub_type').val(subtype);
            };
        }

        $.ajax({
            url: url,
            data: {
                'use_type': type,
            },
            success: success,
        });
    }

    function refreshPage(){
        if (type === '1'){
            $('label[for="id_use_sub_type"]').hide();
            $('#id_use_sub_type').hide();  
            $('label[for="id_units"]').html('Enter Number of Residential units to be built:');
            $('label[for="id_units"]').show();
            $('#id_units').show();
            document.getElementById("id_units").required = true;
            $('label[for="id_square_feet"]').html('Enter Size of Individual Residential Unit (square feet):');
            $('label[for="id_square_feet"]').show();
            $('#id_square_feet').show();
            $('#results').html('Amount (Per Unit)');
            document.getElementById("id_square_feet").required = true;
        } else if (type === '3'){
            if (subtype === '7') {
                $('label[for="id_use_sub_type"]').show();
                $('#id_use_sub_type').show();
                document.getElementById("id_use_sub_type").required = true; 
                $('label[for="id_units"]').html('Enter Number of Hotel Rooms to be built:');
                $('label[for="id_units"]').show();
                $('#id_units').show();  
                document.getElementById("id_units").required = true;
                $('label[for="id_square_feet"]').hide();
                $('#id_square_feet').hide(); 
                $('#results').html('Amount (Per Unit)');
                document.getElementById("id_square_feet").required = false;
            } else {
                $('label[for="id_use_sub_type"]').show();
                $('#id_use_sub_type').show();
                document.getElementById("id_use_sub_type").required = true;  
                $('label[for="id_units"]').hide();
                $('#id_units').hide();  
                document.getElementById("id_units").required = false;        
                $('label[for="id_square_feet"]').html('Enter Size of Building (square feet):');
                $('label[for="id_square_feet"]').show();
                $('#id_square_feet').show(); 
                document.getElementById("id_square_feet").required = true;
            }
        } else {
            $('label[for="id_use_sub_type"]').show();
            $('#id_use_sub_type').show();
            document.getElementById("id_use_sub_type").required = true;  
            $('label[for="id_units"]').hide();
            $('#id_units').hide();
            document.getElementById("id_units").required = false;          
            $('label[for="id_square_feet"]').html('Enter Size of Building (square feet):');
            $('label[for="id_square_feet"]').show();
            $('#id_square_feet').show(); 
            document.getElementById("id_square_feet").required = true;
        }
    };

    document.getElementById('id_use_type').addEventListener('change', function() {
        type = this.value;
        subtype = '';
        $('#fees').hide();
        dropdowns();
        refreshPage();
    });

    document.getElementById('id_use_sub_type').addEventListener('change', function() { 
        subtype = this.value; 
        $('#fees').hide();
        refreshPage(); 
    });
    
    refreshPage();
    dropdowns();
});
