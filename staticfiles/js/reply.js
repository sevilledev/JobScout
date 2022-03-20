parent_id = document.querySelector(".hidden-input")
main_parent_id = document.querySelector(".main-hidden-input")
reply_name = document.getElementById("reply-name")
reply_message = document.getElementById("reply-content")
reply_info = document.getElementById("reply_info")


function reply_comment(comment_id){
    reply_info.style.display = "block"
    parent_id.value = comment_id
    username = document.getElementsByClassName(comment_id)[0].textContent;
    message = document.getElementsByClassName(comment_id)[1].textContent;
    reply_name.innerHTML = username
    reply_message.innerHTML = message
    main_parent_id.value = comment_id
}

function no_reply_comment(){
    parent_id.value = "null"
    reply_info.style.display = "none"
}
 
function reply_to_reply(param, param2){
    reply_comment(param2)
    main_parent_id.value = param.getAttribute("data-id") 
}






