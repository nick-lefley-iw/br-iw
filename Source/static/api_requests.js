function deleteRound(roundId) {
    var xhr = new XMLHttpRequest();
    xhr.open("DELETE", "/drinks-round?id=" + roundId.toString(), true);
    xhr.send();
    xhr.onload = () => location.reload();
}

function deleteDrinkFromRound(roundId, drinkId) {
    var xhr = new XMLHttpRequest();
    xhr.open("DELETE", "/drinks-order?round_id=" + roundId.toString() + "&drink_id=" + drinkId.toString(), true);
    xhr.send();
    xhr.onload = () => location.reload();
}

function deleteOrderFromRound(roundId) {
    var xhr = new XMLHttpRequest();
    var teamMemberId = null;
    Array.prototype.filter.call(document.getElementsByClassName('selection'), function(selection) {
        teamMemberId = selection.dataset.id;
    });
    xhr.open("DELETE", "/drinks-order?round_id=" + roundId.toString() + "&team_member_id=" + teamMemberId.toString(), true);
    xhr.send();
    xhr.onload = () => location.reload();
}

function confirmOrder(roundId) {
    var xhr = null;

    Array.prototype.filter.call(document.getElementsByClassName('team-member-order'), function(selection) {
        xhr = new XMLHttpRequest();
        xhr.open("POST", "/drinks-order?round_id=" + roundId.toString() + "&team_member_id=" + selection.dataset.teammemberid + "&drink_id=" + selection.childNodes[1].childNodes[1].value, true);
        xhr.send();
    });

    xhr.onload = () => location.reload();
}

function clearOrders() {
    Array.prototype.filter.call(document.getElementsByClassName('order-table'), function(element) {
        element.style.display = "none"
    });

    var table = document.getElementById("order-body");
    document.getElementById("select-team-member-button").style.display = ""

    Array.prototype.filter.call(document.getElementsByClassName('team-member-order'), function(selection) {
        selection.remove()
    });
    Array.prototype.filter.call(document.getElementsByClassName('requires-selection-multiple'), function(button) {
        button.disabled = true
    });
}

function randomBrewer() {
    Array.prototype.filter.call(document.getElementsByClassName('round_brewer'), function(element) {
        var values = []
        for (i = 1; i < element.options.length; i++) {
            values.push(element.options[i].value)
        }
        element.value = values[Math.floor(Math.random()*values.length)]
    });
}