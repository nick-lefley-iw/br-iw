(function() {
    'use strict';
    window.addEventListener('load', function() {
        Array.prototype.filter.call(document.getElementsByClassName('needs-validation'), function(form) {
            form.addEventListener('submit', function(event) {
                Array.prototype.filter.call(form.getElementsByClassName('required'), function(input) {
                    if (!input.value) {
                        event.preventDefault();
                        event.stopPropagation();
                        input.classList.add("is-invalid");
                        input.parentElement.parentElement.getElementsByClassName("helper")[0].style.display = "initial";
                    } else {
                        input.classList.remove("is-invalid");
                        input.parentElement.parentElement.getElementsByClassName("helper")[0].style.display = "none";
                    }
                })
            }, false);

            var validate = function (input) {
                if (!input.value) {
                    input.classList.add("is-invalid");
                    input.parentElement.parentElement.getElementsByClassName("helper")[0].style.display = "initial";
                } else {
                    input.classList.remove("is-invalid");
                    input.parentElement.parentElement.getElementsByClassName("helper")[0].style.display = "none";
                }
            }

            Array.prototype.filter.call(document.getElementsByClassName('required'), function(input) {
                input.addEventListener('keyup', function(event) {
                    validate(input)
                }, false);
                input.addEventListener('click', function(event) {
                    validate(input)
                }, false);
            });
        });

        Array.prototype.filter.call(document.getElementsByClassName('close-modal'), function(modal) {
            modal.addEventListener('click', function() {
                Array.prototype.filter.call(document.getElementsByClassName('form-control'), function(input) {
                    input.value = ""
                    input.classList.remove("is-invalid");
                    input.parentElement.parentElement.getElementsByClassName("helper")[0].style.display = "none";
                });
            });
        });

        Array.prototype.filter.call(document.getElementsByClassName('update-modal'), function(button) {
            button.addEventListener('click', function() {
                Array.prototype.filter.call(document.getElementsByClassName('team-member-name'), function(input) {
                    input.value = button.dataset.teammembername;
                });
                Array.prototype.filter.call(document.getElementsByClassName('team-member-preference'), function(input) {
                    input.value = button.dataset.teammemberpreference;
                });
                Array.prototype.filter.call(document.getElementsByClassName('team-member-id'), function(input) {
                    input.value = button.dataset.teammemberid;
                });
            });
        });
    }, false);
})();
