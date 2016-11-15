from flask import Blueprint
from views.admin import *


companies = Blueprint('companies', __name__)


def companies_template():
    side      = "Company Information" 
    side_desc = "Hover over or search for a company to see its information" 
    return side, side_desc


################################################################################
#                                                                              #
#   Activity Hierarchy                                                         #
#                                                                              #
################################################################################


@companies.route("/companies/activity/fprox/nodes")
def activity_fprox_nodes():
    graphURL = "/static/data/companies_activity_fprox_nodes.json"
    main     = "Company Functional Proximity, Activity Hierarchy - " \
               "Node Similarity (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/activity/fprox/edges")
def activity_fprox_edges():
    graphURL = "/static/data/companies_activity_fprox_edges.json"
    main     = "Company Functional Proximity, Activity Hierarchy - " \
               "Edge Similarity (Top 3 inputs & outputs)"
    side, side_desc = companies_template()
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/activity/fprox/simrank")
def activity_fprox_simrank():
    graphURL = "/static/data/companies_activity_fprox_simrank.json"
    main     = "Company Functional Proximity, Activity Hierarchy - " \
               "Simrank Score (Top 10 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/activity/fprox/neighbor")
def activity_fprox_neighbor():
    graphURL = "/static/data/companies_activity_fprox_neighbor.json"
    main     = "Company Functional Proximity, Activity Hierarchy - " \
               "Neighbor Similarity (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/activity/fprox/vector")
def activity_fprox_vector():
    graphURL = "/static/data/companies_activity_fprox_vector.json"
    main     = "Company Functional Proximity, Activity Hierarchy - " \
               "Vector Similarity (Top 10 inputs & outputs, edge weight > 0.01)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/activity/fprox/mean")
def activity_fprox_mean():
    graphURL = "/static/data/companies_activity_fprox_mean.json"
    main     = "Company Functional Proximity, Activity Hierarchy - " \
               "Mean Similarity (Top 10 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#   Supply                                                                     #
################################################################################


@companies.route("/companies/activity/supply/downstream")
def activity_supply_downstream():
    graphURL = "/static/data/companies_activity_supply_downstream.json"
    main     = "Supply Chain Company Connections, Activity Hierarchy - " \
               "Downstreamness Distance (Top 30 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/activity/supply/markov")
def activity_supply_markov():
    graphURL = "/static/data/companies_activity_supply_markov.json"
    main     = "Supply Chain Company Connections, Activity Hierarchy - " \
               "Markov Distance (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/activity/supply/maxflow")
def activity_supply_maxflow():
    graphURL = "/static/data/companies_activity_supply_maxflow.json"
    main     = "Supply Chain Company Connections, Activity Hierarchy - " \
               "Max Flow (Top 5 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/activity/supply/mean")
def activity_supply_mean():
    graphURL = "/static/data/companies_activity_supply_mean.json"
    main     = "Supply Chain Company Connections, Activity Hierarchy - " \
               "Mean Distance (Top 5 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#   Competition                                                                #
################################################################################


@companies.route("/companies/activity/competition/connections")
def activity_competition_connections():
    graphURL = "/static/data/companies_activity_competition_connections.json"
    main     = "Competition Company Connections, Activity Hierarchy - " \
               "Connections (Top 5 Inputs & Outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/activity/competition/competitiveness")
def activity_competition_competitiveness():
    graphURL = "/static/data/companies_activity_competition_competitiveness.json"
    main     = "Competition Company Connections, Activity Hierarchy - " \
               "Competitiveness (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#                                                                              #
#   Resource Hierarchy                                                         #
#                                                                              #
################################################################################


@companies.route("/companies/resource/fprox/nodes")
def resource_fprox_nodes():
    graphURL = "/static/data/companies_resource_fprox_nodes.json"
    main     = "Company Functional Proximity, Resource Hierarchy - " \
               "Node Similarity (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/resource/fprox/edges")
def resource_fprox_edges():
    graphURL = "/static/data/companies_resource_fprox_edges.json"
    main     = "Company Functional Proximity, Resource Hierarchy - " \
               "Edge Similarity (Top 3 inputs & outputs)"
    side, side_desc = companies_template()
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/resource/fprox/simrank")
def resource_fprox_simrank():
    graphURL = "/static/data/companies_resource_fprox_simrank.json"
    main     = "Company Functional Proximity, Resource Hierarchy - " \
               "Simrank Score (Top 10 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/resource/fprox/neighbor")
