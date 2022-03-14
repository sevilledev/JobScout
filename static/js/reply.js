parent_id = document.querySelector(".hidden-input")
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
}

function no_reply_comment(){
    parent_id.value = "null"
    reply_info.style.display = "none"
}

$(".reply_btn").on("click",function(){
    console.log($(this).data("id"))
})
// kec




