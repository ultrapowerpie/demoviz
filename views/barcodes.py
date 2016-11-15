from flask import Blueprint
from views.admin import *


barcodes = Blueprint('barcodes', __name__)


def barcode_template():
    side      = "Barcode Information"
    side_desc = "Hover over or search for a barcode or its work locus " \
                " to see its information" 
    return side, side_desc


################################################################################
#                                                                              #
#   Activity Hierarchy                                                         #
#                                                                              #
################################################################################


@barcodes.route("/barcodes/activity/fprox/nodes")
def activity_fprox_nodes():
    graphURL = "/static/data/barcodes_activity_fprox_nodes.json"
    main     = "Barcode Functional Proximity, Activity Hierarchy - " \
               "Node Similarity (Top 3 inputs & outputs)"
    side, side_desc = barcode_template() 
    return quick_render(graphURL, main, side, side_desc)


@barcodes.route("/barcodes/activity/fprox/edges")
def activity_fprox_edges():
    graphURL = "/static/data/barcodes_activity_fprox_edges.json"
    main     = "Barcode Functional Proximity, Activity Hierarchy - " \
               "Edge Similarity (Top 3 inputs & outputs)"
    side, side_desc = barcode_template()
    return quick_render(graphURL, main, side, side_desc)


@barcodes.route("/barcodes/activity/fprox/simrank")
def activity_fprox_simrank():
    graphURL = "/static/data/barcodes_activity_fprox_simrank.json"
    main     = "Barcode Functional Proximity, Activity Hierarchy - " \
               "Simrank Score (Top 10 inputs & outputs)"
    side, side_desc = barcode_template() 
    return quick_render(graphURL, main, side, side_desc)


@barcodes.route("/barcodes/activity/fprox/neighbor")
def activity_fprox_neighbor():
    graphURL = "/static/data/barcodes_activity_fprox_neighbor.json"
    main     = "Barcode Functional Proximity, Activity Hierarchy - " \
               "Neighbor Similarity (Top 3 inputs & outputs)"
    side, side_desc = barcode_template() 
    return quick_render(graphURL, main, side, side_desc)


@barcodes.route("/barcodes/activity/fprox/vector")
def activity_fprox_vector():
    graphURL = "/static/data/barcodes_activity_fprox_vector.json"
    main     = "Barcode Functional Proximity, Activity Hierarchy - " \
               "Vector Similarity (Top 3 inputs & outputs, edge weight > 0.01)"
    side, side_desc = barcode_template() 
    return quick_render(graphURL, main, side, side_desc)


@barcodes.route("/barcodes/activity/fprox/mean")
def activity_fprox_mean():
    graphURL = "/static/data/barcodes_activity_fprox_mean.json"
    main     = "Barcode Functional Proximity, Activity Hierarchy - " \
               "Mean Similarity (Top 5 inputs & outputs)"
    side, side_desc = barcode_template() 
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#   Supply                                                                     #
################################################################################


@barcodes.route("/barcodes/activity/supply/downstream")
def activity_supply_downstream():
    graphURL = "/static/data/barcodes_activity_supply_downstream.json"
    main     = "Supply Chain Barcode Connections, Activity Hierarchy - " \
               "Downstreamness Distance (Top 50 inputs & outputs)"
    side, side_desc = barcode_template() 
    return quick_render(graphURL, main, side, side_desc)


@barcodes.route("/barcodes/activity/supply/markov")
def activity_supply_markov():
    graphURL = "/static/data/barcodes_activity_supply_markov.json"
    main     = "Supply Chain Barcode Connections, Activity Hierarchy - " \
               "Markov Distance (Top 5 inputs & outputs)"
    side, side_desc = barcode_template() 
    return quick_render(graphURL, main, side, side_desc)


@barcodes.route("/barcodes/activity/supply/maxflow")
def activity_supply_maxflow():
    graphURL = "/static/data/barcodes_activity_supply_maxflow.json"
    main     = "Supply Chain Barcode Connections, Activity Hierarchy - " \
               "Max Flow (Top 1 input & output, edge weight > 0.1)"
    side, side_desc = barcode_template() 
    return quick_render(graphURL, main, side, side_desc)


