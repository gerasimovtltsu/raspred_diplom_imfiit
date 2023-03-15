let form = document.querySelector('form')
let theme = document.getElementById('id_topic_title');
let supervisor = document.getElementById('id_supervisor_name');

form.method = "POST";

supervisor.setAttribute('disabled', '');

theme.addEventListener('change', function () {
    if (theme.value != '---------') {
        supervisor.removeAttribute('disabled');
    }
})