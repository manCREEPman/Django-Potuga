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

const titles = ["genres", "artists", "albums", "compositions"]
for(let i = 0; i < 4; i++){
    document.getElementById(titles[i]).addEventListener("click", titleClickHandler)
}