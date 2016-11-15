/******************************************************************************/
/*  Comparators for sorting nodes                                             */
/******************************************************************************/

function comparator(a, b) {
    return d3.ascending(a.name, b.name);
}

function compareWeight(a, b) { return a.weight > b.weight; }

function compareWeightDes(a, b) { return b.weight - a.weight; }

/******************************************************************************/
/*  Function for centering the main svg graph when it's drawn                 */
/******************************************************************************/

function svgTranslate () {
    var x = window.getComputedStyle(document.getElementById('bundleWrapper')).getPropertyValue('width');
    x = parseInt(x.substring(0,x.length-2)) / 2;

    var y = window.getComputedStyle(document.getElementById('bundleWrapper')).getPropertyValue('height');
    y = parseInt(y.substring(0,y.length-2)) / 2;

    return [x,y];
}

/******************************************************************************/
/*  Graph data variables                                                      */
/******************************************************************************/

// have sliders and search bar been initialized?
var isDrawn = false;

// for calculating the top weighted input and output nodes
var pqs = {},
    inTop = {},
    outTop = {},
    inEdges = {},
    outEdges = {};

// json object of all node/edge/name/parent/description data
var masterData;

/******************************************************************************/
/*  Main graph layout                                                         */
/******************************************************************************/

// svg graph variables
var diameter = 800,
    radius = diameter / 2,
    innerRadius = radius - 100;

var cluster = d3.layout.cluster()
    .size([360, innerRadius])
    .sort(comparator)
    .value(function(d) { return d.size; });

var bundle = d3.layout.bundle();

/******************************************************************************/
/*  Modal graph layout                                                        */
/******************************************************************************/

// svg graph variables
var modalDiameter = 500,
    modalRadius = modalDiameter / 2,
    modalInnerRadius = modalRadius - 100;

var modalCluster = d3.layout.cluster()
    .size([360, modalInnerRadius])
    .sort(comparator)
    .value(function(d) { return d.size; });

/******************************************************************************/
/*  Drawing the main graph                                                    */
/******************************************************************************/

var line = d3.svg.line.radial()
    .interpolate("bundle")
    .tension(0.7)
    .radius(function(d) { return d.y; })
    .angle(function(d) { return d.x / 180 * Math.PI; });

var myZoom = d3.behavior.zoom()
              .scaleExtent([.01, 100])
              .on("zoom", zoom);

function zoom() {
    svg.attr("transform",
    "translate(" + d3.event.translate + ")"
    + " scale(" + d3.event.scale + ")");
}

var svg = d3.select("#mainStage").append("svg")
    .attr("width", "100%")
    .attr("height", "100%")
    .attr("id", "bundleWrapper")
    .on("dblclick.zoom", null)
    .call(myZoom)
  .append("g")
    .attr("id", "bundleGraph");

myZoom.translate(svgTranslate());

svg = svg.attr("transform", "translate(" + svgTranslate() + ")");

var link = svg.append("g").selectAll(".link"),
    node = svg.append("g").selectAll(".node");

/******************************************************************************/
/*  Draw the modal graph                                                      */
/******************************************************************************/

var modalSvg = d3.select("#modalStage").append("svg")
    .attr("width", modalDiameter)
    .attr("height", modalDiameter)
    .attr("id", "bundleWrapper")
  .append("g")
    .attr("id", "bundleGraph")
    .attr("transform", "translate(" + modalRadius + "," + modalRadius + ")");

var modalLink = modalSvg.append("g").selectAll(".link"),
    modalNode = modalSvg.append("g").selectAll(".node");

/******************************************************************************/
/*  Drawing the main legend                                                   */
/******************************************************************************/
var legend = svg.append("g")
      .attr("class", "legend")
      .attr("x", radius-100)
      .attr("y", -radius)
      .attr("height", 100)
      .attr("width", 100);

legend.append("rect")
      .attr("x", radius-200)
      .attr("y", 10-radius)
      .attr("width", 10)
      .attr("height", 10)
      .style("fill", "#2ca02c");

legend.append("rect")
      .attr("x", radius-200)
      .attr("y", 30-radius)
      .attr("width", 10)
      .attr("height", 10)
      .style("fill", "#d62728");

legend.append("text")
      .attr("x", radius-180)
      .attr("y", 20-radius)
      .style("fill", "#2ca02c")
      .text("Incoming");

legend.append("text")
      .attr("x", radius-180)
      .attr("y", 40-radius)
      .style("fill", "#d62728")
      .text("Outgoing");

/******************************************************************************/
/*  Drawing the modal Legend                                                  */
/******************************************************************************/
var modalLegend = modalSvg.append("g")
      .attr("class", "legend")
      .attr("x", modalRadius-90)
      .attr("y", -modalRadius)
      .attr("height", 100)
      .attr("width", 100);

modalLegend.append("rect")
      .attr("x", modalRadius-90)
      .attr("y", 10-modalRadius)
      .attr("width", 10)
      .attr("height", 10)
      .style("fill", "#2ca02c");

modalLegend.append("rect")
      .attr("x", modalRadius-90)
      .attr("y", 30-modalRadius)
      .attr("width", 10)
      .attr("height", 10)
      .style("fill", "#d62728");

modalLegend.append("text")
      .attr("x", modalRadius-70)
      .attr("y", 20-modalRadius)
      .style("fill", "#2ca02c")
      .text("Incoming");

modalLegend.append("text")
      .attr("x", modalRadius-70)
      .attr("y", 40-modalRadius)
      .style("fill", "#d62728")
      .text("Outgoing");

/******************************************************************************/
/*  Options variables                                                         */
/******************************************************************************/

var fillToggle = document.getElementById('fillIn'),
    fillnode = "transparent";

var edgeToggle = document.getElementById('toggleIn'),
    hoverlink = false;

var nodeSlider = document.getElementById("nodeSlide"),
    nodeInput = document.getElementById('nodeIn'),
    fontsize = 8;

var edgeSlider = document.getElementById("edgeSlide"),
    edgeInput = document.getElementById('edgeIn'),
    edgewidth = 1;

var tensionSlider = document.getElementById("tension"),
    tensionInput = document.getElementById('tensionIn');

var weightSlider = document.getElementById("weight"),
    weightMinInput = document.getElementById('weightMinIn'),
    weightMaxInput = document.getElementById('weightMaxIn'),
    weightMin  = 0,
    weightMax = Number.POSITIVE_INFINITY,
    MAXWEIGHT = -1;

var inSlider = document.getElementById("topIn"),
    inInput = document.getElementById('inIn'),
    maxIn = Number.POSITIVE_INFINITY,
    MAXIN = -1;

var outSlider = document.getElementById("topOut"),
    outInput = document.getElementById('outIn'),
    maxOut = Number.POSITIVE_INFINITY,
    MAXOUT = -1;

// for integer values in the sliders
var toInt = wNumb({ decimals: 0 });
