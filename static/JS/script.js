import { jsHelper } from "../JSHelper/helper.js"

const helper = new jsHelper()

// Navbar
let homePageXpath = "//img[contains(@alt,'home')]"
let isHomePage = helper.getElementNode({xpath: homePageXpath})

let node = helper.getElementNode({css: 'nav'})
let cl = node.getAttribute('class')

function styleNavOnMouseover() {
    helper.getElementNode({css: '#nav-event'})? helper.getElementNode({css: '#nav-event'}).setAttribute('class', cl + ' bg-primary') : null
}

function styleNavOnMouseout() {
    helper.getElementNode({css: '#nav-event'})? helper.getElementNode({css: '#nav-event'}).setAttribute('class', cl) : null
}

if (isHomePage) {
    helper.addEvent({css: '#nav-event'}, 'mouseover', styleNavOnMouseover)
    helper.addEvent({css: '#nav-event'}, 'mouseout', styleNavOnMouseout)
    let navMarginNode = helper.getElementNode({css: 'div#nav-margin'})
    if (navMarginNode) { navMarginNode.style.display = 'none'}
} else {
    styleNavOnMouseover()
}


