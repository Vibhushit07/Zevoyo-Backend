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

// $("#filter").click(function() {

//     var filter = document.getElementById('filter').value;

//     let parent = document.getElementById("div-data");
//     parent.innerHTML = "";

//     if (filter === 'checkIn' || filter === 'checkOut') {

//         var input = document.createElement("input");
//         input.setAttribute("id", "data");
//         input.setAttribute("type", "date");
//         input.setAttribute("name", "data");
//         parent.append(input);

//     } else if (filter === 'status') {

//         let select = document.createElement("select");
//         select.setAttribute("class", "form-control");
//         select.setAttribute("id", "data");
//         select.setAttribute("name", "data");

//         let res = ['Available', 'Not Available']

//         for (let i = 0; i < res.length; i++) {

//             let child = document.createElement("option");
//             child.innerHTML = res[i];
//             child.setAttribute("value", i + 1)
//             select.append(child)
//         }

//         parent.append(select);

//     } else if (filter === 'roomType') {

//         let select = document.createElement("select");
//         select.setAttribute("class", "form-control");
//         select.setAttribute("id", "data");
//         select.setAttribute("name", "data");

//         let res = ['Premium', 'Deluxe', 'Basic']

//         for (let i = 0; i < res.length; i++) {

//             let child = document.createElement("option");
//             child.innerHTML = res[i];
//             child.setAttribute("value", i + 1)
//             select.append(child)
//         }

//         parent.append(select);

//     } else {

//         $.ajax({
//             url: '/myApp/staff/filter/',
//             data: {
//                 'filter': filter
//             },
//             dataType: 'json',
//             success: function(res) {

//                 let select = document.createElement("select");
//                 select.setAttribute("class", "form-control");
//                 select.setAttribute("id", "data");
//                 select.setAttribute("name", "data");

//                 for (let i = 0; i < res.length; i++) {

//                     let child = document.createElement("option");
//                     child.innerHTML = res[i];
//                     child.setAttribute("value", res[i])
//                     select.append(child)
//                 }

//                 parent.append(select);
//             }
//         });
//     }
// })