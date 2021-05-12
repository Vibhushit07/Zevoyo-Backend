function getHotel(c) {

    var city = document.getElementById('city-2').value;

    $.ajax({
        url: '/myApp/staff/searchDashboard/',
        data: {
            'city': city
        },
        dataType: 'json',
        success: function(res) {

            let cities = res;
            let parent = document.getElementById("hotel");
            parent.innerHTML = "";

            for (let i = 0; i < cities.length; i++) {

                let child = document.createElement("option");
                child.innerHTML = cities[i].name;
                parent.appendChild(child)
            }

        }
    });
}