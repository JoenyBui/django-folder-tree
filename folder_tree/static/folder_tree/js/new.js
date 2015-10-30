/**
 * Created by JOENY on
 * Menu New Folder
 */

$(document).ready(function () {
    var new_tree = new Portal.Tree('#new_folder_tree',
                                   '#new_folder_selected',
                                   {}
    );

    // Get the new folder structure.
    new_tree.getTreeJsonFromServer();

    $('#btnCancel').click(function (e) {
        window.location.href = "/dash/";
    });

    // Create new folder
    $('#btnOkay').click(function(){
        var name = $('#inputCreateFolderName').val();
        var folder_path = $('#new_folder_selected').val();

        $.post('/api/profile/folder/',
            {name:name, path:folder_path},
            function(data) {
                /*Redirect to home*/
                window.location.replace("/dash/");
            },
            'json'
        ).fail(
            function (jqXHR, status) {
                var DATA = JSON.parse(jqXHR.responseText);

                if (DATA.hasOwnProperty('name')) {
                    $('#warning').text(DATA['name']).show("slow");
                }

            }
        );
    });
});