let browserInnerHeight = window.innerHeight;

function getElementNode(selector = {}) {
	if (selector.css) {
		let elNOde = document.querySelector(selector.css)
	}
	if (selector.xpath) {
		elNOde = document.evaluate(selector.xpath, null, document, )
	}
}