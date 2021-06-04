$(function() {
    $(".progress").each(function() {
        var value = $(this).attr('data-value')
        var left = $(this).find('.progress-left .progress-bar')
        var right = $(this).find('.progress-right .progress-bar')

        if (value > 0) {
            if (value <= 50) {
                right.css('transform', 'rotate(' + percentageToDegrees(value) + 'deg)')
            } else {
                right.css('transform', 'rotate(180deg)')
                left.css('transform', 'rotate(' + percentageToDegrees(value - 50) + 'deg)')
            }
        }
    })

    function percentageToDegrees(percentage) {

        return percentage / 100 * 360

    }

})

$("#city-2").click(function() {

    $.ajax({
        url: '/myApp/staff/searchDashboard/',
        data: {
            'city': $("#city-2").val()

        },
        dataType: 'json',
        success: function(res) {

            let parent = document.getElementById("hotel");
            parent.innerHTML = "";

            for (let i = 0; i < res.length; i++) {

                let child = document.createElement("option");
                child.innerHTML = res[i].name;
                parent.appendChild(child)
            }

        }
    });
})