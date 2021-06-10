$(document).ready(function () {
    $(".sidenav").sidenav({
        edge: "right"
    });
    $('.modal').modal();
    $(".dropdown-trigger").dropdown();
    $('select').formSelect();
    $('.tooltipped').tooltip();

    ingredientFieldSetup();
    methodFieldSetup();
    setupModal();
});

//Add_recipe.html
function ingredientFieldSetup() {
    var ingredientField = $(".ingredient").length;
    $("#add_ingredient").on("click", function () {
        $("select").formSelect("destroy");
        $(".new-ingredient:first").clone().insertBefore("#add_ingredient").find("input[type='text'], select, textarea").val("");
        $("select").formSelect();
        ingredientField += 1;
    });
    $("#remove_ingredient").on("click", function () {
        if (ingredientField > 1) {
            $(this).siblings(".new-ingredient:last").remove();
            ingredientField -= 1;
        }
    });
}
//Add method
function methodFieldSetup() {
    var methodField = $(".method").length;
    $("#add_method").on("click", function () {
        $("select").formSelect("destroy");
        $(".new-method:first").clone().insertBefore("#add_method").find("input[type='text'], select, textarea").val("");
        $("select").formSelect();
        methodField += 1;
    });
    $("#remove_method").on("click", function () {
        if (methodField > 1) {
            $(this).siblings(".new-method:last").remove();
            methodField -= 1;
        }
    });
}

//Modal function
function setupModal() {
    const modalOkBtn = document.getElementById('modalOkBtn');

    $('.remove-btn').click((event) => {
        const modal = document.getElementById('confirmationDialog');
        const instance = M.Modal.init(modal, {
            dismissible: false
        });
        instance.open();

        modalOkBtn.href = event.currentTarget.href;

        return false;
    });
}