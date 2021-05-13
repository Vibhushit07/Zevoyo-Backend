function getHotel(c) {

    var city = document.getElementById('city-2').value;

    console.log(city)

    $.ajax({
        url: '/myApp/staff/searchDashboard/',
        data: {
            'city': city
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
}