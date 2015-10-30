$(document).ready(function () {
    var tree = new Portal.Tree('#folder_tree', '#folder_selected', {});
    tree.getTreeJsonFromServer();

    $('#btnCancel').click(function (e) {
        window.location.href = "/dash/";
    });

    $('#btnOkay').click(function () {
        var name = $('#folder_name').val();
        var folder_path = $('#folder_selected').val();

        $.delete('/api/profile/folder/',
            {name: name, path: folder_path},
            function (data) {
                window.location.replace('/dash/');
            }
        ).fail(
            function (jqXHR, status) {
                $('#warning').text(jqXHR.responseText);
            }
        );
    });
});