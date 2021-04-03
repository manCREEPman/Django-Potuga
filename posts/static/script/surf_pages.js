function titleClickHandler(event){
    const receiverID = event.currentTarget.id
    if(receiverID == "genres"){
        window.location.href = "/posts/genres/"
        return
    }
    if(receiverID == "artists"){
        window.location.href = "/posts/artists/"
        return
    }
    if(receiverID == "albums"){
        window.location.href = "/posts/albums/"
        return
    }
    if(receiverID == "compositions"){
        window.location.href = "/posts/compositions/"
        return
    }
}

function newItemAddingHandler(event){
    let receiverID = event.currentTarget.id
    if(receiverID == "add-genre-button"){
        window.location.href = "/posts/genres/update?table=genre"
        return
    }
    if(receiverID == "add-artist-button"){
        window.location.href = "/posts/artists/update?table=artist"
        return
    }
    if(receiverID == "add-album-button"){
        window.location.href = "/posts/albums/update?table=album"
        return
    }
    if(receiverID == "add-composition-button"){
        window.location.href = "/posts/compositions/update?table=composition"
        return
    }
}

const titles = ["genres", "artists", "albums", "compositions"]
for(let i = 0; i < 4; i++){
    document.getElementById(titles[i]).addEventListener("click", titleClickHandler)
}

const list = document.getElementsByTagName('input')
const addButton = list[list.length - 1]
console.log(addButton.id)
if(addButton != null) addButton.addEventListener('click', newItemAddingHandler)