function getDetails(c) {

    var filter = document.getElementById('filter').value;

    $.ajax({
        url: '/myApp/staff/allbookings/filter/',
        data: {
            'filter': filter
        },
        dataType: 'json',
        success: function(res) {

            let parent = document.getElementById("data");
            parent.innerHTML = "";

            for (let i = 0; i < res.length; i++) {

                let child = document.createElement("option");
                child.innerHTML = res[i];
                child.setAttribute("value", res[i])
                parent.appendChild(child)
            }

        }
    });
}

// function getData(c) {

//     console.log(document.getElementById("data").value)

//     var filter = document.getElementById('filter').value;
//     var data = document.getElementById("data").value

//     $.ajax({
//         url: '/myApp/staff/allbookings/filter/data',
//         data: {
//             'filter': filter,
//             'data': data
//         },
//         dataType: 'json',
//         success: function(res) {

//             let parent = document.getElementById("data");
//             parent.innerHTML = "";

//             for (let i = 0; i < res.length; i++) {

//                 let child = document.createElement("option");
//                 child.innerHTML = res[i];
//                 child.setAttribute("value", res[i])
//                 parent.appendChild(child)
//             }

//         }
//     });
// }