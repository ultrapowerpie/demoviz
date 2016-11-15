from flask import Blueprint
from views.admin import *


seattle = Blueprint('seattle', __name__)


def seattle_template():
    side      = "Barcode Information"
    side_desc = "Hover over or search for a barcode to see its information" 
    return side, side_desc


################################################################################
#   Generated Data                                                             #
################################################################################


################################################################################
#   Activity Hierarchy                                                         #
################################################################################

    
@seattle.route("/seattle/gen/activity/downstream")
def gen_activity_downstream():
    graphURL = "/static/data/seattle_gen_activity_downstream.json"
    main     = "Generated Seattle Supply Chain Connections, Activity Hierarchy - " \
               "Downstreamness Distance"
    side, side_desc = seattle_template()
    return quick_render(graphURL, main, side, side_desc)


@seattle.route("/seattle/gen/activity/markov")
def gen_activity_markov():
    graphURL = "/static/data/seattle_gen_activity_markov.json"
    main     = "Generated Seattle Supply Chain Connections, Activity Hierarchy - " \
               "Markovian Distance"
    side, side_desc = seattle_template()
    return quick_render(graphURL, main, side, side_desc)


@seattle.route("/seattle/gen/activity/maxflow")
def gen_activity_maxflow():
    graphURL = "/static/data/seattle_gen_activity_maxflow.json"
    main     = "Generated Seattle Supply Chain Connections, Activity Hierarchy - Max Flow"
    side, side_desc = seattle_template()
    return quick_render(graphURL, main, side, side_desc)


@seattle.route("/seattle/gen/activity/mean")
def gen_activity_mean():
    graphURL = "/static/data/seattle_gen_activity_mean.json"
    main     = "Generated Seattle Supply Chain Connections, Activity Hierarchy - Mean"
    side, side_desc = seattle_template()
    return quick_render(graphURL, main, side, side_desc)



################################################################################
#   Resource Hierarchy                                                         #
################################################################################


@seattle.route("/seattle/gen/resource/downstream")
def gen_resource_downstream():
    graphURL = "/static/data/seattle_gen_resource_downstream.json"
    main     = "Generated Seattle Supply Chain Connections, Resource Hierarchy - " \
               "Downstreamness Distance"
    side, side_desc = seattle_template()
    return quick_render(graphURL, main, side, side_desc)


@seattle.route("/seattle/gen/resource/markov")
def gen_resource_markov():
    graphURL = "/static/data/seattle_gen_resource_markov.json"
    main     = "Generated Seattle Supply Chain Connections, Resource Hierarchy - " \
               "Markovian Distance"
    side, side_desc = seattle_template()
    return quick_render(graphURL, main, side, side_desc)


@seattle.route("/seattle/gen/resource/maxflow")
def gen_resource_maxflow():
    graphURL = "/static/data/seattle_gen_resource_maxflow.json"
    main     = "Generated Seattle Supply Chain Connections, Resource Hierarchy - Max Flow"
    side, side_desc = seattle_template()
    return quick_render(graphURL, main, side, side_desc)


@seattle.route("/seattle/gen/resource/mean")
def gen_resource_mean():
    graphURL = "/static/data/seattle_gen_resource_mean.json"
    main     = "Generated Seattle Supply Chain Connections, Resource Hierarchy - Mean"
    side, side_desc = seattle_template()
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#   Real Data                                                                  #
################################################################################


################################################################################
#   Activity Hierarchy                                                         #
################################################################################


@seattle.route("/seattle/real/activity/downstream")
def real_activity_downstream():
    graphURL = "/static/data/seattle_real_activity_downstream.json"
    main     = "Real Seattle Supply Chain Connections, Activity Hierarchy - " \
               "Downstreamness Distance"
    side, side_desc = seattle_template()
    return quick_render(graphURL, main, side, side_desc)


@seattle.route("/seattle/real/activity/markov")
def real_activity_markov():
    graphURL = "/static/data/seattle_real_activity_markov.json"
    main     = "Real Seattle Supply Chain Connections, Activity Hierarchy - " \
               "Markovian Distance"
    side, side_desc = seattle_template()
    return quick_render(graphURL, main, side, side_desc)


@seattle.route("/seattle/real/activity/maxflow")
def real_activity_maxflow():
    graphURL = "/static/data/seattle_real_activity_maxflow.json"
    main     = "Real Seattle Supply Chain Connections, Activity Hierarchy - Max Flow"
    side, side_desc = seattle_template()
    return quick_render(graphURL, main, side, side_desc)


@seattle.route("/seattle/real/activity/mean")
def real_activity_mean():
    graphURL = "/static/data/seattle_real_activity_mean.json"
    main     = "Real Seattle Supply Chain Connections, Activity Hierarchy - Mean"
    side, side_desc = seattle_template()
    return quick_render(graphURL, main, side, side_desc)



################################################################################
#   Resource Hierarchy                                                         #
################################################################################


@seattle.route("/seattle/real/resource/downstream")
def real_resource_downstream():
    graphURL = "/static/data/seattle_real_resource_downstream.json"
    main     = "Real Seattle Supply Chain Connections, Resource Hierarchy - " \
               "Downstreamness Distance"
    side, side_desc = seattle_template()
    return quick_render(graphURL, main, side, side_desc)


@seattle.route("/seattle/real/resource/markov")
def real_resource_markov():
    graphURL = "/static/data/seattle_real_resource_markov.json"
    main     = "Real Seattle Supply Chain Connections, Resource Hierarchy - " \
               "Markovian Distance"
    side, side_desc = seattle_template()
    return quick_render(graphURL, main, side, side_desc)


@seattle.route("/seattle/real/resource/maxflow")
def real_resource_maxflow():
    graphURL = "/static/data/seattle_real_resource_maxflow.json"
    main     = "Real Seattle Supply Chain Connections, Resource Hierarchy - Max Flow"
    side, side_desc = seattle_template()
    return quick_render(graphURL, main, side, side_desc)


@seattle.route("/seattle/real/resource/mean")
def real_resource_mean():
    graphURL = "/static/data/seattle_real_resource_mean.json"
    main     = "Real Seattle Supply Chain Connections, Resource Hierarchy - Mean"
    side, side_desc = seattle_template()
    return quick_render(graphURL, main, side, side_desc)