import { jsHelper } from "../JSHelper/helper.js"

const helper = new jsHelper()

let node = helper.getElementNode({css: 'nav'})
let cl = node.getAttribute('class')

function styleNavOnMouseover() {
    helper.getElementNode({css: '#nav-event'})? helper.getElementNode({css: '#nav-event'}).setAttribute('class', cl + ' bg-primary') : null
}

function styleNavOnMouseout() {
    helper.getElementNode({css: '#nav-event'})? helper.getElementNode({css: '#nav-event'}).setAttribute('class', cl) : null
}

helper.addEvent({css: '#nav-event'}, 'mouseover', styleNavOnMouseover)
helper.addEvent({css: '#nav-event'}, 'mouseout', styleNavOnMouseout)