def resource_fprox_neighbor():
    graphURL = "/static/data/companies_resource_fprox_neighbor.json"
    main     = "Company Functional Proximity, Resource Hierarchy - " \
               "Neighbor Similarity (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/resource/fprox/vector")
def resource_fprox_vector():
    graphURL = "/static/data/companies_resource_fprox_vector.json"
    main     = "Company Functional Proximity, Resource Hierarchy - " \
               "Vector Similarity (Top 10 inputs & outputs, edge weight > 0.01)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/resource/fprox/mean")
def resource_fprox_mean():
    graphURL = "/static/data/companies_resource_fprox_mean.json"
    main     = "Company Functional Proximity, Resource Hierarchy - " \
               "Mean Similarity (Top 10 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#   Supply                                                                     #
################################################################################


@companies.route("/companies/resource/supply/downstream")
def resource_supply_downstream():
    graphURL = "/static/data/companies_resource_supply_downstream.json"
    main     = "Supply Chain Company Connections, Resource Hierarchy - " \
               "Downstreamness Distance (Top 30 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/resource/supply/markov")
def resource_supply_markov():
    graphURL = "/static/data/companies_resource_supply_markov.json"
    main     = "Supply Chain Company Connections, Resource Hierarchy - " \
               "Markov Distance (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/resource/supply/maxflow")
def resource_supply_maxflow():
    graphURL = "/static/data/companies_resource_supply_maxflow.json"
    main     = "Supply Chain Company Connections, Resource Hierarchy - " \
               "Max Flow (Top 5 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/resource/supply/mean")
def resource_supply_mean():
    graphURL = "/static/data/companies_resource_supply_mean.json"
    main     = "Supply Chain Company Connections, Resource Hierarchy - " \
               "Mean Distance (Top 5 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#   Competition                                                                #
################################################################################


@companies.route("/companies/resource/competition/connections")
def resource_competition_connections():
    graphURL = "/static/data/companies_resource_competition_connections.json"
    main     = "Competition Company Connections, Resource Hierarchy - " \
               "Connections (Top 5 Inputs & Outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/resource/competition/competitiveness")
def resource_competition_competitiveness():
    graphURL = "/static/data/companies_resource_competition_competitiveness.json"
    main     = "Competition Company Connections, Resource Hierarchy - " \
               "Competitiveness (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#                                                                              #
#   NAICS Hierarchy                                   	                       #
#                                                                              #
################################################################################


@companies.route("/companies/naics/fprox/nodes")
def naics_fprox_nodes():
    graphURL = "/static/data/companies_naics_fprox_nodes.json"
    main     = "Company Functional Proximity, NAICS Hierarchy - " \
               "Node Similarity (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/naics/fprox/edges")
def naics_fprox_edges():
    graphURL = "/static/data/companies_naics_fprox_edges.json"
    main     = "Company Functional Proximity, NAICS Hierarchy - " \
               "Edge Similarity (Top 3 inputs & outputs)"
    side, side_desc = companies_template()
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/naics/fprox/simrank")
def naics_fprox_simrank():
    graphURL = "/static/data/companies_naics_fprox_simrank.json"
    main     = "Company Functional Proximity, NAICS Hierarchy - " \
               "Simrank Score (Top 5 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/naics/fprox/neighbor")
def naics_fprox_neighbor():
    graphURL = "/static/data/companies_naics_fprox_neighbor.json"
    main     = "Company Functional Proximity, NAICS Hierarchy - " \
               "Neighbor Similarity (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/naics/fprox/vector")
def naics_fprox_vector():
    graphURL = "/static/data/companies_naics_fprox_vector.json"
    main     = "Company Functional Proximity, NAICS Hierarchy - " \
               "Vector Similarity(Top 50 inputs & outputs, edge weight > 0.01)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/naics/fprox/mean")
def naics_fprox_mean():
    graphURL = "/static/data/companies_naics_fprox_mean.json"
    main     = "Company Functional Proximity, NAICS Hierarchy - " \
               "Mean Similarity (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#   Supply                                                                     #
################################################################################


@companies.route("/companies/naics/supply/downstream")
def naics_supply_downstream():
    graphURL = "/static/data/companies_naics_supply_downstream.json"
    main     = "Supply Chain Company Connections, NAICS Hierarchy - " \
               "Downstreamness Distance (Top 50 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/naics/supply/markov")
def naics_supply_markov():
    graphURL = "/static/data/companies_naics_supply_markov.json"
    main     = "Supply Chain Company Connections, NAICS Hierarchy - " \
               "Markov Distance (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/naics/supply/maxflow")
