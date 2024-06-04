$(document).ready(function () {

    var urlSplit = $(location).attr('href').split('/');
    let regex = /[A-Za-z0-9]+_/i;
    let page = null;
    for (var index in urlSplit) {
        if (regex.test(urlSplit[index])) {
            page = urlSplit[index].split('_')[0];
        }
    }
    //
    $('input[type="button"][id*="task-check-"]').on('click', function () {
        $(`input[type="checkbox"][id*=${this.id}]`).attr("checked", true);
        localStorage.setItem(page + "task-check-complete_coll_" + this.id, true);
    })

    $('[id*="task-check-"]').each(function () {
        if (localStorage.getItem(page + "task-check-complete_coll_" + this.id) === "true") {
            $(`details.activity > summary span[id="${this.id}"]`)
                .addClass("text-bg-success")
                .html("Completed");
            $(`details.activity > input[type="button"][id="${this.id}"]`)
                .addClass('btn-danger')
                .removeClass('btn-success')
                .attr("disabled", true)
        } else {
            !$(`details.activity > summary span[id="${this.id}"]`)
                .addClass("text-bg-primary")
                .html("Not Completed");
            $(this).attr('checked', false);
        }
    })
    //
    // console.log(localStorage)
})