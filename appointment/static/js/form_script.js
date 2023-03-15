let form = document.getElementsByClassName('post-form');
let theme = document.getElementById('id_topic_title');
let supervisor = document.getElementById('id_supervisor_name');

form.method = "POST";

if (document.body.contains(supervisor)) {
    supervisor.setAttribute('disabled', '');
}

if (document.body.contains(theme)) {
    theme.addEventListener('change', function () {
        if (theme.value != '---------') {
            supervisor.removeAttribute('disabled');
        }
    })
}