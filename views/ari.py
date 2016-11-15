from flask import Blueprint
from views.admin import *


ari = Blueprint('ari', __name__)


def ari_template():
    side      = "Barcode Information"
    side_desc = "Hover over or search for a barcode to see its information" 
    return side, side_desc


################################################################################
#   Generated Data 	                                                           #
################################################################################


################################################################################
#   Activity Hierarchy                                                         #
################################################################################

	
@ari.route("/ari/gen/activity/downstream")
def gen_activity_downstream():
    graphURL = "/static/data/ari_gen_activity_downstream.json"
    main     = "Generated Ari Supply Chain Connections, Activity Hierarchy - " \
    		   "Downstreamness Distance (Top 100 inputs & outputs)"
    side, side_desc = ari_template()
    return quick_render(graphURL, main, side, side_desc)


@ari.route("/ari/gen/activity/markov")
def gen_activity_markov():
    graphURL = "/static/data/ari_gen_activity_markov.json"
    main     = "Generated Ari Supply Chain Connections, Activity Hierarchy - " \
    		   "Markovian Distance (Top 5 inputs & outputs)"
    side, side_desc = ari_template()
    return quick_render(graphURL, main, side, side_desc)


@ari.route("/ari/gen/activity/maxflow")
def gen_activity_maxflow():
    graphURL = "/static/data/ari_gen_activity_maxflow.json"
    main     = "Generated Ari Supply Chain Connections, Activity Hierarchy - " \
               "Max Flow (Top 1 input & output with edge weight > 0.1)"
    side, side_desc = ari_template()
    return quick_render(graphURL, main, side, side_desc)


@ari.route("/ari/gen/activity/mean")
def gen_activity_mean():
    graphURL = "/static/data/ari_gen_activity_mean.json"
    main     = "Generated Ari Supply Chain Connections, Activity Hierarchy - " \
               "Mean (Top 20 inputs & outputs)"
    side, side_desc = ari_template()
    return quick_render(graphURL, main, side, side_desc)



################################################################################
#   Resource Hierarchy                                                         #
################################################################################


@ari.route("/ari/gen/resource/downstream")
def gen_resource_downstream():
    graphURL = "/static/data/ari_gen_resource_downstream.json"
    main     = "Generated Ari Supply Chain Connections, Resource Hierarchy - " \
    		   "Downstreamness Distance (Top 100 inputs & outputs)"
    side, side_desc = ari_template()
    return quick_render(graphURL, main, side, side_desc)


@ari.route("/ari/gen/resource/markov")
def gen_resource_markov():
    graphURL = "/static/data/ari_gen_resource_markov.json"
    main     = "Generated Ari Supply Chain Connections, Resource Hierarchy - " \
    		   "Markovian Distance (Top 5 inputs & outputs)"
    side, side_desc = ari_template()
    return quick_render(graphURL, main, side, side_desc)


@ari.route("/ari/gen/resource/maxflow")
def gen_resource_maxflow():
    graphURL = "/static/data/ari_gen_resource_maxflow.json"
    main     = "Generated Ari Supply Chain Connections, Resource Hierarchy - " \
               "Max Flow (Top 1 input & output with edge weight > 500)"
    side, side_desc = ari_template()
    return quick_render(graphURL, main, side, side_desc)


@ari.route("/ari/gen/resource/mean")
def gen_resource_mean():
    graphURL = "/static/data/ari_gen_resource_mean.json"
    main     = "Generated Ari Supply Chain Connections, Resource Hierarchy - " \
               "Mean (Top 20 inputs & outputs)"
    side, side_desc = ari_template()
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#   Real Data 	                          	                                   #
################################################################################


################################################################################
#   Activity Hierarchy                                                         #
################################################################################


@ari.route("/ari/real/activity/downstream")
def real_activity_downstream():
    graphURL = "/static/data/ari_real_activity_downstream.json"
    main     = "Real Ari Supply Chain Connections, Activity Hierarchy - " \
    		   "Downstreamness Distance (Top 50 inputs & outputs)"
    side, side_desc = ari_template()
    return quick_render(graphURL, main, side, side_desc)


@ari.route("/ari/real/activity/markov")
def real_activity_markov():
    graphURL = "/static/data/ari_real_activity_markov.json"
    main     = "Real Ari Supply Chain Connections, Activity Hierarchy - " \
    		   "Markovian Distance (Top 5 inputs & outputs)"
    side, side_desc = ari_template()
    return quick_render(graphURL, main, side, side_desc)


@ari.route("/ari/real/activity/maxflow")
def real_activity_maxflow():
    graphURL = "/static/data/ari_real_activity_maxflow.json"
    main     = "Real Ari Supply Chain Connections, Activity Hierarchy - " \
               "Max Flow (Top 1 input & output with edge weight > 500)"
    side, side_desc = ari_template()
    return quick_render(graphURL, main, side, side_desc)


@ari.route("/ari/real/activity/mean")
def real_activity_mean():
    graphURL = "/static/data/ari_real_activity_mean.json"
    main     = "Real Ari Supply Chain Connections, Activity Hierarchy - " \
               "Mean (Top 10 inputs & outputs)"
    side, side_desc = ari_template()
    return quick_render(graphURL, main, side, side_desc)



################################################################################
#   Resource Hierarchy                                                         #
################################################################################


@ari.route("/ari/real/resource/downstream")
def real_resource_downstream():
    graphURL = "/static/data/ari_real_resource_downstream.json"
    main     = "Real Ari Supply Chain Connections, Resource Hierarchy - " \
    		   "Downstreamness Distance (Top 50 inputs & outputs)"
    side, side_desc = ari_template()
    return quick_render(graphURL, main, side, side_desc)


@ari.route("/ari/real/resource/markov")
def real_resource_markov():
    graphURL = "/static/data/ari_real_resource_markov.json"
    main     = "Real Ari Supply Chain Connections, Resource Hierarchy - " \
    		   "Markovian Distance (Top 5 inputs & outputs)"
    side, side_desc = ari_template()
    return quick_render(graphURL, main, side, side_desc)


@ari.route("/ari/real/resource/maxflow")
def real_resource_maxflow():
    graphURL = "/static/data/ari_real_resource_maxflow.json"
    main     = "Real Ari Supply Chain Connections, Resource Hierarchy - " \
               "Max Flow (Top 1 input & output with edge weight > 0.1)"
    side, side_desc = ari_template()
    return quick_render(graphURL, main, side, side_desc)


@ari.route("/ari/real/resource/mean")
def real_resource_mean():
    graphURL = "/static/data/ari_real_resource_mean.json"
    main     = "Real Ari Supply Chain Connections, Resource Hierarchy - " \
               "Mean (Top 10 inputs & outputs)"
    side, side_desc = ari_template()
    return quick_render(graphURL, main, side, side_desc)