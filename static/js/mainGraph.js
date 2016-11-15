/******************************************************************************/
/*  load the json data asynchronously, and only once per page view            */
/******************************************************************************/
d3.json(graphURL, function(error, flaredata) {
  if (error) throw error;
    
  masterData = flaredata;

  // initializing the graph
  d3.select(self.frameElement).style("height", diameter + "px");
  drawGraph();
})

/******************************************************************************/
/*  Main graph drawing function                                               */
/******************************************************************************/
function drawGraph() {

  var nodes = cluster.nodes(packageHierarchy(masterData)),
      links = packageGoesto(nodes);

  link = link
      .data(bundle(links))
    .enter().append("path")
      .each(function(d) { d.source = d[0], d.target = d[d.length - 1]; })
      .attr("class", "link")
      .attr("d", line)
      .style("stroke-width", String(edgewidth)+"px")
      .on("mouseover", edgeovered)
      .on("mouseout", edgeouted);

  node = node
      .data(nodes.filter(function(n) { return !n.children; }))
    .enter().append("text")
      .attr("class", "node")
      .attr("dy", ".31em")
      .attr("id", "node-text")
      .attr("transform", function(d) { return "rotate(" + (d.x - 90) + ")translate(" + (d.y + parseFloat(fontsize)) + ",0)" + (d.x < 180 ? "" : "rotate(180)"); })
      .style("text-anchor", function(d) { return d.x < 180 ? "start" : "end"; })
      .style("font-size", String(fontsize)+"px")
      .style("fill", fillnode)
      .text(function(d) { return d.key; })
      .on("mouseover", mouseovered)
      .on("mouseout", mouseouted)
      .on("click", mouseclick);

  drawModalGraph();
  if (!isDrawn) {
    drawSliders();
    drawSearch();
  }
}

/******************************************************************************/
/*  Functions for search and mouse hover to make the graph interactive        */
/******************************************************************************/
function mouseovered(d) {
  
  mouseouted(d);
  if (hoverlink) { edgeouted(d); }

  document.getElementById('selfName')
    .innerHTML = String(d.brief).split(",").join("<br>");

  node
      .each(function(n) { n.target = n.source = false; });

  link
      .classed("link-off", true)
      .classed("link--target", function(l) { if (l.target === d) return l.source.source = true; })
      .classed("link--source", function(l) { if (l.source === d) return l.target.target = true; })
    .filter(function(l) { return l.target === d || l.source === d; })
      .each(function() { this.parentNode.appendChild(this); });

  node
    .filter(function(n) { return n.target; })
      .style("font-weight", "700")
      .style("fill", "#d62728");  
  
  node
    .filter(function(n) { return n.source; })
      .style("font-weight", "700")
      .style("fill", "#2ca02c");

  node
    .filter(function(n) { return d.name === n.name})
      .style("font-weight", "700")
      .style("fill", "#000");
}

function mouseouted(d) {

  link
      .classed("link-off", false)
      .classed("link--target", false)
      .classed("link--source", false);

  node
      .style("font-weight", "300")
      .style("fill", fillnode);
}

/******************************************************************************/
/*  Functions for search and mouse hover to make the graph interactive        */
/******************************************************************************/
function edgeovered(d) {
  
  if (!hoverlink) return null;

  edgeouted(d);

  document.getElementById('selfName')
    .innerHTML = "Source:\n"+String(d.source.key)+"<br>Sink:\n"+String(d.target.key);

  node
      .each(function(n) { n.target = n.source = false; });

  link
      .classed("link-on", function(l) { return (l.source === d.source && l.target === d.target); })
      .classed("link-off", function(l) { return !(l.source === d.source && l.target === d.target); });

  node
    .filter(function(n) { return n.name === d.target.name; })
      .style("font-weight", "700")
      .style("fill", "#d62728");  
  
  node
    .filter(function(n) { return n.name === d.source.name; })
      .style("font-weight", "700")
      .style("fill", "#2ca02c");
}

function edgeouted(d) {

  link
      .classed("link-off", false)
      .classed("link-on", false);

  node
      .style("font-weight", "300")
      .style("fill", fillnode);
}

/******************************************************************************/
/*  Redraw the graph (asynchronous processes sometimes get buggy)             */
/******************************************************************************/
function reDraw() {
  d3.selectAll(".link").remove();
  d3.selectAll(".node").remove();  
  d3.selectAll(".modalLink").remove();
  d3.selectAll(".modalNode").remove();
  link = svg.append("g").selectAll(".link");
  node = svg.append("g").selectAll(".node");
  modalLink = modalSvg.append("g").selectAll(".modalLink");
  modalNode = modalSvg.append("g").selectAll(".modalNode");

  drawGraph();
}
