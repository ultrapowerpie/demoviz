from flask_assets import Bundle, Environment

bundles = {

    'menu_css': Bundle(
        'css/lib/bootstrap-responsive.min.css',
        'css/lib/bootstrap.min.css',
        'css/lib/keen-dashboards.css',
        'css/menuStyle.css',
        output='gen/menu.css'),

    'menu_js': Bundle(
        'js/lib/jquery.min.js',
        'js/lib/bootstrap.min.js',
        'js/timer.js',
        output='gen/menu.js'),

    'vis_css': Bundle(
        'css/lib/easy-autocomplete.themes.css',
        'css/lib/easy-autocomplete.min.css',
        'css/lib/nouislider.min.css',
        'css/lib/nouislider.tooltips.css',
        'css/graphStyle.css',
        'css/stageStyle.css',
        'css/modalStyle.css',
        output='gen/vis.css'),

    'vis_head_js': Bundle(
        'js/lib/jquery.easy-autocomplete.min.js',
        'js/lib/nouislider.min.js',
        'js/lib/wNumb.js',
        'js/lib/FastPriorityQueue.js',
        'js/lib/d3.min.js',
        output='gen/vis_head.js'),

    'vis_foot_js': Bundle(
        'js/variables.js',
        'js/mainGraph.js',
        'js/packageGraph.js',
        'js/options.js',
        'js/search.js',
        'js/modalGraph.js',
        output='gen/vis_foot.js')
}