@barcodes.route("/barcodes/activity/supply/mean")
def activity_supply_mean():
    graphURL = "/static/data/barcodes_activity_supply_mean.json"
    main     = "Supply Chain Barcode Connections, Activity Hierarchy - " \
               "Mean Distance (Top 20 inputs & outputs)"
    side, side_desc = barcode_template() 
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#                                                                              #
#   Resource Hierarchy                                                         #
#                                                                              #
################################################################################


@barcodes.route("/barcodes/resource/fprox/nodes")
def resource_fprox_nodes():
    graphURL = "/static/data/barcodes_resource_fprox_nodes.json"
    main     = "Barcode Functional Proximity, Resource Hierarchy - " \
               "Node Similarity (Top 3 inputs & outputs)"
    side, side_desc = barcode_template() 
    return quick_render(graphURL, main, side, side_desc)


@barcodes.route("/barcodes/resource/fprox/edges")
def resource_fprox_edges():
    graphURL = "/static/data/barcodes_resource_fprox_edges.json"
    main     = "Barcode Functional Proximity, Resource Hierarchy - " \
               "Edge Similarity (Top 3 inputs & outputs)"
    side, side_desc = barcode_template()
    return quick_render(graphURL, main, side, side_desc)


@barcodes.route("/barcodes/resource/fprox/simrank")
def resource_fprox_simrank():
    graphURL = "/static/data/barcodes_resource_fprox_simrank.json"
    main     = "Barcode Functional Proximity, Resource Hierarchy - " \
               "Simrank Score (Top 10 inputs & outputs)"
    side, side_desc = barcode_template() 
    return quick_render(graphURL, main, side, side_desc)


@barcodes.route("/barcodes/resource/fprox/neighbor")
def resource_fprox_neighbor():
    graphURL = "/static/data/barcodes_resource_fprox_neighbor.json"
    main     = "Barcode Functional Proximity, Resource Hierarchy - " \
               "Neighbor Similarity (Top 3 inputs & outputs)"
    side, side_desc = barcode_template() 
    return quick_render(graphURL, main, side, side_desc)


@barcodes.route("/barcodes/resource/fprox/vector")
def resource_fprox_vector():
    graphURL = "/static/data/barcodes_resource_fprox_vector.json"
    main     = "Barcode Functional Proximity, Resource Hierarchy - " \
               "Vector Similarity (Top 3 inputs & outputs, edge weight > 0.01)"
    side, side_desc = barcode_template() 
    return quick_render(graphURL, main, side, side_desc)


@barcodes.route("/barcodes/resource/fprox/mean")
def resource_fprox_mean():
    graphURL = "/static/data/barcodes_resource_fprox_mean.json"
    main     = "Barcode Functional Proximity, Resource Hierarchy - " \
               "Mean Similarity (Top 5 inputs & outputs)"
    side, side_desc = barcode_template() 
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#   Supply                                                                     #
################################################################################


@barcodes.route("/barcodes/resource/supply/downstream")
def resource_supply_downstream():
    graphURL = "/static/data/barcodes_resource_supply_downstream.json"
    main     = "Supply Chain Barcode Connections, Resource Hierarchy - " \
               "Downstreamness Distance (Top 50 inputs & outputs)"
    side, side_desc = barcode_template()  
    return quick_render(graphURL, main, side, side_desc)


@barcodes.route("/barcodes/resource/supply/markov")
def resource_supply_markov():
    graphURL = "/static/data/barcodes_resource_supply_markov.json"
    main     = "Supply Chain Barcode Connections, Resource Hierarchy - " \
               "Markov Distance (Top 5 inputs & outputs)"
    side, side_desc = barcode_template()  
    return quick_render(graphURL, main, side, side_desc)


@barcodes.route("/barcodes/resource/supply/maxflow")
def resource_supply_maxflow():
    graphURL = "/static/data/barcodes_resource_supply_maxflow.json"
    main     = "Supply Chain Barcode Connections, Resource Hierarchy - " \
               "Max Flow (Top 1 input & output, edge weight > 0.1)"
    side, side_desc = barcode_template()  
    return quick_render(graphURL, main, side, side_desc)


@barcodes.route("/barcodes/resource/supply/mean")
def resource_supply_mean():
    graphURL = "/static/data/barcodes_resource_supply_mean.json"
    main     = "Supply Chain Barcode Connections, Resource Hierarchy - " \
               "Mean Distance (Top 20 inputs & outputs)"
    side, side_desc = barcode_template()  
    return quick_render(graphURL, main, side, side_desc)
