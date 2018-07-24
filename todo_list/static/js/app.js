var _completes = 0;
var _uncompetles = 0;
function modal_todo(input) {
    let id = $(input).attr('data-id');
    let done = $(input).attr('data-done');
    $("#modal-delete").modal();
    $("#confirm-button").on({
        click: function () {
            $.ajax({
                'url': '/todos/' + id,
                'type': 'delete',
                'success': function () {
                    $(input).parent().remove();
                    if(done == 'true') {
                        _completes -= 1;
                        if(_completes <= 0) {
                            $("#title-completes").hide();
                        }
                    } else {
                        _uncompetles -= 1;
                        if(_uncompetles <= 0) {
                            $("#title-uncompletes").hide();
                        }
                    }
                }
            });
            $("#modal-delete").modal('hide');
        }
    });
}

function todo_complete(input) {
    let id = $(input).attr('data-id');
    let done = $(input).attr('data-done');

    if(done == 'false') {
        done = true;
    } else {
        done = true;
    }
    $(input).parent().children('button[data-id="' + id + '"]').attr('data-done', done);

    $.ajax({
        'url': '/todos/' + id,
        'type': 'put',
        'datatype': 'json',
        'data': {
            'id': id, 'done': done
        },
        'success': function () {
            $("#modal-complete").modal();
            $("#todos-complete").append($(input).parent().parent().parent());
            $(input).remove();
            _uncompetles -= 1;
            _completes += 1;
            $("#title-completes").show();
            if(_uncompetles <= 0) {
                $("#title-uncompletes").hide();
            }
        }
    })
}

$(document).ready( function () {
    $("#save").on({
       click: function () {
           let title = $("#title").val();
           let project = $("#project").val();
           let done = $("#done").is(':checked');

           $.post({
               'url': '/todos',
               'datatype': 'Json',
               'data': {'title': title, 'project': project, 'done': done},
               success: function() {
                   $("#modal-save").modal();
               }
           })
       }
    });
    $("#list").on({
        click: function () {
            $("#add_todo").hide();
            $("#list_todos").fadeIn();
            $.get({
                'url': '/todos',
                'datatype': 'json',
                'success': function (data) {
                    data.forEach(function(todo) {
                        if(todo.done) {
                            _completes += 1;
                            $("#title-completes").show();
                            let card = "<div class='col-3'>" +
                                "<div class='card card-todo'>" +
                                "  <div class='card-body'>" +
                                "    <h5 class='card-title'>" + todo.project + "</h5>" +
                                "    <p class='card-text'>" + todo.title  + "</p>" +
                                "    <button type='button' class='btn btn-danger' onclick='modal_todo(this)' data-id='"+ todo.id +"' data-done='" + todo.done + "'>Delete</button>" +
                                "  </div>" +
                                "</div>" +
                                "</div>";
                            $("#todos-complete").append(card );
                        } else {
                            _uncompetles += 1;
                            $("#title-uncompletes").show();
                            let card = "<div class='col-3'>" +
                                "<div class='card card-todo'>" +
                                "  <div class='card-body'>" +
                                "    <h5 class='card-title'>" + todo.project + "</h5>" +
                                "    <p class='card-text'>" + todo.title  + "</p>" +
                                "    <button type='button' class='btn btn-success' onclick='todo_complete(this)' data-id='" + todo.id + "' data-done='" + todo.done + "'>Complete</button>" +
                                "    <button type='button' class='btn btn-danger' onclick='modal_todo(this)' data-id='"+ todo.id +"' data-done='" + todo.done + "'>Delete</button>" +
                                "  </div>" +
                                "</div>" +
                                "</div>";
                            $("#todos-uncomplete").append(card);
                        }
                    });
                }
            })
        }
    });
    $("#back").on({
        click: function () {
            $("#todos-uncomplete div").remove();
            $("#todos-complete div").remove();
            $("#add_todo").fadeIn();
            $("#list_todos").hide();
        }
    });
});