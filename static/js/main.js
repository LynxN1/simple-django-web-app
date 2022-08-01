$(".open-modal-btn").click(function () {
        var url = $(this).attr("data-url");
        $.ajax({
        url: url,
        type: "GET",
        dataType: "HTML",
        success: function (data) {
            $("#ajaxModal").html(data);
            $("#ajaxModal").modal("show");
        }
    })
});