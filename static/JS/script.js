let browserInnerHeight = window.innerHeight;

function getElementNode(selector) {
	if (selector.css) {
		let elNode = document.querySelector(selector.css)
        elNode = elNode ? elNode : null
	}
	if (selector.xpath) {
		elNode = document.evaluate(selector.xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null)
        elNode = elNode.singleNodeValue ? elNode.singleNodeValue : null
	}
    return elNode
}

function scrolltoView(selector)  {
    let node = getElementNode(selector)
    if (node) {
        node.scrollIntoView()
    }
    else { console.log("Element with given selector is not present!") }
}

function addInnerText(selector, text) {
    let node = getElementNode(selector)
    if (node) {
        node.textContent = text
    }
    else { console.log("Element with given selector is not present!") }
}

function getwindowHW() {
    let height = window.innerHeight
    let width = window.innerWidth
    return {"height": height, "width": width}
}