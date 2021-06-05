$("#filter").click(function() {

    var filter = document.getElementById('filter').value;

    let parent = document.getElementById("div-data");
    parent.innerHTML = "";

    if (filter === 'checkIn' || filter === 'checkOut') {

        var input = document.createElement("input");
        input.setAttribute("id", "data");
        input.setAttribute("type", "date");
        input.setAttribute("name", "data");
        parent.append(input);

        // } else if (filter === 'roomType') {

        //     let select = document.createElement("select");
        //     select.setAttribute("class", "form-control");
        //     select.setAttribute("id", "data");
        //     select.setAttribute("name", "data");

        //     let res = ['Premium', 'Deluxe', 'Basic']

        //     for (let i = 0; i < res.length; i++) {

        //         let child = document.createElement("option");
        //         child.innerHTML = res[i];
        //         child.setAttribute("value", i + 1)
        //         select.append(child)
        //     }

        //     parent.append(select);

        // } else if (filter === 'statusD') {

        //     let select = document.createElement("select");
        //     select.setAttribute("class", "form-control");
        //     select.setAttribute("id", "data");
        //     select.setAttribute("name", "data");

        //     let res = ['Available', 'Not Available']

        //     for (let i = 0; i < res.length; i++) {

        //         let child = document.createElement("option");
        //         child.innerHTML = res[i];
        //         child.setAttribute("value", i + 1)
        //         select.append(child)
        //     }

        //     parent.append(select);

    } else if (filter === 'statusB') {

        let select = document.createElement("select");
        select.setAttribute("class", "form-control");
        select.setAttribute("id", "data");
        select.setAttribute("name", "data");

        let res = ['Booked', 'Cancelled']

        for (let i = 0; i < res.length; i++) {

            let child = document.createElement("option");
            child.innerHTML = res[i];
            child.setAttribute("value", i + 1)
            select.appendChild(child)
        }

        parent.appendChild(select);

    } else {

        $.ajax({
            url: '/myApp/staff/filter/',
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