(function() {

var RESOURCE_API = '/resources/api/v1/resource';

var app = $('#resources-app'),
    app_body = $('#app-body'),
    app_heading = $('#app-heading'),
    app_categories = $('#categories'),

    gamemakers = app.data('gamemakers');

// Populate slug-to-obj maps
var category_map = {},
    gamemaker_map = {};
for (var k = 0; k < gamemakers.length; k++) {
    var maker = gamemakers[k];
    gamemaker_map[maker['slug']] = maker;
    for (var m = 0; m < maker['categories'].length; m++) {
        var category = maker['categories'][m];
        category_map[category['slug']] = category;
    }
}

// Enable route logging
crossroads.routed.add(console.log, console);

// Show a list of recent CR uploads
crossroads.addRoute('recent', function() {
    $.ajax({
        url: RESOURCE_API,
        data: {order_by: 'created'},
        success: function(data) {
            app_heading.text('Recent Resources');
            app_body.html(ich.resource_grid({
                resources: data.objects
            }));
        }
    });
});

// Show resources in a category
crossroads.addRoute('category/{slug}', function(slug) {
    var category = getattr(category_map, slug);
    if (category !== null) {
        var maker = gamemaker_map[category['maker']];
        $.ajax({
            url: RESOURCE_API,
            data: {category__slug__exact: slug, order_by: 'created'},
            success: function(data) {

                app_heading.text(maker['name'] + ': ' + category['name']);
                app_body.html(ich.resource_grid({
                    resources: data.objects
                }));
            }
        });
    }
});

$(function() {
    // Generate category listing
    app_categories.html(ich.category_tree({
        gamemakers: gamemakers
    }));

    // Hasher handles history
    hasher.initialized.add(crossroads.parse, crossroads); //parse initial hash
    hasher.changed.add(crossroads.parse, crossroads); //parse hash changes
    hasher.init(); //start listening for history change

    // Init app with recent route
    hasher.setHash('recent');
});

})();
