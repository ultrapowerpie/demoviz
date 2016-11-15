from flask import Blueprint
from views.admin import *


loci = Blueprint('loci', __name__)


def loci_template():
    side      = "Locus Information"
    side_desc = "Hover over or search for a locus to see its name" 
    return side, side_desc


################################################################################
#                                                                              #
#   Activity Hierarchy                                                         #
#                                                                              #
################################################################################


@loci.route("/loci/activity/connections")
def activity_connections():
    graphURL = "/static/data/loci_activity_connections.json"
    main     = "Loci Functional Space, Activity Hierarchy - Connections (All)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/activity/fprox/nodes")
def activity_fprox_nodes():
    graphURL = "/static/data/loci_activity_fprox_nodes.json"
    main     = "Loci Functional Proximity, Activity Hierarchy - " \
               "Node Similarity (Top 5 inputs & outputs)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/activity/fprox/edges")
def activity_fprox_edges():
    graphURL = "/static/data/loci_activity_fprox_edges.json"
    main     = "Loci Functional Proximity, Activity Hierarchy - " \
               "Edge Similarity (Top 5 inputs & outputs)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/activity/fprox/simrank")
def activity_fprox_simrank():
    graphURL = "/static/data/loci_activity_fprox_simrank.json"
    main     = "Loci Functional Proximity, Activity Hierarchy " \
               "- SimRank Similarity (Top 20 inputs & outputs)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/activity/fprox/neighbor")
def activity_fprox_neighbor():
    graphURL = "/static/data/loci_activity_fprox_neighbor.json"
    main     = "Loci Functional Proximity, Activity Hierarchy - " \
               "Neighbor Similarity (Top 5 inputs & outputs)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/activity/fprox/vector")
def activity_fprox_vector():
    graphURL = "/static/data/loci_activity_fprox_vector.json"
    main     = "Loci Functional Proximity, Activity Hierarchy - " \
               "Vector Similarity (Top 5 inputs & outputs, edge weights > 0.02)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/activity/fprox/mean")
def activity_fprox_mean():
    graphURL = "/static/data/loci_activity_fprox_mean.json"
    main     = "Loci Functional Proximity, Activity Hierarchy - " \
               "Mean Similarity (Top 10 inputs & outputs)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#   Supply                                                                     #
################################################################################



@loci.route("/loci/activity/supply/downstream")
def activity_supply_downstream():
    graphURL = "/static/data/loci_activity_supply_downstream.json"
    main     = "Supply Chain Loci Connections, Activity Hierarchy - " \
               "Downstreamness Distance (Top 100 inputs & outputs)" 
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/activity/supply/markov")
def activity_supply_markov():
    graphURL = "/static/data/loci_activity_supply_markov.json"
    main     = "Supply Chain Loci Connections, Activity Hierarchy - " \
               "Markovian Distance (Top 8 inputs & outputs)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/activity/supply/maxflow")
def activity_supply_maxflow():
    graphURL = "/static/data/loci_activity_supply_maxflow.json"
    main     = "Supply Chain Loci Connections, Activity Hierarchy - " \
               "Max Flow (Top 5 inputs & outputs, edges weights > 0.0005)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/activity/supply/mean")
def activity_supply_mean():
    graphURL = "/static/data/loci_activity_supply_mean.json"
    main     = "Supply Chain Loci Connections, Activity Hierarchy - " \
               "Mean Distance (Top 50 inputs & outputs)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#                                                                              #
#   Resource Hierarchy                                                         #
#                                                                              #
################################################################################


@loci.route("/loci/resource/connections")
def resource_connections():
    graphURL = "/static/data/loci_resource_connections.json"
    main     = "Loci Functional Space, Resource Hierarchy - Connections (All)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/resource/fprox/nodes")
def resource_fprox_nodes():
    graphURL = "/static/data/loci_resource_fprox_nodes.json"
    main     = "Loci Functional Proximity, Resource Hierarchy - " \
               "Node Similarity (Top 5 inputs & outputs)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/resource/fprox/edges")
def resource_fprox_edges():
    graphURL = "/static/data/loci_resource_fprox_edges.json"
    main     = "Loci Functional Proximity, Resource Hierarchy - " \
               "Edge Similarity (Top 5 inputs & outputs)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/resource/fprox/simrank")
def resource_fprox_simrank():
    graphURL = "/static/data/loci_resource_fprox_simrank.json"
    main     = "Loci Functional Proximity, Resource Hierarchy " \
               "- SimRank Similarity (Top 20 inputs & outputs)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/resource/fprox/neighbor")
def resource_fprox_neighbor():
    graphURL = "/static/data/loci_resource_fprox_neighbor.json"
    main     = "Loci Functional Proximity, Resource Hierarchy - " \
               "Neighbor Similarity (Top 5 inputs & outputs)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/resource/fprox/vector")
def resource_fprox_vector():
    graphURL = "/static/data/loci_resource_fprox_vector.json"
    main     = "Loci Functional Proximity, Resource Hierarchy - " \
               "Vector Similarity (Top 5 inputs & outputs, edge weights > 0.02)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/resource/fprox/mean")
def resource_fprox_mean():
    graphURL = "/static/data/loci_resource_fprox_mean.json"
    main     = "Loci Functional Proximity, Resource Hierarchy - " \
               "Mean Similarity (Top 10 inputs & outputs)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#   Supply                                                                     #
################################################################################



@loci.route("/loci/resource/supply/downstream")
def resource_supply_downstream():
    graphURL = "/static/data/loci_resource_supply_downstream.json"
    main     = "Supply Chain Loci Connections, Resource Hierarchy - " \
               "Downstreamness Distance (Top 100 inputs & outputs)" 
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/resource/supply/markov")
def resource_supply_markov():
    graphURL = "/static/data/loci_resource_supply_markov.json"
    main     = "Supply Chain Loci Connections, Resource Hierarchy - " \
               "Markovian Distance (Top 8 inputs & outputs)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/resource/supply/maxflow")
def resource_supply_maxflow():
    graphURL = "/static/data/loci_resource_supply_maxflow.json"
    main     = "Supply Chain Loci Connections, Resource Hierarchy - " \
               "Max Flow (Top 5 inputs & outputs, edges weights > 0.0005)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)


@loci.route("/loci/resource/supply/mean")
def resource_supply_mean():
    graphURL = "/static/data/loci_resource_supply_mean.json"
    main     = "Supply Chain Loci Connections, Resource Hierarchy - " \
               "Mean Distance (Top 50 inputs & outputs)"
    side, side_desc = loci_template()
    return quick_render(graphURL, main, side, side_desc)