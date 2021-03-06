function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

document.addEventListener('DOMContentLoaded', function () {

    $(document).ready(function () {
        $(".size").click(function () {
            var buttonData = $(this).data("mydata");
            for (var i = 0; i < document.getElementsByClassName('size').length; i++) {
                document.getElementsByClassName('size')[i].className = 'size'
            }
            $(this).toggleClass('size_active')
            var preview = document.getElementById("id_size");
            preview.setAttribute("value", buttonData);
        });
    });

    $(document).ready(function () {
        $(".add_to_fav").click(function () {
            var product = $(this).data('id');
            var redirect = $(this).data('info')
            var in_fav = document.getElementsByClassName('add_to_fav')[0].getAttribute('data-in_fav')
            if (redirect === 'log') {
                window.location.replace("../../account/login/");
            } else {
                if (in_fav === 'add') {
                    $.ajax({
                        data: {'product': product, 'csrfmiddlewaretoken': csrftoken},
                        url: 'http://127.0.0.1:8000/favorites/add/' + product + '/',
                        method: 'post',
                        headers: {'Access-Control-Allow-Origin': '*'},
                        success: function (response) {
                            console.log(response)
                            document.getElementById('img-fav').src = '../../static/img/added.png'
                            document.getElementsByClassName('add_to_fav')[0].setAttribute('data-in_fav', 'added')
                        },
                        error: function (response) {
                            console.log(response)
                        }
                    })
                } else {
                    $.ajax({
                        data: {'product': product, 'csrfmiddlewaretoken': csrftoken},
                        url: 'http://127.0.0.1:8000/favorites/remove/' + product + '/',
                        headers: {'Access-Control-Allow-Origin': '*'},
                        method: 'post',
                        success: function (response) {
                            console.log(response)
                            document.getElementById('img-fav').src = '../../static/img/add.png'
                            document.getElementsByClassName('add_to_fav')[0].setAttribute('data-in_fav', 'add')
                        },
                        error: function (response) {
                            console.log(response)
                        }
                    })
                }
            }
        });
    });
});





