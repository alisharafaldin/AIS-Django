 // داخل ملف ajax.js
  $(document).ready(function() {
    // General function to update dropdowns
    function updateDropdown(url, sourceID, targetID, paramName, callback) {
        var paramValue = $("#" + sourceID).val(); // get the selected ID from the HTML input
        $.ajax({
            url: url,
            data: {
                [paramName]: paramValue
            },
            success: function (data) {
                $("#" + targetID).html(''); // clear the existing options in the target dropdown
                $.each(data, function (key, value) {
                    $("#" + targetID).append('<option value="' + value.id + '">' + value.name_ar + '</option>');
                });
                if (callback) callback(); // execute callback function if provided
            },
            error: function (xhr, errmsg, err) {
                console.log("Error: " + errmsg); // log any error
            }
        });
    }
    // Update regions based on selected country
    function updateRegions() {
        var url = $("#id_countryID").data('url-region'); // the URL to get the regions
        updateDropdown(url, "id_countryID", "id_regionID", "countryID", updateStates);
    }
    // Update states based on selected region
    function updateStates() {
        var url = $("#id_stateID").data('url-state'); // the URL to get the states
        updateDropdown(url, "id_regionID", "id_stateID", "regionID", updateCity);
    }
    // Update cities based on selected state
    function updateCity() {
        var url = $("#id_cityID").data('url-city'); // the URL to get the cities
        updateDropdown(url, "id_stateID", "id_cityID", "stateID");
    }
    // Call functions on page load
    updateRegions();
    updateStates();
    updateCity();
    // Call functions when dropdowns change
    $('#id_countryID').change(updateRegions);
    $('#id_regionID').change(updateStates);
    $('#id_stateID').change(updateCity);
});
