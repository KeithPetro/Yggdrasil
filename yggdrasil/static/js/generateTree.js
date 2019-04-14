const dTree = window.dTree;

var treeData = [{
    "name": "Father",
    "class": "man",
    "textClass": "emphasis",
    "marriages": [{
        "spouse": {
            "name": "Mother",
            "class": "woman",
        },
        "children": [{
            "name": "Son 1",
            "class": "man",
        }, {
            "name": "Son 2",
            "class": "man",
        }, {
            "name": "Daughter 1",
            "class": "woman",
        }]
    }]
}]



dTree.init(treeData, {
    target: "#tree",
    debug: true,
    height: window.height,
    width: window.width,
    callbacks: {
        nodeClick: function(name, extra) {
            console.log(name);
        },
        textRenderer: function(name, extra, textClass) {
            // THis callback is optinal but can be used to customize
            // how the text is rendered without having to rewrite the entire node
            // from screatch.
            if (extra && extra.nickname)
                name = name + " (" + extra.nickname + ")";
            return "<p align='center' class='" + textClass + "'>" + name + "</p>";
        },
        nodeRenderer: function(name, x, y, height, width, extra, id, nodeClass, textClass, textRenderer) {
            // This callback is optional but can be used to customize the
            // node element using HTML.
            let node = '';
            node += '<div ';
            node += 'style="height:100%;width:100%;" ';
            node += 'class="' + nodeClass + '" ';
            node += 'id="node' + id + '">\n';
            node += textRenderer(name, extra, textClass);
            node += '</div>';
            return node;
        }
    }
});
