/******************************************************************************/
/*  Draw the sliders based on observed boundary values in the data            */
/*                                                                            */
/*  The sliders use a naturally logarithmic scale (but not aggressively so)   */
/******************************************************************************/
function drawSliders() {

  noUiSlider.create(nodeSlider, {
    start: [ 8 ],
    connect: 'lower',
    tooltips: [ true ],
    range: {
      'min': [  0 ],
      'max': [ 16 ]
    }
  });

  noUiSlider.create(edgeSlider, {
    start: [ 1 ],
    connect: 'lower',
    tooltips: [ true ],
    range: {
      'min': [  0 ],
      'max': [ 4 ]
    }
  });

  noUiSlider.create(tensionSlider, {
    start: [ 0.7 ],
    connect: 'lower',
    tooltips: [ true ],
    range: {
      'min': [ 0 ],
      'max': [ 1 ]
    }
  });

  noUiSlider.create(weightSlider, {  
    start: [ 0, MAXWEIGHT ],
    connect: true,
    tooltips: [ true, true ],
    range: {
      'min': [  0 ],
      '20%': [ MAXWEIGHT*0.0016 ],
      '40%': [ MAXWEIGHT*0.008 ],
      '60%': [ MAXWEIGHT*0.04 ],
      '80%': [ MAXWEIGHT*0.2 ],
      'max': [ MAXWEIGHT ]
    }
  });

  noUiSlider.create(inSlider, {
    start: [ MAXIN ],
    connect: 'lower',
    tooltips: [ toInt ],
    step: 1,
    range: {
      'min': [  0 ],
      '20%': [ MAXIN*0.0016 ],
      '40%': [ MAXIN*0.008 ],
      '60%': [ MAXIN*0.04 ],
      '80%': [ MAXIN*0.2 ],
      'max': [ MAXIN ]
    }
  });

  noUiSlider.create(outSlider, {
    start: [ MAXOUT ],
    connect: 'lower',
    tooltips: [ toInt ],
    step: 1,
    range: {
      'min': [  0 ],
      '20%': [ MAXOUT*0.0016 ],
      '40%': [ MAXOUT*0.008 ],
      '60%': [ MAXOUT*0.04 ],
      '80%': [ MAXOUT*0.2 ],
      'max': [ MAXOUT ]
    }
  });

  isDrawn = true;
  updateSliders();
}

/******************************************************************************/
/*  Slider update functions                                                   */
/******************************************************************************/
function updateNode(values, handle) {

  nodeIn.value = values[handle];
  fontsize = values[handle];

  reDraw();
}

function updateEdge(values, handle) {

  edgeIn.value = values[handle];
  edgewidth = values[handle];

  reDraw();
}

function updateTension(values, handle) {

  tensionIn.value = values[handle];
  line = line
    .tension(values[handle]);
  link = link
      .each(function(d) { d.source = d[0], d.target = d[d.length - 1]; })
      .attr("d", line);

  modalLink = modalLink
      .each(function(d) { d.source = d[0], d.target = d[d.length - 1]; })
      .attr("d", line);

  reDraw();
}

function updateWeight(values, handle) {

  weightMin = values[0];
  weightMax = values[1];
  weightMinInput.value = weightMin;
  weightMaxInput.value = weightMax;

  d3.selectAll(".link").remove();
  d3.selectAll(".modalLink").remove();
  link = svg.append("g").selectAll(".link");
  modalLink = modalSvg.append("g").selectAll(".modalLink");

  drawGraph();
}

function updateIn(values, handle) {

  maxIn = values[handle];
  inIn.value = Math.round(values[handle]);
  document.getElementById('inText').innerHTML = inIn.value;

  d3.selectAll(".link").remove();
  d3.selectAll(".modalLink").remove();
  link = svg.append("g").selectAll(".link");
  modalLink = modalSvg.append("g").selectAll(".modalLink");

  drawGraph();
}

function updateOut(values, handle) {

  maxOut = values[handle];
  outIn.value = Math.round(values[handle]);
  document.getElementById('outText').innerHTML = outIn.value;

  d3.selectAll(".link").remove();
  d3.selectAll(".modalLink").remove();
  link = svg.append("g").selectAll(".link");
  modalLink = modalSvg.append("g").selectAll(".modalLink");

  drawGraph();
}

/******************************************************************************/
/*  Update the graph on slider input changes                                  */
/******************************************************************************/
function updateSliders() {

  fillToggle.addEventListener('change', function(){

    fillnode = (fillnode === "transparent") ? "#bbb" : "transparent";
    d3.selectAll("#node-text").style("fill", fillnode);
    console.log(fillnode);
  });

  edgeToggle.addEventListener('change', function(){

    hoverlink = !hoverlink;
  });

  nodeSlider.noUiSlider.on('update', updateNode);

  nodeIn.addEventListener('change', function(){
    nodeSlider.noUiSlider.set(this.value);
  });

  edgeSlider.noUiSlider.on('update', updateEdge);

  edgeIn.addEventListener('change', function(){
    edgeSlider.noUiSlider.set(this.value);
  });

  tensionSlider.noUiSlider.on('update', updateTension);

  tensionIn.addEventListener('change', function(){
    tensionSlider.noUiSlider.set(this.value);
  });

  weightSlider.noUiSlider.on('update', updateWeight);

  weightMinInput.addEventListener('change', function(){
    weightSlider.noUiSlider.set([this.value, weightMax]);
  });

  weightMaxInput.addEventListener('change', function(){
    weightSlider.noUiSlider.set([weightMin, this.value]);
  });

  inSlider.noUiSlider.on('update', updateIn);

  inIn.addEventListener('change', function(){
    inSlider.noUiSlider.set(this.value);
  });

  outSlider.noUiSlider.on('update', updateOut);

  outIn.addEventListener('change', function(){
    outSlider.noUiSlider.set(this.value);
  });
}