def naics_supply_maxflow():
    graphURL = "/static/data/companies_naics_supply_maxflow.json"
    main     = "Supply Chain Company Connections, NAICS Hierarchy - " \
               "Max Flow (Top 20 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/naics/supply/mean")
def naics_supply_mean():
    graphURL = "/static/data/companies_naics_supply_mean.json"
    main     = "Supply Chain Company Connections, NAICS Hierarchy - " \
               "Mean Distance (Top 20 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#   Competition                                                                #
################################################################################


@companies.route("/companies/naics/competition/connections")
def naics_competition_connections():
    graphURL = "/static/data/companies_naics_competition_connections.json"
    main     = "Competition Company Connections, NAICS Hierarchy - " \
               "Connections (Top 5 Inputs & Outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/naics/competition/competitiveness")
def naics_competition_competitiveness():
    graphURL = "/static/data/companies_naics_competition_competitiveness.json"
    main     = "Competition Company Connections, NAICS Hierarchy - " \
               "Competitiveness (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#                                                                              #
#   Syntax Hierarchy                                                            #
#                                                                              #
################################################################################


@companies.route("/companies/syntax/fprox/nodes")
def syntax_fprox_nodes():
    graphURL = "/static/data/companies_syntax_fprox_nodes.json"
    main     = "Company Functional Proximity, Syntax Hierarchy - " \
               "Node Similarity (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/syntax/fprox/edges")
def syntax_fprox_edges():
    graphURL = "/static/data/companies_syntax_fprox_edges.json"
    main     = "Company Functional Proximity, Syntax Hierarchy - " \
               "Edge Similarity (Top 3 inputs & outputs)"
    side, side_desc = companies_template()
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/syntax/fprox/simrank")
def syntax_fprox_simrank():
    graphURL = "/static/data/companies_syntax_fprox_simrank.json"
    main     = "Company Functional Proximity, Syntax Hierarchy - " \
               "Simrank Score (Top 5 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/syntax/fprox/neighbor")
def syntax_fprox_neighbor():
    graphURL = "/static/data/companies_syntax_fprox_neighbor.json"
    main     = "Company Functional Proximity, Syntax Hierarchy - " \
               "Neighbor Similarity (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/syntax/fprox/vector")
def syntax_fprox_vector():
    graphURL = "/static/data/companies_syntax_fprox_vector.json"
    main     = "Company Functional Proximity, Syntax Hierarchy - " \
               "Vector Similarity(Top 100 inputs & outputs, edge weight > 0.01)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/syntax/fprox/mean")
def syntax_fprox_mean():
    graphURL = "/static/data/companies_syntax_fprox_mean.json"
    main     = "Company Functional Proximity, Syntax Hierarchy - " \
               "Mean Similarity (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#   Supply                                                                     #
################################################################################


@companies.route("/companies/syntax/supply/downstream")
def syntax_supply_downstream():
    graphURL = "/static/data/companies_syntax_supply_downstream.json"
    main     = "Supply Chain Company Connections, Syntax Hierarchy - " \
               "Downstreamness Distance (Top 50 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/syntax/supply/markov")
def syntax_supply_markov():
    graphURL = "/static/data/companies_syntax_supply_markov.json"
    main     = "Supply Chain Company Connections, Syntax Hierarchy - " \
               "Markov Distance (Top 3 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/syntax/supply/maxflow")
def syntax_supply_maxflow():
    graphURL = "/static/data/companies_syntax_supply_maxflow.json"
    main     = "Supply Chain Company Connections, Syntax Hierarchy - " \
               "Max Flow (Top 50 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/syntax/supply/mean")
def syntax_supply_mean():
    graphURL = "/static/data/companies_syntax_supply_mean.json"
    main     = "Supply Chain Company Connections, Syntax Hierarchy - " \
               "Mean Distance (Top 20 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


################################################################################
#   Competition                                                                #
################################################################################


@companies.route("/companies/syntax/competition/connections")
def syntax_competition_connections():
    graphURL = "/static/data/companies_syntax_competition_connections.json"
    main     = "Competition Company Connections, Syntax Hierarchy - " \
               "Connections (All)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)


@companies.route("/companies/syntax/competition/competitiveness")
def syntax_competition_competitiveness():
    graphURL = "/static/data/companies_syntax_competition_competitiveness.json"
    main     = "Competition Company Connections, Syntax Hierarchy - " \
               "Competitiveness (Top 10 inputs & outputs)"
    side, side_desc = companies_template() 
    return quick_render(graphURL, main, side, side_desc)
