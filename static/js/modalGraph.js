// Get the modal
var modal = document.getElementById('myModal');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

function stringTable(edges) {
  var str = "";
  for (var i = 0; i < edges.length; i++) {
    str += "<tr onclick=\"switchModal('"+String(edges[i].key)+"')\">";
    str += "<td>";
    str += String(edges[i].key);
    str += "</td>";
    str += "<td>";
    str += String(parseFloat(edges[i].weight).toFixed(2));
    str += "</td>";
    str += "</tr>";
  }
  return str;
}

function stringAssocTable(assocs) {
  var str = "";
  for (var i = 0; i < assocs.length; i++) {
    str += "<tr>";
    str += "<td>";
    str += String(assocs[i][0]);
    str += "</td>";
    str += "<td>";
    str += String(assocs[i][1]);
    str += "</td>";
    str += "</tr>";
  }
  return str;
}

function stringAssocHead(head) {
  var str = "<tr>";
    str += "<th>";
    str += String(head[0]);
    str += "</th>";
    str += "<th>";
    str += String(head[1])
    str += "</th>";
    str += "</tr>";
  return str;
}

// functions for search and mouse hover to make the graph interactive
function mouseclick(d) {
  document.getElementById('incoming').innerHTML = stringTable(inEdges[d.name]);
  document.getElementById('outgoing').innerHTML = stringTable(outEdges[d.name]);
  document.getElementById('assocHead').innerHTML = stringAssocHead(d.assocHead);
  document.getElementById('associated').innerHTML = stringAssocTable(d.associated);

  modal.style.display = "block";
  document.getElementById('modalTitle').innerHTML = "Node Information for: "+String(d.key);
  document.getElementById('descTitle').innerHTML = "Node Description for: "+String(d.key);
  document.getElementById('node-desc').innerHTML = String(d.desc);
  modalHighlight(d);  
}

function switchModal(key) {
  node
      .filter(function(d) { return d.key === key; })
      .each(function(d) { mouseclick(d); });
}

// modal graph drawing function (draws lines connected to given node)
function drawModalGraph() {

  var modalNodes = modalCluster.nodes(packageHierarchy(masterData)),
      modalLinks = packageGoesto(modalNodes);

  modalLink = modalLink
      .data(bundle(modalLinks))
    .enter().append("path")
      .each(function(d) { d.source = d[0], d.target = d[d.length - 1]; })
      .attr("class", "modalLink")
      .attr("d", line);

  modalNode = modalNode
      .data(modalNodes.filter(function(n) { return !n.children; }))
    .enter().append("text")
      .attr("class", "modalNode")
      .attr("dy", ".31em")
      .attr("id", function(d){ return 'name' + d.name; })
      .attr("transform", function(d) { return "rotate(" + (d.x - 90) + ")translate(" + (d.y + 10) + ",0)" + (d.x < 180 ? "" : "rotate(180)"); })
      .style("text-anchor", function(d) { return d.x < 180 ? "start" : "end"; })
      .style("fill", "transparent")
      .text(function(d) { return d.key; });
}

// functions for search and mouse hover to make the graph interactive
function modalHighlight(d) {
  
  modalOff();

  modalNode
      .each(function(n) { n.target = n.source = false; });

  modalLink
      .classed("link--target", function(l) { if (l.target === d) return l.source.source = true; })
      .classed("link--source", function(l) { if (l.source === d) return l.target.target = true; })
    .filter(function(l) { return l.target === d || l.source === d; })
      .each(function() { this.parentNode.appendChild(this); });

  modalNode
    .filter(function(n) { return n.target; })
      .style("font-weight", "700")
      .style("fill", "#d62728");  
  
  modalNode
    .filter(function(n) { return n.source; })
      .style("font-weight", "700")
      .style("fill", "#2ca02c");

  modalNode
    .filter(function(n) { return d.name === n.name})
      .style("font-weight", "700")
      .style("fill", "#000");
}

function modalOff() {

  modalLink
      .classed("link--target", false)
      .classed("link--source", false);

  modalNode
      .style("font-weight", "300")
      .style("fill", "transparent");
}

// // Construct the package hierarchy from class names
// // Structure must be: grandparent.parent.child.grandchild.etc...
// function packageHierarchy(classes) {
//   var map = {};

//   function find(name, data) {
//     var node = map[name], i;
//     if (!node) {
//       node = map[name] = data || {name: name, children: []};
//       if (name.length) {
//         node.parent = find(name.substring(0, i = name.lastIndexOf(".")));
//         node.parent.children.push(node);
//         node.key = name.substring(i + 1);
//       }
//     }
//     return node;
//   }

//   classes.forEach(function(d) {
//     find(d.name, d);
//   });

//   return map[""];
// }

// // Return a list of outgoing edges for the given array of nodes.
// function packageGoesto(nodes) {
//   var map = {},
//       goesto = [];

//   // Compute a map from name to node.
//   nodes.forEach(function(d) {
//     map[d.name] = d;
//   });

//   // Sort the input nodes to each node
//   if (MAXIN < 0) {
//     nodes.forEach(function(d) {
//       pqs[d.name] = new FastPriorityQueue(function(a,b) {return a.weight > b.weight});
//     });

//     nodes.forEach(function(d) {
//       if (d.goesto) d.goesto.forEach(function(i) {
//         if(i[0] in pqs) {
//           pqs[i[0]].add({ source: d.name, weight: i[1] });
//         }
//       });
//     });

//     nodes.forEach(function(d) {
//       inWeights[d.name] = {}
//       var pos = 0;
//       while (! pqs[d.name].isEmpty()) {
//         pos++;
//         name = pqs[d.name].poll()['source'];
//         inWeights[d.name][name] = pos;
//       }
//       if (pos > MAXIN) MAXIN = pos;
//     });
//   }

//    // Sort the output nodes to each node
//   if (MAXOUT < 0) {
//     pqs = {}
//     nodes.forEach(function(d) {
//       if (!pqs[d.name]) {
//         pqs[d.name] = new FastPriorityQueue(function(a,b) {return a.weight > b.weight});
//       }

//       if (d.goesto) d.goesto.forEach(function(i) {
//         pqs[d.name].add({ sink: i[0], weight: i[1] });
//       });
//     });

//     nodes.forEach(function(d) {
//       outWeights[d.name] = {}
//       var pos = 0;
//       while (! pqs[d.name].isEmpty()) {
//         pos++;
//         name = pqs[d.name].poll()['sink'];
//         outWeights[d.name][name] = pos;
//       }
//       if (pos > MAXOUT) MAXOUT = pos;
//     });
//   }

//   // For each node, construct a link from the source to target node.
//   nodes.forEach(function(d) {
//     if (d.goesto) d.goesto.forEach(function(i) {
//       if(i[0] in map) {
        
//         if (i[1] < weightMin) return null;
//         if (i[1] > weightMax) return null;
//         if (inWeights[i[0]][d.name] > maxIn) return null;
//         if (outWeights[d.name][i[0]] > maxOut) return null;

//         goesto.push({ source: map[d.name], target: map[i[0]] });

//         if (i[1] > MAXWEIGHT) MAXWEIGHT = i[1]; 
//       }
//     });
//   });

//   return goesto;
// }

// // redraw the graph
// function reDraw() {
//   d3.selectAll(".link").remove();
//   d3.selectAll(".node").remove();
//   link = svg.append("g").selectAll(".link");
//   link = svg.append("g").selectAll(".node");

//   drawGraph();
// }
