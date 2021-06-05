$("#filter").click(function() {

    var filter = document.getElementById('filter').value;

    let parent = document.getElementById("div-data");
    parent.innerHTML = "";

    if (filter === 'checkIn' || filter === 'checkOut') {

        var input = document.createElement("input");
        input.setAttribute("id", "data");
        input.setAttribute("type", "date");
        input.setAttribute("name", "data");
        input.setAttribute("class", "form-control");
        parent.append(input);

    } else if (filter === 'allBookings' || filter === 'allUserBookings' || filter === 'allRooms') {

        var input = document.createElement("input");
        input.setAttribute("type", "hidden");
        input.setAttribute("name", "data");

        if (filter === 'allBookings')
            input.setAttribute("value", "allBookings");
        else if (filter === 'allUserBookings')
            input.setAttribute("value", "allUserbookings");
        else
            input.setAttribute("value", "allRooms");

        parent.append(input);

    } else {

        $.ajax({
            url: '/myApp/filter/',
            data: {
                'filter': filter
            },
            dataType: 'json',
            success: function(res) {

                let select = document.createElement("select");
                select.setAttribute("class", "form-control");
                select.setAttribute("id", "data");
                select.setAttribute("name", "data");

                for (let i = 0; i < res.length; i++) {

                    let child = document.createElement("option");
                    child.innerHTML = res[i];
                    child.setAttribute("value", res[i])
                    select.append(child)
                }

                parent.append(select);
            }
        });
    }
})