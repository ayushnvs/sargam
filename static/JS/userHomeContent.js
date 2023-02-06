const jsmediatags = window.jsmediatags

const uploadSong = document.querySelector('input#upload')
const coverImg = document.querySelector('div#cover')
const songTitle = document.querySelector('div.song-info .title')
const songAlbum = document.querySelector('div.song-info .album')
const songArtist = document.querySelector('div.song-info .artist')

uploadSong.addEventListener('change', (event) => {
    const song = event.target.files[0]

    jsmediatags.read(song, {
        onSuccess: function (tag) {
            console.log(tag)

            // Array buffer to base64
            const data = tag.tags.picture.data
            const format = tag.tags.picture.format
            let base64String = ""
            for (let i = 0; i < data.length; i++) {
                base64String += String.fromCharCode(data[i])
            }

            console.log(base64String === "")
            coverImg.style.backgroundImage = base64String !== "" ? `url(data:${format};base64,${window.btoa(base64String)})` : `url("/static/IMG/dflt-msc-icon.png")`
            songTitle.textContent = tag.tags.title
            songAlbum.textContent = tag.tags.album
            songArtist.textContent = tag.tags.artist
        },
        onError: function (error) {
            console.log(error)
        }
    }) 
})