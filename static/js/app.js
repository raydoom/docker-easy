/**
 * appjs.
 */
function parse_result(data) {
    if (data.ret) {
        alert('success!')
    } else {
        alert('failed!')
    }
}

function container_opt(server_ip, server_port, container_Id, opt) {
    $.get("/" + server_ip + "/" + server_port + "/" + container_Id + "/" + opt + "/", function (data, status) {
        parse_result(data)
    });
}


function tail_log(server_ip, server_port, container_Id) {
    window.open("/" + server_ip + "/" + server_port + "/" + container_Id + "/tail/")
}

function show_server_status(server_id) {
    $.get("/" + server_ip + "/" + server_port + "/" + container_Id + "/"+ "/status/", function (data, status) {
        $('#server_div').html(data)
    });
}

