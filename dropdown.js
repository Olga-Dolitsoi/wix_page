//$(document).ready(function () {
//    // Initialize the datepicker
//    $("#datepicker").datepicker({
//        onSelect: function (date) {
//            // Parse the selected date to match the format in your DataFrame
//            // This is just an example; adjust the date parsing as needed
//            var selectedDate = new Date(date);
//            selectedDate = selectedDate.toISOString().slice(0, 10); // Convert to yyyy-mm-dd format
//
//            // Filter the DataFrame based on the selected date
//            var filteredData = df[df['date'] === selectedDate];
//
//            // Update the Plotly plot with the filtered data
//            Plotly.update("plot", {
//                x: [filteredData['date']],
//                y: [filteredData['net_pnl']],
//            });
//        }
//    });
//});
