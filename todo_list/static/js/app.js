function todo_post(input) {
    let id = $(input).attr('data-id');
    let done = $(input).attr('data-done');

    if(done == 'true') {
        $(input).attr('data-done', 'false');
        done = false;
    } else {
        $(input).attr('data-done', 'true');
        done = true;
    }

    $.ajax({
        'url': '/todos/' + id,
        'type': 'put',
        'datatype': 'json',
        'data': {
            'id': id, 'done': done
        },
        'success': function (data) {
            console.log(data);
            alert('Todo alterada com sucesso!');
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
               success: function(data) {
                   console.log(data);
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
                            $("#todos").append(
                                '<li class="todo_available">' + todo.title + ', ' + todo.project + '<input type="checkbox" data-id="' + todo.id + '" data-done="'+ todo.done +'" checked onclick="todo_post(this)">' + '</li>'
                            )
                        } else {
                            $("#todos").append(
                                '<li class="todo_available">' + todo.title + ', ' + todo.project + '<input type="checkbox" data-id="' + todo.id + '"  data-done="' + todo.done + '" onclick="todo_post(this)">' + '</li>'
                            )
                        }
                    });
                }
            })
        }
    });
    $("#back").on({
        click: function () {
            $("#add_todo").fadeIn();
            $("#list_todos").hide();
        }
    });
});