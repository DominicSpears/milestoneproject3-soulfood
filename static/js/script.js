 $(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
});

$(document).ready(function(){
    $('select').formSelect();
});

$(document).ready(function(){
    $('.tooltipped').tooltip();
  });

// ingredients list function
// function ingrList() {
//     let item = document.getElementById("ingrInput").nodeValue
//     let text = document.createTextNode(item)
//     let newItem = document.createElement("li")
//     newItem.appendChild(text)
//     document.getElementById("ingrList").appendChild(newItem)
// }

// metho function
function methodList() {
    let item = document.getElementById("method").value
    let text = document.createTextNode(item)
    let newItem = document.createElement("li")
    newItem.appendChild(text)
    document.getElementById("methodList").appendChild(newItem)
}









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


