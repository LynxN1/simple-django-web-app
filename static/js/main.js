function modalLoad() {
    $.ajax({
        url: "/tasks/create",
        type: "GET",
        dataType: "HTML",
        success: function (data) {
            $("#exampleModal").html(data);
            $("#exampleModal").modal("show");
        }
    })
}