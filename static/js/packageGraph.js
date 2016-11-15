/******************************************************************************/
/*  Construct the package hierarchy from class names                          */
/*  Structure must be: grandparent.parent.child.grandchild.etc...             */
/******************************************************************************/
function packageHierarchy(classes) {
  var map = {};

  function find(name, data) {
    var node = map[name], i;
    if (!node) {
      node = map[name] = data || {name: name, children: []};
      if (name.length) {
        node.parent = find(name.substring(0, i = name.lastIndexOf(".")));
        node.parent.children.push(node);
        node.key = name.substring(i + 1);
      }
    }
    return node;
  }

  classes.forEach(function(d) {
    find(d.name, d);
  });

  return map[""];
}

/******************************************************************************/
/*  Return a list of outgoing edges for the given array of nodes              */
/******************************************************************************/
function packageGoesto(nodes) {
  var map = {},
      goesto = [];

  // Compute a map from name to node.
  nodes.forEach(function(d) {
    map[d.name] = d;
  });

  // Sort the input nodes to each node
  if (MAXIN < 0) {
    nodes.forEach(function(d) {
      pqs[d.name] = new FastPriorityQueue(compareWeight);
      inEdges[d.name] = [];
    });

    nodes.forEach(function(d) {
      if (d.goesto) d.goesto.forEach(function(i) {
        if(i[0] in pqs) {
          pqs[i[0]].add({ source: d.name, weight: i[1] });
          inEdges[i[0]].push({ key: d.name.substring(d.name.lastIndexOf(".")+1), weight: i[1] })
        }
      });
    });

    nodes.forEach(function(d) {
      inEdges[d.name] = inEdges[d.name].sort(compareWeightDes)
      inTop[d.name] = {}
      var pos = 0;
      while (! pqs[d.name].isEmpty()) {
        pos++;
        name = pqs[d.name].poll()['source'];
        inTop[d.name][name] = pos;
      }
      if (pos > MAXIN) MAXIN = pos;
    });
  }

   // Sort the output nodes to each node
  if (MAXOUT < 0) {
    pqs = {}
    nodes.forEach(function(d) {
      if (!pqs[d.name]) {
        pqs[d.name] = new FastPriorityQueue(compareWeight);
        outEdges[d.name] = []
      }

      if (d.goesto) d.goesto.forEach(function(i) {
        pqs[d.name].add({ sink: i[0], weight: i[1] });
        outEdges[d.name].push({ key: i[0].substring(i[0].lastIndexOf(".")+1), weight: i[1] })
      });
    });

    nodes.forEach(function(d) {
      outEdges[d.name] = outEdges[d.name].sort(compareWeightDes)

      outTop[d.name] = {}
      var pos = 0;
      while (! pqs[d.name].isEmpty()) {
        pos++;
        name = pqs[d.name].poll()['sink'];
        outTop[d.name][name] = pos;
      }
      if (pos > MAXOUT) MAXOUT = pos;
    });
  }

  // For each node, construct a link from the source to target node.
  nodes.forEach(function(d) {
    if (d.goesto) d.goesto.forEach(function(i) {
      if(i[0] in map) {
        
        if (i[1] < weightMin) return null; 
        if (i[1] > weightMax) return null;
        if (inTop[i[0]][d.name] > maxIn) return null;
        if (outTop[d.name][i[0]] > maxOut) return null;

        goesto.push({ source: map[d.name], target: map[i[0]] });

        if (i[1] > MAXWEIGHT) MAXWEIGHT = i[1]; 
      }
    });
  });

  return goesto;
}
