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