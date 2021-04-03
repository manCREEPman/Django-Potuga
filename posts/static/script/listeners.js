function newItemEditingHandler(event){
    let receiverID = event.currentTarget.id
    if(receiverID == "edit-genre-button"){
        window.location.href = "/posts/genres/change?table=genre"
        return
    }
    if(receiverID == "edit-artist-button"){
        window.location.href = "/posts/artists/change?table=artist"
        return
    }
    if(receiverID == "edit-album-button"){
        window.location.href = "/posts/albums/change?table=album"
        return
    }
    if(receiverID == "edit-composition-button"){
        window.location.href = "/posts/compositions/change?table=composition"
        return
    }
}

const list = document.getElementsByTagName('input')
const editBtn = list[list.length - 1]
if(editBtn != null) editBtn.addEventListener('click', newItemEditingHandler)