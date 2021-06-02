$(document).ready(function () {
    $(".sidenav").sidenav({
        edge: "right"
    });

    $('select').formSelect();
    $('.tooltipped').tooltip();
    ingredientFieldSetup();
    methodFieldSetup();
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

//-----------------------------------Add_recipe.html








 // validateMaterializeSelect();
 //     function validateMaterializeSelect() {
 //         let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
 //         let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
 //         if ($("select.validate").prop("required")) {
 //             $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
 //         }
 //         $(".select-wrapper input.select-dropdown").on("focusin", function () {
 //             $(this).parent(".select-wrapper").on("change", function () {
 //                 if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
 //                     $(this).children("input").css(classValid);
 //                 }
 //             });
 //         }).on("click", function () {
 //             if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
 //                 $(this).parent(".select-wrapper").children("input").css(classValid);
 //             } else {
 //                 $(".select-wrapper input.select-dropdown").on("focusout", function () {
 //                     if ($(this).parent(".select-wrapper").children("select").prop("required")) {
 //                         if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
 //                             $(this).parent(".select-wrapper").children("input").css(classInvalid);
 //                         }
 //                     }
 //                 });
 //             }
 //         });
 //     };