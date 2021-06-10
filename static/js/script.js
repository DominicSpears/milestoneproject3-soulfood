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


//-----------------------------------Add_recipe.html
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
            /* only remove the :last item */
            $(this).siblings(".new-ingredient:last").remove();
            /* ensure original ingredient line never gets deleted */
            ingredientField-= 1;
        }
    });
}

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
            /* only remove the :last item */
            $(this).siblings(".new-method:last").remove();
            /* ensure original method line never gets deleted */
            methodField-= 1;
        }
    });
}


function setupModal() {
    const modalOkBtn = document.getElementById('modalOkBtn');

    /** All remove button that require the modal dialogs should have the class remove-btn added */
    $('.remove-btn').click((event) => {
        const modal = document.getElementById('confirmationDialog');
        const instance = M.Modal.init(modal, { dismissible:false });
        instance.open();

        modalOkBtn.href = event.currentTarget.href;

        return false;
    });
}