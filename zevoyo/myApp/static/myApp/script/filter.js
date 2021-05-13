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
                parent.appendChild(child)
            }

        }
    });
}