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

function container_opt(server_ip, server_port, container_id, opt) {
    $.get("/" + server_ip + "/" + server_port + "/" + container_id + "/" + opt + "/", function (data, status) {
        parse_result(data)
    });
}


function tail_log(server_ip, server_port, container_id) {
    window.open("/" + server_ip + "/" + server_port + "/" + container_id + "/tail/")
}
