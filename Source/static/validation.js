(function() {
    'use strict';
    window.addEventListener('load', function() {
        Array.prototype.filter.call(document.getElementsByClassName('needs-validation'), function(form) {
            var validate = function (input) {
                if (!input.value) {
                    input.classList.add("is-invalid");
                    input.parentElement.parentElement.getElementsByClassName("helper")[0].style.display = "initial";
                } else {
                    input.classList.remove("is-invalid");
                    input.parentElement.parentElement.getElementsByClassName("helper")[0].style.display = "none";
                }
            }

            var validateMatch = function(input) {
                var values = []
                Array.prototype.filter.call(form.getElementsByClassName('match'), function(input) {
                    values.push(input.value)
                })
                if (new Set(values).size != 1) {
                    input.classList.add("is-invalid");
                    input.parentElement.parentElement.getElementsByClassName("match-helper")[0].style.display = "initial";
                } else {
                    input.classList.remove("is-invalid");
                    input.parentElement.parentElement.getElementsByClassName("match-helper")[0].style.display = "none";
                }
            }

            form.addEventListener('submit', function(event) {
                Array.prototype.filter.call(form.getElementsByClassName('required'), function(input) {
                    if (!input.value) {
                        event.preventDefault();
                        event.stopPropagation();
                    }
                    validate(input)
                })

                var values = []
                Array.prototype.filter.call(form.getElementsByClassName('match'), function(input) {
                    values.push(input.value)
                })
                if (new Set(values).size > 1) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                Array.prototype.filter.call(document.getElementsByClassName('second-match'), function(input) {
                    if (new Set(values).size != 1) {
                        input.classList.add("is-invalid");
                        input.parentElement.parentElement.getElementsByClassName("match-helper")[0].style.display = "initial";
                    } else {
                        input.classList.remove("is-invalid");
                        input.parentElement.parentElement.getElementsByClassName("match-helper")[0].style.display = "none";
                    }
                });
            }, false);

            Array.prototype.filter.call(document.getElementsByClassName('required'), function(input) {
                input.addEventListener('keyup', function(event) {
                    validate(input)
                }, false);
                input.addEventListener('click', function(event) {
                    validate(input)
                }, false);
            });

            Array.prototype.filter.call(document.getElementsByClassName('second-match'), function(input) {
                input.addEventListener('keyup', function(event) {
                    validateMatch(input)
                }, false);
                input.addEventListener('click', function(event) {
                    validateMatch(input)
                }, false);
            });
        });

        Array.prototype.filter.call(document.getElementsByClassName('close-modal'), function(modal) {
            modal.addEventListener('click', function() {
                Array.prototype.filter.call(document.getElementsByClassName('required'), function(input) {
                    input.value = ""
                    input.classList.remove("is-invalid");
                    input.parentElement.parentElement.getElementsByClassName("helper")[0].style.display = "none";
                });

                Array.prototype.filter.call(document.getElementsByClassName('hide-on-close'), function(input) {
                    input.style.display = "none";
                });
            });
        });

        Array.prototype.filter.call(document.getElementsByClassName('open-modal'), function(button) {
            button.click()
        });

        Array.prototype.filter.call(document.getElementsByClassName('update-modal'), function(button) {
            button.addEventListener('click', function() {
                Array.prototype.filter.call(document.getElementsByClassName('team-member-name'), function(input) {
                    Array.prototype.filter.call(document.getElementsByClassName('selection'), function(selection) {
                        input.value = selection.dataset.teammembername;
                    });
                });
                Array.prototype.filter.call(document.getElementsByClassName('team-member-preference'), function(input) {
                    Array.prototype.filter.call(document.getElementsByClassName('selection'), function(selection) {
                        input.value = selection.dataset.teammemberpreference;
                    });
                });
                Array.prototype.filter.call(document.getElementsByClassName('team-member-id'), function(input) {
                    Array.prototype.filter.call(document.getElementsByClassName('selection'), function(selection) {
                        input.value = selection.dataset.teammemberid;
                    });
                });
            });
        });

        Array.prototype.filter.call(document.getElementsByClassName('update-drink-modal'), function(button) {
            button.addEventListener('click', function() {
                Array.prototype.filter.call(document.getElementsByClassName('drink-name'), function(input) {
                    Array.prototype.filter.call(document.getElementsByClassName('selection'), function(selection) {
                        input.value = selection.dataset.drinkname;
                    });
                });
                Array.prototype.filter.call(document.getElementsByClassName('drink-id'), function(input) {
                    Array.prototype.filter.call(document.getElementsByClassName('selection'), function(selection) {
                        input.value = selection.dataset.drinkid;
                    });
                });
            });
        });

        Array.prototype.filter.call(document.getElementsByClassName('new-round-modal'), function(button) {
            button.addEventListener('click', function() {
                Array.prototype.filter.call(document.getElementsByClassName('round-id'), function(input) {
                    input.value = button.dataset.roundid;
                });
            });
        });

        Array.prototype.filter.call(document.getElementsByClassName('prepopulate-data'), function(button) {
            button.addEventListener('click', function() {
                Array.prototype.filter.call(document.getElementsByClassName('prepopulate'), function(input) {
                    input.value = "true";
                });
            });
        });

        Array.prototype.filter.call(document.getElementsByClassName('search-drink'), function(search) {
            search.addEventListener('keyup', function(event) {
                if (search.value) {
                    Array.prototype.filter.call(document.getElementsByClassName('drink-item'), function(item) {
                        if (!item.innerText.toLowerCase().includes(search.value.toLowerCase())) {
                            item.parentElement.style.display = "none"
                        } else {
                            item.parentElement.style.display = ""
                        }
                    })
                } else {
                    Array.prototype.filter.call(document.getElementsByClassName('drink-item'), function(item) {
                        item.parentElement.style.display = ""
                    })
                }
            }, false);
        });

        Array.prototype.filter.call(document.getElementsByClassName('search-team-member'), function(search) {
            search.addEventListener('keyup', function(event) {
                if (search.value) {
                    Array.prototype.filter.call(document.getElementsByClassName('team-member-item'), function(item) {
                        if (!item.childNodes.item("item-name").nextElementSibling.innerText.toLowerCase().includes(search.value.toLowerCase())
                                && !item.childNodes.item("item-preference").nextElementSibling.nextElementSibling.innerText.toLowerCase().includes(search.value.toLowerCase())) {
                            item.style.display = "none"
                        } else {
                            item.style.display = ""
                        }
                    })
                } else {
                    Array.prototype.filter.call(document.getElementsByClassName('team-member-item'), function(item) {
                        item.style.display = ""
                    })
                }
            }, false);
        });

        Array.prototype.filter.call(document.getElementsByClassName('clickable-row'), function(row) {
            row.addEventListener('click', function(event) {
                if (row.classList.contains('bg-secondary')){
                    row.classList.remove('bg-secondary');
                    row.classList.remove('text-light');
                    Array.prototype.filter.call(document.getElementsByClassName('requires-selection'), function(button) {
                        button.disabled = true
                    });
                } else {
                    Array.prototype.filter.call(document.getElementsByClassName('clickable-row'), function(sibling) {
                        sibling.classList.remove('bg-secondary');
                        sibling.classList.remove('text-light');
                    });
                    Array.prototype.filter.call(document.getElementsByClassName('requires-selection'), function(button) {
                        button.disabled = false
                    });
                    row.classList.add('selection');
                    row.classList.add('bg-secondary');
                    row.classList.add('text-light');
                }
            }, false);
        });
    }, false);
})();
