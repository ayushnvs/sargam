const music = document.querySelector('#audio')

const musicBanner = document.querySelector('div.msc-banner img')
const musicName = document.querySelector('div.msc-name p')
const seekBar = document.querySelector('input.seek-bar')
const currentTime = document.querySelector('span.current-time')
const songDuration = document.querySelector('span.song-duration')
const forwardBtn = document.querySelector('button.fb-btn.forward')
const backwardBtn = document.querySelector('button.fb-btn.backward')
const playBtn = document.querySelector('button.play-button')
const listedSongs = document.querySelectorAll('div.card.song-lis li')

listedSongs.forEach((listedSong) => {
    listedSong.addEventListener('click', () => {
        let songPath = listedSong.querySelector('div.song-path').innerText
        music.src = songPath
        musicName.innerText = listedSong.querySelector('a').innerText
        currentTime.innerText = '00:00'
        setTimeout(() => {
            seekBar.max = music.duration
            songDuration.innerText = formatTime(music.duration)
        }, 300)
    })
})

playBtn.addEventListener('click', () => {
    playBtn.classList.toggle('pause')
})

const formatTime = (duration) => {
    let min = Math.floor(duration/60)
    let sec = duration - min * 60
    if (min < 10) {
        min = `0${min}`
    }
    if (sec < 10) {
        sec = `0${sec}`
    }
    return `${min}:${sec}`
}



