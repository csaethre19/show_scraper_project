var artistList = []

function addArtist() {
    artist = document.getElementById("artistList").value;
    document.getElementById("artistList").value = ''

    if (artist != '') {
        artistList.push(artist)
        var ul = document.getElementById("artistOutput")
        let i = 0;
        if (artistList != []) {
            i = artistList.length - 1;
        }
        for (; i < artistList.length; i++) {
            var li = document.createElement("li")
            li.appendChild(document.createTextNode(artistList[i]))
            ul.appendChild(li)
        }
    }
}

function getArtists() {
    return artistList
}

